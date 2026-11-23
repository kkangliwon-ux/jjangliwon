# ootdki 모델 × 팬톤 컬러칩 포맷 · 키프레임 프롬프트 (여름 · 말레이시아 착장)

원본 레퍼런스: 9:16, 720×1280, 11.1초, 4 Looks.
포맷 그대로 유지: 흰 배경 + 누끼 모델 전신, 등 뒤에 기울어진 팬톤 컬러칩 3장(위=아우터 색 / 가운데=이너 색 / 아래=하의·신발 색), 화면 맨 아래 부채꼴 팬톤 컬러 가이드. 룩 전환 때는 모델이 흑백으로 빠지고 뒤돌거나 옆으로 걸으면서 컬러칩이 날아 들어오며 색이 입혀짐.
바뀐 것: 모델은 ootdki 모델(@Model), 착장은 2026 여름 인기 스타일 4종.

착장 기준 (말레이시아): 30도 넘는 습한 날씨 → 리넨·코튼·얇은 니트 같은 통기성 소재. 몰·카페·사무실 에어컨이 세서 얇은 가디건/블레이저/셔츠를 한 겹 걸치는 구성(원본 포맷도 룩마다 아우터가 있음). 노출은 과하지 않게, 시내에서 무난하게 입을 수 있는 길이.

| Look | 스타일 (2026 여름 인기) | 컬러칩 3장 (위 / 가운데 / 아래) |
|---|---|---|
| 1 | 리넨 테일러링 · 얇은 리넨 블레이저 + 버뮤다 쇼츠 | Sand #D6C3A5 / Off-White #F4F2EC / Tan #A8744F |
| 2 | 콘플라워 블루 · 얇은 니트 가디건 + 아일렛 캐미 + 새틴 미디스커트 | Cornflower #6F8FD8 / White #FFFFFF / Navy #1F2A55 |
| 3 | 버터옐로 × 초콜릿 · 시스루 오버셔츠 + 홀터 + 리넨 와이드 팬츠 | Butter Yellow #F3E3A2 / Chocolate #5A3A2A / Ivory #EFE9DC |
| 4 | 스포티 시크 · 얇은 나일론 트랙 자켓 + 러닝 쇼츠 | Cherry Red #B5121B / Sky Blue #A9CBE8 / Olive #6B6B3A |

## 사용법
- 모든 프롬프트에 **@Model** (ootdki 모델 레퍼런스 사진)을 첨부하세요. 원본 영상 프레임 캡처를 **@Format**으로 같이 넣으면 컬러칩 배치·여백이 가장 정확하게 나옵니다. (배경은 흰색이라 @Background는 안 씁니다.)
- 컬러칩 라벨의 "PANTONE ○○-○○○○ TCX" 글자는 AI가 뭉개기 쉬워요. 이미지에선 라벨 띠만 받고, 코드는 편집에서 얹는 걸 권장합니다.
- 흑백 컷(KF01, KF03, KF05, KF07)은 컬러로 뽑은 뒤 편집에서 모델만 채도 0으로 빼면 색이 입혀지는 전환을 더 깔끔하게 만들 수 있어요.
- 9:16, seed 고정, 모델 크기·위치를 컷마다 맞추세요.

## 공통 블록 (모든 프롬프트 앞에 붙이기)
```
Vertical 9:16 fashion color-palette lookbook frame. Pure seamless white background. The woman is exactly the person in @Model: same face, hair, skin tone, body proportions. Hair in a high sleek bun, gold hoop earrings. Full body head to toe, cleanly cut out like a studio photo on white, straight-on eye-level camera, centered, occupying about 70% of the frame height.
Behind her, three large Pantone-style color swatch cards, each a solid color square with a white label strip and a pinked zig-zag edge, tilted at different angles and stacked vertically and overlapping: the top card behind her head and shoulders, the middle card behind her torso, the bottom card behind her legs. Along the very bottom edge of the frame, a fanned-out Pantone color guide arcs across in a half-circle, showing many small color chips.
Lightweight breathable summer clothing for hot humid tropical weather. Bright even soft studio light, crisp editorial look, realistic skin and fabric texture, natural hands.
No extra people, no watermark, no captions other than small swatch labels.
```

## 네거티브 (지원 모델만)
```
busy background, room, floor, shadows on wall, heavy winter clothing, coat, fur, wool, extra limbs, distorted hands, wrong outfit colors, cropped feet, cropped head, blurry, extra people, large text, watermark
```

---

## LOOK 1 · 리넨 테일러링

### KF01 · 0.0s · 인트로 (흑백 모델 + 큰 컬러 가이드)
```
[공통 블록] Variation for the opening shot: instead of the three swatch cards, a huge fanned Pantone color guide in warm sands, tans, terracottas and corals fills the lower-left and back of the frame, its chips radiating behind her legs. The woman is rendered in black-and-white while the color guide stays in full color. Outfit: unlined lightweight linen blazer with sleeves pushed up, cotton tank top, knee-length linen Bermuda shorts, flat leather fisherman sandals. She stands at a three-quarter angle, arms crossed over her chest, chin slightly down, cool expression.
```

### KF02 · 2.3s · Look 1 컬러
```
[공통 블록] Swatch cards: top sand beige (#D6C3A5), middle off-white (#F4F2EC), bottom tan (#A8744F). Bottom color guide in warm sands and terracottas. Outfit, in full color: unlined relaxed sand-beige linen blazer with sleeves pushed to the elbow, worn open, off-white ribbed cotton tank top, matching sand linen knee-length Bermuda shorts with a soft pleat, tan leather flat fisherman sandals, woven raffia tote bag. Facing camera, arms crossed, weight on one leg, slight smirk.
```

### KF03 · 4.0s · 전환 (Look 1 뒷모습)
```
[공통 블록] Same Look 1 outfit seen from behind: she has turned her back to the camera, one hand slipping the linen blazer off one shoulder. She is rendered in black-and-white, while the sand and off-white swatch cards behind her are tilting and sliding in with a slight motion blur, mid-transition.
```

## LOOK 2 · 콘플라워 블루

### KF04 · 5.0s · Look 2 컬러
```
[공통 블록] Swatch cards: top cornflower blue (#6F8FD8), middle white (#FFFFFF), bottom navy (#1F2A55). Bottom color guide in blues and periwinkles. Outfit, in full color: thin fine-knit cornflower-blue cropped cardigan with short puff sleeves, buttoned only at the top button, white broderie anglaise eyelet cotton camisole underneath, navy satin bias-cut midi slip skirt, navy mesh ballet flats, small white woven shoulder bag. Facing camera, one hand lightly holding the cardigan edge, the other relaxed at her side.
```

### KF05 · 6.2s · 전환 (Look 2 뒷모습)
```
[공통 블록] Same Look 2 outfit seen from behind, back to camera. The lower half of her body is already black-and-white while the upper half keeps color, as a tilted navy swatch card sweeps diagonally across her like a wipe, slight motion blur.
```

## LOOK 3 · 버터옐로 × 초콜릿

### KF06 · 7.5s · Look 3 컬러
```
[공통 블록] Swatch cards: top butter yellow (#F3E3A2), middle chocolate brown (#5A3A2A), bottom ivory (#EFE9DC). Bottom color guide in yellows, ochres and browns. Outfit, in full color: sheer lightweight butter-yellow organza-cotton button-up shirt worn open as a cover-up with sleeves rolled, chocolate-brown ribbed cotton halter-neck top, high-waisted ivory linen wide-leg drawstring trousers, chocolate-brown leather thong flat sandals, small chocolate leather shoulder bag. Facing camera, one hand on her hip, the other tucked in the trouser pocket, chin up.
```

### KF07 · 8.6s · 전환 (Look 3 옆모습 워킹)
```
[공통 블록] Same Look 3 outfit, side profile mid-stride as she walks to the right, the wide linen trousers and sheer shirt flowing, rendered in black-and-white with slight motion blur on her legs, while a butter-yellow swatch card slides in from the top of the frame in full color.
```

## LOOK 4 · 스포티 시크

### KF08 · 9.5–11.1s · Look 4 컬러 (엔딩 홀드)
```
[공통 블록] Swatch cards: top cherry red (#B5121B), middle sky blue (#A9CBE8), bottom olive (#6B6B3A). Bottom color guide in reds, blues and greens. Outfit, in full color: ultra-light cherry-red nylon zip track jacket with white side stripes, unzipped halfway, sky-blue fitted cotton baby tee underneath, olive-green relaxed nylon running shorts at mid-thigh with white piping, white ankle socks, retro low-profile white-and-red suede sneakers. Facing camera, arms relaxed at her sides, feet together with toes slightly in, calm direct gaze. Final hold pose.
```

---

## 통합 프롬프트 (한 장에 8컷 그리드)
```
A single image laid out as a clean 4-column × 2-row grid of 8 equal vertical 9:16 panels, thin white gutters, summer fashion color-palette lookbook storyboard. Every panel: pure white background, the same woman from @Model (same face, hair, skin tone, body), high sleek bun, gold hoop earrings, full body head to toe, centered, eye-level camera, studio cut-out look. Behind her in most panels, three tilted Pantone-style swatch cards with white label strips and zig-zag edges stacked top / middle / bottom, and a fanned Pantone color guide arcing along the bottom edge. Identical framing and scale in all 8 panels. All clothing is lightweight and breathable for hot tropical weather.

Row 1, left to right:
1) black-and-white woman, arms crossed, three-quarter angle, in a lightweight linen blazer, cotton tank, knee-length linen Bermuda shorts, fisherman sandals; a huge full-color fanned color guide in warm sands and corals behind her instead of swatch cards.
2) full color: unlined sand-beige linen blazer with pushed-up sleeves, off-white ribbed tank, sand linen Bermuda shorts, tan fisherman sandals, raffia tote; swatches sand / off-white / tan; arms crossed.
3) same Look 1 from behind in black-and-white, slipping the blazer off one shoulder; sand and off-white swatches sliding in.
4) full color: thin cornflower-blue fine-knit cropped cardigan, white eyelet cotton camisole, navy satin midi slip skirt, navy mesh ballet flats; swatches cornflower / white / navy.

Row 2, left to right:
5) same Look 2 from behind, lower body black-and-white, a navy swatch card wiping across.
6) full color: sheer butter-yellow button-up shirt worn open, chocolate-brown ribbed halter top, ivory linen wide-leg drawstring trousers, chocolate thong sandals; swatches butter yellow / chocolate / ivory; hand on hip.
7) same Look 3 in side profile mid-stride, black-and-white, trousers flowing, a butter-yellow swatch sliding in from the top.
8) full color: light cherry-red nylon track jacket half-zipped, sky-blue baby tee, olive running shorts with white piping, white socks, retro white-and-red sneakers; swatches cherry red / sky blue / olive; arms at sides, final pose.

Photorealistic, realistic fabric texture, natural hands. No large text, no numbers, no watermark, no extra people.
```

---

## 모션 프롬프트 (image-to-video)

### 공통 모션 블록
```
Locked-off static vertical camera on a pure white background, no zoom, no pan. Full body stays in frame head to toe. The woman keeps her exact face and outfit. Pantone-style swatch cards behind her slide and rotate into place with snappy motion; the fanned color guide along the bottom edge rotates slightly. Light summer fabrics move softly. Real-time speed, upbeat fashion reel energy. No morphing of the face, no extra people.
```

| # | 구간 | 프레임 | 모션 |
|---|---|---|---|
| 1 | 0.0–2.3s | KF01 → KF02 | `Black-and-white, arms crossed, she turns from three-quarter to face camera; the big color guide swings down to the bottom edge while three swatch cards fly in behind her and color floods into her linen outfit from top to bottom.` |
| 2 | 2.3–4.0s | KF02 → KF03 | `She holds the arms-crossed pose, small weight shift, then turns her back to camera slipping the blazer off one shoulder as she drains to black-and-white.` |
| 3 | 4.0–5.9s | KF03 → KF04 | `New swatch cards slide in and wipe across her; she turns back to face camera now in the cornflower cardigan look in full color, the satin skirt swaying, one hand at the cardigan edge.` |
| 4 | 5.9–6.8s | KF04 → KF05 | `She turns her back to camera; a navy swatch card wipes diagonally across her, draining color from the legs up.` |
| 5 | 6.8–8.4s | KF05 → KF06 | `She spins to face camera in the butter-yellow and chocolate look in full color, the sheer shirt fluttering, settles one hand on her hip, chin up.` |
| 6 | 8.4–9.3s | KF06 → KF07 | `She steps to the side in profile, black-and-white with motion blur, wide linen trousers flowing, as a butter-yellow card slides in from the top.` |
| 7 | 9.3–11.1s | KF07 → KF08 | `Swatch cards in cherry red, sky blue and olive drop into place; she appears facing camera in the sporty track-jacket look in full color, arms at her sides, and holds still for the final pose.` |
