# Look 1 — 구간별 영상 프롬프트 (이미지 6장 → 영상 6개, 0.2초 타임라인)

- 시작 이미지: KF1~KF6 (`reel_look1_7kf_prompt.md` 1~6번). 각 영상은 해당 이미지에서 시작.
- 끝 이미지를 지원하는 툴이면 다음 키프레임(KF2~KF7)을 끝 프레임으로 넣으면 연결이 더 정확함.
- 타임라인은 원본 영상 0.2초 분석 기준. 시간은 각 영상 시작 기준 상대 시간.
- 툴의 최소 길이가 구간보다 길면, 가장 짧은 길이로 뽑고 편집에서 구간 길이에 맞게 속도 조절/트림.

---

## SEG 1 — KF1 시작 · 1.2초 (원본 0.0–1.2s)

```
Image-to-video, start from the attached image. Locked-off static camera: no zoom, no pan, no cuts. Split screen: LEFT half = STYLING, RIGHT half = WEARING. Keep both women's face, makeup, loose hair, outfit, room and lighting exactly as in the start image. Physics: the satin skirt has a fixed length; she starts wearing it at her natural waist with the hem grazing the floor; as she pulls the waistband up to her chest the hem rises by exactly the same distance to mid-calf, and the satin swings with realistic weight and gravity. ORIENTATION LOCK: in front views her right side is on image-left and her left side is on image-right of the left half; in back views this flips. The satin goes over HER LEFT shoulder and the shawl-like cascade / wide draped sleeve hangs on HER LEFT arm, the same side as the covered shoulder; her right arm stays bare. The belt is slung low on her hips with the buckle just right of center; the clutch goes in her RIGHT hand. Never mirror the keyframes. Exactly one pair of mules and exactly one clutch exist; the top stays a wrapped satin drape (no seams, no cuffs); the WEARING woman on the right never gets a sleeve. No text. Duration 1.2s.

0.0s  LEFT: she wears the satin skirt the normal way, at her natural waist over the black strapless tube top, exactly like the right half: hem grazing the floor, barefoot toes just peeking out; both hands grip the waistband at the sides of her hips, thumbs hooked inside; standing straight, eyes to camera. RIGHT: standing straight, arms relaxed at sides, same outfit as the left.
0.2s  LEFT: starts pulling the waistband straight up with both hands; it slides up over her ribs; the hem lifts off the floor by the same distance, her toes and feet appear. RIGHT: still.
0.4s  LEFT: waistband now at her lower ribs, covering the bottom of the tube top; hem at the ankles. RIGHT: still.
0.6s  LEFT: pulls the waistband up over the bust, covering the black tube top completely; hem rises to lower calf. RIGHT: moves both hands to the front of her hips.
0.8s  LEFT: final tug: waistband settles straight across her upper chest just under the armpits; hem at mid-calf; satin swings and settles. RIGHT: smooths the skirt with both palms on her hips.
1.0s  LEFT: presses the top edge to her chest with her fingertips at both sides, elbows out; now worn as a strapless tube dress, hem at mid-calf. RIGHT: hands on hips.
1.2s  LEFT: lets go and raises both open palms beside her shoulders in a playful "ta-da", light smile. RIGHT: hands lightly at the sides of her hips.
```

## SEG 2 — KF2 시작 · 1.0초 (원본 1.2–2.2s)

```
Image-to-video, start from the attached image. Locked-off static camera: no zoom, no pan, no cuts. Split screen: LEFT half = STYLING, RIGHT half = WEARING. Keep both women's face, makeup, loose hair, outfit, room and lighting exactly as in the start image. Physics: the satin skirt has a fixed length; opening the zipper on her left side does not lower the skirt: the top edge on her right side stays at bust height and the hem stays at mid-calf; satin moves with realistic weight. ORIENTATION LOCK: in front views her right side is on image-left and her left side is on image-right of the left half; in back views this flips. The satin goes over HER LEFT shoulder and the shawl-like cascade / wide draped sleeve hangs on HER LEFT arm, the same side as the covered shoulder; her right arm stays bare. The belt is slung low on her hips with the buckle just right of center; the clutch goes in her RIGHT hand. Never mirror the keyframes. Exactly one pair of mules and exactly one clutch exist; the top stays a wrapped satin drape (no seams, no cuffs); the WEARING woman on the right never gets a sleeve. No text. Duration 1.0s.

0.0s  LEFT: palms open beside her shoulders, strapless satin tube dress, hem at mid-calf. RIGHT: hands lightly at hip sides.
0.2s  LEFT: opens her arms wider at shoulder height, palms up, light smile. RIGHT: lowers arms to her sides.
0.4s  LEFT: lowers her arms out from her sides at hip level, palms forward. RIGHT: arms relaxed.
0.6s  LEFT: her right hand pinches the skirt's top edge at center front of her chest, holding it in place at bust height; her left hand goes to the top of the zipper on her left side (image-right side of the left half). RIGHT: still.
0.8s  LEFT: her left hand pulls the zipper down along her left side; the top edge on her right side stays at bust height in her right hand; a narrow opening starts on her left chest showing the black tube top. RIGHT: still.
1.0s  LEFT: zipper on her left side fully opened from the top edge down to her natural waist; the left panel folds outward and hangs from the bottom of the zipper, forming a triangular opening from bust to left waist that shows the black tube top; the top edge on her right side is still at bust height, held by her right hand with the lighter inner lining showing at the flap edge; her left hand at her left waist holding the zipper pull, elbow out; hem unchanged at mid-calf. RIGHT: arms relaxed.
```

## SEG 3 — KF3 시작 · 1.4초 (원본 2.2–3.6s)

```
Image-to-video, start from the attached image. Locked-off static camera: no zoom, no pan, no cuts. Split screen: LEFT half = STYLING, RIGHT half = WEARING. Keep both women's face, makeup, loose hair, outfit, room and lighting exactly as in the start image. Physics: the satin skirt has a fixed length; as fabric is gathered and pulled over her shoulder, the hem rises by exactly the amount of fabric used, first on her left side, then across the front. No fabric appears from nowhere. Realistic satin weight and gravity. ORIENTATION LOCK: in front views her right side is on image-left and her left side is on image-right of the left half; in back views this flips. The satin goes over HER LEFT shoulder and the shawl-like cascade / wide draped sleeve hangs on HER LEFT arm, the same side as the covered shoulder; her right arm stays bare. The belt is slung low on her hips with the buckle just right of center; the clutch goes in her RIGHT hand. Never mirror the keyframes. Exactly one pair of mules and exactly one clutch exist; the top stays a wrapped satin drape (no seams, no cuffs); the WEARING woman on the right never gets a sleeve. No text. Duration 1.4s.

0.0s  LEFT: zipper on her left side fully opened from the top edge down to her natural waist; the left panel folds outward and hangs from the bottom of the zipper, forming a triangular opening from bust to left waist that shows the black tube top; the top edge on her right side is still at bust height, held by her right hand with the lighter inner lining showing at the flap edge; her left hand at her left waist holding the zipper pull, elbow out; hem unchanged at mid-calf. RIGHT: arms relaxed.
0.2s  LEFT: holds the opened zipper, the left panel swaying slightly; right side top edge stays at bust height. RIGHT: still.
0.4s  LEFT: brings the opened left panel back up across her chest with both hands so only a thin strip of the black tube top shows at the top edge; her left hand then grabs the loose satin at her left side. RIGHT: still.
0.6s  LEFT: right forearm across her chest holding the top edge in place; left hand pulls the loose satin at her left side outward and up to waist height; the left side of the hem rises toward the knee, the right side stays at mid-calf. RIGHT: still.
0.8s  LEFT: her right arm crosses her chest holding the top edge at her left chest; her left hand lifts the gathered satin from her left hip toward her left chest; the left side of the hem rises to the knee, the right side stays at mid-calf. RIGHT: still.
1.0s  LEFT: her right hand grips the gathered satin at her left upper chest; her left hand lifts the corner up toward her left shoulder; the more fabric she lifts, the shorter the hem gets: just above the knee on her right leg, higher on her left leg. RIGHT: still.
1.2s  LEFT: both hands at her left upper chest raising a large section of satin; a cascade forms down her left side (image-right); her left thigh becomes exposed under it, the hem on her right leg (image-left) at mid-thigh. RIGHT: still.
1.4s  LEFT: both shoulders still bare, fabric NOT over the shoulder yet; top edge runs diagonally from under her right armpit (image-left) up to her left shoulder (image-right); her right hand crosses her chest gripping gathered satin just below her left collarbone; her left hand, elbow bent and raised, holds the lifted corner at her left shoulder height with the lighter inner lining showing at the edge; a wide cascade hangs down her left side (image-right) to mid-thigh showing the darker inner side; hem at mid-thigh on her right leg (image-left), her left upper thigh (image-right) exposed under the cascade. RIGHT: arms relaxed.
```

## SEG 4 — KF4 시작 · 2.4초 (원본 3.6–6.0s)

```
Image-to-video, start from the attached image. Locked-off static camera: no zoom, no pan, no cuts. Split screen: LEFT half = STYLING, RIGHT half = WEARING. Keep both women's face, makeup, outfit, room and lighting exactly as in the start image. Hair stays loose and down the whole time. Physics: as she lays the lifted corner over her left shoulder the hem stays short (mid-thigh on her right leg, upper thigh on her left); the cascade swings and settles with realistic weight; when she turns, the satin follows the turn with a slight delay. ORIENTATION LOCK: in front views her right side is on image-left and her left side is on image-right of the left half; in back views this flips. The satin goes over HER LEFT shoulder and the shawl-like cascade / wide draped sleeve hangs on HER LEFT arm, the same side as the covered shoulder; her right arm stays bare. The belt is slung low on her hips with the buckle just right of center; the clutch goes in her RIGHT hand. Never mirror the keyframes. Exactly one pair of mules and exactly one clutch exist; the top stays a wrapped satin drape (no seams, no cuffs); the WEARING woman on the right never gets a sleeve. No text. Duration 2.4s.

0.0s  LEFT: both shoulders still bare, fabric NOT over the shoulder yet; top edge runs diagonally from under her right armpit (image-left) up to her left shoulder (image-right); her right hand crosses her chest gripping gathered satin just below her left collarbone; her left hand, elbow bent and raised, holds the lifted corner at her left shoulder height with the lighter inner lining showing at the edge; a wide cascade hangs down her left side (image-right) to mid-thigh showing the darker inner side; hem at mid-thigh on her right leg (image-left), her left upper thigh (image-right) exposed under the cascade. RIGHT: arms relaxed.
0.2s  LEFT: her left hand lifts the corner up onto the top of her left shoulder (image-right); her right hand stays at her left collarbone; cascade sways. RIGHT: still.
0.4s  LEFT: the corner is laid over her left shoulder so the satin now covers her left shoulder and falls down over her left upper arm like a cape; she starts tilting her head down; right shoulder stays bare. RIGHT: still.
0.6s  LEFT: head down; her LEFT shoulder and LEFT upper arm are completely covered by the satin like a cape, only her left forearm and hand come up from under it, elbow down at her side, left hand at her upper chest just left of center; her bare right arm crosses to meet it, right hand pinching the top edge at the same spot; she begins twisting the top edge. RIGHT: turns her head to her left (image-right) into three-quarter profile, chin slightly down.
0.8s  LEFT: both hands together at her upper chest just left of center twist the top edge into a small tight roll; the satin cape stays over her left shoulder and upper arm, the cascade hanging over the outside of her left arm as a wide wing on image-right to mid-thigh. RIGHT: holds the profile.
1.0s  LEFT: head down, both hands at her upper chest tucking the twisted roll under the top edge to secure the drape; left shoulder and upper arm still covered by the cape, right shoulder and right arm bare. RIGHT: profile.
1.2s  LEFT: presses the tucked end in firmly with her fingertips. RIGHT: profile.
1.4s  LEFT: her left hand lets go and drops to her left hip, holding the lower edge of the drape under the cascade; her right hand stays on the secured point; she lifts her head. RIGHT: profile.
1.6s  LEFT: looks at camera; her right hand lies flat on her chest just below the secured point at her left shoulder, pressing it; left hand at her left hip under the cascade. RIGHT: profile.
1.8s  LEFT: her right hand smooths the top edge across her chest toward her right side. RIGHT: profile.
2.0s  LEFT: her right fingertips run along the top edge to her right armpit (image-left) and press it flat against her side so it stays. RIGHT: turns her head back toward camera.
2.2s  LEFT: picks up the leather belt from the bed edge with her right hand and starts turning around to her left, satin following the turn. RIGHT: facing front, arms relaxed.
2.4s  LEFT: back view, turned away from camera, loose hair swept forward over her right shoulder; the satin goes over her LEFT shoulder (image-left in this back view) with the top edge running diagonally from under her right armpit up to her left shoulder; her left arm extended out and down at 45 degrees holding the cascade, which starts at her left shoulder, fanned out wide; right arm relaxed holding the belt; right shoulder blade bare; mini hem at upper thigh. RIGHT: facing front, arms relaxed.
```

## SEG 5 — KF5 시작 · 2.4초 (원본 6.0–8.4s)

```
Image-to-video, start from the attached image. Locked-off static camera: no zoom, no pan, no cuts. Split screen: LEFT half = STYLING, RIGHT half = WEARING. Keep both women's face, makeup, loose hair, outfit, room and lighting exactly as in the start image. Physics: a pair of brown satin open-toe mules sits on the floor beside her right foot and the wide dark-brown leather belt is already in her right hand; nothing appears out of nowhere. Cinching the belt blouses the satin over it and lifts the hem to upper thigh. Realistic satin weight. ORIENTATION LOCK: in front views her right side is on image-left and her left side is on image-right of the left half; in back views this flips. The satin goes over HER LEFT shoulder and the shawl-like cascade / wide draped sleeve hangs on HER LEFT arm, the same side as the covered shoulder; her right arm stays bare. The belt is slung low on her hips with the buckle just right of center; the clutch goes in her RIGHT hand. Never mirror the keyframes. Exactly one pair of mules and exactly one clutch exist; the top stays a wrapped satin drape (no seams, no cuffs); the WEARING woman on the right never gets a sleeve. No text. Duration 2.4s.

0.0s  LEFT: back view, left arm holding the satin cascade out to the side. RIGHT: facing front, arms relaxed.
0.2s  LEFT: lowers her left arm, satin swings back to her body. RIGHT: still.
0.4s  LEFT: back view, both arms at her sides. RIGHT: still.
0.6s  LEFT: turns back toward camera to her right, satin following. RIGHT: still.
0.8s  LEFT: front view, head down, right arm out to the side holding the end of the wide leather belt; hem at mid-thigh. RIGHT: starts lifting her right hand.
1.0s  LEFT: wraps the belt low around her hips over the satin, right hand holding the square silver buckle at center. RIGHT: points her right index finger toward the left half at waist level, left hand at her waist.
1.2s  LEFT: threads the belt into the buckle, head down. RIGHT: keeps pointing.
1.4s  LEFT: pulls the belt snug; the satin blouses over it; she steps into the brown satin mules on the floor. RIGHT: pointing.
1.6s  LEFT: now standing in the mules; right hand on her right hip holding the belt tail, left hand at the buckle just right of center, belt slung low on her hips; the drape lifts on her right side showing dark brown mini shorts; hem at upper thigh. RIGHT: pointing.
1.8s  LEFT: pulls the belt tail along her right hip. RIGHT: pointing.
2.0s  LEFT: presses the belt end at her right hip, gaze down. RIGHT: pointing.
2.2s  LEFT: tucks the belt tail into the belt at her right hip; satin bloused like a peplum above the shorts. RIGHT: pointing.
2.4s  LEFT: looks up at camera, right hand at her right thigh tugging the satin hem, left arm lowered in the voluminous draped sleeve. RIGHT: lowers her arm, left hand lightly at hip.
```

## SEG 6 — KF6 시작 · 2.0초 (원본 8.4–10.4s)

```
Image-to-video, start from the attached image. Locked-off static camera: no zoom, no pan, no cuts. Split screen: LEFT half = STYLING, RIGHT half = WEARING. Keep both women's face, makeup, loose hair, outfit, room and lighting exactly as in the start image. Physics: a small cream woven leather clutch rests on the bed edge just behind her right hip within reach; she picks it up, it does not appear from nowhere. Hem stays at upper thigh; the draped sleeve billows and settles with realistic weight. ORIENTATION LOCK: in front views her right side is on image-left and her left side is on image-right of the left half; in back views this flips. The satin goes over HER LEFT shoulder and the shawl-like cascade / wide draped sleeve hangs on HER LEFT arm, the same side as the covered shoulder; her right arm stays bare. The belt is slung low on her hips with the buckle just right of center; the clutch goes in her RIGHT hand. Never mirror the keyframes. Exactly one pair of mules and exactly one clutch exist; the top stays a wrapped satin drape (no seams, no cuffs); the WEARING woman on the right never gets a sleeve. No text. Duration 2.0s.

0.0s  LEFT: looking at camera, right hand at her right thigh tugging the hem, left arm in the draped sleeve. RIGHT: left hand lightly at hip.
0.2s  LEFT: shifts her weight onto one leg in a slight contrapposto, left forearm bent outward showing the wide sleeve. RIGHT: smooths the skirt at her hip.
0.4s  LEFT: angles her body slightly to her left, right hand at her thigh. RIGHT: arms relaxed.
0.6s  LEFT: faces front, left arm out with the sleeve billowing, slight smile. RIGHT: arms relaxed at sides.
0.8s  LEFT: right hand reaches back to her side and picks up the cream clutch, legs together. RIGHT: still.
1.0s  LEFT: holds the clutch at her right hip, left forearm bent outward at waist level, right foot starts crossing in front of the left. RIGHT: still.
1.2s  LEFT: legs crossed at the ankles, right foot in front, in the open-toe heels; confident gaze into camera, subtle smile. RIGHT: neutral smile.
1.4s  LEFT: holds the pose, sleeve settling. RIGHT: still.
1.6s  LEFT: slight shoulder shift toward camera. RIGHT: still.
1.8s  LEFT: holds still. RIGHT: still.
2.0s  LEFT: final pose, clutch at hip, crossed legs, confident subtle smile into camera. RIGHT: standing straight, arms relaxed, neutral smile.
```
