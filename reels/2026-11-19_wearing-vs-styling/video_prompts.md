# Wearing vs Styling — 내 키프레임 9장 영상 프롬프트

> 내 키프레임 9장을 원본 영상과 비교하고, 9장을 시작/끝 프레임으로 쓰는 15초 영상 프롬프트를 짰어요.

| 항목 | 내용 |
|---|---|
| 길이 | 15.0초 · 클립 9개 (1.2~3.2초) |
| 착장 변경 | 브라렛 → 화이트 롱 튜브탑 · 부츠 → 처음에 벗었던 핑크 메리제인 힐을 다시 신음 |
| 방식 | 시작/끝 프레임 지정 영상 생성 (Kling, Veo, Seedance 등). 클립당 5초 안팎으로 만들고 편집에서 배속 + 점프컷 |
| 합성 | 오른쪽은 클립 C1~C9, 왼쪽은 15초 대기 클립 1개를 각각 중앙 50% 크롭해서 이어 붙이면 왼쪽이 끊기지 않음 |

## 원본 영상과 비교

| 내 이미지 | 원본 위치 | 장면 | 비교 |
|---|---|---|---|
| K01 | 0.00s | 오프닝 · 양쪽 동일 | 원본과 같음. 오른쪽은 팔을 옆으로 내리고, 왼쪽은 손을 앞으로 모음. |
| K02 | 1.30s | 힐 벗고 들기 | 원본은 오른손 하나로 힐을 들고, 내 이미지는 두 손으로 허리 앞에 들고 다리를 살짝 꼼. 흐름에는 문제없음. |
| K03 | 2.50s | 상체 허리까지 내림 | 브라렛이 화이트 롱 튜브탑으로 바뀜. 허리에 뭉친 원단을 잡은 포즈는 원본과 같음. |
| — | 4.40s | (없음) U넥 피나포어 단독 | 원본에 있는 '드레스를 뒤로 돌려 입은 직후' 장면이 9장에는 없음. 그래서 C3 한 클립 안에서 드레스 뒤집기와 블라우스 입기가 다 일어나야 함. 아래 '선택: C3 나누기'로 한 장 추가하면 더 자연스러움. |
| K04 | 5.60s | 블라우스 레이어링 | 원본과 같음. 양손으로 칼라 정리, 리본은 아직 풀린 상태, 네크라인 안쪽에 튜브탑이 보임. |
| K05 | 7.60s | 리본 완성 | 포즈는 원본과 같음. 다만 리본 꼬리가 밑단 아래까지 길게 내려오는데, K06~K09에서는 가슴 아래까지로 짧음. C5 프롬프트에 '리본을 다시 매만져 꼬리가 짧아지는' 동작을 넣어서 이어지게 했음. |
| K06 | 9.20s | 레이스 타이츠 | 원본과 같음. 신발 없이 타이츠만 신고 정자세. |
| K07 | 11.10s | 핑크 힐 다시 신고 허리 포즈 | 원본의 니하이 부츠 대신 처음에 벗었던 핑크 힐을 다시 신음. 원본은 짝다리, 내 이미지는 발목을 꼬고 섬. |
| K08 | 11.80s | 미니백 들기 | 원본과 같음. 가방을 윗손잡이로 들고 내려다봄. |
| K09 | 13.30s | 피날레 · 왼쪽이 쳐다봄 | 원본과 같음. 가방은 오른쪽 어깨, 손 모은 포즈, 왼쪽이 고개를 돌려 오른쪽을 봄. 15.0초까지 유지. |

## 영상 프롬프트

### C1 · 0.0–1.6s (1.6초) — 훅 + 힐 벗기 · K01 → K02

- 0.4초 동안 좌우 똑같이 정지 → 오른쪽만 무릎 들어 핑크 힐을 한 짝씩 차서 벗음 → 두 짝을 집어 허리 앞에 들고 내려다봄.

```text
Vertical 9:16 split-screen video, locked-off tripod, zero camera movement. The same bright white apartment continues across both halves (white kitchen with a stainless wall oven and dried flowers in a blue-grey vase on a dark stool behind the left half, a white paneled door with a black lever handle and a light-grey boucle sofa arm behind the right half, light oak floor, soft daylight, airy pastel-pink grade). Both halves show the same young East Asian woman as in the start image, with long dark-brown wavy hair parted in the middle, small gold hoop earrings, fair skin and soft natural makeup. LEFT HALF: she stays almost frozen in the plain pink tweed boucle sleeveless mini dress with white flecks, crew neck, princess seams, dropped waist, scalloped bubble skirt and frayed fringe trim and dusty-pink suede pointed-toe Mary Jane kitten heels with a thin buckle strap and slim clear heel, hands clasped in front, only breathing and blinking. RIGHT HALF: she holds still for a beat exactly like the left half, then lifts her right knee and kicks off her right dusty-pink suede Mary Jane kitten heel, then the left one, bends to pick both shoes up and holds them in front of her waist with both hands, barefoot, looking down at them with a small smile. Quick, natural, confident getting-ready movements; tweed, satin and lace move realistically; hands stay anatomically correct; face, hair and every garment detail match the start and end images exactly. One continuous shot.

Start image: K01. End image: K02.
```

### C2 · 1.6–3.0s (1.4초) — 상체 내리기 (튜브탑) · K02 → K03

- 힐을 프레임 오른쪽 밖으로 던짐 → 팔을 빼고 드레스 상체를 허리까지 내림 → 화이트 롱 튜브탑이 드러남 → 허리 원단을 잡고 내려다봄.

```text
Vertical 9:16 split-screen video, locked-off tripod, zero camera movement. The same bright white apartment continues across both halves (white kitchen with a stainless wall oven and dried flowers in a blue-grey vase on a dark stool behind the left half, a white paneled door with a black lever handle and a light-grey boucle sofa arm behind the right half, light oak floor, soft daylight, airy pastel-pink grade). Both halves show the same young East Asian woman as in the start image, with long dark-brown wavy hair parted in the middle, small gold hoop earrings, fair skin and soft natural makeup. LEFT HALF: she stays almost frozen in the plain pink tweed boucle sleeveless mini dress with white flecks, crew neck, princess seams, dropped waist, scalloped bubble skirt and frayed fringe trim and dusty-pink suede pointed-toe Mary Jane kitten heels with a thin buckle strap and slim clear heel, hands clasped in front, only breathing and blinking. RIGHT HALF: she tosses the pink heels out of frame to the right with a playful swing, crosses one arm over her chest to slip out of the armholes, and peels the pink tweed bodice down to her waist, revealing a smooth white strapless longline tube top; she ends gripping the folded tweed at her hips with both hands, looking down. Quick, natural, confident getting-ready movements; tweed, satin and lace move realistically; hands stay anatomically correct; face, hair and every garment detail match the start and end images exactly. One continuous shot.

Start image: K02. End image: K03.
```

### C3 · 3.0–6.2s (3.2초) — 드레스 뒤집기 + 블라우스 · K03 → K04

- 드레스를 허리에서 180° 돌려 다시 입음(U넥 피나포어) → 아이보리 블라우스를 들어 털어 펼침 → 피나포어 안에 입은 상태로 양손 칼라 정리. 9장 중 가장 긴 변화라 편집에서 점프컷 2~3번 넣기.

```text
Vertical 9:16 split-screen video, locked-off tripod, zero camera movement. The same bright white apartment continues across both halves (white kitchen with a stainless wall oven and dried flowers in a blue-grey vase on a dark stool behind the left half, a white paneled door with a black lever handle and a light-grey boucle sofa arm behind the right half, light oak floor, soft daylight, airy pastel-pink grade). Both halves show the same young East Asian woman as in the start image, with long dark-brown wavy hair parted in the middle, small gold hoop earrings, fair skin and soft natural makeup. LEFT HALF: she stays almost frozen in the plain pink tweed boucle sleeveless mini dress with white flecks, crew neck, princess seams, dropped waist, scalloped bubble skirt and frayed fringe trim and dusty-pink suede pointed-toe Mary Jane kitten heels with a thin buckle strap and slim clear heel, hands clasped in front, only breathing and blinking. RIGHT HALF: she rotates the whole dress 180 degrees around her waist, pulls it back up and slides her arms through the armholes so the low scooped back now sits in front as a deep U-neck pinafore over the white tube top; then she lifts an ivory satin blouse with a pointed collar, cascading ruffle jabot, long untied satin ribbon ties, balloon sleeves gathered at the forearm and knife-pleated flared cuffs and shakes it open; finally, already wearing it under the pinafore with the ribbons hanging loose, she raises both hands to her neck to straighten the collar, sleeves billowing out to the sides. Quick, natural, confident getting-ready movements; tweed, satin and lace move realistically; hands stay anatomically correct; face, hair and every garment detail match the start and end images exactly. One continuous shot.

Start image: K03. End image: K04.
```

### C4 · 6.2–7.9s (1.7초) — 소매 + 리본 · K04 → K05

- 팔을 내리며 벌룬 소매를 털어 플리츠 커프스를 펼침 → 칼라 앞 리본을 크게 묶음 → 손을 앞으로 모으고 미소.

```text
Vertical 9:16 split-screen video, locked-off tripod, zero camera movement. The same bright white apartment continues across both halves (white kitchen with a stainless wall oven and dried flowers in a blue-grey vase on a dark stool behind the left half, a white paneled door with a black lever handle and a light-grey boucle sofa arm behind the right half, light oak floor, soft daylight, airy pastel-pink grade). Both halves show the same young East Asian woman as in the start image, with long dark-brown wavy hair parted in the middle, small gold hoop earrings, fair skin and soft natural makeup. LEFT HALF: she stays almost frozen in the plain pink tweed boucle sleeveless mini dress with white flecks, crew neck, princess seams, dropped waist, scalloped bubble skirt and frayed fringe trim and dusty-pink suede pointed-toe Mary Jane kitten heels with a thin buckle strap and slim clear heel, hands clasped in front, only breathing and blinking. RIGHT HALF: she lowers her arms and shakes out the balloon sleeves so the knife-pleated cuffs flare, ties the long ivory satin ribbons into an oversized bow at her collar above the ruffle jabot, lets the tails fall down the front, and rests her hands clasped in front of her waist with a soft smile. Quick, natural, confident getting-ready movements; tweed, satin and lace move realistically; hands stay anatomically correct; face, hair and every garment detail match the start and end images exactly. One continuous shot.

Start image: K04. End image: K05.
```

### C5 · 7.9–9.6s (1.7초) — 레이스 타이츠 · K05 → K06

- 리본을 매만져 꼬리를 가슴 높이로 정리(K05와 K06 리본 길이 차이 연결) → 다리를 들어 레이스 타이츠를 신음 → 정자세로 미소.

```text
Vertical 9:16 split-screen video, locked-off tripod, zero camera movement. The same bright white apartment continues across both halves (white kitchen with a stainless wall oven and dried flowers in a blue-grey vase on a dark stool behind the left half, a white paneled door with a black lever handle and a light-grey boucle sofa arm behind the right half, light oak floor, soft daylight, airy pastel-pink grade). Both halves show the same young East Asian woman as in the start image, with long dark-brown wavy hair parted in the middle, small gold hoop earrings, fair skin and soft natural makeup. LEFT HALF: she stays almost frozen in the plain pink tweed boucle sleeveless mini dress with white flecks, crew neck, princess seams, dropped waist, scalloped bubble skirt and frayed fringe trim and dusty-pink suede pointed-toe Mary Jane kitten heels with a thin buckle strap and slim clear heel, hands clasped in front, only breathing and blinking. RIGHT HALF: she quickly re-adjusts the satin bow so its tails sit higher at mid-chest, then lifts her right leg and pulls sheer white lace tights with a diamond lattice and tiny bow pattern up to her thigh, switches legs, smooths them up under the bubble skirt, and stands straight with feet together, arms relaxed at her sides and the pleated cuffs draping, with a soft smile. Quick, natural, confident getting-ready movements; tweed, satin and lace move realistically; hands stay anatomically correct; face, hair and every garment detail match the start and end images exactly. One continuous shot.

Start image: K05. End image: K06.
```

### C6 · 9.6–11.4s (1.8초) — 핑크 힐 다시 신기 · K06 → K07

- 프레임 오른쪽에서 처음에 던졌던 핑크 힐을 다시 집어 옴 → 한 짝씩 신고 스트랩 채움 → 일어나 양손 허리 + 발목 꼬기.

```text
Vertical 9:16 split-screen video, locked-off tripod, zero camera movement. The same bright white apartment continues across both halves (white kitchen with a stainless wall oven and dried flowers in a blue-grey vase on a dark stool behind the left half, a white paneled door with a black lever handle and a light-grey boucle sofa arm behind the right half, light oak floor, soft daylight, airy pastel-pink grade). Both halves show the same young East Asian woman as in the start image, with long dark-brown wavy hair parted in the middle, small gold hoop earrings, fair skin and soft natural makeup. LEFT HALF: she stays almost frozen in the plain pink tweed boucle sleeveless mini dress with white flecks, crew neck, princess seams, dropped waist, scalloped bubble skirt and frayed fringe trim and dusty-pink suede pointed-toe Mary Jane kitten heels with a thin buckle strap and slim clear heel, hands clasped in front, only breathing and blinking. RIGHT HALF: she reaches to the right edge of the frame and picks up the same dusty-pink suede Mary Jane kitten heels she kicked off at the start, steps into them one at a time over the lace tights, bends to fasten the thin buckle straps, then straightens up, puts both hands on her hips with elbows out and crosses one ankle in front of the other with a confident smile. Quick, natural, confident getting-ready movements; tweed, satin and lace move realistically; hands stay anatomically correct; face, hair and every garment detail match the start and end images exactly. One continuous shot.

Start image: K06. End image: K07.
```

### C7 · 11.4–12.6s (1.2초) — 미니백 · K07 → K08

- 다리를 풀고 손을 허리에서 내림 → 프레임 오른쪽에서 크림 미니백을 윗손잡이로 집어 들고 내려다봄.

```text
Vertical 9:16 split-screen video, locked-off tripod, zero camera movement. The same bright white apartment continues across both halves (white kitchen with a stainless wall oven and dried flowers in a blue-grey vase on a dark stool behind the left half, a white paneled door with a black lever handle and a light-grey boucle sofa arm behind the right half, light oak floor, soft daylight, airy pastel-pink grade). Both halves show the same young East Asian woman as in the start image, with long dark-brown wavy hair parted in the middle, small gold hoop earrings, fair skin and soft natural makeup. LEFT HALF: she stays almost frozen in the plain pink tweed boucle sleeveless mini dress with white flecks, crew neck, princess seams, dropped waist, scalloped bubble skirt and frayed fringe trim and dusty-pink suede pointed-toe Mary Jane kitten heels with a thin buckle strap and slim clear heel, hands clasped in front, only breathing and blinking. RIGHT HALF: she uncrosses her ankles, drops her hands from her hips, reaches to the right edge of the frame and picks up a small cream leather flap bag with a gold twist-lock and a short top handle by its handle, holding it in front of her hip with her right hand and looking down at it with a soft smile. Quick, natural, confident getting-ready movements; tweed, satin and lace move realistically; hands stay anatomically correct; face, hair and every garment detail match the start and end images exactly. One continuous shot.

Start image: K07. End image: K08.
```

### C8 · 12.6–13.8s (1.2초) — 피날레 · K08 → K09

- 가방을 오른쪽 어깨에 메고 정리 → 손 모은 오프닝 포즈. 왼쪽은 후반에 천천히 고개를 돌려 오른쪽을 봄.

```text
Vertical 9:16 split-screen video, locked-off tripod, zero camera movement. The same bright white apartment continues across both halves (white kitchen with a stainless wall oven and dried flowers in a blue-grey vase on a dark stool behind the left half, a white paneled door with a black lever handle and a light-grey boucle sofa arm behind the right half, light oak floor, soft daylight, airy pastel-pink grade). Both halves show the same young East Asian woman as in the start image, with long dark-brown wavy hair parted in the middle, small gold hoop earrings, fair skin and soft natural makeup. LEFT HALF: she stays almost frozen in the plain pink tweed boucle sleeveless mini dress with white flecks, crew neck, princess seams, dropped waist, scalloped bubble skirt and frayed fringe trim and dusty-pink suede pointed-toe Mary Jane kitten heels with a thin buckle strap and slim clear heel, hands clasped in front, only breathing and blinking. RIGHT HALF: she slides the bag onto her right shoulder and settles into the opening pose with hands loosely clasped in front of her and a soft confident smile at the camera. EXCEPTION FOR THE LEFT HALF in this clip: in the second half, the left woman slowly turns her head toward the right half and looks at the styled version with an amused, impressed smile. Quick, natural, confident getting-ready movements; tweed, satin and lace move realistically; hands stay anatomically correct; face, hair and every garment detail match the start and end images exactly. One continuous shot.

Start image: K08. End image: K09.
```

### C9 · 13.8–15.0s (1.2초) — 홀드 + 루프 · K09 → K09

- 둘 다 거의 정지. 오른쪽은 미소 유지, 왼쪽은 계속 쳐다보다가 마지막 0.3초에 정면으로 돌아옴 → K01로 루프.

```text
Vertical 9:16 split-screen video, locked-off tripod, zero camera movement. The same bright white apartment continues across both halves (white kitchen with a stainless wall oven and dried flowers in a blue-grey vase on a dark stool behind the left half, a white paneled door with a black lever handle and a light-grey boucle sofa arm behind the right half, light oak floor, soft daylight, airy pastel-pink grade). Both halves show the same young East Asian woman as in the start image, with long dark-brown wavy hair parted in the middle, small gold hoop earrings, fair skin and soft natural makeup. LEFT HALF: she stays almost frozen in the plain pink tweed boucle sleeveless mini dress with white flecks, crew neck, princess seams, dropped waist, scalloped bubble skirt and frayed fringe trim and dusty-pink suede pointed-toe Mary Jane kitten heels with a thin buckle strap and slim clear heel, hands clasped in front, only breathing and blinking. RIGHT HALF: she holds the final pose with a confident closed-mouth smile and only the slightest natural sway. EXCEPTION FOR THE LEFT HALF in this clip: the left woman keeps looking at the right half with an amused smile, and only in the very last moment turns her head back to face the camera. Quick, natural, confident getting-ready movements; tweed, satin and lace move realistically; hands stay anatomically correct; face, hair and every garment detail match the start and end images exactly. One continuous shot.

Start image: K09. Use K09 as both start and end image (hold).
```

## 선택: C3 나누기 (K03.5 한 장 추가)

### K03.5 이미지 프롬프트 (K03 첨부해서 편집)

```text
Edit the attached image (K03). Keep everything else identical: the left half, the room, the camera framing, the lighting, and the right woman's face, hair, body and bare feet. Change only the right woman's outfit and pose: the pink tweed dress is now pulled back up and worn backwards as a deep U-neck pinafore, with the smooth white strapless longline tube top showing inside the scooped neckline; the same scalloped bubble skirt and frayed trim. Her right hand rests at the center of the neckline adjusting it, her left hand smooths the skirt at her hip, she looks down at the neckline with a small smile, feet together.
```

### C3a · 3.0–4.8s — 드레스 뒤집기 · K03 → K03.5

- 드레스를 180° 돌려 다시 입어 U넥 피나포어 완성 (튜브탑 위).

```text
Vertical 9:16 split-screen video, locked-off tripod, zero camera movement. The same bright white apartment continues across both halves (white kitchen with a stainless wall oven and dried flowers in a blue-grey vase on a dark stool behind the left half, a white paneled door with a black lever handle and a light-grey boucle sofa arm behind the right half, light oak floor, soft daylight, airy pastel-pink grade). Both halves show the same young East Asian woman as in the start image, with long dark-brown wavy hair parted in the middle, small gold hoop earrings, fair skin and soft natural makeup. LEFT HALF: she stays almost frozen in the plain pink tweed boucle sleeveless mini dress with white flecks, crew neck, princess seams, dropped waist, scalloped bubble skirt and frayed fringe trim and dusty-pink suede pointed-toe Mary Jane kitten heels with a thin buckle strap and slim clear heel, hands clasped in front, only breathing and blinking. RIGHT HALF: she rotates the whole dress 180 degrees around her waist, pulls it back up and slides her arms through the armholes so the low scooped back now sits in front as a deep U-neck pinafore over the white tube top, and smooths the neckline with one hand. Quick, natural, confident getting-ready movements; tweed, satin and lace move realistically; hands stay anatomically correct; face, hair and every garment detail match the start and end images exactly. One continuous shot.

Start image: K03. End image: K03.5.
```

### C3b · 4.8–6.2s — 블라우스 · K03.5 → K04

- 아이보리 블라우스를 들어 털어 펼침 → 피나포어 안에 입은 상태로 양손 칼라 정리.

```text
Vertical 9:16 split-screen video, locked-off tripod, zero camera movement. The same bright white apartment continues across both halves (white kitchen with a stainless wall oven and dried flowers in a blue-grey vase on a dark stool behind the left half, a white paneled door with a black lever handle and a light-grey boucle sofa arm behind the right half, light oak floor, soft daylight, airy pastel-pink grade). Both halves show the same young East Asian woman as in the start image, with long dark-brown wavy hair parted in the middle, small gold hoop earrings, fair skin and soft natural makeup. LEFT HALF: she stays almost frozen in the plain pink tweed boucle sleeveless mini dress with white flecks, crew neck, princess seams, dropped waist, scalloped bubble skirt and frayed fringe trim and dusty-pink suede pointed-toe Mary Jane kitten heels with a thin buckle strap and slim clear heel, hands clasped in front, only breathing and blinking. RIGHT HALF: she lifts an ivory satin blouse with a pointed collar, cascading ruffle jabot, long untied satin ribbon ties, balloon sleeves gathered at the forearm and knife-pleated flared cuffs into frame and shakes it open in front of her; then, already wearing it under the pinafore with the ribbons hanging loose, she raises both hands to her neck to straighten the collar, sleeves billowing out to the sides. Quick, natural, confident getting-ready movements; tweed, satin and lace move realistically; hands stay anatomically correct; face, hair and every garment detail match the start and end images exactly. One continuous shot.

Start image: K03.5. End image: K04.
```

## L · 왼쪽 대기 클립 (15초)

```text
Vertical 9:16 video, 15 seconds, locked-off tripod, zero camera movement. Bright white apartment: white shaker kitchen cabinets, a stainless wall oven, dried flowers in a blue-grey vase on a dark wood stool, light oak floor, soft daylight. The same young East Asian woman as in the start image, with long dark-brown wavy hair parted in the middle, small gold hoop earrings, fair skin and soft natural makeup stands still and upright facing the camera in a plain pink tweed boucle sleeveless mini dress with white flecks, crew neck, princess seams, dropped waist, scalloped bubble skirt and frayed fringe trim and dusty-pink suede pointed-toe Mary Jane kitten heels with a thin buckle strap and slim clear heel, hands loosely clasped in front of her hips, calm face with a faint smile. For most of the clip she only breathes, blinks and sways very slightly. At about 13 seconds she slowly turns her head to her left (toward screen right) and looks sideways with an amused smile, and in the last moment turns back to face the camera.
```

## 편집

| 항목 | 내용 |
|---|---|
| 클립 길이 | C1 1.6초 · C2 1.4초 · C3 3.2초 · C4 1.7초 · C5 1.7초 · C6 1.8초 · C7 1.2초 · C8 1.2초 · C9 1.2초 = 15.0초. C3을 나누면 C3a 1.8초 + C3b 1.4초. |
| 속도·컷 | 클립을 5초 안팎으로 생성 → 1.5~2배속 + 점프컷 1~2번으로 위 길이에 맞춤. 원본도 오른쪽은 0.4~0.7초마다 점프컷이라 잘라낸 티가 나도 자연스러움. |
| 좌우 합성 | 9:16 캔버스에 왼쪽 대기 클립(L)을 왼쪽 50%, C1~C9를 오른쪽 50%로 크롭해서 배치. 클립마다 왼쪽이 살짝 달라지는 문제가 없어짐. 귀찮으면 C1~C9를 통째로 이어 붙여도 됨. |
| 비트 | 약 120BPM, 1초마다 강박. 힐 던지는 순간(약 2초), 피나포어 완성(약 4.8초), 리본 완성(7.9초), 힐 다시 신기 끝(11.4초), 가방(12.6초)을 강박에 맞추기. |
| 마무리 | 13.8~15.0초는 피날레 홀드. 왼쪽이 마지막에 정면으로 돌아오면 첫 프레임(K01)으로 루프가 자연스럽게 이어짐. |
