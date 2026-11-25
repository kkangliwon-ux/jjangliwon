# Look 1 — 어깨 고정 장면 (원본 3.6–6.0s)

원본 동작: 4번(3.6s)에서 왼쪽 어깨 높이로 든 모서리를 어깨에 올리고(3.8–4.0s), 고개를 숙여 두 손으로 모서리와 윗단을 꼬아 말아서 어깨 위에 끼워 고정(4.2–4.8s), 왼손은 골반으로 내리고 오른손으로 고정한 지점을 눌러 확인(5.0–5.2s), 윗단을 오른쪽 겨드랑이까지 쓸어 눌러 정리(5.4–5.6s), 그 뒤 돌아서 뒷모습(6.0s).

## 고정 장면 키프레임 (원본 4.6s) — 이미지 프롬프트

모델 사진 + 4번 이미지 첨부.

```
Generate one vertical 9:16 image. It is a keyframe of a continuous fashion reel shot on a locked-off camera.

MODEL REFERENCE: use the attached model photo as the identity reference for BOTH halves. Match her face, makeup, skin tone, hair color and hair length exactly. Hair loose (no bun, no ponytail).

LAYOUT: split screen divided down the middle by a thin seam. LEFT half = STYLING, RIGHT half = WEARING. Same woman in both halves, full body head to toe, static front-facing eye-level camera.

SETTING: minimal bedroom, pale grey wall, low bed with white dotted bedding behind her, dark wood plank floor, soft diffused daylight. On the left half, a pair of brown satin open-toe mules sits on the floor beside her right foot, and a wide dark-brown leather belt and a small cream woven clutch lie on the bed edge behind her.

ORIENTATION LOCK: front view, so her right side is on image-left and her left side is on image-right of the left half. The satin goes over HER LEFT shoulder (image-right). Her right shoulder and right arm (image-left) are bare. Do not mirror.

LEFT half (STYLING): barefoot. She is securing a bronze-brown liquid satin maxi skirt as a one-shoulder drape over a black strapless tube top (the tube top is fully covered).
POSITION LOCK:
- COVERAGE LOCK: her LEFT shoulder and her entire LEFT upper arm (image-right) are completely COVERED by the satin, which falls over them like a cape. No bare skin on her left shoulder or left upper arm.
- Only her left forearm and left hand are visible, coming up from under the cape: her left elbow is down at her side (NOT raised, NOT out to the side), forearm bent upward, left hand at her upper chest just left of center.
- Her bare RIGHT arm (image-left) is bent and crosses toward the center; her right hand meets the left hand at the same spot on her upper chest. Right shoulder and right arm fully bare.
- Both hands together are twisting the satin's top edge into a small tight roll and tucking it under the top edge to lock the drape.
- The top edge runs from just under her right armpit (image-left) straight across the bust, then up and over her left shoulder.
- Her head is tilted down, eyes on her hands.
- The cascade hangs over the outside of her left arm as a wide satin wing on image-right reaching mid-thigh, darker inner side visible; dark brown mini shorts peek out below it.
- Hem: the front panel curves from upper thigh on image-left; the cascade hangs to mid-thigh on image-right.
- No sewn seams, no cuffs: it is clearly a wrapped skirt.

RIGHT half (WEARING): black strapless tube top tucked into the bronze-brown satin mermaid maxi skirt worn at the natural waist, fitted at the hips and flaring so the hem grazes the floor, thin brown strappy heels. Her head is turned to her left (image-right) in three-quarter profile, chin slightly down. Arms relaxed and bare at her sides; no sleeve, no shawl.

PHYSICS: the skirt has a fixed length; the fabric over the shoulder and in the cascade is taken from the length, so the hem is short. Satin hangs under gravity from her covered left shoulder.

STYLE: photorealistic, natural skin texture, realistic satin sheen, smartphone fashion reel look. No text, labels, captions or watermark. No extra people.
```

## 영상 프롬프트 — 2.4초 (원본 3.6–6.0s, 0.2초 타임라인)

시작 이미지 = 4번, 중간 키프레임 = 위 고정 장면(1.0s), 끝 이미지 = 5번.
중간 키프레임을 못 넣는 툴이면 두 구간으로 나눠서: 4번→고정 장면(0.0–1.0s), 고정 장면→5번(1.0–2.4s).

```
Image-to-video, one continuous 2.4-second shot. Keyframes attached in order: image A at 0.0s (start), image B at 1.0s (securing the shoulder), image C at 2.4s (back view, end). The video must pass exactly through each keyframe at its timestamp.

CAMERA: locked-off static camera. No zoom, no pan, no cuts.

LAYOUT: split screen divided down the middle by a thin seam. LEFT half = STYLING, RIGHT half = WEARING. Same woman in both halves; keep her face, makeup, skin tone and loose hair exactly as in the keyframes. Room and lighting never change.

ORIENTATION LOCK: in front views her right side is on image-left and her left side is on image-right of the left half; in the back view this flips. The satin goes over HER LEFT shoulder and the cascade hangs on HER LEFT arm. Her right arm stays bare. The WEARING woman on the right never gets a sleeve. Never mirror the keyframes.

PROPS (LEFT half): brown mules on the floor beside her right foot; wide dark-brown leather belt and cream clutch on the bed edge behind her. Only her hands move them; at 2.2s she picks up the belt.

PHYSICS: the skirt has a fixed length; the hem stays short (mid-thigh on her right leg) because the fabric is over the shoulder and in the cascade. Twisting the top edge into a roll and tucking it at her upper chest locks the drape, so after 1.2s it stays in place without her hands. From 0.4s on, her left shoulder and left upper arm stay covered by the satin like a cape; only her left forearm and hand show. Satin has realistic weight and follows the turn with a slight delay.

STYLE: photorealistic, natural skin texture, realistic satin sheen, natural human motion speed. No text, labels, captions or watermark. No extra people.

TIMELINE (LEFT = styling, RIGHT = wearing):
0.0s  [KEYFRAME A]  LEFT: both shoulders bare; her right hand grips gathered satin just below her left collarbone; her left hand holds the lifted corner at her left shoulder height; cascade on her left side (image-right). RIGHT: arms relaxed.
0.2s  LEFT: her left hand lifts the corner up onto the top of her left shoulder (image-right); her right hand stays at her left collarbone; cascade sways. RIGHT: still.
0.4s  LEFT: the corner is laid over her left shoulder so the satin now covers her left shoulder and falls down over her left upper arm like a cape; she starts tilting her head down; right shoulder stays bare. RIGHT: still.
0.6s  LEFT: head down; her LEFT shoulder and LEFT upper arm are completely covered by the satin like a cape, only her left forearm and hand come up from under it, elbow down at her side, left hand at her upper chest just left of center; her bare right arm crosses to meet it, right hand pinching the top edge at the same spot; she begins twisting the top edge. RIGHT: turns her head to her left (image-right) into three-quarter profile, chin slightly down.
0.8s  LEFT: both hands together at her upper chest just left of center twist the top edge into a small tight roll; the satin cape stays over her left shoulder and upper arm, the cascade hanging over the outside of her left arm as a wide wing on image-right to mid-thigh. RIGHT: holds the profile.
1.0s  [KEYFRAME B]  LEFT: head down, both hands at her upper chest tucking the twisted roll under the top edge to secure the drape; left shoulder and upper arm still covered by the cape, right shoulder and right arm bare. RIGHT: profile.
1.2s  LEFT: presses the tucked end in firmly with her fingertips. RIGHT: profile.
1.4s  LEFT: her left hand lets go and drops to her left hip, holding the lower edge of the drape under the cascade; her right hand stays on the secured point; she lifts her head. RIGHT: profile.
1.6s  LEFT: looks at camera; her right hand lies flat on her chest just below the secured point at her left shoulder, pressing it; left hand at her left hip under the cascade. RIGHT: profile.
1.8s  LEFT: her right hand smooths the top edge across her chest toward her right side. RIGHT: profile.
2.0s  LEFT: her right fingertips run along the top edge to her right armpit (image-left) and press it flat against her side so it stays. RIGHT: turns her head back toward camera.
2.2s  LEFT: picks up the leather belt from the bed edge with her right hand, sweeps her loose hair forward over her right shoulder, and starts turning around to her left, satin following the turn. RIGHT: facing front, arms relaxed.
2.4s  [KEYFRAME C]  LEFT: back view; the satin goes over her LEFT shoulder (image-left in this back view), top edge running diagonally from under her right armpit up to her left shoulder; her left arm extended out and down at 45 degrees holding the cascade fanned out wide; right arm relaxed holding the belt; mini hem at upper thigh. RIGHT: facing front, arms relaxed.
```
