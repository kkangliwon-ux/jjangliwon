# ootdki 모델 × 팬톤 컬러칩 포맷 · 키프레임 프롬프트 (착장 교체)

원본 레퍼런스: 9:16, 720×1280, 11.1초, 4 Looks.
포맷 그대로 유지: 흰 배경 + 누끼 모델 전신, 등 뒤에 기울어진 팬톤 컬러칩 3장(위=아우터 색 / 가운데=이너 색 / 아래=하의·신발 색), 화면 맨 아래 부채꼴 팬톤 컬러 가이드. 룩 전환 때는 모델이 흑백으로 빠지고 뒤돌거나 옆으로 걸으면서 컬러칩이 날아 들어오며 색이 입혀짐.
바뀐 것: 모델은 ootdki 모델(@Model), 착장은 2026 겨울 인스타 인기 스타일 4종.

| Look | 스타일 (2026 겨울 인스타 인기) | 컬러칩 3장 (위 / 가운데 / 아래) |
|---|---|---|
| 1 | 예티코어 · 롱파일 인조 퍼 (Lyst 이번 겨울 1위 트렌드) | Chocolate Brown #5A3A2A / Cloud Dancer Ivory #F0EEE9 / Camel #B98A5E |
| 2 | 2016 리바이벌 · 패딩 봄버 + 스트라이프 폴로 + 배기진 (Transformative Teal) | Teal #0F6E73 / Cherry Red #B5121B / Mid Denim #6E8FB5 |
| 3 | 레이디라이크 · 80s 파워숄더 부클레 스커트 수트 | Oxblood #5C1A22 / Blush Pink #F2C9CF / Black #1A1A1A |
| 4 | 메인캐릭터 롱코트 · 숄 스카프 + 니트 헤어밴드 + 턴업 와이드 팬츠 | Navy #1F2A44 / Forest Green #1E5B3A / Cream #EDE3D1 |

## 사용법
- 모든 프롬프트에 **@Model** (ootdki 모델 레퍼런스 사진)을 첨부하세요. 원본 영상 프레임 캡처를 **@Format**으로 같이 넣으면 컬러칩 배치·여백이 가장 정확하게 나옵니다. (@Background는 이 포맷에서 안 씁니다: 배경은 흰색.)
- 컬러칩 라벨의 "PANTONE ○○-○○○○ TCX" 글자는 AI가 뭉개기 쉬워요. 이미지에선 라벨 띠만 받고, 정확한 코드는 편집에서 얹는 걸 권장합니다.
- 흑백 컷(KF01, KF03, KF05, KF07)은 프롬프트에 모델만 흑백으로 넣어 두었지만, 컬러로 뽑은 뒤 편집에서 모델만 채도 0으로 빼면 컬러가 입혀지는 전환을 더 깔끔하게 만들 수 있어요.
- 9:16, seed 고정, 모델 크기·위치를 컷마다 맞추세요.

## 공통 블록 (모든 프롬프트 앞에 붙이기)
```
Vertical 9:16 fashion color-palette lookbook frame. Pure seamless white background. The woman is exactly the person in @Model: same face, hair, skin tone, body proportions. Hair in a high sleek bun, black cat-eye sunglasses, gold hoop earrings. Full body head to toe, cleanly cut out like a studio photo on white, straight-on eye-level camera, centered, occupying about 70% of the frame height.
Behind her, three large Pantone-style color swatch cards, each a solid color square with a white label strip and a pinked zig-zag edge, tilted at different angles and stacked vertically and overlapping: the top card behind her head and shoulders, the middle card behind her torso, the bottom card behind her legs. Along the very bottom edge of the frame, a fanned-out Pantone color guide arcs across in a half-circle, showing many small color chips.
Bright even soft studio light, crisp editorial look, realistic skin and fabric texture, natural hands.
No extra people, no watermark, no captions other than small swatch labels.
```

## 네거티브 (지원 모델만)
```
busy background, room, floor, shadows on wall, extra limbs, distorted hands, wrong outfit colors, cropped feet, cropped head, blurry, extra people, large text, watermark
```

---

## LOOK 1 · 예티코어 퍼

### KF01 · 0.0s · 인트로 (흑백 모델 + 큰 컬러 가이드)
```
[공통 블록] Variation for the opening shot: instead of the three swatch cards, a huge fanned Pantone color guide in warm browns, camels, terracottas and deep reds fills the lower-left and back of the frame, its chips radiating behind her legs. The woman is rendered in black-and-white while the color guide stays in full color. Outfit: shaggy long-pile faux-fur cropped jacket, chunky ribbed knit turtleneck, suede mini skirt, knee-high suede boots. She stands at a three-quarter angle, arms crossed over her chest, chin slightly down, cool expression.
```

### KF02 · 2.3s · Look 1 컬러
```
[공통 블록] Swatch cards: top chocolate brown (#5A3A2A), middle Cloud Dancer ivory (#F0EEE9), bottom camel (#B98A5E). Bottom color guide in warm browns and terracottas. Outfit, in full color: shaggy long-pile chocolate-brown faux-fur cropped jacket, chunky ivory ribbed knit turtleneck, camel suede A-line mini skirt, chocolate-brown suede knee-high boots with a low block heel, small fuzzy ivory shoulder bag. Facing camera, arms crossed, weight on one leg, slight smirk.
```

### KF03 · 4.0s · 전환 (Look 1 뒷모습)
```
[공통 블록] Same Look 1 outfit seen from behind: she has turned her back to the camera, one hand pulling the faux-fur jacket off one shoulder. She is rendered in black-and-white, while the chocolate-brown and ivory swatch cards behind her are tilting and sliding in with a slight motion blur, mid-transition.
```

## LOOK 2 · 2016 리바이벌 봄버

### KF04 · 5.0s · Look 2 컬러
```
[공통 블록] Swatch cards: top transformative teal (#0F6E73), middle cherry red (#B5121B), bottom mid-wash denim blue (#6E8FB5). Bottom color guide in blues and teals. Outfit, in full color: glossy oversized teal padded bomber jacket worn open, cherry-red and white striped knit polo shirt, mid-wash light-blue baggy barrel-leg jeans pooling slightly at the ankle, chunky white leather sneakers, thin red knit beanie optional. Facing camera, both hands in the jacket pockets, slight lean on one hip, relaxed.
```

### KF05 · 6.2s · 전환 (Look 2 뒷모습)
```
[공통 블록] Same Look 2 outfit seen from behind, back to camera, hands in pockets. The lower half of her body is already black-and-white while the upper half keeps color, as a tilted cherry-red swatch card sweeps diagonally across her like a wipe, slight motion blur.
```

## LOOK 3 · 레이디라이크 스커트 수트

### KF06 · 7.5s · Look 3 컬러
```
[공통 블록] Swatch cards: top oxblood (#5C1A22), middle blush pink (#F2C9CF), bottom black (#1A1A1A). Bottom color guide in reds, pinks and berries. Outfit, in full color: oxblood bouclé cropped jacket with strong padded 80s shoulders and gold buttons, matching oxblood bouclé mini skirt, blush-pink satin blouse with a big soft bow at the neck, sheer black tights, black patent slingback kitten heels, small structured black top-handle bag. Facing camera, one hand on her hip, the other holding the bag at her side, chin up.
```

### KF07 · 8.6s · 전환 (Look 3 옆모습 워킹)
```
[공통 블록] Same Look 3 outfit, side profile mid-stride as she walks to the right, rendered in black-and-white with slight motion blur on her legs, while an oxblood swatch card slides in from the top of the frame in full color.
```

## LOOK 4 · 메인캐릭터 롱코트

### KF08 · 9.5–11.1s · Look 4 컬러 (엔딩 홀드)
```
[공통 블록] Swatch cards: top navy (#1F2A44), middle forest green (#1E5B3A), bottom cream (#EDE3D1). Bottom color guide in blues and greens. Outfit, in full color: oversized floor-length navy wool coat with strong shoulders worn open, forest-green chunky knit shawl scarf draped over the shoulders, matching forest-green knitted headband over the sleek bun, cream fine-knit top, cream wide-leg wool trousers with exaggerated deep turn-up cuffs, dark-brown leather loafers. Facing camera, arms relaxed at her sides, feet together with toes slightly in, calm direct gaze. Final hold pose.
```

---

## 통합 프롬프트 (한 장에 8컷 그리드)
```
A single image laid out as a clean 4-column × 2-row grid of 8 equal vertical 9:16 panels, thin white gutters, fashion color-palette lookbook storyboard. Every panel: pure white background, the same woman from @Model (same face, hair, skin tone, body), high sleek bun, black cat-eye sunglasses, gold hoop earrings, full body head to toe, centered, eye-level camera, studio cut-out look. Behind her in most panels, three tilted Pantone-style swatch cards with white label strips and zig-zag edges stacked top / middle / bottom, and a fanned Pantone color guide arcing along the bottom edge. Identical framing and scale in all 8 panels.

Row 1, left to right:
1) black-and-white woman, arms crossed, three-quarter angle, in a shaggy faux-fur cropped jacket, knit turtleneck, suede mini skirt, knee boots; a huge full-color fanned color guide in warm browns and reds behind her instead of swatch cards.
2) full color: chocolate-brown shaggy faux-fur cropped jacket, ivory chunky turtleneck, camel suede mini skirt, chocolate suede knee boots; swatches chocolate / ivory / camel; arms crossed.
3) same Look 1 from behind in black-and-white, pulling the fur jacket off one shoulder; brown and ivory swatches sliding in.
4) full color: glossy teal padded bomber worn open, cherry-red striped polo, light-blue baggy barrel jeans, chunky white sneakers; swatches teal / cherry red / denim blue; hands in pockets.

Row 2, left to right:
5) same Look 2 from behind, lower body black-and-white, a red swatch card wiping across.
6) full color: oxblood bouclé power-shoulder cropped jacket with gold buttons and matching mini skirt, blush-pink satin bow blouse, sheer black tights, black patent slingbacks, black top-handle bag; swatches oxblood / blush pink / black; hand on hip.
7) same Look 3 in side profile mid-stride, black-and-white, an oxblood swatch sliding in from the top.
8) full color: floor-length oversized navy wool coat, forest-green knit shawl scarf and knitted headband, cream knit top, cream wide-leg trousers with deep turn-ups, brown loafers; swatches navy / forest green / cream; arms at sides, final pose.

Photorealistic, realistic fabric texture, natural hands. No large text, no numbers, no watermark, no extra people.
```

---

## 모션 프롬프트 (image-to-video)

### 공통 모션 블록
```
Locked-off static vertical camera on a pure white background, no zoom, no pan. Full body stays in frame head to toe. The woman keeps her exact face, sunglasses and outfit. Pantone-style swatch cards behind her slide and rotate into place with snappy motion; the fanned color guide along the bottom edge rotates slightly. Real-time speed, upbeat fashion reel energy. No morphing of the face, no extra people.
```

| # | 구간 | 프레임 | 모션 |
|---|---|---|---|
| 1 | 0.0–2.3s | KF01 → KF02 | `Black-and-white, arms crossed, she turns from three-quarter to face camera; the big color guide swings down to the bottom edge while three swatch cards fly in behind her and color floods into her outfit from top to bottom.` |
| 2 | 2.3–4.0s | KF02 → KF03 | `She holds the arms-crossed pose, small weight shift, then turns her back to camera pulling the fur off one shoulder as she drains to black-and-white.` |
| 3 | 4.0–5.9s | KF03 → KF04 | `New swatch cards slide in and wipe across her; she turns back to face camera now in the teal bomber look in full color, hands into pockets, slight hip lean.` |
| 4 | 5.9–6.8s | KF04 → KF05 | `She turns her back to camera; a red swatch card wipes diagonally across her, draining color from the legs up.` |
| 5 | 6.8–8.4s | KF05 → KF06 | `She spins to face camera in the oxblood skirt-suit look in full color, settles one hand on her hip, chin up.` |
| 6 | 8.4–9.3s | KF06 → KF07 | `She steps to the side in profile, black-and-white with motion blur, as an oxblood card slides in from the top.` |
| 7 | 9.3–11.1s | KF07 → KF08 | `Swatch cards in navy, green and cream drop into place; she appears facing camera in the long navy coat look in full color, arms at her sides, and holds still for the final pose.` |
