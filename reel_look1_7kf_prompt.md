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

ORIENTATION LOCK (most important, applies to every image): directions are given as image-left / image-right of the LEFT half as the viewer sees it. In FRONT views her right side is on image-left and her left side is on image-right. In the BACK view (image 5) this flips: her left side is on image-left. The satin always goes over HER LEFT shoulder, and the shawl-like cascade / wide draped sleeve always hangs down HER LEFT arm, on the SAME side as the covered shoulder. Her right shoulder and her entire right arm, from shoulder to hand, stay completely bare; no fabric ever hangs from her right arm. Do not mirror the images.

PHYSICS RULES:
- The skirt is one piece of fabric with a fixed length. Worn at the natural waist its hem grazes the floor.
- Wherever the waistband is lifted, the hem rises by exactly the same distance (waistband at chest = hem at mid-calf). Feet and ankles are visible whenever the waistband is above the waist; no fabric pools on the floor.
- Fabric gathered, folded or draped over the shoulder is subtracted from the length, so the hem gets shorter accordingly. No fabric appears from nowhere.
- Gravity: satin hangs straight down from where it is held or supported.

STYLE: photorealistic, natural skin texture, realistic satin reflections, smartphone fashion reel look. No text, labels, captions, numbers or watermark. No extra people.

IMAGES:
1. LEFT: barefoot, feet together, mules on the floor beside her right foot, belt and clutch on the bed edge behind her. Both arms raised to chest height, elbows slightly bent, hands pinching the skirt's waistband and stretching it wide at upper chest just under the armpits; the edge of the black tube top peeks above the waistband. The skirt hangs as a wide flared cone, hem at mid-calf, ankles and feet visible. Neutral face, eyes to camera. | RIGHT: standing straight, arms relaxed at sides, neutral face.
2. LEFT: barefoot, props unchanged. The skirt is worn as a strapless tube dress, top edge across the bust, hem at mid-calf, bare shoulders. Both hands raised beside her shoulders, palms open facing camera in a playful "ta-da", light smile. | RIGHT: hands resting lightly at the sides of her hips.
3. LEFT: barefoot, props unchanged. POSITION LOCK (her right = image-left side of the left half, her left = image-right side): the skirt's top edge on HER RIGHT side stays at bust height, straight across just below the armpit, exactly where it was in image 2, held by her right hand pinching it at center front with the lighter inner lining showing at the flap edge. The vertical zipper on HER LEFT side is opened from the top edge down to her natural waist; the left panel folds outward and hangs from the bottom of the open zipper, forming a triangular opening from the bust down to her left waist through which the black strapless tube top is visible. Her left hand is at her left waist holding the zipper pull at the bottom of the opening, elbow bent outward. The skirt is NOT pulled down: only the zipper is open. Hem unchanged at mid-calf, feet visible. Eyes to camera. | RIGHT: arms relaxed at sides.
4. LEFT: barefoot, props unchanged (mules on the floor beside her right foot, belt and clutch on the bed edge). FRONT view. Both shoulders still bare; the fabric is NOT over the shoulder yet. The satin's top edge runs diagonally from just under her right armpit (image-left) up to her left shoulder (image-right). Her right arm crosses her chest and her right hand grips gathered satin just below her left collarbone. Her left hand (image-right), elbow bent and raised, holds the lifted corner at her left shoulder height, lighter inner lining showing along that edge. The lifted fabric forms a wide cascade hanging down her LEFT side (image-right) to mid-thigh, darker inner side visible. Nothing hangs on image-left. Hem at mid-thigh on her right leg (image-left); her left upper thigh (image-right) exposed beneath the cascade. Eyes to camera. | RIGHT: arms relaxed at sides.
5. LEFT: BACK view, she faces away from camera, barefoot. Because this is a back view, her LEFT side is on image-LEFT. Her loose hair is swept forward over her RIGHT shoulder (image-right) so the drape on her back is clearly visible. ONE-SHOULDER LOCK: the satin goes OVER her LEFT shoulder (image-left). Its top edge runs diagonally across her back from under her right armpit (image-right, low) up to the top of her left shoulder (image-left, high); her right shoulder blade and upper right back are bare. It is NOT a strapless tube: there is no straight horizontal top edge. The cascade starts AT her left shoulder and falls down the back of her left side; her LEFT arm (image-left) is extended out to the side and slightly down at about 45 degrees, holding the edge of the cascade at hip height so it fans out wide from shoulder to hand. Her RIGHT arm (image-right) hangs relaxed and bare, holding the wide dark-brown leather belt, which dangles from her right hand. HEM LOCK: mini length, just below the buttocks at upper thigh, the same short length as in image 4; the backs of her knees and her whole calves are visible. NOT midi, NOT knee-length. The brown mules sit on the floor beside her right foot (image-right); the cream clutch lies on the bed edge. | RIGHT: facing front, arms relaxed at sides.
6. LEFT: FRONT view, now wearing the brown satin open-toe mules; the clutch still lies on the bed edge behind her right hip (image-left). The satin covers her LEFT shoulder (image-right); her right shoulder and whole right arm (image-left) are bare. A voluminous bishop-style draped sleeve wraps her LEFT arm (image-right), gathered at the wrist. A wide dark-brown leather belt is already fastened, slung LOW on her hips (not at the waist), the square silver buckle at the front just right of center toward image-right; the satin is bloused and gathered over the belt like a peplum, dark brown mini shorts visible below; hem at upper thigh. She looks up at camera; her right hand (image-left) is down at her right thigh tugging the satin hem; her left arm (image-right) hangs in the sleeve, slightly bent, hand near the hip. Hands are NOT on the buckle. | RIGHT: arms lowering, left hand lightly at hip.
7. LEFT: FRONT view, final look, bed edge now empty. Same belted look: satin over her LEFT shoulder (image-right), voluminous draped sleeve on her LEFT arm (image-right), right shoulder and right arm (image-left) bare; belt slung low on the hips with the square silver buckle just right of center; peplum drape over dark brown mini shorts; hem at upper thigh. Her RIGHT hand (image-left) holds the cream woven leather clutch at her right hip (image-left). Her left forearm (image-right) is bent outward at waist level inside the billowing sleeve. Legs crossed at the ankles, right foot in front, brown open-toe mules. Confident gaze into camera, subtle smile. | RIGHT: standing straight, arms relaxed at sides, neutral smile.
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
