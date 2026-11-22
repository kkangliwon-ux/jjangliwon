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
