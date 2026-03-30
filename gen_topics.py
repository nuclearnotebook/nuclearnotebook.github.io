#!/usr/bin/env python3
"""Generate all Classical Mechanics topic pages"""

import os

TOPICS = [
    {
        "slug": "newtons-laws",
        "num": "01",
        "title": "Newton's Laws of Motion",
        "icon": "⚙",
        "subtitle": "The Three Fundamental Principles of Classical Dynamics",
        "tags": ["Dynamics", "Forces", "Inertia"],
        "sim": False,
        "keywords": "Newton's laws of motion, inertia, F=ma, action reaction, classical mechanics, force, acceleration, mass",
        "description": "A comprehensive study of Newton's three laws of motion — the foundation of classical mechanics. Covers inertia, the second law F=ma, action-reaction pairs, applications, and historical context.",
        "img": "https://images.unsplash.com/photo-1635070041078-e363dbe005cb?w=1200&q=75&auto=format",
        "img_alt": "Newton's laws physics concept — gears and mechanical forces",
        "content": """
<p>Isaac Newton's three laws of motion, published in the <em>Principia Mathematica</em> in 1687, represent one of the greatest intellectual achievements in human history. These laws unified terrestrial and celestial mechanics under a single framework, transforming natural philosophy into quantitative science. They remain the cornerstone of classical mechanics and continue to govern the design of everything from bridges to spacecraft.</p>

<h2>The First Law — Law of Inertia</h2>
<p><strong>Statement:</strong> <em>An object at rest stays at rest, and an object in uniform motion continues in a straight line at constant velocity, unless acted upon by a net external force.</em></p>
<p>This law defines inertia — the resistance of any physical object to changes in its state of motion. A bowling ball rolling on a frictionless surface would continue forever in the same direction at the same speed. In reality, friction and air resistance are always present to slow objects down, which historically misled observers into believing that force was required to maintain motion. Newton's genius was recognising that undisturbed motion continues unchanged.</p>

<div class="info-box info-box--note">
  <div class="info-box-title" style="color:var(--accent-plasma)">💡 Key Insight</div>
  <p style="margin:0">The First Law also defines what physicists mean by an <strong>inertial reference frame</strong> — a frame in which a body not subject to forces moves in a straight line at constant velocity. All of Newton's mechanics is formulated in inertial frames.</p>
</div>

<p>The quantitative measure of inertia is mass (m), measured in kilograms. A more massive object has more inertia — it is harder to accelerate and harder to stop. This is why a loaded truck takes much longer to brake than an empty bicycle.</p>

<h2>The Second Law — Law of Acceleration</h2>
<p><strong>Statement:</strong> <em>The net force on an object equals the rate of change of its momentum. For constant mass, this reduces to F = ma.</em></p>

<div class="formula-block">
  <span class="formula-label">Newton's Second Law</span>
  F⃗<sub>net</sub> = m · a⃗  &nbsp;|&nbsp;  F = dp/dt
</div>

<p>This is the most important equation in classical mechanics. It tells us that force (measured in Newtons, N) equals the product of mass (kg) and acceleration (m/s²). The relationship is:</p>
<ul style="margin:0 0 16px 20px;color:var(--text-secondary)">
  <li style="margin-bottom:8px"><strong>Proportional to force:</strong> Double the force → double the acceleration</li>
  <li style="margin-bottom:8px"><strong>Inversely proportional to mass:</strong> Double the mass → halve the acceleration</li>
  <li style="margin-bottom:8px"><strong>Vector relationship:</strong> Force and acceleration point in the same direction</li>
</ul>
<p>The more general form dp/dt (rate of change of momentum) applies even when mass changes — for example, in rocket propulsion where the rocket loses mass as it expels fuel.</p>

<div class="info-box info-box--fact">
  <div class="info-box-title" style="color:#a078ff">📊 Quantitative Example</div>
  <p style="margin:0">A 1500 kg car accelerates from rest to 27.8 m/s (100 km/h) in 8 seconds. The required net force is: F = 1500 × (27.8/8) = 1500 × 3.47 = <strong>5,212 N</strong>, or about 5.2 kN.</p>
</div>

<h2>The Third Law — Law of Action-Reaction</h2>
<p><strong>Statement:</strong> <em>For every action, there is an equal and opposite reaction. When object A exerts a force on object B, object B simultaneously exerts an equal and opposite force on object A.</em></p>

<div class="formula-block">
  <span class="formula-label">Third Law</span>
  F⃗<sub>A on B</sub> = −F⃗<sub>B on A</sub>
</div>

<p>This law is frequently misunderstood. The action and reaction forces:</p>
<ul style="margin:0 0 16px 20px;color:var(--text-secondary)">
  <li style="margin-bottom:8px">Always act on <strong>different objects</strong> — they never cancel each other out</li>
  <li style="margin-bottom:8px">Are always equal in magnitude and opposite in direction</li>
  <li style="margin-bottom:8px">Are always of the same type (both gravitational, both normal force, etc.)</li>
  <li style="margin-bottom:8px">Act simultaneously — there is no time delay</li>
</ul>

<p>Consider a horse pulling a cart. The horse pulls the cart forward with force F. The cart pulls the horse backward with the same force F. So why does the system accelerate? Because the horse's hooves push backward on the ground, and the ground pushes the horse forward (a third-law pair). It is this ground reaction that accelerates the horse-cart system.</p>

<h2>Types of Forces in Classical Mechanics</h2>
<p>Newton's laws apply to all forces. The most common forces encountered in mechanics are:</p>

<div class="table-wrap">
<table>
<thead><tr><th>Force Type</th><th>Symbol</th><th>Direction</th><th>Formula</th></tr></thead>
<tbody>
<tr><td>Weight / Gravity</td><td>W or F<sub>g</sub></td><td>Downward (toward Earth's centre)</td><td>W = mg</td></tr>
<tr><td>Normal Force</td><td>N or F<sub>N</sub></td><td>Perpendicular to surface</td><td>Varies (from constraint)</td></tr>
<tr><td>Tension</td><td>T</td><td>Along rope / string (inward)</td><td>Varies</td></tr>
<tr><td>Friction</td><td>f</td><td>Parallel to surface, opposing motion</td><td>f = μN</td></tr>
<tr><td>Spring Force</td><td>F<sub>s</sub></td><td>Toward equilibrium position</td><td>F = −kx</td></tr>
<tr><td>Air Drag</td><td>D or F<sub>D</sub></td><td>Opposing velocity</td><td>D = ½ρCdAv²</td></tr>
</tbody>
</table>
</div>

<h2>Free Body Diagrams</h2>
<p>A free body diagram (FBD) is an essential tool for applying Newton's second law. It shows a single object with all forces acting on it drawn as arrows from the object's centre. The procedure is:</p>
<ol style="margin:0 0 16px 20px;color:var(--text-secondary)">
  <li style="margin-bottom:8px">Identify the object of interest</li>
  <li style="margin-bottom:8px">Draw all forces acting on that object (not forces it exerts on others)</li>
  <li style="margin-bottom:8px">Set up coordinate axes (often with one axis along the direction of motion)</li>
  <li style="margin-bottom:8px">Resolve forces into components and apply ΣF = ma separately for each axis</li>
  <li style="margin-bottom:8px">Solve the resulting system of equations</li>
</ol>

<h2>Applications Across Science and Engineering</h2>
<p>Newton's laws are not mere abstractions — they underpin virtually every branch of engineering and applied science. Structural engineers use them to ensure buildings and bridges do not collapse. Aerospace engineers apply them to calculate the thrust needed to orbit a satellite. Every automobile is designed with F=ma in mind, from braking distance to suspension response.</p>
<p>In biomechanics, Newton's laws explain how muscles generate locomotion, how bones withstand forces, and how sports techniques can be optimised. In robotics, they govern the equations of motion that controllers must solve in real time.</p>

<h2>Limitations of Newton's Laws</h2>
<p>Despite their extraordinary success, Newton's laws break down in two regimes:</p>
<ul style="margin:0 0 16px 20px;color:var(--text-secondary)">
  <li style="margin-bottom:10px"><strong>Very high velocities (approaching c):</strong> Special relativity replaces classical mechanics. Mass becomes velocity-dependent and the simple F=ma must be replaced with relativistic equations.</li>
  <li style="margin-bottom:10px"><strong>Very small scales (atomic/subatomic):</strong> Quantum mechanics governs. The deterministic trajectories of Newton give way to probabilistic wavefunctions governed by the Schrödinger equation.</li>
</ul>
<p>Nevertheless, for the vast majority of everyday phenomena — from cars and buildings to planets and galaxies — Newton's laws remain exact to extraordinary precision.</p>

<div class="info-box info-box--tip">
  <div class="info-box-title" style="color:var(--accent-green)">🎓 Historical Context</div>
  <p style="margin:0">Newton built on the work of Galileo Galilei, who first identified inertia and the independence of horizontal and vertical motion. Newton's great synthesis was the recognition that the same force (gravity) that makes apples fall also keeps the Moon in orbit — unifying terrestrial and celestial mechanics for the first time.</p>
</div>
"""
    },
    {
        "slug": "projectile-motion",
        "num": "02",
        "title": "Projectile Motion",
        "icon": "🎯",
        "subtitle": "Two-Dimensional Kinematics Under Gravity",
        "tags": ["Kinematics", "2D Motion", "Gravity"],
        "sim": True,
        "keywords": "projectile motion, range equation, trajectory, ballistics, maximum height, angle of projection, horizontal range, physics",
        "description": "Complete guide to projectile motion — trajectory equations, range, maximum height, optimal angles, air resistance effects, and real-world applications including ballistics and sports physics.",
        "img": "https://images.unsplash.com/photo-1604881989793-466aca8dd319?w=1200&q=75&auto=format",
        "img_alt": "Projectile trajectory arc over landscape",
        "sim_html": """
<!-- ═══════════════ PROJECTILE MOTION SIMULATION ═══════════════ -->
<div class="simulation-wrapper">
  <div class="simulation-toolbar">
    <span class="simulation-title">🎯 Projectile Motion Simulator</span>
    <div class="sim-control">
      <label>Angle (°)</label>
      <input type="range" id="sim-angle" min="5" max="85" value="45" step="1"/>
      <span id="val-angle">45°</span>
    </div>
    <div class="sim-control">
      <label>Speed (m/s)</label>
      <input type="range" id="sim-speed" min="10" max="100" value="50" step="5"/>
      <span id="val-speed">50 m/s</span>
    </div>
    <div class="sim-control">
      <label>Gravity (m/s²)</label>
      <input type="range" id="sim-gravity" min="1.6" max="24.8" value="9.8" step="0.2"/>
      <span id="val-gravity">9.8</span>
    </div>
    <button id="sim-launch" class="btn btn-primary" style="padding:7px 18px;font-size:0.78rem">Launch</button>
    <button id="sim-reset"  class="btn btn-outline" style="padding:7px 14px;font-size:0.78rem">Reset</button>
  </div>
  <div class="sim-canvas-wrap">
    <canvas id="proj-canvas" height="380"></canvas>
  </div>
  <div style="padding:14px 20px;display:flex;gap:24px;flex-wrap:wrap;font-family:var(--font-mono);font-size:0.78rem;color:var(--text-muted);background:rgba(0,0,0,0.2);border-top:1px solid var(--border-dim)">
    <span>Range: <strong id="out-range" style="color:var(--accent-plasma)">—</strong></span>
    <span>Max Height: <strong id="out-height" style="color:var(--accent-green)">—</strong></span>
    <span>Time of Flight: <strong id="out-time" style="color:var(--accent-gold)">—</strong></span>
    <span>Vx: <strong id="out-vx" style="color:var(--text-secondary)">—</strong></span>
    <span>Vy₀: <strong id="out-vy" style="color:var(--text-secondary)">—</strong></span>
  </div>
</div>
<script>
(function(){
  const canvas  = document.getElementById('proj-canvas');
  const ctx     = canvas.getContext('2d');
  const slAngle = document.getElementById('sim-angle');
  const slSpeed = document.getElementById('sim-speed');
  const slGrav  = document.getElementById('sim-gravity');
  const btnL    = document.getElementById('sim-launch');
  const btnR    = document.getElementById('sim-reset');
  const vAngle  = document.getElementById('val-angle');
  const vSpeed  = document.getElementById('val-speed');
  const vGrav   = document.getElementById('val-gravity');
  const oRange  = document.getElementById('out-range');
  const oHeight = document.getElementById('out-height');
  const oTime   = document.getElementById('out-time');
  const oVx     = document.getElementById('out-vx');
  const oVy     = document.getElementById('out-vy');

  let anim = null, points = [], animIdx = 0;
  const PAD = 50;

  function resize(){
    canvas.width  = canvas.offsetWidth || canvas.parentElement.offsetWidth;
    canvas.height = 380;
  }
  resize();
  window.addEventListener('resize', ()=>{ resize(); drawEmpty(); });

  slAngle.oninput = ()=>{ vAngle.textContent  = slAngle.value+'°'; };
  slSpeed.oninput = ()=>{ vSpeed.textContent  = slSpeed.value+' m/s'; };
  slGrav.oninput  = ()=>{ vGrav.textContent   = parseFloat(slGrav.value).toFixed(1); };

  function calcPoints(v0, angleDeg, g){
    const theta = angleDeg * Math.PI / 180;
    const vx = v0 * Math.cos(theta);
    const vy = v0 * Math.sin(theta);
    const tFlight = 2 * vy / g;
    const range   = vx * tFlight;
    const hMax    = (vy * vy) / (2 * g);
    const pts = [];
    const steps = 300;
    for(let i = 0; i <= steps; i++){
      const t = (i / steps) * tFlight;
      pts.push({ x: vx * t, y: vy * t - 0.5 * g * t * t });
    }
    return { pts, range, hMax, tFlight, vx, vy };
  }

  function toCanvas(px, py, range, hMax){
    const W = canvas.width  - 2*PAD;
    const H = canvas.height - 2*PAD;
    const sx = PAD + (px / (range * 1.1)) * W;
    const sy = (canvas.height - PAD) - (py / (hMax * 1.3)) * H;
    return [sx, sy];
  }

  function drawEmpty(){
    ctx.clearRect(0,0,canvas.width,canvas.height);
    // Ground
    ctx.beginPath();
    ctx.strokeStyle = 'rgba(0,212,255,0.2)';
    ctx.lineWidth = 1;
    ctx.moveTo(PAD, canvas.height - PAD);
    ctx.lineTo(canvas.width - PAD, canvas.height - PAD);
    ctx.stroke();
    // Axes labels
    ctx.fillStyle = 'rgba(100,150,200,0.4)';
    ctx.font = '11px JetBrains Mono, monospace';
    ctx.fillText('x (m) →', canvas.width - 80, canvas.height - PAD + 18);
    ctx.save();
    ctx.translate(PAD - 18, canvas.height/2);
    ctx.rotate(-Math.PI/2);
    ctx.fillText('y (m) ↑', 0, 0);
    ctx.restore();
  }

  function drawPath(allPts, upTo, range, hMax, vx, vy){
    ctx.clearRect(0,0,canvas.width,canvas.height);
    drawEmpty();

    if(allPts.length < 2) return;

    // Full ghost path
    ctx.beginPath();
    ctx.strokeStyle = 'rgba(0,212,255,0.12)';
    ctx.lineWidth = 1.5;
    ctx.setLineDash([4,4]);
    const [x0,y0] = toCanvas(allPts[0].x, allPts[0].y, range, hMax);
    ctx.moveTo(x0,y0);
    allPts.forEach(p => { const [cx,cy] = toCanvas(p.x,p.y,range,hMax); ctx.lineTo(cx,cy); });
    ctx.stroke();
    ctx.setLineDash([]);

    // Drawn path so far
    ctx.beginPath();
    ctx.strokeStyle = '#00d4ff';
    ctx.lineWidth = 2.5;
    ctx.shadowColor = '#00d4ff';
    ctx.shadowBlur = 8;
    const s0 = toCanvas(allPts[0].x, allPts[0].y, range, hMax);
    ctx.moveTo(s0[0], s0[1]);
    for(let i=1;i<=upTo && i<allPts.length;i++){
      const [cx,cy] = toCanvas(allPts[i].x,allPts[i].y,range,hMax);
      ctx.lineTo(cx,cy);
    }
    ctx.stroke();
    ctx.shadowBlur = 0;

    // Projectile dot
    if(upTo < allPts.length){
      const [bx,by] = toCanvas(allPts[upTo].x, allPts[upTo].y, range, hMax);
      ctx.beginPath();
      ctx.arc(bx, by, 7, 0, Math.PI*2);
      ctx.fillStyle = '#ff6b1a';
      ctx.shadowColor = '#ff6b1a';
      ctx.shadowBlur = 12;
      ctx.fill();
      ctx.shadowBlur = 0;
    }

    // Max height marker
    const peakIdx = allPts.reduce((mi,p,i,arr)=> p.y > arr[mi].y ? i : mi, 0);
    if(upTo >= peakIdx){
      const [px2,py2] = toCanvas(allPts[peakIdx].x, allPts[peakIdx].y, range, hMax);
      ctx.beginPath();
      ctx.arc(px2, py2, 4, 0, Math.PI*2);
      ctx.fillStyle = '#00ff88';
      ctx.fill();
      ctx.fillStyle = '#00ff88';
      ctx.font = '10px JetBrains Mono, monospace';
      ctx.fillText(`H=${hMax.toFixed(1)}m`, px2+8, py2-6);
    }
  }

  function launch(){
    cancelAnimationFrame(anim);
    const v0 = parseFloat(slSpeed.value);
    const ang = parseFloat(slAngle.value);
    const g   = parseFloat(slGrav.value);
    const { pts, range, hMax, tFlight, vx, vy } = calcPoints(v0, ang, g);
    points = pts;
    animIdx = 0;

    oRange.textContent  = range.toFixed(1) + ' m';
    oHeight.textContent = hMax.toFixed(1) + ' m';
    oTime.textContent   = tFlight.toFixed(2) + ' s';
    oVx.textContent     = vx.toFixed(1) + ' m/s';
    oVy.textContent     = vy.toFixed(1) + ' m/s';

    function step(){
      drawPath(pts, animIdx, range, hMax, vx, vy);
      if(animIdx < pts.length - 1){ animIdx+=2; anim = requestAnimationFrame(step); }
      else drawPath(pts, pts.length-1, range, hMax, vx, vy);
    }
    step();
  }

  function reset(){
    cancelAnimationFrame(anim);
    points = [];
    drawEmpty();
    [oRange,oHeight,oTime,oVx,oVy].forEach(el=>el.textContent='—');
  }

  btnL.addEventListener('click', launch);
  btnR.addEventListener('click', reset);
  drawEmpty();
})();
</script>
""",
        "content": """
<p>Projectile motion describes the two-dimensional motion of an object launched with an initial velocity and subsequently subject only to the constant downward acceleration due to gravity. It is perhaps the most classical problem in physics — Galileo studied it in the early 17th century — and it underpins ballistics, sports science, and the design of any object that travels through the air.</p>

<h2>The Key Principle: Independence of Motion</h2>
<p>Galileo's greatest insight was that <strong>horizontal and vertical motion are completely independent of one another</strong>. The horizontal motion of a projectile is uniform (constant velocity, since there is no horizontal force, ignoring air resistance). The vertical motion is uniformly accelerated downward at g = 9.81 m/s².</p>
<p>This means we can decompose any projectile problem into two separate 1D kinematics problems and solve them independently.</p>

<div class="formula-block">
  <span class="formula-label">Decomposed Initial Velocity</span>
  v<sub>x</sub> = v₀ cos θ &nbsp;&nbsp;&nbsp; v<sub>y0</sub> = v₀ sin θ
</div>

<h2>Equations of Motion for a Projectile</h2>
<p>Let the launch point be the origin, launch speed v₀, angle θ above horizontal, and gravitational acceleration g downward:</p>

<div class="formula-block">
  <span class="formula-label">Position Components</span>
  x(t) = v₀ cos θ · t<br/>
  y(t) = v₀ sin θ · t − ½g t²
</div>

<div class="formula-block">
  <span class="formula-label">Velocity Components</span>
  v<sub>x</sub>(t) = v₀ cos θ &nbsp; (constant)<br/>
  v<sub>y</sub>(t) = v₀ sin θ − g·t
</div>

<h2>Key Derived Quantities</h2>
<div class="table-wrap">
<table>
<thead><tr><th>Quantity</th><th>Formula</th><th>Derivation</th></tr></thead>
<tbody>
<tr><td>Time to peak</td><td>t<sub>peak</sub> = v₀ sin θ / g</td><td>Set v_y = 0</td></tr>
<tr><td>Maximum height</td><td>H = v₀² sin²θ / (2g)</td><td>y at t = t_peak</td></tr>
<tr><td>Total flight time</td><td>T = 2v₀ sin θ / g</td><td>y(T) = 0</td></tr>
<tr><td>Horizontal range</td><td>R = v₀² sin 2θ / g</td><td>x at t = T</td></tr>
</tbody>
</table>
</div>

<h2>The Trajectory Equation (Parabolic Path)</h2>
<p>Eliminating t from the x and y equations gives the trajectory — the shape of the path in space. The result is always a parabola (for constant g, no air resistance):</p>

<div class="formula-block">
  <span class="formula-label">Trajectory Equation</span>
  y = x tan θ − gx² / (2v₀² cos²θ)
</div>

<p>This is the equation of an inverted parabola opening downward, with the vertex at the maximum height point.</p>

<h2>Optimal Angle for Maximum Range</h2>
<p>The range R = v₀² sin 2θ / g is maximised when sin 2θ = 1, i.e., when 2θ = 90°, giving <strong>θ = 45°</strong>. This result assumes flat terrain, no air resistance, and launch at ground level.</p>

<div class="info-box info-box--note">
  <div class="info-box-title" style="color:var(--accent-plasma)">💡 Complementary Angles</div>
  <p style="margin:0">Two launch angles that are supplementary to 45° — such as 30° and 60° — give the <strong>same horizontal range</strong> but different trajectories. The 30° shot is flatter and faster; the 60° shot is higher and slower.</p>
</div>

<h2>Effect of Air Resistance</h2>
<p>In reality, air drag significantly alters projectile motion. The drag force is approximately proportional to v² (for fast objects) or v (for slow ones), directed opposite to velocity. This makes the equations nonlinear and non-separable. Key consequences of air resistance are:</p>
<ul style="margin:0 0 16px 20px;color:var(--text-secondary)">
  <li style="margin-bottom:8px">The optimal angle for maximum range decreases below 45° (typically to 30°–40° for sports balls)</li>
  <li style="margin-bottom:8px">The trajectory is no longer symmetric — the descent is steeper than the ascent</li>
  <li style="margin-bottom:8px">The projectile asymptotically approaches terminal velocity if it falls far enough</li>
  <li style="margin-bottom:8px">The maximum height and range are both reduced</li>
</ul>

<h2>Applications: Sports, Ballistics, and Space</h2>
<p>Projectile motion has profound practical applications. In sports science, understanding the optimal launch angle helps athletes in shot put (around 41°–42°), long jump, and basketball free throws. Ballistics engineers apply projectile equations to artillery shells, though at long ranges the Earth's curvature, Coriolis effect, and aerodynamics must all be considered.</p>
<p>In space exploration, the launch and re-entry of spacecraft involves projectile-like arcs at the boundary where atmospheric drag becomes important. The design of orbital insertion manoeuvres builds on the same fundamental kinematics.</p>

<h2>Projectile Motion on Other Worlds</h2>
<p>The same equations apply on any celestial body with different gravitational acceleration. On the Moon (g = 1.62 m/s²), a ball thrown at 45° with v₀ = 20 m/s would travel <strong>6 times further</strong> than on Earth. On Jupiter (g = 24.8 m/s²), it would travel only about 40% as far. The simulation above lets you explore these scenarios.</p>
"""
    },
    {
        "slug": "conservation-of-energy",
        "num": "03",
        "title": "Conservation of Energy",
        "icon": "⚡",
        "subtitle": "Work, Energy, and the Principle of Conservation",
        "tags": ["Energy", "Work", "Conservation Laws"],
        "sim": True,
        "keywords": "conservation of energy, kinetic energy, potential energy, work energy theorem, conservative forces, mechanical energy, energy transformation",
        "description": "In-depth exploration of energy conservation in classical mechanics — work-energy theorem, kinetic and potential energy, conservative forces, and energy conservation in systems.",
        "img": "https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?w=1200&q=75&auto=format",
        "img_alt": "Energy and power — electrical systems representing energy conservation",
        "sim_html": """
<div class="simulation-wrapper">
  <div class="simulation-toolbar">
    <span class="simulation-title">⚡ Energy Skate Park Simulator</span>
    <div class="sim-control">
      <label>Mass (kg)</label>
      <input type="range" id="ep-mass" min="1" max="20" value="5" step="1"/>
      <span id="ep-mass-val">5 kg</span>
    </div>
    <div class="sim-control">
      <label>Height (m)</label>
      <input type="range" id="ep-height" min="1" max="20" value="10" step="1"/>
      <span id="ep-height-val">10 m</span>
    </div>
    <button id="ep-start" class="btn btn-primary" style="padding:7px 18px;font-size:0.78rem">Drop</button>
    <button id="ep-reset" class="btn btn-outline"  style="padding:7px 14px;font-size:0.78rem">Reset</button>
  </div>
  <div class="sim-canvas-wrap"><canvas id="ep-canvas" height="340"></canvas></div>
  <div style="padding:14px 20px;display:flex;gap:28px;flex-wrap:wrap;font-family:var(--font-mono);font-size:0.78rem;color:var(--text-muted);background:rgba(0,0,0,0.2);border-top:1px solid var(--border-dim)">
    <span>KE: <strong id="ep-ke" style="color:var(--accent-plasma)">0 J</strong></span>
    <span>PE: <strong id="ep-pe" style="color:var(--accent-nova)">0 J</strong></span>
    <span>Total E: <strong id="ep-te" style="color:var(--accent-gold)">0 J</strong></span>
    <span>Speed: <strong id="ep-v"  style="color:var(--accent-green)">0 m/s</strong></span>
  </div>
</div>
<script>
(function(){
  const canvas = document.getElementById('ep-canvas');
  const ctx    = canvas.getContext('2d');
  const massSl = document.getElementById('ep-mass');
  const hSl    = document.getElementById('ep-height');
  const massV  = document.getElementById('ep-mass-val');
  const hV     = document.getElementById('ep-height-val');
  let raf=null, y=0, vy=0, running=false;
  const g=9.81;
  function W(){ return canvas.width = canvas.offsetWidth||600; }
  function H(){ return canvas.height=340; }
  W(); H();
  window.addEventListener('resize',()=>{W();draw();});
  massSl.oninput=()=>massV.textContent=massSl.value+' kg';
  hSl.oninput=()=>hV.textContent=hSl.value+' m';
  const m=()=>parseFloat(massSl.value);
  const h0=()=>parseFloat(hSl.value);
  function updateInfo(y,vy){
    const m2=m(), h=h0(), scale=(canvas.height-80)/h;
    const curH = Math.max(0, h - y/scale);
    const pe=m2*g*curH, ke=0.5*m2*vy*vy, te=m2*g*h;
    document.getElementById('ep-ke').textContent=(ke).toFixed(1)+' J';
    document.getElementById('ep-pe').textContent=(pe).toFixed(1)+' J';
    document.getElementById('ep-te').textContent=(te).toFixed(1)+' J';
    document.getElementById('ep-v' ).textContent=Math.abs(vy).toFixed(2)+' m/s';
  }
  function draw(){
    const W2=canvas.width, H2=canvas.height, m2=m(), h=h0();
    const scale=(H2-80)/h;
    ctx.clearRect(0,0,W2,H2);
    // Sky gradient
    const grad=ctx.createLinearGradient(0,0,0,H2);
    grad.addColorStop(0,'#050810'); grad.addColorStop(1,'#0d1530');
    ctx.fillStyle=grad; ctx.fillRect(0,0,W2,H2);
    // Ground
    ctx.fillStyle='rgba(0,212,255,0.15)'; ctx.fillRect(0,H2-50,W2,50);
    ctx.strokeStyle='rgba(0,212,255,0.4)'; ctx.lineWidth=2;
    ctx.beginPath(); ctx.moveTo(0,H2-50); ctx.lineTo(W2,H2-50); ctx.stroke();
    // Height reference line
    const topY=40;
    ctx.setLineDash([6,6]); ctx.strokeStyle='rgba(123,47,255,0.3)'; ctx.lineWidth=1;
    ctx.beginPath(); ctx.moveTo(80,topY); ctx.lineTo(W2-80,topY); ctx.stroke();
    ctx.setLineDash([]);
    ctx.fillStyle='rgba(123,47,255,0.5)'; ctx.font='11px JetBrains Mono, monospace';
    ctx.fillText(`h = ${h} m`, W2-120, topY-6);
    // Energy bars
    const barX=W2-70, barMaxH=H2-100, barW=20;
    const te=m2*g*h;
    const curH2=Math.max(0, h-(y/scale||0));
    const pe=m2*g*curH2; const ke=te-pe;
    // PE bar
    ctx.fillStyle='rgba(123,47,255,0.2)'; ctx.fillRect(barX-5,40,barW,barMaxH);
    const peH=(pe/te)*barMaxH;
    ctx.fillStyle='rgba(123,47,255,0.7)'; ctx.fillRect(barX-5,40+barMaxH-peH,barW,peH);
    ctx.fillStyle='rgba(123,47,255,0.9)'; ctx.font='9px JetBrains Mono,monospace';
    ctx.fillText('PE',barX-3,35);
    // KE bar
    const bx2=barX+barW+4;
    ctx.fillStyle='rgba(0,212,255,0.15)'; ctx.fillRect(bx2,40,barW,barMaxH);
    const keH=(ke/te)*barMaxH;
    ctx.fillStyle='rgba(0,212,255,0.7)'; ctx.fillRect(bx2,40+barMaxH-keH,barW,keH);
    ctx.fillStyle='rgba(0,212,255,0.9)'; ctx.fillText('KE',bx2+2,35);
    // Ball
    const ballX=W2/2-60;
    const ballY=topY + (y||0);
    ctx.beginPath(); ctx.arc(ballX,ballY,14,0,Math.PI*2);
    ctx.fillStyle='#ff6b1a'; ctx.shadowColor='#ff6b1a'; ctx.shadowBlur=16; ctx.fill(); ctx.shadowBlur=0;
  }
  function start(){
    if(running)return;
    running=true; y=0; vy=0;
    const h=h0(), scale=(canvas.height-80)/h;
    const maxY=h*scale;
    let last=null;
    function step(ts){
      if(!last)last=ts;
      const dt=Math.min((ts-last)/1000,0.03); last=ts;
      vy+=g*dt; y+=vy*dt*scale;
      if(y>=maxY){y=maxY;vy=-vy*0.7;}
      updateInfo(y,vy); draw();
      if(running && Math.abs(vy)>0.1) raf=requestAnimationFrame(step);
      else running=false;
    }
    raf=requestAnimationFrame(step);
  }
  function reset(){ cancelAnimationFrame(raf); running=false; y=0; vy=0; draw(); updateInfo(0,0); }
  document.getElementById('ep-start').onclick=start;
  document.getElementById('ep-reset').onclick=reset;
  draw(); updateInfo(0,0);
})();
</script>
""",
        "content": """
<p>The conservation of energy is one of the most fundamental and far-reaching principles in all of science. In classical mechanics, it states that the total mechanical energy of an isolated system — the sum of kinetic and potential energy — remains constant in time. This is not merely a convenience; it reflects a deep symmetry of nature known as <em>time-translation symmetry</em> (Noether's theorem), and it holds across every domain of physics from the quantum scale to cosmology.</p>

<h2>Work and the Work-Energy Theorem</h2>
<p>The concept of energy in mechanics begins with the concept of <strong>work</strong>. The work done by a force on an object is defined as the force component along the direction of displacement, multiplied by the displacement magnitude:</p>

<div class="formula-block">
  <span class="formula-label">Work Done by a Force</span>
  W = F⃗ · d⃗ = Fd cos θ
</div>

<p>Where θ is the angle between the force vector and the displacement vector. If θ = 0° (force parallel to motion), W = Fd, the maximum work. If θ = 90° (force perpendicular to motion, as in circular motion), W = 0. If θ = 180° (force opposing motion), W = −Fd, negative work.</p>

<p>The work-energy theorem connects work to the change in kinetic energy:</p>

<div class="formula-block">
  <span class="formula-label">Work-Energy Theorem</span>
  W<sub>net</sub> = ΔKE = ½mv<sub>f</sub>² − ½mv<sub>i</sub>²
</div>

<h2>Kinetic Energy</h2>
<p>Kinetic energy (KE) is the energy an object possesses due to its motion. For a particle of mass m moving at speed v:</p>

<div class="formula-block">
  <span class="formula-label">Kinetic Energy</span>
  KE = ½mv²
</div>

<p>Kinetic energy is always non-negative and is measured in Joules (J = kg·m²/s²). It is proportional to the square of speed — doubling the speed quadruples the kinetic energy. This is why high-speed collisions are so much more destructive than low-speed ones.</p>

<h2>Potential Energy</h2>
<p>Potential energy (PE) is stored energy associated with the configuration of a system. The most important forms in classical mechanics are:</p>
<ul style="margin:0 0 20px 20px;color:var(--text-secondary)">
  <li style="margin-bottom:12px"><strong>Gravitational PE:</strong> U<sub>g</sub> = mgh (near Earth's surface, h measured from reference level)</li>
  <li style="margin-bottom:12px"><strong>Elastic PE:</strong> U<sub>e</sub> = ½kx² (spring compressed or stretched by x from equilibrium)</li>
  <li style="margin-bottom:12px"><strong>Gravitational PE (general):</strong> U<sub>g</sub> = −GMm/r (between masses M and m separated by distance r)</li>
</ul>

<h2>Conservative vs. Non-Conservative Forces</h2>
<p>A force is <strong>conservative</strong> if the work it does on a particle is independent of the path taken — it depends only on the initial and final positions. Gravity and spring forces are conservative. For such forces, we can define a potential energy function U such that F = −dU/dx.</p>
<p>A force is <strong>non-conservative</strong> if the work done depends on the path. Friction and air drag are non-conservative; they always do negative work, converting mechanical energy to thermal energy.</p>

<div class="formula-block">
  <span class="formula-label">Conservation of Mechanical Energy (conservative forces only)</span>
  KE + PE = constant<br/>
  ½mv₁² + U₁ = ½mv₂² + U₂
</div>

<h2>Energy Transformation</h2>
<p>When an object falls under gravity, its potential energy is continuously converted to kinetic energy. At the bottom of the fall (just before impact), all the original potential energy has been converted to kinetic energy (ignoring air resistance):</p>

<div class="formula-block">
  <span class="formula-label">Free Fall Energy</span>
  mgh = ½mv² &nbsp;⟹&nbsp; v = √(2gh)
</div>

<p>This shows that the final speed of a falling object depends only on the height fallen, not on the mass — exactly as Galileo famously demonstrated. It also means that a ball released from height h and a ball that slides frictionlessly down a curved ramp of height h both arrive at the bottom with the same speed.</p>

<h2>Power</h2>
<p>Power is the rate of doing work — how fast energy is transferred:</p>

<div class="formula-block">
  <span class="formula-label">Power</span>
  P = dW/dt = F⃗ · v⃗ = Fv cos θ
</div>

<p>The SI unit of power is the Watt (W = J/s). A 1 kW motor lifting a 100 kg object can raise it at 100/9.81 ≈ 10.2 kg·m/s, or about 1 m/s. The older unit of horsepower (1 hp ≈ 746 W) is still used for engines.</p>

<h2>Non-Conservative Systems and Heat</h2>
<p>When friction acts, mechanical energy is not conserved — it is converted to thermal energy (heat). The total energy of the universe is still conserved, but the mechanical energy decreases. For a system with friction:</p>

<div class="formula-block">
  <span class="formula-label">With Friction</span>
  ΔKE + ΔPE = −W<sub>friction</sub>
</div>

<p>where W<sub>friction</sub> is the work done by friction (a positive number, since friction always removes mechanical energy). The "lost" energy heats the surfaces in contact — a tire skidding on a road heats both the tire and the road.</p>

<div class="info-box info-box--tip">
  <div class="info-box-title" style="color:var(--accent-green)">🎓 Noether's Theorem</div>
  <p style="margin:0">The deep reason that energy is conserved is that the laws of physics do not change with time — they are the same today as yesterday and tomorrow. This time-translation symmetry, via Emmy Noether's theorem (1915), guarantees the existence of a conserved quantity we call energy. Every symmetry in nature corresponds to a conservation law.</p>
</div>
"""
    },
    {
        "slug": "simple-harmonic-motion",
        "num": "07",
        "title": "Simple Harmonic Motion",
        "icon": "〜",
        "subtitle": "The Mathematics of Periodic Oscillation",
        "tags": ["Oscillations", "SHM", "Waves"],
        "sim": True,
        "keywords": "simple harmonic motion, SHM, pendulum, spring mass system, oscillation, period, frequency, amplitude, phase, angular frequency",
        "description": "Complete treatment of simple harmonic motion — spring-mass systems, pendulums, the equation of SHM, phase, amplitude, energy in SHM, and applications in physics and engineering.",
        "img": "https://images.unsplash.com/photo-1606761568499-6d2451b23c66?w=1200&q=75&auto=format",
        "img_alt": "Pendulum clock and oscillation physics",
        "sim_html": """
<div class="simulation-wrapper">
  <div class="simulation-toolbar">
    <span class="simulation-title">〜 Spring-Mass + Pendulum Simulator</span>
    <div class="sim-control">
      <label>Mode</label>
      <select id="shm-mode" style="background:var(--bg-deep);color:var(--text-primary);border:1px solid var(--border-dim);padding:4px 8px;border-radius:6px;font-size:0.78rem">
        <option value="spring">Spring-Mass</option>
        <option value="pendulum">Pendulum</option>
      </select>
    </div>
    <div class="sim-control">
      <label>Amplitude</label>
      <input type="range" id="shm-amp" min="20" max="120" value="80" step="5"/>
      <span id="shm-amp-val">80px</span>
    </div>
    <div class="sim-control">
      <label>Period (T)</label>
      <input type="range" id="shm-period" min="1" max="6" value="2" step="0.5"/>
      <span id="shm-period-val">2 s</span>
    </div>
    <button id="shm-toggle" class="btn btn-primary" style="padding:7px 18px;font-size:0.78rem">Start</button>
  </div>
  <div class="sim-canvas-wrap"><canvas id="shm-canvas" height="360"></canvas></div>
  <div style="padding:14px 20px;display:flex;gap:24px;flex-wrap:wrap;font-family:var(--font-mono);font-size:0.78rem;color:var(--text-muted);background:rgba(0,0,0,0.2);border-top:1px solid var(--border-dim)">
    <span>x(t): <strong id="shm-x" style="color:var(--accent-plasma)">—</strong></span>
    <span>v(t): <strong id="shm-v" style="color:var(--accent-green)">—</strong></span>
    <span>KE: <strong id="shm-ke" style="color:var(--accent-gold)">—</strong></span>
    <span>PE: <strong id="shm-pe" style="color:#a078ff">—</strong></span>
    <span>Phase: <strong id="shm-phase" style="color:var(--text-secondary)">—</strong></span>
  </div>
</div>
<script>
(function(){
  const cv=document.getElementById('shm-canvas'), cx=cv.getContext('2d');
  const ampSl=document.getElementById('shm-amp'), perSl=document.getElementById('shm-period');
  const modeSel=document.getElementById('shm-mode'), btn=document.getElementById('shm-toggle');
  let running=false, raf=null, t=0;
  function W(){return cv.width=cv.offsetWidth||700;}
  function H(){return cv.height=360;}
  W();H();window.addEventListener('resize',()=>{W();if(!running)draw(0);});
  ampSl.oninput=()=>document.getElementById('shm-amp-val').textContent=ampSl.value+'px';
  perSl.oninput=()=>document.getElementById('shm-period-val').textContent=perSl.value+' s';
  const A=()=>parseInt(ampSl.value), T=()=>parseFloat(perSl.value);
  const omega=()=>2*Math.PI/T();
  function draw(time){
    const w=cv.width,h=cv.height,mode=modeSel.value;
    const amp=A(), T2=T(), om=omega();
    const x0=w*0.28, y0=h/2;
    const x=amp*Math.cos(om*time);
    const v=-amp*om*Math.sin(om*time);
    const phase=((om*time)%(2*Math.PI)).toFixed(2);
    const ke=0.5*v*v/(amp*amp); const pe=0.5*x*x/(amp*amp);
    document.getElementById('shm-x').textContent=(x/10).toFixed(2)+' cm';
    document.getElementById('shm-v').textContent=(v/10).toFixed(2)+' cm/s';
    document.getElementById('shm-ke').textContent=(ke*100).toFixed(1)+'%';
    document.getElementById('shm-pe').textContent=(pe*100).toFixed(1)+'%';
    document.getElementById('shm-phase').textContent=phase+' rad';
    cx.clearRect(0,0,w,h);
    const bg=cx.createLinearGradient(0,0,0,h);
    bg.addColorStop(0,'#050810');bg.addColorStop(1,'#0a0e20');
    cx.fillStyle=bg;cx.fillRect(0,0,w,h);
    // Draw trace
    const traceW=w*0.55, traceX=w*0.42, pts=200;
    cx.beginPath(); cx.strokeStyle='rgba(0,212,255,0.2)'; cx.lineWidth=1;
    cx.moveTo(traceX,y0);cx.lineTo(traceX+traceW,y0);cx.stroke();
    cx.beginPath(); cx.strokeStyle='#00d4ff'; cx.lineWidth=2;
    cx.shadowColor='#00d4ff'; cx.shadowBlur=6;
    for(let i=0;i<=pts;i++){
      const tt=time-(i/pts)*T2*2;
      const xx=amp*Math.cos(om*tt);
      const px=traceX+traceW*(1-i/pts);
      const py=y0-xx;
      i===0?cx.moveTo(px,py):cx.lineTo(px,py);
    }
    cx.stroke(); cx.shadowBlur=0;
    if(mode==='spring'){
      // Wall
      cx.fillStyle='rgba(0,212,255,0.1)'; cx.fillRect(30,y0-70,16,140);
      cx.fillStyle='rgba(0,212,255,0.3)'; cx.fillRect(44,y0-70,4,140);
      // Spring zigzag
      const sx=48, ex=x0+x-20, zig=12, segs=14;
      cx.beginPath(); cx.strokeStyle='#7b2fff'; cx.lineWidth=2.5;
      cx.moveTo(sx,y0);
      for(let i=1;i<=segs;i++){
        const px=sx+((ex-sx)*i/segs);
        const py=y0+(i%2===0?zig:-zig);
        cx.lineTo(px,py);
      }
      cx.lineTo(ex,y0); cx.stroke();
      // Mass
      cx.beginPath(); cx.arc(x0+x,y0,22,0,Math.PI*2);
      cx.fillStyle='#ff6b1a'; cx.shadowColor='#ff6b1a'; cx.shadowBlur=14; cx.fill(); cx.shadowBlur=0;
    } else {
      // Pivot
      cx.beginPath(); cx.arc(x0,60,8,0,Math.PI*2); cx.fillStyle='rgba(0,212,255,0.5)'; cx.fill();
      // String
      const len=amp+80;
      const angle=Math.asin(x/len);
      const bx=x0+len*Math.sin(angle), by=60+len*Math.cos(angle);
      cx.beginPath(); cx.strokeStyle='rgba(200,200,255,0.5)'; cx.lineWidth=1.5;
      cx.moveTo(x0,60); cx.lineTo(bx,by); cx.stroke();
      // Bob
      cx.beginPath(); cx.arc(bx,by,18,0,Math.PI*2);
      cx.fillStyle='#7b2fff'; cx.shadowColor='#7b2fff'; cx.shadowBlur=14; cx.fill(); cx.shadowBlur=0;
    }
    // Equilibrium marker
    cx.setLineDash([4,4]); cx.strokeStyle='rgba(255,255,255,0.12)'; cx.lineWidth=1;
    cx.beginPath(); cx.moveTo(x0,30); cx.lineTo(x0,h-30); cx.stroke(); cx.setLineDash([]);
  }
  function loop(ts){
    t=ts/1000; draw(t); raf=requestAnimationFrame(loop);
  }
  btn.onclick=()=>{
    if(running){ cancelAnimationFrame(raf); running=false; btn.textContent='Start'; }
    else { running=true; btn.textContent='Pause'; raf=requestAnimationFrame(loop); }
  };
  draw(0);
})();
</script>
""",
        "content": """
<p>Simple harmonic motion (SHM) is the most fundamental type of periodic motion in physics. It describes the oscillation of any system in which the restoring force is proportional to displacement from equilibrium. From the vibration of atoms in a crystal lattice to the oscillation of a child's swing, from the alternating current in an electrical circuit to the quantum ground state of a harmonic oscillator, SHM appears throughout the physical world as the simplest and most natural form of periodic behaviour.</p>

<h2>Defining Simple Harmonic Motion</h2>
<p>A system undergoes simple harmonic motion when it satisfies the equation:</p>

<div class="formula-block">
  <span class="formula-label">Equation of SHM</span>
  d²x/dt² = −ω²x &nbsp;&nbsp; or equivalently &nbsp;&nbsp; F = −kx
</div>

<p>Where x is the displacement from equilibrium, ω (omega) is the angular frequency, and k is the spring constant or equivalent restoring force constant. The negative sign ensures the force is always directed back toward equilibrium — this is what makes it oscillatory. Crucially, the force is proportional to displacement: double the displacement, double the restoring force.</p>

<h2>The General Solution</h2>
<p>Solving the differential equation d²x/dt² = −ω²x gives the general solution:</p>

<div class="formula-block">
  <span class="formula-label">Position in SHM</span>
  x(t) = A cos(ωt + φ)
</div>

<p>Where A is the amplitude (maximum displacement), ω is the angular frequency, t is time, and φ (phi) is the initial phase — which determines where in the cycle the oscillation begins.</p>

<h2>Key Parameters</h2>
<div class="table-wrap">
<table>
<thead><tr><th>Parameter</th><th>Symbol</th><th>Unit</th><th>Relationship</th></tr></thead>
<tbody>
<tr><td>Amplitude</td><td>A</td><td>metres (m)</td><td>Maximum displacement from equilibrium</td></tr>
<tr><td>Period</td><td>T</td><td>seconds (s)</td><td>T = 2π/ω = 1/f</td></tr>
<tr><td>Frequency</td><td>f</td><td>Hertz (Hz)</td><td>f = ω/(2π) = 1/T</td></tr>
<tr><td>Angular frequency</td><td>ω</td><td>rad/s</td><td>ω = 2πf = √(k/m)</td></tr>
<tr><td>Phase</td><td>φ</td><td>radians</td><td>Determined by initial conditions</td></tr>
</tbody>
</table>
</div>

<h2>Velocity and Acceleration in SHM</h2>
<p>Differentiating the displacement equation gives velocity and acceleration:</p>

<div class="formula-block">
  <span class="formula-label">Velocity</span>
  v(t) = −Aω sin(ωt + φ) &nbsp;&nbsp;→&nbsp;&nbsp; v<sub>max</sub> = Aω (at equilibrium)
</div>

<div class="formula-block">
  <span class="formula-label">Acceleration</span>
  a(t) = −Aω² cos(ωt + φ) &nbsp;&nbsp;→&nbsp;&nbsp; a<sub>max</sub> = Aω² (at extremes)
</div>

<p>Velocity is maximum at the equilibrium position and zero at the extremes. Acceleration is maximum at the extremes and zero at equilibrium. Notice that acceleration is always opposite in direction to displacement — this is the very definition of SHM.</p>

<h2>The Spring-Mass System</h2>
<p>The archetypal SHM system is a mass m attached to a spring of spring constant k. By Hooke's law, the spring force is F = −kx. Applying Newton's second law:</p>

<div class="formula-block">
  <span class="formula-label">Spring-Mass Period</span>
  T = 2π√(m/k) &nbsp;&nbsp;⟹&nbsp;&nbsp; ω = √(k/m)
</div>

<p>This reveals a profound result: the period depends on mass and spring constant, but <strong>not on amplitude</strong>. A spring oscillating with large amplitude takes exactly the same time per cycle as one with tiny amplitude. This amplitude independence is the hallmark of SHM and was crucial to the development of accurate clocks.</p>

<h2>The Simple Pendulum</h2>
<p>For small angles (θ ≪ 1 radian ≈ 15°), a pendulum of length L oscillates with SHM. The restoring force is the component of gravity along the arc, giving:</p>

<div class="formula-block">
  <span class="formula-label">Simple Pendulum Period</span>
  T = 2π√(L/g)
</div>

<p>Remarkably, the period is independent of both mass and amplitude (for small angles). This was the basis of Galileo's discovery while watching a chandelier swing in Pisa Cathedral. The dependence on √(L/g) was used historically to measure g by timing pendulum oscillations.</p>

<h2>Energy in SHM</h2>
<p>The total mechanical energy in SHM is constant and proportional to the square of the amplitude:</p>

<div class="formula-block">
  <span class="formula-label">Total Energy in SHM</span>
  E = ½kA² = ½mω²A²
</div>

<p>Energy oscillates back and forth between kinetic and potential forms:</p>
<ul style="margin:0 0 16px 20px;color:var(--text-secondary)">
  <li style="margin-bottom:8px"><strong>At equilibrium (x=0):</strong> All energy is kinetic. KE = ½mω²A², PE = 0</li>
  <li style="margin-bottom:8px"><strong>At extremes (x=±A):</strong> All energy is potential. KE = 0, PE = ½kA²</li>
  <li style="margin-bottom:8px"><strong>At intermediate x:</strong> KE = ½mω²(A²−x²), PE = ½kx²</li>
</ul>

<div class="info-box info-box--note">
  <div class="info-box-title" style="color:var(--accent-plasma)">💡 Velocity from Energy</div>
  <p style="margin:0">From energy conservation, the velocity at position x is: v = ω√(A² − x²). This gives v<sub>max</sub> = ωA at x = 0, and v = 0 at x = ±A, consistent with the differential approach.</p>
</div>

<h2>Universal Importance of SHM</h2>
<p>SHM is ubiquitous in physics because near any stable equilibrium, the potential energy looks like a parabola, and parabolic potential energy means a linear restoring force — which is precisely SHM. This is why atoms in crystals vibrate as harmonic oscillators, why quantum mechanics uses the harmonic oscillator as its most fundamental solvable system, and why AC electrical circuits exhibit oscillation analogous to mechanical SHM.</p>
"""
    },
]

def make_topic_html(topic, branch_name="Classical Mechanics", branch_slug="classical-mechanics"):
    sim_section = ""
    if topic.get("sim") and topic.get("sim_html"):
        sim_section = f"""
      <h2 id="simulation">Interactive Simulation</h2>
      {topic["sim_html"]}
"""

    tags_html = " ".join([f'<span class="tc-tag" style="padding:5px 12px;font-size:0.75rem">{t}</span>' for t in topic["tags"]])

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>{topic["title"]} — {branch_name} | QuantumAtlas</title>
  <meta name="description" content="{topic["description"]}"/>
  <meta name="keywords" content="{topic["keywords"]}"/>
  <link rel="canonical" href="https://yourdomain.com/topics/{branch_slug}/{topic["slug"]}.html"/>
  <meta property="og:title" content="{topic["title"]} | QuantumAtlas"/>
  <meta property="og:description" content="{topic["description"]}"/>
  <meta property="og:type" content="article"/>
  <meta property="og:image" content="{topic["img"]}"/>
  <meta name="twitter:card" content="summary_large_image"/>
  <script type="application/ld+json">{{
    "@context":"https://schema.org","@type":"Article",
    "headline":"{topic["title"]}",
    "description":"{topic["description"]}",
    "image":"{topic["img"]}",
    "author":{{"@type":"Organization","name":"QuantumAtlas"}},
    "publisher":{{"@type":"Organization","name":"QuantumAtlas","url":"https://yourdomain.com"}},
    "breadcrumb":{{"@type":"BreadcrumbList","itemListElement":[
      {{"@type":"ListItem","position":1,"name":"Home","item":"https://yourdomain.com/"}},
      {{"@type":"ListItem","position":2,"name":"Branches","item":"https://yourdomain.com/theory.html"}},
      {{"@type":"ListItem","position":3,"name":"{branch_name}","item":"https://yourdomain.com/branches/{branch_slug}.html"}},
      {{"@type":"ListItem","position":4,"name":"{topic["title"]}"}}
    ]}}
  }}</script>

  <script async src="https://www.googletagmanager.com/gtag/js?id=G-4X0M6RM0F6"></script>
  <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-4X0M6RM0F6',{{page_title:document.title,page_location:window.location.href}});</script>
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-2633513915753897" crossorigin="anonymous"></script>
  <meta name="google-adsense-account" content="ca-pub-2633513915753897">

  <link rel="stylesheet" href="../../css/global.css"/>
  <link rel="stylesheet" href="../../css/nav.css"/>
  <link rel="stylesheet" href="../../css/topic.css"/>
</head>
<body>
<div id="nav-placeholder"></div>

<main>
  <!-- Hero -->
  <section class="topic-hero">
    <img src="{topic["img"]}" alt="{topic["img_alt"]}" class="topic-hero-bg-img" loading="eager"/>
    <div class="topic-hero-overlay"></div>
    <div class="container topic-hero-content">
      <nav class="breadcrumb">
        <a href="../../index.html">Home</a><span class="sep">›</span>
        <a href="../../theory.html">Branches</a><span class="sep">›</span>
        <a href="../../branches/{branch_slug}.html">{branch_name}</a><span class="sep">›</span>
        <span class="current">{topic["title"]}</span>
      </nav>
      <div style="display:flex;gap:10px;flex-wrap:wrap;margin-bottom:18px">
        <span class="badge badge-plasma">{branch_name}</span>
        {"<span class='badge badge-green'>Interactive Simulation</span>" if topic.get("sim") else ""}
        <span class="badge badge-nova">Topic {topic["num"]}</span>
      </div>
      <h1 class="topic-hero-title">{topic["icon"]} {topic["title"]}</h1>
      <p class="topic-hero-sub">{topic["subtitle"]}</p>
      <div style="display:flex;gap:8px;flex-wrap:wrap;margin-top:20px">
        {tags_html}
      </div>
    </div>
  </section>

  <div class="container topic-layout">
    <!-- Article -->
    <article class="topic-article">
      <!-- AdSense top -->
      <div class="ad-container" style="margin-bottom:36px">
        <div style="text-align:center;width:100%">
          <span class="ad-label">Advertisement</span>
          <ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-2633513915753897" data-ad-slot="auto" data-ad-format="auto" data-full-width-responsive="true"></ins>
          <script>(adsbygoogle=window.adsbygoogle||[]).push({{}});</script>
        </div>
      </div>

      {sim_section}

      <div class="topic-body">
        {topic["content"]}
      </div>

      <!-- AdSense bottom -->
      <div class="ad-container" style="margin-top:40px">
        <div style="text-align:center;width:100%">
          <span class="ad-label">Advertisement</span>
          <ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-2633513915753897" data-ad-slot="auto" data-ad-format="auto" data-full-width-responsive="true"></ins>
          <script>(adsbygoogle=window.adsbygoogle||[]).push({{}});</script>
        </div>
      </div>
    </article>

    <!-- Sidebar -->
    <aside class="topic-sidebar">
      <div class="sidebar-card">
        <h4 style="font-family:var(--font-mono);font-size:0.75rem;text-transform:uppercase;letter-spacing:0.12em;color:var(--accent-plasma);margin-bottom:14px">// Topic Info</h4>
        <div class="sidebar-stat"><span>Branch</span><span>{branch_name}</span></div>
        <div class="sidebar-stat"><span>Topic</span><span>{topic["num"]} / 22</span></div>
        <div class="sidebar-stat"><span>Level</span><span>Advanced</span></div>
        <div class="sidebar-stat"><span>Simulation</span><span>{"Yes ✓" if topic.get("sim") else "No"}</span></div>
      </div>

      <div class="sidebar-card">
        <h4 style="font-family:var(--font-mono);font-size:0.75rem;text-transform:uppercase;letter-spacing:0.12em;color:var(--accent-plasma);margin-bottom:14px">// All Topics</h4>
        <ul style="list-style:none;display:flex;flex-direction:column;gap:6px">
          <li><a href="newtons-laws.html" style="font-size:0.82rem;color:var(--text-muted);text-decoration:none" class="{"active-topic" if topic["slug"]=="newtons-laws" else ""}">01. Newton's Laws</a></li>
          <li><a href="projectile-motion.html" style="font-size:0.82rem;color:var(--text-muted);text-decoration:none">02. Projectile Motion</a></li>
          <li><a href="conservation-of-energy.html" style="font-size:0.82rem;color:var(--text-muted);text-decoration:none">03. Conservation of Energy</a></li>
          <li><a href="linear-momentum.html" style="font-size:0.82rem;color:var(--text-muted);text-decoration:none">04. Linear Momentum</a></li>
          <li><a href="circular-motion.html" style="font-size:0.82rem;color:var(--text-muted);text-decoration:none">05. Circular Motion</a></li>
          <li><a href="gravitational-force.html" style="font-size:0.82rem;color:var(--text-muted);text-decoration:none">06. Gravitational Force</a></li>
          <li><a href="simple-harmonic-motion.html" style="font-size:0.82rem;color:var(--text-muted);text-decoration:none">07. Simple Harmonic Motion</a></li>
          <li><a href="rotational-dynamics.html" style="font-size:0.82rem;color:var(--text-muted);text-decoration:none">08. Rotational Dynamics</a></li>
          <li><a href="work-and-power.html" style="font-size:0.82rem;color:var(--text-muted);text-decoration:none">09. Work & Power</a></li>
          <li><a href="friction-and-drag.html" style="font-size:0.82rem;color:var(--text-muted);text-decoration:none">10. Friction & Drag</a></li>
          <li><a href="keplers-laws.html" style="font-size:0.82rem;color:var(--text-muted);text-decoration:none">11. Kepler's Laws</a></li>
          <li><a href="waves-and-oscillations.html" style="font-size:0.82rem;color:var(--text-muted);text-decoration:none">12. Waves & Oscillations</a></li>
          <li><a href="centre-of-mass.html" style="font-size:0.82rem;color:var(--text-muted);text-decoration:none">13. Centre of Mass</a></li>
          <li><a href="statics-and-equilibrium.html" style="font-size:0.82rem;color:var(--text-muted);text-decoration:none">14. Statics & Equilibrium</a></li>
          <li><a href="fluid-mechanics.html" style="font-size:0.82rem;color:var(--text-muted);text-decoration:none">15. Fluid Mechanics</a></li>
          <li><a href="elasticity-and-stress.html" style="font-size:0.82rem;color:var(--text-muted);text-decoration:none">16. Elasticity & Stress</a></li>
          <li><a href="kinematics.html" style="font-size:0.82rem;color:var(--text-muted);text-decoration:none">17. Kinematics</a></li>
          <li><a href="damped-oscillations.html" style="font-size:0.82rem;color:var(--text-muted);text-decoration:none">18. Damped Oscillations</a></li>
          <li><a href="lagrangian-mechanics.html" style="font-size:0.82rem;color:var(--text-muted);text-decoration:none">19. Lagrangian Mechanics</a></li>
          <li><a href="hamiltonian-mechanics.html" style="font-size:0.82rem;color:var(--text-muted);text-decoration:none">20. Hamiltonian Mechanics</a></li>
          <li><a href="rigid-body-motion.html" style="font-size:0.82rem;color:var(--text-muted);text-decoration:none">21. Rigid Body Motion</a></li>
          <li><a href="non-inertial-frames.html" style="font-size:0.82rem;color:var(--text-muted);text-decoration:none">22. Non-Inertial Frames</a></li>
        </ul>
      </div>

      <!-- Sidebar AdSense -->
      <div class="ad-container" style="min-height:250px;flex-direction:column">
        <span class="ad-label">Advertisement</span>
        <ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-2633513915753897" data-ad-slot="auto" data-ad-format="auto" data-full-width-responsive="true"></ins>
        <script>(adsbygoogle=window.adsbygoogle||[]).push({{}});</script>
      </div>
    </aside>
  </div>
</main>

<div id="footer-placeholder"></div>
<script src="../../js/components.js"></script>
</body>
</html>
"""

# Write the 4 fully detailed topics
os.makedirs('/home/claude/physics-website/topics/classical-mechanics', exist_ok=True)

for topic in TOPICS:
    html = make_topic_html(topic)
    path = f'/home/claude/physics-website/topics/classical-mechanics/{topic["slug"]}.html'
    with open(path, 'w') as f:
        f.write(html)
    print(f"Created: {topic['slug']}.html ({len(html):,} chars)")

print("Done with main topics")
