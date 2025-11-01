#!/usr/bin/env python3
"""
Translate knowledge-base.json from Korean to English
"""
import json

# Translation mappings for titles and content
translations = {
    "travel-001": {
        "title": "Jeju Seongsan Ilchulbong - Magnificent Sunrise at UNESCO World Natural Heritage",
        "content": "Seongsan Ilchulbong is a volcanic crater located at the eastern tip of Jeju Island, designated as a UNESCO World Natural Heritage Site. You can reach the 182m summit in about 30 minutes, and the sunrise view from the top is considered one of the most beautiful sunrises in Korea. You can enjoy a 360-degree panoramic view while walking along the crater rim, and watch Jeju haenyeo (female divers) performances at the coastal area below. The surrounding area has many photo zones including Seopjikoji and Gwangchigi Beach, making it a popular photography destination."
    },
    "travel-002": {
        "title": "Gyeongju Bomun Tourist Complex - Exploring Cultural Heritage of the Millennium-Old Capital",
        "content": "Gyeongju is a city where the thousand-year history of Silla comes alive. Bulguksa Temple and Seokguram Grotto are representative cultural properties designated as UNESCO World Cultural Heritage Sites. You can feel the traces of history while strolling through the ancient tomb complex in the Daereungwon area, and Cheomseongdae is one of the oldest astronomical observatories in the world. Anapji (Donggung Palace and Wolji Pond) is especially beautiful at night and is popular as a dating course for couples. The Bomun Tourist Complex has concentrated hotels and restaurants, making comfortable accommodation possible."
    },
    "travel-003": {
        "title": "Yangyang Surfing Beaches in Gangwon-do - Thrilling Wave Riding Experience",
        "content": "Yangyang is known as the mecca of surfing in Korea. Good surfing waves form year-round at beaches like Jukdo Beach, Ingu Beach, and Gisamun Beach. There are surfing schools everywhere for beginners, offering one-stop solutions from equipment rental to lessons. After surfing, enjoy the leisure of watching the sunset with a beer at beachside cafes. In summer, you can enjoy both swimming and surfing, and nearby Naksansa Temple and Hajodae are also worth visiting. Especially popular among young people in their 20s and 30s."
    },
    "travel-004": {
        "title": "Busan Haeundae - Coastal City Where City Meets the Sea",
        "content": "Haeundae is Busan's representative tourist attraction, crowded with beachgoers in summer. Haeundae Beach boasts a 1.5km long white sand beach, surrounded by high-rise buildings in Marine City creating an urban skyline. At Dongbaek Island's Nurimaru APEC House, you can tour the APEC conference venue and enjoy camellia trees and ocean views while walking along the coastal trail. Haeundae Dalmaji Road is also famous for cherry blossoms, and the coastal drive to Cheongsapo and Songjeong Beach is recommended."
    },
    "travel-005": {
        "title": "Jeonju Hanok Village - City of Tradition and Taste",
        "content": "Jeonju Hanok Village is Korea's largest hanok preservation district with over 700 traditional hanoks concentrated in one area. Walking through narrow alleys, you can experience various traditional cultures including hanok stays, traditional craft experiences, and hanbok rentals. Jeonju is famous as the birthplace of bibimbap, and at Nambu Market's night market you can taste Jeonju's 10 delicacies. Gyeonggijeon Hall houses the portrait of King Taejo Yi Seong-gye of Joseon, and from Omokdae you can capture the entire view of Hanok Village in one glance. Spring cherry blossoms and fall foliage are especially beautiful."
    },
    "travel-006": {
        "title": "Seoraksan National Park - Famous Mountain with Four-Season Scenery",
        "content": "Seoraksan is Korea's third highest mountain, boasting beautiful scenery in all four seasons including spring azaleas, summer valleys, fall foliage, and winter snow. There are various courses by difficulty level, from climbing to Daecheongbong Peak (1,708m) to the cable car connecting Sinheungsa Temple and Gwongeumseong Fortress. Magnificent waterfalls like Biryong Falls, Towangseong Falls, and Daeseung Falls are hidden throughout, and Cheonbuldong Valley is popular as a summer resort. To explore both outer and inner Seoraksan thoroughly requires at least 2-3 days."
    },
    "travel-007": {
        "title": "Yeosu Night Sea - Romantic Marine Cable Car",
        "content": "Yeosu is a port city on the southern coast that became even more famous through the song 'Yeosu Night Sea.' The Yeosu Marine Cable Car connects Dolsan Park and Jasan Park, offering spectacular views of Yeosu's coastal waters along the 1.5km section crossing above the sea. Odongdo Island is famous for camellias, and you can explore the entire island walking along the coastal trail. At night, the night views of Yeosu Expo Marine Park and Dolsan Bridge are beautiful, and the Central Market and Gosodong Mural Village are also worth visiting."
    },
    "travel-008": {
        "title": "Nami Island - Island with Beautiful Metasequoia Path",
        "content": "Nami Island is a crescent-shaped island in the North Han River, made famous as a filming location for the drama 'Winter Sonata.' The entire island is designed like an arboretum, especially famous for its metasequoia and ginkgo tree-lined paths. You can rent bicycles or take an electric tram to circle the island, with photo zones and sculpture works installed throughout. Spring brings cherry blossoms and canola flowers, while fall offers stunning foliage and ginkgo leaves. It's close to downtown Chuncheon and perfect for a day trip."
    },
    "travel-009": {
        "title": "Sokcho Jungang Market - Fresh Seafood and Traditional Market Charm",
        "content": "Sokcho Jungang Market is the largest traditional market on the East Coast, famous for fresh seafood and food. You can taste Sokcho's unique foods like squid sundae, dakgangjeong (sweet crispy chicken), and abai sundae. Inside the market are concentrated sashimi restaurants where you can have fresh fish sliced and eaten on the spot, and the nearby Sokcho Tourist Fish Market is also worth visiting. From Sokcho Port, you can take a cruise to enjoy the East Sea, and driving around nearby Yeongrang Lake and Cheongcho Lake is also recommended."
    },
    "travel-010": {
        "title": "Boryeong Mud Festival - World-Famous Summer Festival",
        "content": "The Boryeong Mud Festival is Korea's representative summer festival held every July at Daecheon Beach. You can enjoy various mud experience programs like mud slides, mud pools, and mud massages, known to be good for skin beauty. At night, EDM parties and fireworks on the beach bring the festival atmosphere to its peak. Daecheon Beach is the largest beach on the west coast with wide white sand and shallow water, popular with family visitors. Other nearby beaches like Muchangpo and Wonsando are also worth exploring."
    },
    "travel-011": {
        "title": "Gangneung Jeongdongjin - Sunrise Spot at the Train Station",
        "content": "Jeongdongjin, named for being directly east of Gwanghwamun in Seoul, is listed in the Guinness Book of Records as the train station closest to the sea in the world. Famous as a sunrise spot, it's crowded with tourists every January 1st to see the first sunrise of the new year. Jeongdongjin Station's Hourglass Park has the world's largest hourglass, and the coastal walking path along the beach is beautiful. At nearby Jumunjin Port you can taste fresh sashimi, and Gangneung Coffee Street and Anmok Beach are also worth visiting."
    },
    "travel-012": {
        "title": "Tongyeong Cable Car - Panoramic View of Hallyeohaesang",
        "content": "Tongyeong Cable Car connects to Mireuksan Peak (461m) over about 1.8km, one of Korea's longest cable car rides. From the summit, you can enjoy a 360-degree view of Hallyeohaesang's blue sea and islands creating a spectacular scene. Tongyeong is a historic place where Admiral Yi Sun-sin's Samdo Sugun Tongjeyeong was located, and the pretty alleys of Dongpirang Mural Village and Seopirang Village are popular photo zones. At Tongyeong Jungang Market you can taste local specialties like honey bread and Tongyeong chungmu gimbap, and luge experiences are also available."
    },
    "travel-013": {
        "title": "Damyang Juknokwon - Cool Bamboo Forest Path",
        "content": "Juknokwon is a bamboo forest covering about 160,000㎡, with 8 walking paths established through the dense bamboo. It provides cool shade even in summer, and the sound of bamboo leaves swaying in the wind brings peace to the mind. At the Juknokwon entrance there's a metasequoia tree-lined street worth exploring together, and Gwanbangjerim's zelkova forest is also good for walking. Damyang, true to being the home of bamboo, is famous for bamboo shoot dishes and tteokgalbi (grilled short rib patties), and traditional gardens like Soswaewon and Myeongok Hunwon are also nearby."
    },
    "travel-014": {
        "title": "Pohang Homigot - Sunrise Spot at Korea's Easternmost Point",
        "content": "Homigot is a cape at the easternmost point of the Korean Peninsula, famous as a sunrise viewing spot. The Hands of Coexistence sculpture reaching out over the sea is impressive and has become Pohang's landmark. At Homigot Lighthouse Museum you can see various lighthouse models and history from around the country, and from Haeareum Square you can enjoy the wide open East Sea. Nearby Guryongpo Past Meogi Culture Hall and Japanese House Street are worth visiting, and in winter during the past meogi season you can taste fresh past meogi (semi-dried herring)."
    },
    "travel-015": {
        "title": "Andong Hahoe Village - UNESCO World Heritage Traditional Village",
        "content": "Hahoe Village is a representative Korean folk village with 600 years of tradition, designated as a UNESCO World Heritage Site. The village with harmoniously arranged tile-roofed and thatched houses is situated where the Nakdong River winds in an S-shape. You can watch Hahoe Byeolsingut Talchum (mask dance) performances and experience traditional culture like making Hahoe masks. Climbing Buyongdae for a view of the entire village is the highlight, and you can also experience the life of ancient scholars through traditional hanok stays. Andong jjimdak (braised chicken) and Andong salted mackerel are must-try foods."
    },
    "travel-016": {
        "title": "Taean Anmyeondo - Beach Paradise on the West Coast",
        "content": "Anmyeondo is the largest island on the west coast, scattered with beautiful beaches like Kkotji Beach, Mongsanpo Beach, and Bangpo Beach. The sunset between Grandmother Rock and Grandfather Rock at Kkotji Beach is especially famous for its spectacular view. The pine forest at Anmyeondo Natural Recreation Forest is rich in phytoncides, good for forest bathing, and from Wind Hill you can view the wide sea with wind turbines. Various trekking courses in Taean Coast National Park are also popular, and you can enjoy fresh crab and clams at affordable prices."
    },
    "travel-017": {
        "title": "Gapyeong Morning Calm Arboretum - Beauty of Four-Season Gardens",
        "content": "Morning Calm Arboretum is a 5-hectare garden with over 20 themed gardens established. Spring brings tulips and azaleas, summer brings hydrangeas and lotus flowers, fall brings chrysanthemums and foliage, and winter features the Five-Colored Starlight Garden Festival, offering beautiful scenery all four seasons. Especially the trumpet creeper on Sky Road in May-June and fall foliage in October-November reach their peak. During night opening periods, soft lighting makes the garden even more fantastic, with photo zones throughout for capturing life-time photos. Gapyeong Jarasum Island and Nami Island are also nearby for combined visits."
    },
    "travel-018": {
        "title": "Suncheonman National Garden - World's Top 5 Coastal Wetland and Garden",
        "content": "Suncheonman is one of the world's top 5 coastal wetlands, with spectacular scenery created by vast reed fields and S-shaped waterways. The view of Suncheonman from Yongsan Observatory is considered one of Korea's most beautiful landscapes. Suncheonman National Garden, site of the 2013 International Garden Expo, has gardens from various countries and traditional Korean gardens established. During the fall reed festival season, you can see the spectacular sight of golden reeds swaying in the wind, and the Skycube connecting Suncheonman Wetland and National Garden is worth trying."
    },
    "travel-019": {
        "title": "Jinju Namgang Yudeung Festival - River Colored with Light",
        "content": "Jinju Namgang Yudeung Festival is a representative fall festival held every October in the Jinjuseong Fortress area. The festival originated from the history of militia floating lanterns on the river to defeat Japanese forces during the Imjin War, creating a spectacular sight with colorful lanterns filling the Namgang River. Lights are installed along the Jinjuseong Fortress walls, and various large lantern artworks are displayed. At night, you can experience floating small lanterns on the river along with fireworks. Jinju bibimbap and Jinju naengmyeon are also famous, and the historical value of Jinjuseong Fortress and Chokseongnu is also high."
    },
    "travel-020": {
        "title": "Ulleungdo Dokdo - Mysterious Volcanic Island Journey",
        "content": "Ulleungdo is a volcanic island in the East Sea, boasting spectacular scenery with steep cliffs, dense forests, and clear seas. Various experiences are possible including climbing Seonginbong Peak, walking through Nari Basin, visiting Dokdo Museum, and there are also ferry services to Dokdo (weather permitting). Ulleungdo squid, rice with mussels, and barnacle kalguksu are famous local dishes, and the sunset at Jeodong Port's Chottae Rock and Taeha Lighthouse is beautiful. A coastal road drive around the island is recommended, and from Dodong Observatory accessible by cable car you can see the entire view of Ulleungdo."
    },
    "travel-021": {
        "title": "Jeju Udo Island - Coral Beach and Peanut Ice Cream Island",
        "content": "Udo is a small island east of Jeju Island, called Udo (Cow Island) because it resembles a lying cow. Seobin Baeksa Beach is Korea's only red algae nodule beach, boasting emerald waters mixed with coral sand. One lap around the island by bicycle or electric vehicle takes only 2-3 hours, and the view from Udobong Peak is beautiful. Peanut ice cream and peanut makgeolli made from Udo's specialty peanuts are famous, and the black sand beach is also unique. Ferries operate every 15 minutes from Seongsan Port."
    },
    "travel-022": {
        "title": "Incheon Chinatown - Exotic Streets and Chinese Cuisine",
        "content": "Incheon Chinatown is Korea's first Chinatown, formed after the opening of the port in 1883 as Chinese people gathered and lived there. Pailu (arched gates) and Chinese-style buildings create an exotic atmosphere, and alleys are lined with Chinese restaurant specialists. Gonghwachun, the origin of jajangmyeon, operates a jajangmyeon museum, where you can also taste jjamppong and sweet and sour pork. Nearby Songwol-dong Fairy Tale Village has various fairy tale character murals that are popular photo zones, and Freedom Park and Port Opening Museum are also worth visiting. Wolmido Island and Incheon coastal waters are also nearby for combined visits."
    },
    "travel-023": {
        "title": "Pyeongchang Daegwallyeong Sheep Ranch - Sheep and Windmills on the Meadow",
        "content": "Daegwallyeong Sheep Ranch is Korea's largest sheep ranch located at 850m-900m above sea level. White sheep grazing leisurely on green meadows evoke the pastoral scenery of Europe. You can feed sheep while walking along trails, and the windmill and ranch view from the hill are famous photo spots. You can enjoy cool highland weather even in summer, and nearby Daegwallyeong Sky Ranch and Samyang Ranch are also worth visiting. Pyeongchang restaurants and Alpensia Resort are also nearby."
    },
    "travel-024": {
        "title": "Gwangju Yangnim-dong Penguin Village - Alley Art Journey",
        "content": "Yangnim-dong is Gwangju's representative modern historic cultural village, with various murals and artworks hidden throughout narrow alleys. Nicknamed Penguin Village, cute penguin sculptures and murals decorate the village everywhere. Over 100-year-old hanoks and modern architecture coexist, and unique cafes and accessory shops are located throughout alleys. You can see historic buildings like Choi Seung-hyo House, Holly Tree Hill, and Lee Jang-woo House, and from Yangnim Mountain summit you can view the entire downtown Gwangju."
    },
    "travel-025": {
        "title": "Geoje Wind Hill - Blue Sea and White Windmills",
        "content": "Wind Hill is a scenic viewpoint located on a hill in Dojangpo Village, southern Geoje Island. The scenery combining blue sea, white windmills, and yellow canola flowers (in spring) resembles Jeju Island. It became famous as a filming location for dramas 'Eve's Garden' and 'Merry-Go-Round.' Haegeumgang Rock and Oedo Island viewed from the hill are beautiful, and you can enjoy wide sea views walking along trails. Nearby Sinseondae and Haegeumgang cruise tours are also enjoyable, and you can taste fresh seafood at Geoje Sashimi Center."
    },
    "travel-026": {
        "title": "Gongju Baekje Cultural Complex - Recreation of Baekje Royal Palace",
        "content": "Gongju Baekje Cultural Complex is a historic theme park that recreates the Baekje period royal palace and Sabi Palace. Established over 330,000㎡ with Woongjinseong Fortress, Sabi Palace, Neungsa Temple, and Living Culture Village, you can experience Baekje's brilliant culture. The Baekje History and Culture Museum exhibits Baekje history and cultural properties, operating traditional costume and craft experience programs. Every fall, the Baekje Cultural Festival is held with various performances and events. Nearby Gongsanseong Fortress and Songsan-ri Ancient Tombs are also UNESCO World Heritage sites worth visiting together."
    },
    "travel-027": {
        "title": "Pyeongtaek Jebudo Island - Mysterious Island Where the Sea Path Opens",
        "content": "Jebudo is an island in Pyeongtaek, Gyeonggi-do, famous for Moses' miracle where the sea path opens twice a day during low tide, allowing walking access. You must visit according to tide times, and the experience of walking the approximately 1.5km sea path to the island is special. The island has beaches and sashimi restaurants, and you can rent bicycles to tour around the island. Famous for beautiful sunsets, and in winter you can taste fresh oysters and clams. Nearby Jeongok Port and Poseung Embankment are also good driving routes."
    },
    "travel-028": {
        "title": "Goseong DMZ Peace Ecology Park - DMZ Where Nature Has Recovered",
        "content": "Goseong DMZ Peace Ecology Park is a demilitarized zone that has been opened to the public as an eco-tourism site where civilian access was restricted. Primitive nature has been preserved as it was for 70 years without human touch, where you can observe endangered flora and fauna. At the DMZ Museum you can learn about the history of division, and from the observatory you can look into North Korean territory. DMZ trekking programs walking along ecological trails are popular, and you can safely explore with guides. Nearby Hwajinpo Beach and Unification Observatory are also worth visiting."
    },
    "travel-029": {
        "title": "Mokpo Yudalsan - Night View Spot of the Port City",
        "content": "Yudalsan is a 228m mountain in downtown Mokpo, with strange rocks and various sculpture works throughout. It takes about 30 minutes to reach the summit, offering spectacular views of Mokpo coastal waters and islands of the archipelago sea. Especially the sunset time and night view are beautiful, popular as a dating course for couples. At the foot of the mountain are Mokpo Modern History and Culture Space and Mokpo Fish Market worth visiting together, and you can enjoy Mokpo's 9 flavors at restaurants. You can easily reach the summit using the cable car."
    },
    "travel-030": {
        "title": "Boseong Green Tea Fields - Green Waves of Tea Plantations",
        "content": "Boseong green tea fields are Korea's largest tea cultivation area, creating spectacular scenery with vast green tea fields filling the hills. Daehan Dawon and Korea Tea Sound Culture Park are representative tourist sites, where you can smell the fragrance of green tea walking along paths between tea fields. Spring's light green new shoots and the May Tea Scent Festival are especially beautiful, and you can taste green tea ice cream and green tea dishes. Boseong town's Beolgyo cockles are also famous local specialties, and nearby Yulpo Beach and Bibong Dinosaur Park are also worth visiting."
    },
    "travel-031": {
        "title": "Yongin Everland - Korea's Largest Theme Park",
        "content": "Everland is Korea's largest theme park in Yongin, a comprehensive entertainment resort combining various rides, zoo, and gardens. From thrilling rides like T-Express and Amazon Express to rides enjoyable for families, there's variety. At Lost Valley Safari you can observe lions, tigers, bears and other predators up close, and seasonal flower festivals are held with tulips, roses, chrysanthemums. At night, Moonlight Parade and fireworks are presented, and in winter a snow sledding area also operates."
    },
    "travel-032": {
        "title": "Daejeon Expo Science Park - Meeting of Science and Nature",
        "content": "Expo Science Park is a complex cultural space combining science museum and park where the 1993 Daejeon Expo was held. Hanbit Tower is Daejeon's landmark where you can view downtown Daejeon from the observatory, with beautiful night lighting. The National Science Museum operates various science exhibitions and experience programs, with science education programs for children being especially popular. With wide lawns and lakes inside the park, it's also good as a family picnic spot, with beautiful spring cherry blossoms and fall foliage. Daejeon Sungsimdang Bakery and Eurachachacha Buckwheat Kalguksu are nearby."
    },
    "travel-033": {
        "title": "Samcheok Hwanseongul Cave - Mysterious Limestone Cave Exploration",
        "content": "Hwanseongul is a limestone cave designated as a natural monument, the largest in Korea. Of its total 6.2km length, about 1.6km is open to the public, and the cave interior maintains 10-15°C year-round, cool in summer and warm in winter. Various limestone formations like stalactites, stalagmites, and stone pillars create fantastic scenery, with LED lighting creating a mysterious atmosphere. Cave exploration takes about 1.5 hours, requiring stamina due to many stairs. Nearby Daegeum Cave and Gwaneum Cave are also worth exploring, and Samcheok Ocean Cable Car and Samcheok Beach are worth visiting."
    },
    "travel-034": {
        "title": "Buyeo Gungnaji Pond - Baekje Royal Pond",
        "content": "Gungnaji is an artificial pond created during Baekje's King Mu period, a historic site recorded in Samguk Sagi as Korea's first artificial pond. With an island and pavilion in the middle of the pond, summer when lotus flowers bloom fully is most beautiful. Every July the Seodong Lotus Festival is held with colorful performances and experience programs. You can feel Baekje history walking along the pond's walking paths, and the atmosphere becomes even more elegant when night lighting turns on. Nearby Buyeo Jeongnimsa Temple 5-story Stone Pagoda and Busosanseong Fortress are also UNESCO World Heritage sites worth visiting."
    },
    "travel-035": {
        "title": "Cheongsong Jusangsan - Famous Mountain of Rock Cliffs",
        "content": "Jusangsan is a national park in Cheongsong, North Gyeongsang Province, a mountain with spectacular vertical cliffs and strange rocks. Jusangsan's representative course is about a 4-hour course passing 1-3 waterfalls along Juwang Valley to Juwangam Hermitage, with beautiful clear valleys and waterfalls. Fall foliage is especially famous, with the harmony of red-tinged rock cliffs and autumn leaves being spectacular. Jusanji Pond is a photo spot where submerged willow trees create a mysterious landscape, and Cheongsong apples and Cheongsong Korean beef are local specialties. You can also relieve climbing fatigue at Jusangsan Hot Springs."
    },
    "travel-036": {
        "title": "Taebaek Coal Mine Culture Village - Place Preserving Coal History",
        "content": "Taebaek Coal Museum and Coal Mine Culture Village are places where you can experience Korea's coal industry history. In the exhibition hall recreating actual coal mine tunnels, you can directly experience miners' working environment and learn about coal mining processes and history. Cheolam Coal Mine Village with houses crowded on hillsides and stilt buildings creates unique scenery, preserving the past coal mining village appearance intact. Taebaek has the most snow in Korea with beautiful winter snow scenes, and the Taebaek Mountain Snow Festival is also famous. Hwangji Pond and Gumunso are also worth visiting."
    },
    "travel-037": {
        "title": "Gochang Seonunsa Temple - Ancient Temple Where Camellias Bloom",
        "content": "Seonunsa is a thousand-year-old temple founded during Baekje period, famous for its camellia forest. Late March to early April when red camellias bloom fully is most beautiful, with the red carpet of fallen camellia petals also spectacular. Seonunsa Temple's Daeungjeon Hall and Stone Seated Jijang Bodhisattva are designated as treasures, and Dosolam Rock-carved Seated Buddha is famous as a giant rock-carved Buddha. The temple grounds have many cherry blossom and maple trees, especially beautiful in spring and fall. Nearby Gochang mudflats and Gochang Eupseong Fortress are also UNESCO World Heritage sites worth visiting."
    },
    "travel-038": {
        "title": "Namhae German Village - Village with Exotic Scenery",
        "content": "Namhae German Village is a village where miners and nurses dispatched to Germany in the 1960-70s settled after returning. German-style houses lined up on hills create exotic scenery as if in a European village. Located in a position overlooking Namhae's blue sea with good views, there are restaurants and cafes where you can taste traditional German food. Nearby Gacheon Darangyi Village is beautiful with terraced rice paddies, especially spectacular during May-June rice planting season and September-October golden waves. Namhae Geumsan Mountain and Sangju Silver Sand Beach are also worth visiting."
    },
    "travel-039": {
        "title": "Miryang Ice Valley - Mystery of Ice Forming Even in Midsummer",
        "content": "Miryang Ice Valley is a mysterious valley designated as a natural monument, where reverse phenomenon occurs with ice forming in rock crevices even in midsummer and warm air coming out in winter. Walking along the trail established along the valley, you can feel cool air, popular as a summer resort. Miryang Pyochungsa Temple is a temple honoring Samyeong Daesa who raised militia during the Imjin War, famous for its 3-story stone pagoda and Jeongryeogak pavilion. Nearby Yeongnam Alps' Cheonhwangsan and Jaeyaksan hiking courses are also popular, and Miryang pork soup and Miryang jujubes are local specialties."
    },
    "travel-040": {
        "title": "Yeongwol Donggang Rafting - Thrilling Experience in Pristine Valley",
        "content": "Donggang is one of Korea's cleanest pristine valleys, called the holy land of rafting. With rapids and gentle sections appropriately mixed, it's enjoyable from beginners to experienced rafters, rafting down a 14km section over about 2-3 hours. In summer you can enjoy thrilling adventure with cool water play, and the surrounding scenery is also excellent for enjoying nature. At Donggang Photo Museum you can view beautiful Donggang scenery in photographs, and Yeongwol Korean Peninsula Terrain and Cheongnyeongpo are also nearby worth visiting. Yeongwol gondeure namul bap (thistle rice) is also a must-try dish."
    },
    "travel-041": {
        "title": "Jeju Hamdeok Beach - Emerald Waters and Seowoobong Peak",
        "content": "Hamdeok Beach is a white sand beach in Jocheon-eup, Jeju City, popular with family travelers for its transparent emerald waters and shallow depth. Behind the beach, Seowoobong Peak is an oreum (parasitic volcano) you can climb in about 20 minutes, offering beautiful views of Hamdeok Beach and Jeju's northern coast from the summit. Beachside cafes abound, especially good for sunset time cafe terrace atmosphere. Nearby Gimnyeong Maze Park and Woljeong-ri Beach are also worth visiting, and at Jeju Haenyeo's House you can taste sea urchin seaweed soup and abalone porridge."
    },
    "travel-042": {
        "title": "Hwacheon Mountain Trout Festival - Ice Fishing in Winter",
        "content": "Hwacheon Mountain Trout Festival is Korea's representative winter festival held every January on frozen Hwacheoncheon Stream. Ice fishing by drilling holes in the frozen ice is the main program, and caught mountain trout can be eaten as sashimi or grilled on the spot. Various winter leisure sports and experience programs like bare-hand catching, sledding, and snow sculpture exhibitions are prepared, and nighttime ice rink experience on Milky Way Road is also popular. Warm clothing is essential due to cold weather, and there are many heated rest areas and food booths around the festival grounds for convenience."
    },
    "travel-043": {
        "title": "Wanju Daedunsan - Honam's Little Geumgangsan with Cloud Bridge",
        "content": "Daedunsan is a famous mountain called Honam's Little Geumgangsan, with beautiful strange rocks and ridges. The most famous section is the 81m long Cloud Bridge connecting Samseon Stairway to Macheon Platform, where you can feel thrilling at dizzying heights. You can take a cable car to the midpoint for easy summit access even for beginner hikers, and the sunset view from Nakjodae is spectacular. Fall foliage is especially beautiful, and traditional temples like Taegosa and Ansimsa are also located there. After hiking, nearby Samnye Cultural Arts Village and Gosan Natural Cheese Village are worth visiting."
    },
    "travel-044": {
        "title": "Paju Heyri Art Village - Artists' Creative Space",
        "content": "Heyri Art Village is a cultural art village in Paju where about 380 artists including writers, painters, and architects live and work. Unique buildings are throughout the village, with over 150 cultural spaces including galleries, museums, workshops, and book cafes concentrated. Various exhibitions and performances are held regularly, and on weekends you can also enjoy flea markets and street performances. With many stylish cafes and restaurants, it's popular as a dating course, and nearby Paju Publishing Complex, Imjingak, and Provence Village are also worth visiting."
    },
    "travel-045": {
        "title": "Muju Firefly Festival - Fireflies of Pristine Nature",
        "content": "Muju Firefly Festival is an ecology festival held every June in pristine Muju. At night, thousands of fireflies glow creating a fantastic sight, with firefly observation experiences and ecology learning programs operated. During the day you can enjoy various programs like firefly ecology hall tours, insect experiences, and traditional games, and the Moru Wine Tunnel and Namdaecheon Stream water play are also popular. Muju Guchen-dong Valley boasts 33 scenic spots, and Deogyusan's Hyangjokbong Peak snow scenery accessible by gondola is also famous. You can see fireflies year-round at Muju반디Land."
    },
    "travel-046": {
        "title": "Seoul Bukchon Hanok Village - Traditional Hanoks in the City",
        "content": "Bukchon Hanok Village is a traditional hanok village between Gyeongbokgung Palace and Changdeokgung Palace, preserving 600 years of history. Traditional hanoks line up along narrow alleys, where you can enjoy the harmony of Seoul's downtown skyline and hanoks centered on Bukchon 8 Views. Various cultural experiences are possible including traditional craft experiences, hanbok rentals, and hanok cafes, and Samcheong-dong street and Insa-dong are also walking distance. Since actual residents live there, quiet viewing is important. Spring cherry blossoms and fall foliage seasons are especially beautiful."
    },
    "travel-047": {
        "title": "Yeongdeok Snow Crab Street - Home of Fresh Snow Crabs",
        "content": "Yeongdeok is the home of snow crabs, with Ganggu Port Snow Crab Street lined with snow crab specialty restaurants. November to May is snow crab season, where you can taste fresh snow crabs at affordable prices. Cooked in various ways like steamed snow crab, snow crab soup, and grilled snow crab, the sweet and chewy crab meat taste is excellent. At Ganggu Port you can also watch fresh seafood auctions, and it's good for coastal drives along Yeongdeok Blue Road. Nearby Chuksan Port, Goraebul Beach, and Yeongdeok Wind Farm's white windmills are also attractions."
    },
    "travel-048": {
        "title": "Danyang Dodamsambong Peaks - Three Peaks of Namhan River",
        "content": "Dodamsambong are three strange rocks rising in the middle of Namhan River, ranked as the first of Danyang Eight Scenic Views. Three peaks floating on water create unique scenery, especially beautiful at sunset with silhouettes. There are photo zones where you can take pictures with Dodamsambong as background, and you can also view them up close on cruise boats. Nearby Seokmun, Gudambong, Oksunbong and other Danyang Eight Scenic Views are worth exploring together, and Gosu Cave and Ondal Fortress are worth visiting. Danyang garlic and Danyang Korean beef are also local specialties."
    },
    "travel-049": {
        "title": "Uiseong Sansuyu Village - Yellow Flower Waves",
        "content": "Uiseong Sagok-ri Sansuyu Village creates spectacular scenery when the entire village is covered with yellow sansuyu flowers in spring. Late March to early April is peak bloom, with sansuyu trees blooming golden flowers along village hills and alleys. You can enjoy spring atmosphere trekking along sansuyu flower paths, and special products like sansuyu tea and sansuyu makgeolli are sold. Uiseong is also famous for garlic, and during the Sansuyu Festival various experience programs and performances are held. Nearby Gounsa Temple and Uiseong Jomungo Historic Site are also good for historical exploration."
    },
    "travel-050": {
        "title": "Gimje Byeokgolje Reservoir - Thousand-Year Ancient Reservoir",
        "content": "Byeokgolje is Korea's oldest reservoir built in the 21st year of King Heulhae of Silla (330 AD), designated as a historic site. The embankment and water gate site built on vast plains remain, showing the history of Gimje plains. Every fall the Horizon Festival is held with various performances and experience programs against golden fields. At Byeokgolje Agricultural Culture Museum you can learn Korean agricultural culture history, and there are cultural properties like Surowang Tomb Site and Byeokgolje Stone Monument. Bicycle tours along Gimje Horizon Road are also popular."
    }
}

# Read the file
with open('data/knowledge-base.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply translations
for item in data:
    item_id = item['id']
    if item_id in translations:
        item['title'] = translations[item_id]['title']
        item['content'] = translations[item_id]['content']

# Write back
with open('data/knowledge-base.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ Successfully translated {len(translations)} records")
