# Look 1 — 구간별 영상 프롬프트 (이미지 6장 → 영상 6개, 0.2초 타임라인)

- 시작 이미지: KF1~KF6 (`reel_look1_7kf_prompt.md` 1~6번). 각 영상은 해당 이미지에서 시작.
- 끝 이미지를 지원하는 툴이면 다음 키프레임(KF2~KF7)을 끝 프레임으로 넣으면 연결이 더 정확함.
- 타임라인은 원본 영상 0.2초 분석 기준. 시간은 각 영상 시작 기준 상대 시간.
- 툴의 최소 길이가 구간보다 길면, 가장 짧은 길이로 뽑고 편집에서 구간 길이에 맞게 속도 조절/트림.

---

## SEG 1 — KF1 시작 · 1.2초 (원본 0.0–1.2s)

```
Image-to-video, start from the attached image. Locked-off static camera: no zoom, no pan, no cuts. Split screen: LEFT half = STYLING, RIGHT half = WEARING. Keep both women's face, makeup, loose hair, outfit, room and lighting exactly as in the start image. Physics: the satin skirt has a fixed length; the hem rises and falls exactly as much as the waistband does, never touches the floor while the waistband is above her waist, and the satin swings with realistic weight and gravity. No text. Duration 1.2s.

0.0s  LEFT: arms at chest height stretching the waistband wide just under her armpits, hem at mid-calf. RIGHT: arms relaxed at sides.
0.2s  LEFT: holds the pose, satin sways slightly. RIGHT: still.
0.4s  LEFT: lifts the stretched waistband to her collarbone, forearms vertical; the hem rises to upper calf. RIGHT: still.
0.6s  LEFT: holds the waistband taut at the collarbone, satin falls in long straight folds. RIGHT: moves both hands to the front of her hips.
0.8s  LEFT: starts bringing her hands inward. RIGHT: smooths the skirt with both palms on her hips.
1.0s  LEFT: lowers the waistband onto her bust and presses it to her chest with her fingertips, elbows out; worn as a strapless tube dress, hem back at mid-calf. RIGHT: hands on hips.
1.2s  LEFT: lets go and raises both open palms beside her shoulders in a playful "ta-da", light smile. RIGHT: hands lightly at the sides of her hips.
```

## SEG 2 — KF2 시작 · 1.0초 (원본 1.2–2.2s)

```
Image-to-video, start from the attached image. Locked-off static camera: no zoom, no pan, no cuts. Split screen: LEFT half = STYLING, RIGHT half = WEARING. Keep both women's face, makeup, loose hair, outfit, room and lighting exactly as in the start image. Physics: the satin skirt has a fixed length; folding the top down does not lengthen it, hem stays at mid-calf, satin moves with realistic weight. No text. Duration 1.0s.

0.0s  LEFT: palms open beside her shoulders, strapless satin tube dress, hem at mid-calf. RIGHT: hands lightly at hip sides.
0.2s  LEFT: opens her arms wider at shoulder height, palms up, light smile. RIGHT: lowers arms to her sides.
0.4s  LEFT: lowers her arms out from her sides at hip level, palms forward. RIGHT: arms relaxed.
0.6s  LEFT: her right hand grips the top edge at center chest, left hand goes to her left hip, elbow out. RIGHT: still.
0.8s  LEFT: right hand pulls the top edge down and outward, revealing the black tube top. RIGHT: still.
1.0s  LEFT: the top of the satin is folded down to just under the bust, black tube top fully visible, right hand holding the folded edge at her left chest, left hand on hip. RIGHT: arms relaxed.
```

## SEG 3 — KF3 시작 · 1.4초 (원본 2.2–3.6s)

```
Image-to-video, start from the attached image. Locked-off static camera: no zoom, no pan, no cuts. Split screen: LEFT half = STYLING, RIGHT half = WEARING. Keep both women's face, makeup, loose hair, outfit, room and lighting exactly as in the start image. Physics: the satin skirt has a fixed length; as fabric is gathered and pulled over her shoulder, the hem rises by exactly the amount of fabric used, first on her left side, then across the front. No fabric appears from nowhere. Realistic satin weight and gravity. No text. Duration 1.4s.

0.0s  LEFT: satin folded under the bust, black tube top visible, right hand at left chest, left hand on hip, hem at mid-calf. RIGHT: arms relaxed.
0.2s  LEFT: holds the fold at the bust line, elbow out. RIGHT: still.
0.4s  LEFT: right arm crosses her chest to gather fabric; left hand takes a section of satin at her left hip and starts lifting it. RIGHT: still.
0.6s  LEFT: right forearm across chest covering the tube top again; left hand lifts the gathered satin to waist height; left side of the hem rises to the knee, right side stays at mid-calf. RIGHT: still.
0.8s  LEFT: right hand holds fabric at her left armpit, left hand raises the gathered corner toward her left shoulder; hem diagonal from mid-calf to knee. RIGHT: still.
1.0s  LEFT: right hand now on her left shoulder holding a fold of satin as it goes over; left side of the hem above the knee. RIGHT: still.
1.2s  LEFT: a large swath of satin pulled over her left shoulder; the front hem rises to upper thigh on her right leg, a cascade hangs from her left shoulder to the knee. RIGHT: still.
1.4s  LEFT: right hand gripping the fabric at her left shoulder, satin twisted diagonally from left shoulder to right hip, right shoulder bare, asymmetric hem: upper thigh on the right, knee-length cascade on the left. RIGHT: arms relaxed.
```

## SEG 4 — KF4 시작 · 2.4초 (원본 3.6–6.0s)

```
Image-to-video, start from the attached image. Locked-off static camera: no zoom, no pan, no cuts. Split screen: LEFT half = STYLING, RIGHT half = WEARING. Keep both women's face, makeup, outfit, room and lighting exactly as in the start image. Hair stays loose and down the whole time. Physics: the drape keeps the same amount of fabric, hem stays at upper thigh in front; the cascade swings and settles with realistic weight; when she turns, the satin follows the turn with a slight delay. No text. Duration 2.4s.

0.0s  LEFT: right hand at her left shoulder, one-shoulder asymmetric drape, eyes to camera. RIGHT: arms relaxed.
0.2s  LEFT: tightens the fold at her shoulder, cascade sways. RIGHT: still.
0.4s  LEFT: drape settles, eyes to camera. RIGHT: still.
0.6s  LEFT: tilts her head down to look at her chest; right forearm horizontal across her upper chest adjusting the fold; the cascade forms a wide wing down her left arm. RIGHT: turns her head to her left into three-quarter profile, chin slightly down.
0.8s  LEFT: both hands at her upper chest tucking the satin edge, head down. RIGHT: holds the profile.
1.0s  LEFT: right hand presses the fabric at her left collarbone. RIGHT: profile.
1.2s  LEFT: right hand flat on her upper chest, head down. RIGHT: profile.
1.4s  LEFT: lifts her head slightly. RIGHT: profile.
1.6s  LEFT: looks up at camera; right hand on her chest just below the left shoulder, left hand under the drape at her left hip. RIGHT: profile.
1.8s  LEFT: right hand on chest, left hand at waist under the satin. RIGHT: profile.
2.0s  LEFT: right fingertips at her left collarbone. RIGHT: turns her head back toward camera.
2.2s  LEFT: picks up the leather belt from the bed edge with her right hand and starts turning around to her left, satin following the turn. RIGHT: facing front, arms relaxed.
2.4s  LEFT: back view, turned away from camera, loose hair down her back; left arm extended out to the side holding the cascading satin away from her body to show its volume; right hand holding the belt; right shoulder and upper back bare; hem just above the knee. RIGHT: facing front, arms relaxed.
```

## SEG 5 — KF5 시작 · 2.4초 (원본 6.0–8.4s)

```
Image-to-video, start from the attached image. Locked-off static camera: no zoom, no pan, no cuts. Split screen: LEFT half = STYLING, RIGHT half = WEARING. Keep both women's face, makeup, loose hair, outfit, room and lighting exactly as in the start image. Physics: a pair of brown satin open-toe mules sits on the floor beside her right foot and the wide dark-brown leather belt is already in her right hand; nothing appears out of nowhere. Cinching the belt blouses the satin over it and lifts the hem to upper thigh. Realistic satin weight. No text. Duration 2.4s.

0.0s  LEFT: back view, left arm holding the satin cascade out to the side. RIGHT: facing front, arms relaxed.
0.2s  LEFT: lowers her left arm, satin swings back to her body. RIGHT: still.
0.4s  LEFT: back view, both arms at her sides. RIGHT: still.
0.6s  LEFT: turns back toward camera to her right, satin following. RIGHT: still.
0.8s  LEFT: front view, head down, right arm out to the side holding the end of the wide leather belt; hem at mid-thigh. RIGHT: starts lifting her right hand.
1.0s  LEFT: wraps the belt around her waist over the satin, right hand holding the square silver buckle at center. RIGHT: points her right index finger toward the left half at waist level, left hand at her waist.
1.2s  LEFT: threads the belt into the buckle, head down. RIGHT: keeps pointing.
1.4s  LEFT: pulls the belt snug; the satin blouses over it; she steps into the brown satin mules on the floor. RIGHT: pointing.
1.6s  LEFT: now standing in the mules; right hand on her right hip holding the belt tail, left hand at the buckle at front-left; the drape lifts on her right side showing dark brown mini shorts; hem at upper thigh. RIGHT: pointing.
1.8s  LEFT: pulls the belt tail along her right hip. RIGHT: pointing.
2.0s  LEFT: presses the belt end at her right hip, gaze down. RIGHT: pointing.
2.2s  LEFT: tucks the belt tail into the belt at her right hip; satin bloused like a peplum above the shorts. RIGHT: pointing.
2.4s  LEFT: looks up at camera, right hand at her right thigh tugging the satin hem, left arm lowered in the voluminous draped sleeve. RIGHT: lowers her arm, left hand lightly at hip.
```

## SEG 6 — KF6 시작 · 2.0초 (원본 8.4–10.4s)

```
Image-to-video, start from the attached image. Locked-off static camera: no zoom, no pan, no cuts. Split screen: LEFT half = STYLING, RIGHT half = WEARING. Keep both women's face, makeup, loose hair, outfit, room and lighting exactly as in the start image. Physics: a small cream woven leather clutch rests on the bed edge just behind her right hip within reach; she picks it up, it does not appear from nowhere. Hem stays at upper thigh; the draped sleeve billows and settles with realistic weight. No text. Duration 2.0s.

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
