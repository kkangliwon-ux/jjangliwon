# Look 1 릴스 키프레임 생성 프롬프트

- 비율 **9:16 (세로)**, 1장 = 왼쪽 화면 1컷. 2분할은 편집에서 오른쪽 '정석' 컷(KF-R)과 붙이기
- **일관성 유지**: KF1을 먼저 생성 → 마음에 드는 결과를 이후 모든 컷의 **레퍼런스 이미지(캐릭터/의상 참조)**로 넣고 시드 고정
- 각 프롬프트 = `[공통 블록] + [컷별 블록]`

---

## 공통 블록 (모든 컷 앞에 붙이기)

```
Vertical 9:16 full-body fashion reel frame, static front-facing camera at eye level, model centered head to toe.
A slim young East Asian woman with black hair pulled back, wispy see-through bangs, glossy red lips, small gold earrings, thin gold bracelet.
Garment: a single bronze-brown liquid satin maxi skirt with high sheen and soft fluid folds.
Setting: minimal bedroom, pale grey wall, low bed with white bedding with tiny dot pattern behind her, dark wood plank floor.
Soft diffused daylight, natural skin texture, realistic fabric reflections, photorealistic, sharp focus, smartphone fashion content look.
```

## 네거티브 (지원 툴만)

```
text, captions, watermark, logo, split screen, extra people, extra limbs, deformed hands, distorted fabric, cropped feet, blurry, cartoon, 3D render, over-smoothed skin
```

---

## KF1 — 0.0s 훅: 치마를 가슴까지 들어 올림

```
She stands barefoot, holding the waistband of the brown satin maxi skirt up at chest level with both hands, the skirt hanging straight to the floor like a long strapless gown, fabric pooling slightly at her feet. Neutral expression looking at camera, curious hook moment.
```

## KF2 — 1.5s: 스트랩리스 튜브 드레스처럼 입기

```
She wears the brown satin skirt pulled up as a strapless tube midi dress, top edge across her chest, hem at mid-calf, bare shoulders. Barefoot, hands lifted slightly at her sides in a playful "ta-da" gesture, light smile.
```

## KF3 — 3.5s: 접기 시작 (안에 검정 튜브탑)

```
A black strapless tube top is visible underneath as she folds the top of the brown satin skirt down and gathers excess fabric at her waist with one hand, the other hand on her hip. Barefoot, looking down at the fabric, mid-styling action, slight motion in the satin.
```

## KF4 — 5.0s: 한쪽 어깨로 넘겨 드레이프

```
She has wrapped the brown satin fabric diagonally across her body and over her left shoulder, right shoulder bare, creating an asymmetric draped one-shoulder mini dress with cascading folds falling off her left arm like a wide sleeve, hem at upper thigh. Right hand holding the fabric at her left shoulder, adjusting the drape. Barefoot.
```

## KF5 — 5.5s: 뒷모습 + 머리 묶기

```
Back view: she faces away from camera, hair tied into a neat high bun, the brown satin draped over her left shoulder, right shoulder and upper back bare, asymmetric mini hem at upper thigh. Barefoot, standing straight.
```

## KF6 — 6.5s: 벨트 채우기 + 힐

```
Front view in the one-shoulder draped brown satin mini dress, hair in a high bun with bangs. She fastens a wide dark-brown leather belt with a square silver buckle at her waist, both hands at the buckle, looking down. Dark brown mini shorts peek out under the asymmetric drape. Wearing brown satin open-toe mule heels.
```

## KF7 — 8.5–10s 완성 포즈 (커버 컷)

```
Final styled look: one-shoulder draped bronze-brown satin mini dress cinched with a wide brown leather belt with square silver buckle, voluminous draped sleeve on her left arm, right shoulder bare. She holds a small cream woven leather clutch in her right hand at hip level, legs crossed at the ankles in a confident fashion pose, brown satin open-toe heels, looking straight into camera with a subtle confident smile. Polished editorial finish.
```

---

## KF-R — 오른쪽 '정석' 컷 (전 구간 고정)

```
She wears the outfit the standard way: a black strapless tube top tucked into the bronze-brown satin mermaid maxi skirt, skirt fitted at the hips and flaring at the hem to the floor, thin brown strappy heels. Standing straight, arms relaxed at her sides, neutral expression facing camera.
```

---

## 영상화(이미지→비디오)할 때 컷 연결
| 구간 | 시작 → 끝 키프레임 | 모션 프롬프트 |
|---|---|---|
| 0–1.5s | KF1 → KF2 | `she lifts and settles the satin skirt into a strapless dress, fabric flowing` |
| 1.5–3.5s | KF2 → KF3 | `she folds the top of the dress down and gathers the satin at her waist` |
| 3.5–6s | KF3 → KF4 → KF5 | `she sweeps the fabric over her left shoulder, then turns around showing her back` |
| 6–8s | KF5 → KF6 | `she turns back to camera and buckles a wide leather belt` |
| 8–10s | KF6 → KF7 | `she picks up a clutch and crosses her legs into a confident pose` |

카메라는 전 구간 **고정(static camera, no zoom)**, 조명·배경 동일 유지.
