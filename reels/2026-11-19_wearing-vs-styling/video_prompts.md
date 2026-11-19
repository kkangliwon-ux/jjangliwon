# Wearing vs Styling — 내 키프레임 9장 영상 프롬프트

> 내 키프레임 9장을 원본 영상과 비교하고, 9장을 시작/끝 프레임으로 쓰는 3초짜리 영상 프롬프트 8개를 짰어요.

| 항목 | 내용 |
|---|---|
| 길이 | 클립 8개 × 3초 = 24초 · 15초로 쓰려면 편집에서 1.6배속 |
| 착장 변경 | 브라렛 → 화이트 롱 튜브탑 · 부츠 → 처음에 벗었던 핑크 메리제인 힐을 다시 신음 |
| 방식 | 시작/끝 프레임 지정 영상 생성, 클립당 3초 |
| 합성 | 오른쪽은 C1~C8, 왼쪽은 대기 클립 1개를 각각 중앙 50% 크롭해서 이어 붙이면 왼쪽이 끊기지 않음 |

## 원본 영상과 비교

| 내 이미지 | 원본 위치 | 장면 | 비교 |
|---|---|---|---|
| K01 | 0.00s | 오프닝 · 양쪽 동일 | 원본과 같음. 오른쪽은 팔을 옆으로 내리고, 왼쪽은 손을 앞으로 모음. |
| K02 | 1.30s | 힐 벗고 들기 | 원본은 오른손 하나로 힐을 들고, 내 이미지는 두 손으로 허리 앞에 들고 다리를 살짝 꼼. 흐름에는 문제없음. |
| K03 | 2.50s | 상체 허리까지 내림 | 브라렛이 화이트 롱 튜브탑으로 바뀜. 허리에 뭉친 원단을 잡은 포즈는 원본과 같음. |
| — | 4.40s | (없음) U넥 피나포어 단독 | 원본에 있는 '드레스를 뒤로 돌려 입은 직후' 장면 없이 진행. C3 한 클립에서 드레스 뒤집기와 블라우스가 한 번에 바뀜. |
| K04 | 5.60s | 블라우스 레이어링 | 원본과 같음. 양손으로 칼라 정리, 리본은 아직 풀린 상태, 네크라인 안쪽에 튜브탑이 보임. |
| K05 | 7.60s | 리본 완성 | 포즈는 원본과 같음. 다만 리본 꼬리가 밑단 아래까지 길게 내려오는데, K06~K09에서는 가슴 아래까지로 짧음. C5 프롬프트에 '리본을 다시 매만져 꼬리가 짧아지는' 동작을 넣어서 이어지게 했음. |
| K06 | 9.20s | 레이스 타이츠 | 원본과 같음. 신발 없이 타이츠만 신고 정자세. |
| K07 | 11.10s | 핑크 힐 다시 신고 허리 포즈 | 원본의 니하이 부츠 대신 처음에 벗었던 핑크 힐을 다시 신음. 원본은 짝다리, 내 이미지는 발목을 꼬고 섬. |
| K08 | 11.80s | 미니백 들기 | 원본과 같음. 가방을 윗손잡이로 들고 내려다봄. |
| K09 | 13.30s | 피날레 · 왼쪽이 쳐다봄 | 원본과 같음. 가방은 오른쪽 어깨, 손 모은 포즈, 왼쪽이 고개를 돌려 오른쪽을 봄. 마지막 프레임. |

## 영상 프롬프트

### C1 · 0.0–3.0s (3.0초) — 힐 벗기 · K01 → K02

- 잠깐 좌우 똑같이 정지 → 핑크 힐을 한 짝씩 차서 벗음 → 두 짝 집어 허리 앞에 들고 내려다봄.

```text
3-second vertical 9:16 split-screen clip, locked-off tripod, no camera movement. The same bright white apartment continues across both halves (white kitchen and dried flowers behind the left, white paneled door and grey boucle sofa behind the right, light oak floor, soft daylight, pastel-pink grade). Both halves show the same young East Asian woman as in the start image, with long dark-brown wavy hair parted in the middle, small gold hoop earrings, fair skin and soft natural makeup. LEFT HALF: she stays still in the plain pink tweed bubble mini dress and dusty-pink Mary Jane heels, hands clasped in front, only breathing and blinking. RIGHT HALF: after a brief still moment matching the left half, she kicks off both dusty-pink suede Mary Jane heels one after the other, bends, picks them up and holds them in front of her waist with both hands, barefoot, smiling down at them. Brisk, natural movements that fit in three seconds; tweed, satin and lace move realistically; hands stay anatomically correct; face, hair and every garment detail match the start and end images exactly.

Start image: K01. End image: K02.
```

### C2 · 3.0–6.0s (3.0초) — 상체 내리기 (튜브탑) · K02 → K03

- 힐을 0.5초 만에 던짐 → 오른손으로 왼쪽 어깨끈을 밀어 팔 아래로 내리고 왼팔을 진동에서 빼냄 → 오른팔도 같은 방식 → 빈 상체(둥근 목선 + 빈 진동 2개)를 허리까지 밀어 내려 뒤집힌 덮개로 접음 → 그때 튜브탑이 보임 → 양손 허리. 생성 영상에서 드레스가 스트랩리스로 바뀌던 문제를 막는 문장을 넣음.

```text
3-second vertical 9:16 split-screen clip, locked-off tripod, no camera movement. The same bright white apartment continues across both halves (white kitchen and dried flowers behind the left, white paneled door and grey boucle sofa behind the right, light oak floor, soft daylight, pastel-pink grade). Both halves show the same young East Asian woman as in the start image, with long dark-brown wavy hair parted in the middle, small gold hoop earrings, fair skin and soft natural makeup. LEFT HALF: she stays still in the plain pink tweed bubble mini dress and dusty-pink Mary Jane heels, hands clasped in front, only breathing and blinking.

RIGHT HALF, one continuous action, like taking off the top half of a sleeveless jumpsuit:
0.0-0.5s: she quickly tosses the pink heels out of frame to the right.
0.5-1.4s: LEFT ARM OUT. Her right hand grabs the left shoulder of the sleeveless tweed bodice and pushes it sideways off her left shoulder and down her upper arm; she bends her left elbow and pulls her left forearm and hand back out through the armhole. Her left arm is now bare and outside the dress, and the empty left half of the bodice hangs loose.
1.4-2.0s: RIGHT ARM OUT. Her left hand pushes the right shoulder of the bodice off her right shoulder and down her arm, and she pulls her right arm out through the right armhole the same way. Both arms are now outside the dress; the whole bodice, still with its round crew neckline and two empty armholes, hangs loose in front of her chest.
2.0-3.0s: she pushes the empty bodice down to her waist; it flips inside out and drapes over the top of the bubble skirt as a folded flap, revealing the smooth white strapless longline tube top underneath. She ends gripping the folded tweed at her hips with both hands, elbows out, looking down, as in the end image.

Key details: the shoulders and armholes of the bodice stay visible and travel down her arms; the bodice comes off by its shoulders, it is never peeled down from the neckline; the round crew neckline never turns into a straight strapless edge; the dress is never strapless while she still wears the bodice; the bubble skirt stays unchanged; the tube top only shows once the bodice has dropped below her chest. Realistic tweed weight, hands anatomically correct, face and hair identical to the start and end images.

Start image: K02. End image: K03.
```

**네거티브 프롬프트 (입력칸이 있으면)**

```text
dress becoming strapless, shoulder straps disappearing, neckline turning into a straight band, rolling the dress down like a tube, arms staying inside the dress, morphing, sudden outfit change, garment swap, tube top appearing instantly, skirt changing shape, flickering, extra arms, extra hands, deformed fingers, camera movement
```

### C3 · 6.0–9.0s (3.0초) — 드레스 뒤집기 + 블라우스 · K03 → K04

- 드레스를 허리에서 돌려 U넥 피나포어로 다시 입음 → 안에 블라우스를 입은 상태로 양손 칼라 정리. 9장 중 변화가 가장 큰 구간.

```text
3-second vertical 9:16 split-screen clip, locked-off tripod, no camera movement. The same bright white apartment continues across both halves (white kitchen and dried flowers behind the left, white paneled door and grey boucle sofa behind the right, light oak floor, soft daylight, pastel-pink grade). Both halves show the same young East Asian woman as in the start image, with long dark-brown wavy hair parted in the middle, small gold hoop earrings, fair skin and soft natural makeup. LEFT HALF: she stays still in the plain pink tweed bubble mini dress and dusty-pink Mary Jane heels, hands clasped in front, only breathing and blinking. RIGHT HALF: she spins the dress around her waist and pulls it back up as a deep U-neck pinafore over the tube top; then, now wearing an ivory satin blouse with a pointed collar, cascading ruffle jabot, loose untied satin ribbon ties, balloon sleeves gathered at the forearm and knife-pleated flared cuffs underneath, she raises both hands to her neck to straighten the collar, sleeves billowing out to the sides. Brisk, natural movements that fit in three seconds; tweed, satin and lace move realistically; hands stay anatomically correct; face, hair and every garment detail match the start and end images exactly.

Start image: K03. End image: K04.
```

### C4 · 9.0–12.0s (3.0초) — 소매 + 리본 · K04 → K05

- 팔을 내리며 소매를 털어 플리츠 커프스를 펼침 → 칼라 앞 리본을 크게 묶음 → 손을 앞으로 모으고 미소.

```text
3-second vertical 9:16 split-screen clip, locked-off tripod, no camera movement. The same bright white apartment continues across both halves (white kitchen and dried flowers behind the left, white paneled door and grey boucle sofa behind the right, light oak floor, soft daylight, pastel-pink grade). Both halves show the same young East Asian woman as in the start image, with long dark-brown wavy hair parted in the middle, small gold hoop earrings, fair skin and soft natural makeup. LEFT HALF: she stays still in the plain pink tweed bubble mini dress and dusty-pink Mary Jane heels, hands clasped in front, only breathing and blinking. RIGHT HALF: she lowers her arms, shakes out the balloon sleeves so the knife-pleated cuffs flare, ties the satin ribbons into an oversized bow at her collar above the ruffle jabot, and rests her hands clasped in front of her waist with a soft smile. Brisk, natural movements that fit in three seconds; tweed, satin and lace move realistically; hands stay anatomically correct; face, hair and every garment detail match the start and end images exactly.

Start image: K04. End image: K05.
```

### C5 · 12.0–15.0s (3.0초) — 레이스 타이츠 · K05 → K06

- 리본 꼬리를 가슴 높이로 정리(K05와 K06 리본 길이 차이 연결) → 한쪽씩 레이스 타이츠 신기 → 정자세로 미소.

```text
3-second vertical 9:16 split-screen clip, locked-off tripod, no camera movement. The same bright white apartment continues across both halves (white kitchen and dried flowers behind the left, white paneled door and grey boucle sofa behind the right, light oak floor, soft daylight, pastel-pink grade). Both halves show the same young East Asian woman as in the start image, with long dark-brown wavy hair parted in the middle, small gold hoop earrings, fair skin and soft natural makeup. LEFT HALF: she stays still in the plain pink tweed bubble mini dress and dusty-pink Mary Jane heels, hands clasped in front, only breathing and blinking. RIGHT HALF: she tucks the long bow tails up to mid-chest, lifts one leg and pulls on sheer white lace tights with a diamond lattice and tiny bow pattern, then the other leg, smooths them under the bubble skirt and stands straight with arms at her sides and a soft smile. Brisk, natural movements that fit in three seconds; tweed, satin and lace move realistically; hands stay anatomically correct; face, hair and every garment detail match the start and end images exactly.

Start image: K05. End image: K06.
```

### C6 · 15.0–18.0s (3.0초) — 핑크 힐 다시 신기 · K06 → K07

- 프레임 오른쪽에서 처음에 던진 핑크 힐을 다시 집어 옴 → 타이츠 위에 신음 → 양손 허리 + 발목 꼬기.

```text
3-second vertical 9:16 split-screen clip, locked-off tripod, no camera movement. The same bright white apartment continues across both halves (white kitchen and dried flowers behind the left, white paneled door and grey boucle sofa behind the right, light oak floor, soft daylight, pastel-pink grade). Both halves show the same young East Asian woman as in the start image, with long dark-brown wavy hair parted in the middle, small gold hoop earrings, fair skin and soft natural makeup. LEFT HALF: she stays still in the plain pink tweed bubble mini dress and dusty-pink Mary Jane heels, hands clasped in front, only breathing and blinking. RIGHT HALF: she picks the same dusty-pink Mary Jane heels back up from the right edge of the frame, steps into them over the lace tights, then straightens up with both hands on her hips and one ankle crossed in front of the other, smiling confidently. Brisk, natural movements that fit in three seconds; tweed, satin and lace move realistically; hands stay anatomically correct; face, hair and every garment detail match the start and end images exactly.

Start image: K06. End image: K07.
```

### C7 · 18.0–21.0s (3.0초) — 미니백 · K07 → K08

- 다리 풀고 손을 내림 → 프레임 오른쪽에서 크림 미니백을 윗손잡이로 집어 들고 내려다봄.

```text
3-second vertical 9:16 split-screen clip, locked-off tripod, no camera movement. The same bright white apartment continues across both halves (white kitchen and dried flowers behind the left, white paneled door and grey boucle sofa behind the right, light oak floor, soft daylight, pastel-pink grade). Both halves show the same young East Asian woman as in the start image, with long dark-brown wavy hair parted in the middle, small gold hoop earrings, fair skin and soft natural makeup. LEFT HALF: she stays still in the plain pink tweed bubble mini dress and dusty-pink Mary Jane heels, hands clasped in front, only breathing and blinking. RIGHT HALF: she uncrosses her ankles, drops her hands, picks up a small cream leather flap bag with a gold twist-lock and a short top handle from the right edge of the frame and holds it by the handle in front of her hip, looking down at it with a soft smile. Brisk, natural movements that fit in three seconds; tweed, satin and lace move realistically; hands stay anatomically correct; face, hair and every garment detail match the start and end images exactly.

Start image: K07. End image: K08.
```

### C8 · 21.0–24.0s (3.0초) — 피날레 · K08 → K09

- 가방을 오른쪽 어깨에 메고 손 모은 포즈로 미소. 왼쪽은 마지막 1초에 고개를 돌려 오른쪽을 봄.

```text
3-second vertical 9:16 split-screen clip, locked-off tripod, no camera movement. The same bright white apartment continues across both halves (white kitchen and dried flowers behind the left, white paneled door and grey boucle sofa behind the right, light oak floor, soft daylight, pastel-pink grade). Both halves show the same young East Asian woman as in the start image, with long dark-brown wavy hair parted in the middle, small gold hoop earrings, fair skin and soft natural makeup. LEFT HALF: she stays still in the plain pink tweed bubble mini dress and dusty-pink Mary Jane heels, hands clasped in front, only breathing and blinking. RIGHT HALF: she slides the bag onto her right shoulder and settles into a hands-clasped pose with a confident smile at the camera. EXCEPTION FOR THE LEFT HALF: in the last second, the left woman turns her head toward the right half and looks at her with an amused, impressed smile. Brisk, natural movements that fit in three seconds; tweed, satin and lace move realistically; hands stay anatomically correct; face, hair and every garment detail match the start and end images exactly.

Start image: K08. End image: K09.
```

## 선택: C2 나누기

고친 C2로도 팔이 안 빠지면, 팔을 다 뺀 중간 이미지(K02.5)를 한 장 만들어서 C2a(팔 빼기) + C2b(접어 내리기) 두 클립으로 나누기. 동작이 작아져서 시작/끝 프레임 방식이 훨씬 잘 따라옴.

### K02.5 · 이미지 프롬프트 (K03 첨부해서 편집)

```text
Edit the attached image (K03). Keep everything else identical: the left half, the room, the camera framing, the lighting, and the right woman's face, hair, body, bare feet and bubble skirt. Change only the right woman's upper body: both of her bare arms are outside the dress, and the empty pink tweed bodice, with its round crew neckline and two empty armholes clearly visible, hangs loosely down in front of her stomach, not yet folded; her right hand holds the bodice at her left hip, her left hand rests at her waist. The top part of the smooth white strapless longline tube top shows above the hanging bodice. She looks down at the bodice.
```

### C2a · 3.0–4.8s — 힐 던지기 + 팔 빼기 · K02 → K02.5

- 힐을 던지고 → 왼팔, 오른팔 순서로 진동에서 빼서 빈 상체가 가슴 앞에 늘어진 상태까지.

```text
3-second vertical 9:16 split-screen clip, locked-off tripod, no camera movement. The same bright white apartment continues across both halves (white kitchen and dried flowers behind the left, white paneled door and grey boucle sofa behind the right, light oak floor, soft daylight, pastel-pink grade). Both halves show the same young East Asian woman as in the start image, with long dark-brown wavy hair parted in the middle, small gold hoop earrings, fair skin and soft natural makeup. LEFT HALF: she stays still in the plain pink tweed bubble mini dress and dusty-pink Mary Jane heels, hands clasped in front, only breathing and blinking. RIGHT HALF: she quickly tosses the pink heels out of frame to the right; then her right hand pushes the left shoulder of the sleeveless tweed bodice off her shoulder and down her arm and she pulls her left arm out through the armhole; then she does the same with her right arm. Both arms end bare and outside the dress, and the empty bodice, with its round crew neckline and two empty armholes, hangs loose in front of her stomach. The bodice comes off by its shoulders and never turns strapless. Brisk, natural movements that fit in three seconds; tweed, satin and lace move realistically; hands stay anatomically correct; face, hair and every garment detail match the start and end images exactly.

Start image: K02. End image: K02.5.
```

### C2b · 4.8–6.0s — 접어 내리기 · K02.5 → K03

- 늘어진 상체를 허리까지 밀어 내려 뒤집힌 덮개로 접고 → 양손으로 허리를 잡음.

```text
3-second vertical 9:16 split-screen clip, locked-off tripod, no camera movement. The same bright white apartment continues across both halves (white kitchen and dried flowers behind the left, white paneled door and grey boucle sofa behind the right, light oak floor, soft daylight, pastel-pink grade). Both halves show the same young East Asian woman as in the start image, with long dark-brown wavy hair parted in the middle, small gold hoop earrings, fair skin and soft natural makeup. LEFT HALF: she stays still in the plain pink tweed bubble mini dress and dusty-pink Mary Jane heels, hands clasped in front, only breathing and blinking. RIGHT HALF: she pushes the hanging empty bodice down to her waist; it flips inside out and drapes over the top of the bubble skirt as a folded flap, fully revealing the white strapless longline tube top; she ends gripping the folded tweed at her hips with both hands, elbows out, looking down. The bubble skirt stays unchanged. Brisk, natural movements that fit in three seconds; tweed, satin and lace move realistically; hands stay anatomically correct; face, hair and every garment detail match the start and end images exactly.

Start image: K02.5. End image: K03.
```

## L · 왼쪽 대기 클립 (24초)

```text
Vertical 9:16 video, 24 seconds, locked-off tripod, zero camera movement. Bright white apartment: white shaker kitchen cabinets, a stainless wall oven, dried flowers in a blue-grey vase on a dark wood stool, light oak floor, soft daylight. The same young East Asian woman as in the start image, with long dark-brown wavy hair parted in the middle, small gold hoop earrings, fair skin and soft natural makeup stands still and upright facing the camera in a plain pink tweed boucle sleeveless mini dress with white flecks, crew neck, princess seams, dropped waist, scalloped bubble skirt and frayed fringe trim and dusty-pink suede pointed-toe Mary Jane kitten heels with a thin buckle strap and slim clear heel, hands loosely clasped in front of her hips, calm face with a faint smile. For most of the clip she only breathes, blinks and sways very slightly. In the last two seconds she slowly turns her head to her left (toward screen right) and looks sideways with an amused smile.
```

## 편집

| 항목 | 내용 |
|---|---|
| 클립 길이 | C1~C8 각 3초 = 24초. |
| 15초로 맞추기 | 전체를 1.6배속 하거나, 클립마다 앞뒤를 잘라 1.9초 안팎으로 줄이기. 원본도 오른쪽이 점프컷이라 잘라낸 티가 나도 자연스러움. |
| 좌우 합성 | 왼쪽 대기 클립(L)을 왼쪽 50%, C1~C8을 오른쪽 50%로 크롭해서 배치하면 클립이 바뀔 때 왼쪽이 튀지 않음. 귀찮으면 C1~C8을 통째로 이어 붙여도 됨. |
| 비트 | 약 120BPM, 1초마다 강박. 힐 던지는 순간, 피나포어 완성, 리본 완성, 힐 다시 신기, 가방 메기를 강박에 맞추기. |
| 마무리 | 마지막 K09 프레임을 1초 정도 정지시키면 첫 프레임(K01)으로 루프가 자연스럽게 이어짐. |
