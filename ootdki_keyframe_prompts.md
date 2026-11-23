# ootdki 스타일 키프레임 프롬프트 (착장 유지)

원본: 9:16, 720×1280, 19.8초, 3 Looks / 컷 10개 → 키프레임 12장 (자막 바뀌는 지점마다 1장)

## 사용법
- 모든 프롬프트에 **@Model** (ootdki 모델 레퍼런스 사진)과 **@Background** (ootdki 배경 레퍼런스) 두 장을 함께 첨부하세요.
- 착장 레퍼런스가 필요하면 해당 원본 프레임 캡처를 **@Outfit**으로 같이 넣으면 옷 재현이 가장 정확합니다.
- 자막("Look 1 / leggings" 등)은 이미지에 넣지 말고 편집에서 올리세요. 프롬프트에 no text를 넣어두었습니다.
- 비율 9:16, 같은 seed 고정을 권장합니다.

## 공통 블록 (모든 프롬프트 앞에 붙이기)
```
Vertical 9:16 full-body fashion photo, straight-on eye-level camera, subject centered head to toe with feet visible.
The woman is exactly the person in @Model: same face, hair, skin tone, body proportions. Hair in a high sleek bun, black cat-eye sunglasses, gold hoop earrings.
Setting matches @Background exactly: same space, colors, lighting and mood, ootdki aesthetic.
Natural soft daylight, realistic skin texture, crisp editorial outfit-of-the-day look.
No text, no captions, no watermark, no extra people.
```

## 네거티브 (지원 모델만)
```
text, letters, captions, logo, watermark, extra limbs, distorted hands, changed outfit, wrong colors, cropped feet, blurry
```

---

## LOOK 1

### KF01 · 0.0s · "leggings"
```
[공통 블록] Outfit: fitted white ribbed scoop-neck tank top, high-waisted black matte leggings, white crew socks, no shoes. Standing relaxed, arms at her sides, slight smile.
```

### KF02 · 1.8s · "turtleneck"
```
[공통 블록] Outfit: slim black fitted turtleneck tucked into high-waisted black matte leggings, white crew socks, no shoes, thin gold necklace. One hand touching the collar, the other raised slightly as she presents the top.
```

### KF03 · 3.6s · "belted houndstooth blazer"
```
[공통 블록] Outfit: black turtleneck under a dark charcoal houndstooth double-breasted blazer, cinched at the waist with a black leather belt with a gold buckle, high-waisted black leggings, white crew socks, no shoes. One hand resting on her chest, the other gesturing outward.
```

### KF04 · 5.4s · "pointed ankle boots"
```
[공통 블록] Outfit: black turtleneck, charcoal houndstooth double-breasted blazer belted with a black gold-buckle belt, black leggings, black leather pointed-toe stiletto ankle boots, holding a structured black leather top-handle bag in her left hand. Standing tall, the finished look.
```

## LOOK 2

### KF05 · 7.1s · "leggings"
```
[공통 블록] Outfit: fitted white ribbed scoop-neck tank top, high-waisted black matte leggings, white crew socks, no shoes. Relaxed stance, arms at her sides.
```

### KF06 · 8.2s · "fitted top"
```
[공통 블록] Outfit: black sleeveless mock-neck fitted top, high-waisted black leggings, white crew socks, no shoes, layered gold pendant necklaces. One hand raised to her shoulder, mouth open as if mid-sentence.
```

### KF07 · 9.9s · "belted oatmeal cardigan"
```
[공통 블록] Outfit: black sleeveless mock-neck top under an oversized chunky oatmeal-beige shawl-collar knit cardigan with balloon sleeves, wrapped and cinched at the waist with a wide dark-brown leather belt with a gold buckle, black leggings, white crew socks, no shoes, gold necklaces. One hand touching her earring.
```

### KF08 · 11.7s · "tall boots"
```
[공통 블록] Outfit: belted oversized oatmeal shawl-collar cardigan with dark-brown belt over a black top, black leggings, black leather knee-high boots with a low block heel, holding a small burgundy leather top-handle bag. Finished look, relaxed confident pose.
```

## LOOK 3

### KF09 · 13.5s · "leggings"
```
[공통 블록] Outfit: fitted white ribbed scoop-neck tank top, high-waisted black matte leggings, white crew socks, no shoes. Slight body angle, one arm slightly away from her hip.
```

### KF10 · 14.4s · "turtleneck"
```
[공통 블록] Outfit: fitted cream/ivory ribbed turtleneck tucked into high-waisted black leggings, white crew socks, no shoes, gold watch. One hand raised near her shoulder, presenting the top.
```

### KF11 · 15.8s · "belted brown sleeveless duster"
```
[공통 블록] Outfit: cream ribbed turtleneck under a long chocolate-brown sleeveless knit duster vest with cap-shoulder drape, hitting below the knee, cinched at the waist with a thin dark-brown leather belt, black leggings, white crew socks, no shoes. Arms relaxed at her sides.
```

### KF12 · 17.8s · "tall boots"
```
[공통 블록] Outfit: cream turtleneck, belted long chocolate-brown sleeveless duster, black leggings, dark-brown leather knee-high riding boots with a low block heel, holding a burgundy leather tote bag in her right hand. Finished look, standing tall.
```

---

## 영상화 (키프레임 → 비디오, 선택)
인접한 키프레임 쌍을 start/end frame으로 넣고 아래 프롬프트를 쓰세요. 원본처럼 하드컷으로 편집하려면 각 키프레임을 1–3초 정지에 가까운 클립으로 따로 만들고 이어 붙이면 됩니다.
```
Static locked-off vertical camera. The woman in @Model stands in the @Background space and makes small natural movements: a slight weight shift, a hand gesture toward the outfit, a subtle head tilt. Outfit stays exactly the same, no camera movement, no text.
```

| 컷 | 구간 | 키프레임 |
|---|---|---|
| 1 | 0.00–1.77 | KF01 |
| 2 | 1.77–5.40 | KF02 → KF03 |
| 3 | 5.40–7.07 | KF04 |
| 4 | 7.07–8.23 | KF05 |
| 5 | 8.23–9.90 | KF06 |
| 6 | 9.90–13.47 | KF07 → KF08 |
| 7 | 13.47–14.37 | KF09 |
| 8 | 14.37–15.77 | KF10 |
| 9 | 15.77–17.77 | KF11 |
| 10 | 17.77–19.78 | KF12 |

---

## 통합 프롬프트 (한 장에 12컷 그리드)
```
A single image laid out as a clean 4-column × 3-row grid of 12 equal vertical 9:16 panels, thin white gutters, fashion layering lookbook storyboard. Every panel shows the same woman from @Model (same face, hair, skin tone, body), high sleek bun, black cat-eye sunglasses, gold hoop earrings, full body head to toe, straight-on eye-level camera, centered, in the exact space of @Background with the same soft natural daylight and ootdki aesthetic. Identical camera, framing, lighting and background in all 12 panels; only the outfit and pose change.

Row 1 (Look 1), left to right:
1) fitted white ribbed scoop-neck tank, high-waisted black matte leggings, white crew socks, no shoes, arms relaxed.
2) slim black turtleneck tucked into black leggings, white socks, thin gold necklace, hand touching collar.
3) black turtleneck under a charcoal houndstooth double-breasted blazer cinched with a black gold-buckle belt, black leggings, white socks, hand on chest.
4) same belted houndstooth blazer look with black pointed-toe stiletto ankle boots, holding a structured black leather top-handle bag.

Row 2 (Look 2), left to right:
5) white ribbed tank, black leggings, white socks, no shoes.
6) black sleeveless mock-neck fitted top, black leggings, white socks, layered gold necklaces, hand at shoulder.
7) oversized chunky oatmeal shawl-collar cardigan with balloon sleeves over the black top, wrapped and cinched with a wide dark-brown gold-buckle belt, black leggings, white socks, hand at earring.
8) same belted oatmeal cardigan look with black knee-high block-heel boots, holding a small burgundy top-handle bag.

Row 3 (Look 3), left to right:
9) white ribbed tank, black leggings, white socks, no shoes.
10) fitted cream ribbed turtleneck tucked into black leggings, white socks, gold watch, hand near shoulder.
11) long chocolate-brown sleeveless knit duster below the knee over the cream turtleneck, cinched with a thin dark-brown belt, black leggings, white socks.
12) same belted brown duster look with dark-brown knee-high riding boots, holding a burgundy leather tote.

Photorealistic, realistic skin texture, natural hands, crisp editorial outfit-of-the-day look. No text, no captions, no numbers, no watermark, no extra people.
```

---

## 모션 프롬프트 (image-to-video, 클립 10개)
그리드에서 잘라낸 키프레임을 start frame으로 넣으세요. 클립 2와 6은 start/end frame 두 장을 씁니다. 길이는 원본 컷에 맞추고, 생성은 5초로 한 뒤 잘라 쓰면 됩니다.

### 공통 모션 블록 (모든 클립 앞에 붙이기)
```
Locked-off static vertical camera, no zoom, no pan, no camera shake. Full body stays in frame head to toe. The woman keeps her exact face, outfit, sunglasses and background throughout; nothing changes except her natural body movement. Real-time speed, casual outfit-of-the-day reel energy, soft natural daylight. No text, no morphing, no extra people.
```

| # | 길이 | 프레임 | 모션 |
|---|---|---|---|
| 1 | 1.8s | KF01 | `She stands relaxed, shifts her weight onto one hip, gives a small smile and lets her arms swing slightly.` |
| 2 | 3.6s | KF02 → KF03 | `She touches the turtleneck collar, then in one smooth motion slips on the houndstooth blazer, cinches the belt at her waist and rests one hand on her chest, gesturing outward with the other.` |
| 3 | 1.7s | KF04 | `She stands tall in the ankle boots, lifts the black bag slightly, small turn of the hips to show the silhouette, then settles back facing camera.` |
| 4 | 1.2s | KF05 | `Quick relaxed stance, slight weight shift, arms loose at her sides.` |
| 5 | 1.7s | KF06 | `She raises one hand to her shoulder, speaks a few words to the camera, head tilting slightly.` |
| 6 | 3.6s | KF07 → KF08 | `She adjusts the belted oatmeal cardigan and touches her earring, then appears in black knee-high boots holding the burgundy bag, shifting her weight with a confident pose.` |
| 7 | 0.9s | KF09 | `Brief relaxed stance, slight body angle, one arm moving slightly away from her hip.` |
| 8 | 1.4s | KF10 | `She lifts one hand near her shoulder to present the cream turtleneck, small head tilt.` |
| 9 | 2.0s | KF11 | `She smooths the front of the brown duster, the long knit fabric swaying gently as she shifts her weight.` |
| 10 | 2.0s | KF12 | `She stands tall in the riding boots, swings the burgundy tote slightly, small hip turn, duster hem swaying, then holds the final pose.` |

### 통합 모션 프롬프트 (한 번에 이어서 생성할 때)
```
Locked-off static vertical 9:16 camera, full body head to toe, same woman from @Model in the @Background space, soft natural daylight. Hard-cut outfit-of-the-day layering reel, about 20 seconds. Look 1: white tank and black leggings, then a black turtleneck, then a belted charcoal houndstooth blazer, then black pointed ankle boots with a black top-handle bag. Look 2: white tank and leggings, then a black sleeveless mock-neck top, then a belted oversized oatmeal cardigan, then black knee-high boots with a burgundy bag. Look 3: white tank and leggings, then a cream turtleneck, then a belted long chocolate-brown sleeveless duster, then brown knee-high riding boots with a burgundy tote. Each shot lasts 1–3 seconds with a hard cut to the next layer. In every shot she makes small natural gestures toward the outfit: a weight shift, a hand at the collar or shoulder, a slight hip turn. Identical framing and lighting across every cut. No camera movement, no text, no morphing between outfits.
```

---

## 릴스 통합 영상 프롬프트 (최종, 이것만 쓰면 됨)
레퍼런스로 12컷 그리드 이미지를 **@Image1**로 첨부. 9:16, 15초.
```
Vertical 9:16 Instagram Reels outfit-of-the-day layering video, 15 seconds, 12 shots with fast hard cuts on the beat. @Image1 is the storyboard: a 4×3 grid of 12 panels, read left to right, top to bottom; each shot recreates one panel exactly — same woman, same face and body, same outfit, same background, same framing. Locked-off static camera at eye level, full body head to toe centered in every shot, identical framing and soft natural daylight across all cuts, so only the outfit changes between cuts. The woman wears a high sleek bun, black cat-eye sunglasses and gold hoop earrings throughout.

0.0–1.2s panel 1: white ribbed tank, black leggings, white socks; she shifts her weight onto one hip.
1.2–2.4s panel 2: black turtleneck added; she touches the collar.
2.4–3.6s panel 3: belted charcoal houndstooth blazer added; hand on chest, other hand gesturing out.
3.6–5.0s panel 4: black pointed ankle boots and black top-handle bag; slight hip turn to show the silhouette.
5.0–6.0s panel 5: back to white tank and black leggings; relaxed weight shift.
6.0–7.2s panel 6: black sleeveless mock-neck top; hand at her shoulder, says a few words to camera.
7.2–8.4s panel 7: oversized oatmeal cardigan with wide brown belt; touches her earring.
8.4–10.0s panel 8: black knee-high boots and burgundy bag; confident pose.
10.0–11.0s panel 9: back to white tank and black leggings; slight body angle.
11.0–12.2s panel 10: cream turtleneck; hand near shoulder, small head tilt.
12.2–13.4s panel 11: belted long chocolate-brown sleeveless duster; the knit sways as she shifts.
13.4–15.0s panel 12: brown knee-high riding boots and burgundy tote; small hip turn, holds the final pose.

Clean hard cuts only, no transitions, no morphing between outfits, no camera movement. Photorealistic, natural hands, realistic fabric motion. No text, no captions, no watermark, no extra people.
