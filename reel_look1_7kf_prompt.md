# Look 1 — 키프레임 7장 프롬프트 (원본 영상 분할 지점 기준)

원본 0.0–10.4s를 아래 7개 지점에서 6구간으로 분할. 각 키프레임 = 구간의 시작/끝 프레임.
원본 구간 클립과 기준 프레임은 세션 스크래치패드 look1_clips/에 있음 (seg1~6.mp4, kf1~7.jpg, 원본 영상 파생물이라 커밋 안 함).

| 키프레임 | 원본 시점 | 구간 | 길이 |
|---|---|---|---|
| KF1 | 0.0s | seg1: KF1→KF2 | 1.2s |
| KF2 | 1.2s | seg2: KF2→KF3 | 1.0s |
| KF3 | 2.2s | seg3: KF3→KF4 | 1.4s |
| KF4 | 3.6s | seg4: KF4→KF5 | 2.4s |
| KF5 | 6.0s | seg5: KF5→KF6 | 2.4s |
| KF6 | 8.4s | seg6: KF6→KF7 | 2.0s |
| KF7 | 10.4s | | |

## 이미지 프롬프트 (모델 사진 첨부 후 한 번에)

```
Generate 7 separate images, one at a time, each as its own standalone vertical 9:16 image (not a grid, not a collage). They are keyframes of one continuous fashion reel shot on a locked-off camera, so everything not described as changing stays identical across all 7.

MODEL REFERENCE: use the attached model photo as the identity reference for BOTH halves. Match her face, makeup, skin tone, hair color and hair length exactly. Hair is worn loose and down in every image (no bun, no ponytail, no updo).

LAYOUT: split screen divided down the middle by a thin seam. LEFT half = STYLING, RIGHT half = WEARING. Same woman in both halves, full body head to toe in each half, static front-facing eye-level camera.

SETTING: minimal bedroom, pale grey wall, low bed with white dotted bedding behind her, dark wood plank floor, soft diffused daylight.

GARMENT: one bronze-brown liquid satin maxi skirt with high sheen and fluid folds. Under it on the left she wears a black strapless tube top and dark brown mini shorts.

PROPS (LEFT half only, they never appear or vanish without being moved):
- A pair of brown satin open-toe mule heels on the floor just beside her right foot (images 1-5), then on her feet (images 6-7).
- A wide dark-brown leather belt with a square silver buckle lying on the edge of the bed behind her (images 1-4), held in her right hand (image 5), then fastened at her waist (images 6-7).
- A small cream woven leather clutch lying on the edge of the bed behind her right hip (images 1-6), then in her right hand (image 7).

RIGHT half (WEARING) base look in all 7: black strapless tube top tucked into the bronze-brown satin mermaid maxi skirt worn at the natural waist, fitted at the hips and flaring so the hem grazes the floor, thin brown strappy heels. Only her pose changes, as listed.

PHYSICS RULES:
- The skirt is one piece of fabric with a fixed length. Worn at the natural waist its hem grazes the floor.
- Wherever the waistband is lifted, the hem rises by exactly the same distance (waistband at chest = hem at mid-calf). Feet and ankles are visible whenever the waistband is above the waist; no fabric pools on the floor.
- Fabric gathered, folded or draped over the shoulder is subtracted from the length, so the hem gets shorter accordingly. No fabric appears from nowhere.
- Gravity: satin hangs straight down from where it is held or supported.

STYLE: photorealistic, natural skin texture, realistic satin reflections, smartphone fashion reel look. No text, labels, captions, numbers or watermark. No extra people.

IMAGES:
1. LEFT: barefoot, feet together, mules on the floor beside her right foot, belt and clutch on the bed edge behind her. Both arms raised to chest height, elbows slightly bent, hands pinching the skirt's waistband and stretching it wide at upper chest just under the armpits; the edge of the black tube top peeks above the waistband. The skirt hangs as a wide flared cone, hem at mid-calf, ankles and feet visible. Neutral face, eyes to camera. | RIGHT: standing straight, arms relaxed at sides, neutral face.
2. LEFT: barefoot, props unchanged. The skirt is worn as a strapless tube dress, top edge across the bust, hem at mid-calf, bare shoulders. Both hands raised beside her shoulders, palms open facing camera in a playful "ta-da", light smile. | RIGHT: hands resting lightly at the sides of her hips.
3. LEFT: barefoot, props unchanged. She has opened the side zipper at her left waist and loosened the skirt's waistband, which has slipped down to the bust line so the black strapless tube top shows above it. Her right hand holds the opened waistband edge away from her chest at her left front, showing the lighter inner lining; her left hand holds the opened side at her left hip. Because the waistband dropped slightly, the hem is at lower calf, feet visible. Eyes to camera. | RIGHT: arms relaxed at sides.
4. LEFT: barefoot, props unchanged. A large swath of satin has been pulled diagonally across her torso and over her left shoulder, right shoulder bare. Because so much fabric goes over the shoulder, the front hem has risen to upper thigh on her right leg, while a cascade hangs from her left shoulder down her left side to the knee. Her right hand grips the gathered fabric at her left shoulder. Eyes to camera. | RIGHT: arms relaxed at sides.
5. LEFT: back view, turned away from camera, barefoot, hair loose down her back, mules on the floor beside her right foot, clutch on the bed edge. Satin over her left shoulder, right shoulder and upper back bare; her left arm extended out to the side holding the cascading satin away from her body to show its volume; her right arm hangs relaxed holding the leather belt, which dangles from her hand; hem just above the knee. | RIGHT: facing front, arms relaxed at sides.
6. LEFT: front view, now wearing the brown satin open-toe mules; clutch still on the bed edge behind her right hip. One-shoulder satin drape cinched at the waist by the wide dark-brown leather belt with the square silver buckle at front-left; satin bloused over the belt like a peplum; dark brown mini shorts visible underneath; hem at upper thigh. She looks up at camera, right hand down at her right thigh tugging the satin hem, left arm lowered inside a voluminous draped sleeve, left hand near hip. | RIGHT: arms lowering, left hand lightly at hip.
7. LEFT: final look: same belted one-shoulder satin mini drape, hem at upper thigh, bed edge now empty. Holding the cream woven leather clutch in her right hand at her right hip, left forearm bent outward at waist level with the voluminous satin sleeve billowing. Legs crossed at the ankles, right foot in front, brown open-toe mules. Confident gaze into camera, subtle smile. | RIGHT: standing straight, arms relaxed at sides, neutral smile.
```

## 구간별 영상 모션 프롬프트 (시작 이미지 → 끝 이미지)

| 구간 | 프롬프트 |
|---|---|
| seg1 KF1→KF2 (1.2s) | `She lifts the stretched waistband up to her collarbone, then lowers it onto her bust and lets go, raising both open palms beside her shoulders. Satin swings and settles. Static camera. Right side: she places both hands on the front of her hips.` |
| seg2 KF2→KF3 (1.0s) | `She lowers her arms, grips the top edge with her right hand, puts her left hand on her hip and folds the satin down to reveal the black tube top. Static camera. Right side stands still.` |
| seg3 KF3→KF4 (1.4s) | `She gathers the satin at her left hip, lifts it up her left side and pulls it over her left shoulder; the hem rises diagonally to upper thigh as the fabric goes over the shoulder. Static camera. Right side stands still.` |
| seg4 KF4→KF5 (2.4s) | `She looks down and adjusts the drape at her chest with her right hand, looks up, then turns around to show her back while extending her left arm to spread the cascading satin. Static camera. Right side turns her head to her left in profile, then back to front.` |
| seg5 KF5→KF6 (2.4s) | `She turns back to camera, wraps a wide leather belt around her waist and buckles it, tucks the belt end at her right hip, then looks up and tugs the hem. Static camera. Right side points her right index finger toward the left half, then lowers her arm.` |
| seg6 KF6→KF7 (2.0s) | `She shifts her weight, adjusts the hem, picks up a cream clutch in her right hand and crosses her legs at the ankles into a confident pose, sleeve billowing. Static camera. Right side stands still with a slight smile.` |
