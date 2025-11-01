#!/usr/bin/env python3
"""Detailed Evaluation Results Output"""
import json
from pathlib import Path

SEPARATOR = "─" * 100
LINE = "=" * 100

def get_score_color(score, threshold=3.0):
    if score >= 4.5:
        return "\033[92m"
    elif score >= threshold:
        return "\033[93m"
    else:
        return "\033[91m"

def reset_color():
    return "\033[0m"

def get_score_indicator(score, threshold=3.0):
    if score >= 4.5:
        return "✅"
    elif score >= threshold:
        return "⚠️"
    else:
        return "❌"

def extract_query_text(query_input):
    if isinstance(query_input, list):
        for item in query_input:
            if isinstance(item, dict) and item.get("role") == "user":
                content = item.get("content", [])
                if isinstance(content, list) and len(content) > 0:
                    return content[0].get("text", "")
    return ""

def extract_response_text(response):
    if isinstance(response, list):
        for item in response:
            if isinstance(item, dict) and item.get("role") == "assistant":
                content = item.get("content", [])
                if isinstance(content, list) and len(content) > 0:
                    return content[0].get("text", "")
    return ""

def main():
    eval_output_path = Path("evals/eval-output.json")
    
    print(LINE)
    print("📊 AGENT EVALUATION RESULTS - Detailed Analysis Report")
    print(LINE, "\n")
    
    if not eval_output_path.exists():
        print("❌ Evaluation results file not found.")
        print(f"   File path: {eval_output_path.absolute()}")
        print("\n   Please run cell 5 in 07_evaluate_agents.ipynb first.\n")
        return
    
    with open(eval_output_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    metrics = data.get("metrics", {})
    rows = data.get("rows", [])
    
    # Section 1: Overall Average Scores
    print("⭐ Overall Average Performance Scores")
    print(LINE)
    scores_config = [
        ("Intent Resolution", "intent_resolution.intent_resolution", "Intent Understanding", 3.0),
        ("Task Adherence", "task_adherence.task_adherence", "Task Fidelity", 3.0),
    ]
    
    for name, key, desc, threshold in scores_config:
        if key in metrics:
            score = metrics[key]
            color = get_score_color(score, threshold)
            reset = reset_color()
            indicator = get_score_indicator(score, threshold)
            stars = "★" * int(score) + "☆" * (5 - int(score))
            bar = "█" * int(score * 4) + "░" * (20 - int(score * 4))
            
            print(f"{indicator} {name:20} {color}{score:.2f}/5.0{reset}  {stars}")
            print(f"     {desc:20} [{bar}]")
            if score < threshold:
                print(f"     {color}⚠️ Below threshold (standard: {threshold:.1f}){reset}")
            print()
    
    # Section 2: Operational Metrics
    print("\n⚡ Operational Metrics (Average)")
    print(LINE)
    
    operational_keys = [
        ("operational_metrics.server-run-duration-in-seconds", "Server Execution Time", "s"),
        ("operational_metrics.client-run-duration-in-seconds", "Client Execution Time", "s"),
        ("operational_metrics.prompt-tokens", "Prompt Tokens", "tokens"),
        ("operational_metrics.completion-tokens", "Completion Tokens", "tokens"),
    ]
    
    total_tokens = 0
    for key, desc, unit in operational_keys:
        if key in metrics:
            value = metrics[key]
            if unit == "tokens":
                print(f"  {desc:30} {int(value):>10,} {unit}")
                total_tokens += value
            else:
                print(f"  {desc:30} {value:>10.2f} {unit}")
    
    if total_tokens > 0:
        print(f"  {'Total Token Usage':30} {int(total_tokens):>10,} tokens")
        cost = (total_tokens / 1000) * 0.0025
        print(f"  {'Estimated Cost (GPT-4o)':30} ${cost:>9.4f}")
    print()
    
    # Section 3: Individual Query Detailed Results
    if rows:
        print("\n📋 Detailed Results by Query")
        print(LINE)
        
        for idx, row in enumerate(rows, 1):
            query = extract_query_text(row.get("inputs.query", []))
            response = extract_response_text(row.get("inputs.response", []))
            ground_truth = row.get("inputs.metrics.ground-truth", "")
            
            print(f"\n{SEPARATOR}")
            print(f"🔍 Query #{idx}")
            print(SEPARATOR)
            
            print("\n💬 User Question:")
            print(f"   {query}")
            
            if ground_truth:
                print("\n📌 Expected Behavior (Ground Truth):")
                print(f"   {ground_truth}")
            
            if response:
                print("\n🤖 Agent Response (Summary):")
                response_preview = response[:200] if len(response) > 200 else response
                lines_shown = 0
                for line in response_preview.split("\n"):
                    if line.strip() and lines_shown < 3:
                        print(f"   {line.strip()}")
                        lines_shown += 1
                if len(response) > 200:
                    print(f"   ... (total {len(response):,} characters)")
            
            print("\n📊 Evaluation Scores:")
            
            intent = row.get("outputs.intent_resolution.intent_resolution", "N/A")
            task = row.get("outputs.task_adherence.task_adherence", "N/A")
            tool = row.get("outputs.tool_call_accuracy.tool_call_accuracy", "N/A")
            
            intent_threshold = row.get("outputs.intent_resolution.intent_resolution_threshold", 3)
            task_threshold = row.get("outputs.task_adherence.task_adherence_threshold", 3)
            
            if isinstance(intent, (int, float)):
                color = get_score_color(intent, intent_threshold)
                reset = reset_color()
                indicator = get_score_indicator(intent, intent_threshold)
                print(f"   {indicator} Intent Resolution:  {color}{intent:.1f}/5.0{reset} (threshold: {intent_threshold})")
            else:
                print(f"   • Intent Resolution:  {intent}")
            
            if isinstance(task, (int, float)):
                color = get_score_color(task, task_threshold)
                reset = reset_color()
                indicator = get_score_indicator(task, task_threshold)
                print(f"   {indicator} Task Adherence:     {color}{task:.1f}/5.0{reset} (threshold: {task_threshold})")
            else:
                print(f"   • Task Adherence:     {task}")
            
            print(f"   • Tool Call Accuracy: {tool}")
            
            # Evaluation Reasoning
            print("\n💡 Evaluation Details:")
            
            intent_reason = row.get("outputs.intent_resolution.intent_resolution_reason", "")
            task_reason = row.get("outputs.task_adherence.task_adherence_reason", "")
            tool_reason = row.get("outputs.tool_call_accuracy.tool_call_accuracy_reason", "")
            
            if intent_reason:
                print("\n   [Intent Resolution Evaluation Reason]")
                for sentence in intent_reason.split(". "):
                    if sentence.strip():
                        print(f"   • {sentence.strip()}.")
            
            if task_reason:
                print("\n   [Task Adherence Evaluation Reason]")
                for sentence in task_reason.split(". "):
                    if sentence.strip():
                        print(f"   • {sentence.strip()}.")
            
            if tool_reason:
                print("\n   [Tool Call Accuracy Evaluation Reason]")
                for sentence in tool_reason.split(". "):
                    if sentence.strip():
                        print(f"   • {sentence.strip()}.")
            
            duration = row.get("outputs.operational_metrics.client-run-duration-in-seconds", 0)
            prompt_tokens = row.get("outputs.operational_metrics.prompt-tokens", 0)
            completion_tokens = row.get("outputs.operational_metrics.completion-tokens", 0)
            
            print("\n⏱️  Performance Metrics:")
            print(f"   • Execution Time: {duration:.2f}s")
            print(f"   • Token Usage: {prompt_tokens:,} (input) + {completion_tokens:,} (output) = {prompt_tokens + completion_tokens:,} (total)")
            
            issues = []
            if isinstance(intent, (int, float)) and intent < intent_threshold:
                issues.append(f"Intent Resolution score low ({intent:.1f} < {intent_threshold})")
            if isinstance(task, (int, float)) and task < task_threshold:
                issues.append(f"Task Adherence score low ({task:.1f} < {task_threshold})")
            
            if issues:
                print(f"\n{get_score_color(1.0, 3.0)}⚠️  Issues Found:{reset_color()}")
                for issue in issues:
                    print(f"   • {issue}")
        
        # Section 4: Statistical Summary
        print(f"\n{SEPARATOR}\n")
        print("\n📈 Statistical Summary and Analysis")
        print(LINE)
        
        intent_scores = []
        task_scores = []
        durations = []
        total_tokens_list = []
        failed_queries = []
        
        for idx, row in enumerate(rows, 1):
            intent = row.get("outputs.intent_resolution.intent_resolution")
            task = row.get("outputs.task_adherence.task_adherence")
            duration = row.get("outputs.operational_metrics.client-run-duration-in-seconds", 0)
            prompt = row.get("outputs.operational_metrics.prompt-tokens", 0)
            completion = row.get("outputs.operational_metrics.completion-tokens", 0)
            
            intent_threshold = row.get("outputs.intent_resolution.intent_resolution_threshold", 3)
            task_threshold = row.get("outputs.task_adherence.task_adherence_threshold", 3)
            
            if isinstance(intent, (int, float)):
                intent_scores.append(intent)
                if intent < intent_threshold:
                    query = extract_query_text(row.get("inputs.query", []))
                    failed_queries.append((idx, "Intent Resolution", intent, query[:50]))
            
            if isinstance(task, (int, float)):
                task_scores.append(task)
                if task < task_threshold:
                    query = extract_query_text(row.get("inputs.query", []))
                    failed_queries.append((idx, "Task Adherence", task, query[:50]))
            
            if duration:
                durations.append(duration)
            total_tokens_list.append(prompt + completion)
        
        if intent_scores:
            avg_intent = sum(intent_scores) / len(intent_scores)
            color = get_score_color(avg_intent, 3.0)
            reset = reset_color()
            pass_count = len([s for s in intent_scores if s >= 3.0])
            
            print("\n📊 Intent Resolution (Intent Understanding)")
            print(f"   Average: {color}{avg_intent:.2f}/5.0{reset}")
            print(f"   Highest: {max(intent_scores):.1f}  |  Lowest: {min(intent_scores):.1f}")
            print(f"   Pass Rate: {pass_count}/{len(intent_scores)} ({pass_count/len(intent_scores)*100:.1f}%)")
        
        if task_scores:
            avg_task = sum(task_scores) / len(task_scores)
            color = get_score_color(avg_task, 3.0)
            reset = reset_color()
            pass_count = len([s for s in task_scores if s >= 3.0])
            
            print("\n📊 Task Adherence (Task Fidelity)")
            print(f"   Average: {color}{avg_task:.2f}/5.0{reset}")
            print(f"   Highest: {max(task_scores):.1f}  |  Lowest: {min(task_scores):.1f}")
            print(f"   Pass Rate: {pass_count}/{len(task_scores)} ({pass_count/len(task_scores)*100:.1f}%)")
        
        if durations:
            print("\n⏱️  Execution Time")
            print(f"   Average: {sum(durations)/len(durations):.2f}s")
            print(f"   Maximum: {max(durations):.2f}s  |  Minimum: {min(durations):.2f}s")
        
        if total_tokens_list:
            avg_tokens = sum(total_tokens_list) / len(total_tokens_list)
            total_all_tokens = sum(total_tokens_list)
            
            print("\n💰 Token Usage")
            print(f"   Average: {avg_tokens:,.0f} tokens/query")
            print(f"   Total: {total_all_tokens:,} tokens")
            print(f"   Maximum: {max(total_tokens_list):,}  |  Minimum: {min(total_tokens_list):,}")
            print(f"   Estimated Cost (GPT-4o): ${(total_all_tokens / 1000) * 0.0025:.4f}")
        
        if failed_queries:
            print(f"\n{get_score_color(1.0, 3.0)}⚠️  Queries Needing Improvement ({len(failed_queries)}){reset_color()}")
            print(SEPARATOR)
            
            seen = set()
            for idx, metric, score, query in failed_queries:
                key = (idx, metric)
                if key not in seen:
                    seen.add(key)
                    print(f"   Query #{idx}: {metric} = {score:.1f}")
                    print(f"   └─ {query}...")
                    print()
        else:
            print("\n✅ All queries passed the threshold!")
    
    print(f"\n{LINE}")
    print(f"✅ Total {len(rows)} queries evaluated")
    print(f"📁 Detailed JSON: {eval_output_path.absolute()}")
    print(f"💡 Same results available in notebook (cell 6)")
    print(f"{LINE}\n")

if __name__ == "__main__":
    main()
