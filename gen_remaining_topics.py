#!/usr/bin/env python3
"""Generate remaining 18 Classical Mechanics topic pages as full-content pages"""

import os

BRANCH = "classical-mechanics"
BRANCH_NAME = "Classical Mechanics"

# Each topic: slug, num, title, icon, subtitle, keywords, img, content (~800+ words)
REMAINING = [
    {
        "slug": "linear-momentum",
        "num": "04", "icon": "💥",
        "title": "Linear Momentum & Collisions",
        "subtitle": "Impulse, Conservation, and the Physics of Impacts",
        "tags": ["Momentum","Collisions","Impulse"],
        "sim": False,
        "keywords": "linear momentum, conservation of momentum, impulse, elastic collision, inelastic collision, centre of mass, Newton's cradle, physics",
        "description": "Deep dive into linear momentum — impulse-momentum theorem, conservation of momentum, elastic and inelastic collisions, and the centre of mass frame.",
        "img": "https://images.unsplash.com/photo-1630839437035-dac17da580d0?w=1200&q=75&auto=format",
        "img_alt": "Collision physics and momentum — billiard balls impact",
        "content": """
<p>Linear momentum is one of the most fundamental conserved quantities in physics. The principle of conservation of linear momentum — that the total momentum of an isolated system never changes — is one of the most powerful tools in all of mechanics. It applies equally to collisions between billiard balls, the recoil of a rifle, the propulsion of rockets, and the evolution of galaxies.</p>

<h2>Definition of Linear Momentum</h2>
<p>The linear momentum of a particle is defined as the product of its mass and velocity:</p>
<div class="formula-block"><span class="formula-label">Linear Momentum</span>p⃗ = m·v⃗</div>
<p>Momentum is a vector — it has both magnitude and direction. The SI unit is kg·m/s. Newton's second law in its most general form is actually stated in terms of momentum:</p>
<div class="formula-block"><span class="formula-label">Newton's Second Law (general form)</span>F⃗<sub>net</sub> = dp⃗/dt</div>
<p>For constant mass, this reduces to F = ma. But the momentum form is more general and remains valid even when mass changes, as in rocket propulsion.</p>

<h2>Impulse and the Impulse-Momentum Theorem</h2>
<p>The impulse J⃗ of a force is its time integral — the area under the force-time curve:</p>
<div class="formula-block"><span class="formula-label">Impulse</span>J⃗ = ∫F⃗ dt = Δp⃗</div>
<p>The impulse-momentum theorem states that the impulse acting on a body equals the change in its momentum. This is extremely useful in collision analysis, where forces are large but act for very short times. The average force during a collision is F<sub>avg</sub> = Δp/Δt. A shorter collision time means a larger average force — which is why airbags (which increase collision time) reduce injuries.</p>

<h2>Conservation of Linear Momentum</h2>
<p>For an isolated system (no external forces), the total momentum is conserved:</p>
<div class="formula-block"><span class="formula-label">Conservation of Momentum</span>p⃗<sub>total</sub> = constant &nbsp;&nbsp;⟹&nbsp;&nbsp; Σm<sub>i</sub>v⃗<sub>i</sub> = constant</div>
<p>This follows directly from Newton's third law. In a two-body collision, the forces between the bodies are equal and opposite, so their momentum changes are equal and opposite, and the total momentum is unchanged.</p>

<h2>Types of Collisions</h2>
<div class="table-wrap"><table>
<thead><tr><th>Type</th><th>Momentum</th><th>Kinetic Energy</th><th>Example</th></tr></thead>
<tbody>
<tr><td>Elastic</td><td>Conserved ✓</td><td>Conserved ✓</td><td>Newton's cradle, gas molecules</td></tr>
<tr><td>Inelastic</td><td>Conserved ✓</td><td>Not conserved ✗</td><td>Car crash, clay hitting wall</td></tr>
<tr><td>Perfectly inelastic</td><td>Conserved ✓</td><td>Maximum KE lost</td><td>Objects stick together after collision</td></tr>
</tbody></table></div>

<h2>1D Elastic Collision — Velocity Equations</h2>
<p>For a 1D elastic collision between masses m₁ (velocity u₁) and m₂ (velocity u₂):</p>
<div class="formula-block"><span class="formula-label">Final Velocities — Elastic</span>
v₁ = ((m₁−m₂)u₁ + 2m₂u₂) / (m₁+m₂)<br/>
v₂ = ((m₂−m₁)u₂ + 2m₁u₁) / (m₁+m₂)
</div>
<p>Special case: equal masses (m₁ = m₂) — the velocities are simply exchanged. This explains Newton's cradle.</p>

<h2>Centre of Mass Frame</h2>
<p>The centre of mass (CM) of a system moves at constant velocity if no external forces act. In the CM frame, the total momentum is always zero, simplifying collision analysis. Transforming to and from the CM frame is a powerful technique in particle physics and classical mechanics.</p>

<div class="info-box info-box--fact">
  <div class="info-box-title" style="color:#a078ff">🚀 Rocket Propulsion</div>
  <p style="margin:0">A rocket accelerates by expelling mass at high velocity. By conservation of momentum, as exhaust goes backward, the rocket goes forward. The Tsiolkovsky rocket equation Δv = v<sub>e</sub> ln(m₀/m<sub>f</sub>) gives the velocity change achievable from a given mass ratio.</p>
</div>
"""
    },
    {
        "slug": "circular-motion",
        "num": "05", "icon": "🔄",
        "title": "Circular Motion & Rotation",
        "subtitle": "Angular Kinematics and Centripetal Dynamics",
        "tags": ["Rotation","Circular Motion","Angular Velocity"],
        "sim": False,
        "keywords": "circular motion, centripetal acceleration, angular velocity, angular acceleration, uniform circular motion, centripetal force, radians, period",
        "description": "Complete treatment of circular motion — angular quantities, centripetal acceleration and force, uniform and non-uniform circular motion, and applications including banked curves and satellites.",
        "img": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=1200&q=75&auto=format",
        "img_alt": "Circular motion and rotational mechanics",
        "content": """
<p>Circular motion is one of the most common and important types of motion in nature. Planets orbit the Sun, electrons (in classical models) orbit nuclei, wheels rotate, and the Earth itself spins. Understanding circular motion requires a shift from linear to angular quantities — a conceptual step that opens up the full richness of rotational mechanics.</p>

<h2>Angular Quantities</h2>
<div class="formula-block"><span class="formula-label">Key Angular Quantities</span>
θ = arc length / radius = s/r (radians)<br/>
ω = dθ/dt (angular velocity, rad/s)<br/>
α = dω/dt (angular acceleration, rad/s²)
</div>
<div class="table-wrap"><table>
<thead><tr><th>Linear</th><th>Angular</th><th>Relationship</th></tr></thead>
<tbody>
<tr><td>s (displacement)</td><td>θ (angle)</td><td>s = rθ</td></tr>
<tr><td>v (velocity)</td><td>ω (angular velocity)</td><td>v = rω</td></tr>
<tr><td>a (acceleration)</td><td>α (angular acceleration)</td><td>a<sub>t</sub> = rα</td></tr>
</tbody></table></div>

<h2>Centripetal Acceleration</h2>
<p>For uniform circular motion (constant speed), the direction of velocity continuously changes, meaning there is an acceleration even though the speed is constant. This centripetal acceleration always points toward the centre:</p>
<div class="formula-block"><span class="formula-label">Centripetal Acceleration</span>a<sub>c</sub> = v²/r = ω²r</div>
<p>By Newton's second law, a net centripetal force must provide this acceleration:</p>
<div class="formula-block"><span class="formula-label">Centripetal Force</span>F<sub>c</sub> = mv²/r = mω²r</div>
<p>The centripetal force is not a new type of force — it is whatever force (gravity, tension, friction, normal force) provides the inward acceleration. For the Moon in orbit, it is gravity. For a car turning a corner, it is friction. For a ball on a string, it is tension.</p>

<h2>Banked Curves</h2>
<p>A road banked at angle θ allows vehicles to turn without relying on friction. The banking provides the horizontal component of the normal force as centripetal force. The ideal banking angle for speed v and radius r is:</p>
<div class="formula-block"><span class="formula-label">Banking Angle</span>tan θ = v²/(rg)</div>

<h2>Vertical Circles</h2>
<p>For an object moving in a vertical circle (e.g., a roller coaster loop), the minimum speed at the top is found by setting the centripetal force equal to gravity alone (N = 0 at minimum):</p>
<div class="formula-block"><span class="formula-label">Minimum Speed at Top of Loop</span>v<sub>min</sub> = √(rg)</div>

<h2>Period and Frequency</h2>
<div class="formula-block"><span class="formula-label">Period and Frequency Relations</span>
T = 2π/ω = 2πr/v<br/>
f = 1/T = ω/(2π)
</div>
<p>For circular orbits, combining Newton's law of gravitation with the centripetal force equation gives Kepler's third law as a direct consequence — a beautiful connection between circular motion and gravity.</p>

<div class="info-box info-box--note">
<div class="info-box-title" style="color:var(--accent-plasma)">💡 Non-Uniform Circular Motion</div>
<p style="margin:0">When speed changes along a circular path, there is a tangential acceleration a<sub>t</sub> = rα in addition to the centripetal acceleration. The total acceleration is a⃗ = a⃗<sub>c</sub> + a⃗<sub>t</sub>, with magnitude a = √(a<sub>c</sub>² + a<sub>t</sub>²).</p>
</div>
"""
    },
    {
        "slug": "gravitational-force",
        "num": "06", "icon": "🌐",
        "title": "Gravitational Force & Fields",
        "subtitle": "Newton's Law of Universal Gravitation",
        "tags": ["Gravity","Fields","Potential"],
        "sim": False,
        "keywords": "gravitational force, Newton's law of gravitation, gravitational field, gravitational potential, escape velocity, universal gravitation, G constant",
        "description": "Newton's law of universal gravitation — gravitational fields, potential, escape velocity, tidal forces, and the connection to general relativity.",
        "img": "https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?w=1200&q=75&auto=format",
        "img_alt": "Earth and gravitational field in space",
        "content": """
<p>Gravity is the weakest of the four fundamental forces, yet it dominates at large scales because it is always attractive and has infinite range. Newton's law of universal gravitation, formulated in 1687, was the first unified theory in physics — showing that the same force that makes apples fall also governs the motion of the Moon and planets.</p>

<h2>Newton's Law of Universal Gravitation</h2>
<div class="formula-block"><span class="formula-label">Gravitational Force</span>F = G·m₁·m₂ / r²</div>
<p>Where G = 6.674 × 10⁻¹¹ N·m²/kg² is the universal gravitational constant, m₁ and m₂ are the masses, and r is the separation between their centres. The force is always attractive, along the line connecting the masses.</p>

<h2>Gravitational Field</h2>
<p>The gravitational field g⃗ at a point in space is defined as the gravitational force per unit mass that a test particle would experience:</p>
<div class="formula-block"><span class="formula-label">Gravitational Field</span>g⃗ = F⃗/m = −GM/r² r̂</div>
<p>Near Earth's surface, g ≈ 9.81 m/s² downward. At distance r from Earth's centre (M<sub>E</sub> = 5.972 × 10²⁴ kg):</p>
<div class="formula-block">g(r) = GM<sub>E</sub>/r²</div>
<p>At r = 2R<sub>E</sub> (double Earth's radius), g decreases by factor 4 — the inverse-square law.</p>

<h2>Gravitational Potential Energy</h2>
<div class="formula-block"><span class="formula-label">Gravitational PE (general)</span>U = −GMm/r</div>
<p>The negative sign reflects that gravity is attractive — you must do positive work to pull masses apart, increasing (making less negative) the potential energy. U → 0 as r → ∞ (reference level at infinity).</p>

<h2>Escape Velocity</h2>
<p>The minimum speed needed to escape a body's gravity (ignoring atmosphere) is found by setting KE = |PE|:</p>
<div class="formula-block"><span class="formula-label">Escape Velocity</span>v<sub>esc</sub> = √(2GM/R)</div>
<p>For Earth: v<sub>esc</sub> = √(2 × 6.67×10⁻¹¹ × 5.97×10²⁴ / 6.37×10⁶) ≈ <strong>11.2 km/s</strong>. For the Moon: ~2.4 km/s. For a black hole: v<sub>esc</sub> = c (speed of light at the Schwarzschild radius).</p>

<h2>Tidal Forces</h2>
<p>Tidal forces arise because gravity varies with distance — the near side of Earth is pulled more strongly toward the Moon than the far side. This differential gravity stretches bodies, causing ocean tides and the tidal locking of the Moon (why we always see the same face of the Moon).</p>

<div class="info-box info-box--fact">
<div class="info-box-title" style="color:#a078ff">🔭 Beyond Newton</div>
<p style="margin:0">Newton's gravity works extraordinarily well for everyday scales. However, it is superseded by Einstein's General Relativity for strong gravitational fields, high velocities, or high precision requirements. GR predicts gravitational waves, black holes, and the bending of light — none of which appear in Newtonian gravity.</p>
</div>
"""
    },
    {
        "slug": "rotational-dynamics",
        "num": "08", "icon": "🌀",
        "title": "Rotational Dynamics",
        "subtitle": "Torque, Angular Momentum, and Moment of Inertia",
        "tags": ["Torque","Angular Momentum","Moment of Inertia"],
        "sim": False,
        "keywords": "rotational dynamics, torque, angular momentum, moment of inertia, rotational kinetic energy, rolling motion, conservation of angular momentum",
        "description": "Comprehensive treatment of rotational dynamics — torque, moment of inertia, angular momentum, rotational kinetic energy, and rolling motion.",
        "img": "https://images.unsplash.com/photo-1635070041078-e363dbe005cb?w=1200&q=75&auto=format",
        "img_alt": "Rotational mechanics and angular momentum",
        "content": """
<p>Rotational dynamics is the angular counterpart of Newton's laws for linear motion. Every linear quantity and equation has a rotational analogue, and the parallels run deep. Mastering rotational dynamics is essential for understanding everything from spinning tops and gyroscopes to the moment of inertia in engineering design.</p>

<h2>Torque</h2>
<p>Torque (τ) is the rotational analogue of force — the tendency of a force to cause rotation about an axis:</p>
<div class="formula-block"><span class="formula-label">Torque</span>τ⃗ = r⃗ × F⃗ &nbsp;&nbsp;|&nbsp;&nbsp; |τ| = rF sin θ</div>
<p>Where r is the lever arm (perpendicular distance from the axis to the line of action of the force). Torque is maximised when force is perpendicular to the lever arm (θ = 90°). The SI unit of torque is the newton-metre (N·m).</p>

<h2>Moment of Inertia</h2>
<p>The moment of inertia I is the rotational analogue of mass — it measures resistance to angular acceleration:</p>
<div class="formula-block"><span class="formula-label">Moment of Inertia (discrete)</span>I = Σm<sub>i</sub>r<sub>i</sub>²</div>
<div class="formula-block"><span class="formula-label">Moment of Inertia (continuous)</span>I = ∫r² dm</div>
<div class="table-wrap"><table>
<thead><tr><th>Object</th><th>Axis</th><th>I</th></tr></thead>
<tbody>
<tr><td>Solid sphere</td><td>Through centre</td><td>2/5 MR²</td></tr>
<tr><td>Hollow sphere</td><td>Through centre</td><td>2/3 MR²</td></tr>
<tr><td>Solid cylinder/disk</td><td>Central axis</td><td>½MR²</td></tr>
<tr><td>Thin ring</td><td>Central axis</td><td>MR²</td></tr>
<tr><td>Thin rod</td><td>Through centre</td><td>1/12 ML²</td></tr>
</tbody></table></div>

<h2>Newton's Second Law for Rotation</h2>
<div class="formula-block"><span class="formula-label">Rotational Second Law</span>τ<sub>net</sub> = I·α</div>

<h2>Rotational Kinetic Energy</h2>
<div class="formula-block"><span class="formula-label">Rotational KE</span>KE<sub>rot</sub> = ½Iω²</div>
<p>A rolling object (without slipping) has both translational and rotational KE: KE<sub>total</sub> = ½mv² + ½Iω²</p>

<h2>Angular Momentum and Its Conservation</h2>
<div class="formula-block"><span class="formula-label">Angular Momentum</span>L⃗ = I·ω⃗ &nbsp;&nbsp;|&nbsp;&nbsp; L⃗ = r⃗ × p⃗</div>
<p>Angular momentum is conserved when no net external torque acts. This is why a spinning ice skater spins faster when pulling arms inward (I decreases, ω increases to keep L constant).</p>

<div class="info-box info-box--tip">
<div class="info-box-title" style="color:var(--accent-green)">🌍 Earth's Angular Momentum</div>
<p style="margin:0">Earth's rotation is slowly decelerating due to tidal friction with the Moon. As Earth's angular momentum decreases, the Moon's orbital angular momentum increases — the Moon gradually moves farther away at about 3.8 cm/year.</p>
</div>
"""
    },
    {
        "slug": "work-and-power",
        "num": "09", "icon": "🔧",
        "title": "Work, Power & Machines",
        "subtitle": "Energy Transfer, Mechanical Advantage, and Efficiency",
        "tags": ["Work","Power","Energy","Machines"],
        "sim": False,
        "keywords": "work in physics, power, mechanical advantage, efficiency, simple machines, lever, pulley, variable force, joule, watt",
        "description": "In-depth treatment of work, power, and mechanical advantage — from the dot product definition to variable forces, and the physics of simple machines.",
        "img": "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=1200&q=75&auto=format",
        "img_alt": "Mechanical engineering work and power concepts",
        "content": """
<p>Work and power are the bridge between force and energy in classical mechanics. While force describes how hard you push, and energy describes what you have stored, work describes the process of energy transfer. Power tells you how fast that transfer happens. Together, they form the quantitative basis for all mechanical engineering.</p>

<h2>Work — Precise Definition</h2>
<div class="formula-block"><span class="formula-label">Work (constant force)</span>W = F⃗ · d⃗ = Fd cos θ</div>
<div class="formula-block"><span class="formula-label">Work (variable force)</span>W = ∫F⃗ · dr⃗</div>
<p>Work is a scalar (not a vector). It can be positive (force aids motion), negative (force opposes motion), or zero (force perpendicular to motion). The SI unit is the Joule: 1 J = 1 N·m = 1 kg·m²/s².</p>

<h2>Work Done Against Gravity</h2>
<p>Lifting a mass m through height h against gravity: W = mgh. This work is stored as gravitational potential energy. Note that this is path-independent — carrying the mass up a ramp or straight up requires the same work against gravity.</p>

<h2>Power</h2>
<div class="formula-block"><span class="formula-label">Power</span>P = dW/dt = F⃗ · v⃗</div>
<p>Power is the rate of energy transfer. The SI unit is the Watt: 1 W = 1 J/s. Common values:</p>
<ul style="margin:0 0 16px 20px;color:var(--text-secondary)">
  <li>Human climbing stairs: ~300–500 W</li>
  <li>Car engine: ~75–300 kW (100–400 hp)</li>
  <li>Commercial jet engine: ~30 MW</li>
  <li>Sun's total power output: ~3.8 × 10²⁶ W</li>
</ul>

<h2>Simple Machines and Mechanical Advantage</h2>
<p>A simple machine is a device that changes the magnitude or direction of a force. The mechanical advantage (MA) is the ratio of output force to input force:</p>
<div class="formula-block"><span class="formula-label">Mechanical Advantage</span>MA = F<sub>out</sub> / F<sub>in</sub></div>
<p>Examples: lever (MA = d<sub>in</sub>/d<sub>out</sub>), pulley system (MA = number of rope segments supporting load), inclined plane (MA = L/h). Crucially, machines multiply force but not energy — greater output force comes with proportionally smaller output displacement.</p>

<h2>Efficiency</h2>
<div class="formula-block"><span class="formula-label">Efficiency</span>η = W<sub>out</sub> / W<sub>in</sub> × 100%</div>
<p>No real machine is 100% efficient; friction and other dissipative effects always reduce efficiency. The actual mechanical advantage (AMA) is always less than the ideal mechanical advantage (IMA) due to friction losses.</p>

<div class="info-box info-box--note">
<div class="info-box-title" style="color:var(--accent-plasma)">💡 Energy vs Work</div>
<p style="margin:0">Work is a process — it describes energy being transferred. Energy is a state function — it describes what a system has. Work changes a system's energy. The work-energy theorem (W<sub>net</sub> = ΔKE) is the precise mathematical statement of this relationship.</p>
</div>
"""
    },
    {
        "slug": "friction-and-drag",
        "num": "10", "icon": "🛞",
        "title": "Friction & Air Drag",
        "subtitle": "Dissipative Forces and Terminal Velocity",
        "tags": ["Friction","Drag","Viscosity"],
        "sim": False,
        "keywords": "friction, static friction, kinetic friction, coefficient of friction, air drag, terminal velocity, viscous drag, Stokes law, drag coefficient",
        "description": "Comprehensive study of friction and fluid drag — static and kinetic friction coefficients, drag forces, terminal velocity, and viscous flow.",
        "img": "https://images.unsplash.com/photo-1571988840298-3b5301d5109b?w=1200&q=75&auto=format",
        "img_alt": "Friction and tire contact mechanics",
        "content": """
<p>Friction and drag are dissipative forces — they convert mechanical energy into thermal energy. While often treated as nuisances in introductory physics, these forces are fundamental to everyday life: without friction we could not walk, drive, or grip objects; without drag, parachutes and aerodynamics would not exist. Understanding them quantitatively is essential for engineering design.</p>

<h2>Static Friction</h2>
<p>Static friction prevents relative motion between surfaces in contact. It can take any value up to a maximum:</p>
<div class="formula-block"><span class="formula-label">Maximum Static Friction</span>f<sub>s,max</sub> = μ<sub>s</sub> · N</div>
<p>Where μ<sub>s</sub> is the coefficient of static friction and N is the normal force. Typical values: rubber on dry concrete μ<sub>s</sub> ≈ 0.6–0.8, steel on steel μ<sub>s</sub> ≈ 0.15, ice on ice μ<sub>s</sub> ≈ 0.03.</p>

<h2>Kinetic Friction</h2>
<p>Once sliding begins, kinetic (sliding) friction takes over, which is generally less than maximum static friction:</p>
<div class="formula-block"><span class="formula-label">Kinetic Friction</span>f<sub>k</sub> = μ<sub>k</sub> · N</div>
<p>Kinetic friction is approximately constant regardless of speed (at ordinary speeds). This is why anti-lock brakes are more effective — braking just below the slip threshold (using static friction) gives more stopping force than full skidding (kinetic friction).</p>

<h2>Air Drag</h2>
<p>At high speeds (turbulent flow), air drag is approximately proportional to v²:</p>
<div class="formula-block"><span class="formula-label">Drag Force (high speed)</span>F<sub>D</sub> = ½ρ C<sub>D</sub> A v²</div>
<p>Where ρ is air density (≈1.225 kg/m³ at sea level), C<sub>D</sub> is the drag coefficient (sphere ≈0.47, streamlined car ≈0.25–0.35), and A is the cross-sectional area.</p>
<p>At low speeds (laminar flow — small objects, viscous fluids), Stokes' law applies: F<sub>D</sub> = 6πηrv</p>

<h2>Terminal Velocity</h2>
<p>When drag equals gravity, acceleration stops and the object reaches terminal velocity:</p>
<div class="formula-block"><span class="formula-label">Terminal Velocity</span>v<sub>t</sub> = √(2mg / ρC<sub>D</sub>A)</div>
<p>For a skydiver (m ≈ 80 kg, A ≈ 0.7 m², C<sub>D</sub> ≈ 1.0): v<sub>t</sub> ≈ 55 m/s (200 km/h) in spread position, ~90 m/s (320 km/h) head-down.</p>

<div class="info-box info-box--fact">
<div class="info-box-title" style="color:#a078ff">🏎 Aerodynamics in Motorsport</div>
<p style="margin:0">Formula 1 cars generate enormous downforce (equivalent to 3× their own weight at high speed) using inverted wings. This increases the normal force on tyres, allowing much higher cornering speeds. The drag coefficient of an F1 car is deliberately kept high to enable effective braking.</p>
</div>
"""
    },
    {
        "slug": "keplers-laws",
        "num": "11", "icon": "🪐",
        "title": "Kepler's Laws & Orbital Mechanics",
        "subtitle": "Planetary Motion and the vis-viva Equation",
        "tags": ["Orbits","Kepler","Planetary Motion"],
        "sim": False,
        "keywords": "Kepler's laws, orbital mechanics, elliptical orbits, vis-viva equation, orbital period, aphelion, perihelion, orbital velocity, satellite orbit",
        "description": "Kepler's three laws of planetary motion, orbital mechanics, elliptical orbits, vis-viva equation, and satellite orbital calculations.",
        "img": "https://images.unsplash.com/photo-1502134249126-9f3755a50d78?w=1200&q=75&auto=format",
        "img_alt": "Solar system orbital mechanics from space",
        "content": """
<p>Johannes Kepler's three laws of planetary motion, published between 1609 and 1619, were the first precise mathematical description of planetary behaviour. Newton later showed that all three laws follow as necessary consequences of his law of universal gravitation — a stunning unification that validated both Kepler's empirical observations and Newton's theoretical framework.</p>

<h2>Kepler's First Law — Law of Ellipses</h2>
<p><strong>Each planet moves in an ellipse with the Sun at one focus.</strong></p>
<p>An ellipse is characterized by its semi-major axis a and eccentricity e (0 ≤ e < 1). The perihelion (closest approach) is r<sub>p</sub> = a(1−e) and aphelion (farthest point) is r<sub>a</sub> = a(1+e). Earth's eccentricity is e ≈ 0.017, nearly circular.</p>

<h2>Kepler's Second Law — Law of Equal Areas</h2>
<p><strong>A line from the Sun to the planet sweeps equal areas in equal times.</strong></p>
<p>This is a direct consequence of conservation of angular momentum. When a planet is closer to the Sun, it moves faster; when farther, slower. L = mvr = constant, so v ∝ 1/r at perihelion/aphelion.</p>

<h2>Kepler's Third Law — Law of Periods</h2>
<div class="formula-block"><span class="formula-label">Kepler's Third Law</span>T² ∝ a³ &nbsp;&nbsp;⟹&nbsp;&nbsp; T² = (4π²/GM) a³</div>
<p>The square of the orbital period is proportional to the cube of the semi-major axis. Using Newton's gravity, we can derive the proportionality constant exactly. This law allows us to calculate the mass of any body with orbiting companions — including exoplanet host stars.</p>

<h2>Vis-Viva Equation</h2>
<p>The vis-viva equation gives the orbital speed at any point in an elliptical orbit:</p>
<div class="formula-block"><span class="formula-label">Vis-Viva Equation</span>v² = GM(2/r − 1/a)</div>
<p>At perihelion (r = a(1−e)): maximum speed. At aphelion (r = a(1+e)): minimum speed. For a circular orbit (r = a): v = √(GM/r).</p>

<h2>Orbital Energy</h2>
<div class="formula-block"><span class="formula-label">Orbital Mechanical Energy</span>E = −GMm/(2a)</div>
<p>The total mechanical energy depends only on the semi-major axis, not the eccentricity. Circular and highly elliptical orbits with the same a have the same energy. To move to a higher orbit, you add energy (do positive work); to deorbit, you remove energy.</p>

<div class="info-box info-box--tip">
<div class="info-box-title" style="color:var(--accent-green)">🛰 Geosynchronous Orbit</div>
<p style="margin:0">A satellite in geosynchronous orbit has T = 24 hours. Using Kepler's third law: a = (GM<sub>E</sub>T²/4π²)<sup>1/3</sup> ≈ 42,164 km from Earth's centre (≈35,786 km altitude). At this altitude, the satellite remains stationary above a fixed point on Earth — the basis of GPS and communication satellites.</p>
</div>
"""
    },
    {
        "slug": "waves-and-oscillations",
        "num": "12", "icon": "🌊",
        "title": "Waves & Oscillations",
        "subtitle": "Wave Mechanics, Superposition, and Standing Waves",
        "tags": ["Waves","Standing Waves","Resonance"],
        "sim": False,
        "keywords": "waves, oscillations, wave equation, standing waves, superposition, resonance, wavelength, frequency, wave speed, transverse waves, longitudinal waves",
        "description": "Full treatment of wave physics — the wave equation, types of waves, superposition principle, standing waves, resonance, and wave energy.",
        "img": "https://images.unsplash.com/photo-1505118380757-91f5f5632de0?w=1200&q=75&auto=format",
        "img_alt": "Ocean waves demonstrating wave mechanics",
        "content": """
<p>Waves are one of the most pervasive phenomena in physics. From the ripples on water to electromagnetic radiation, from sound to quantum mechanical probability waves, the mathematics of wave motion appears across every domain of physics. A deep understanding of classical waves is the foundation for understanding optics, acoustics, and even quantum mechanics.</p>

<h2>What is a Wave?</h2>
<p>A wave is a disturbance that travels through space transferring energy without transferring matter. Waves are characterised by wavelength λ, frequency f, and wave speed v:</p>
<div class="formula-block"><span class="formula-label">Fundamental Wave Relation</span>v = fλ = λ/T</div>

<h2>The Wave Equation</h2>
<div class="formula-block"><span class="formula-label">1D Wave Equation</span>∂²y/∂t² = v² ∂²y/∂x²</div>
<p>Solutions are of the form y(x,t) = A sin(kx − ωt + φ), where k = 2π/λ is the wave number, ω = 2πf is the angular frequency, and v = ω/k.</p>

<h2>Transverse vs Longitudinal Waves</h2>
<p><strong>Transverse waves:</strong> Oscillation perpendicular to propagation direction (light, waves on a string). Can be polarized.</p>
<p><strong>Longitudinal waves:</strong> Oscillation parallel to propagation direction (sound, pressure waves). Cannot be polarized. Sound travels as compression-rarefaction cycles through the medium.</p>

<h2>Superposition Principle</h2>
<p>When two or more waves occupy the same region, the resultant displacement is the algebraic sum of the individual displacements. This leads to constructive interference (crest + crest) and destructive interference (crest + trough).</p>

<h2>Standing Waves</h2>
<p>Two waves of equal amplitude and frequency travelling in opposite directions superpose to form a standing wave:</p>
<div class="formula-block"><span class="formula-label">Standing Wave</span>y = 2A sin(kx) cos(ωt)</div>
<p>Nodes (zero amplitude) occur at kx = nπ; antinodes (maximum amplitude) at kx = (n+½)π. For a string fixed at both ends of length L, only certain wavelengths are allowed:</p>
<div class="formula-block"><span class="formula-label">Resonant Wavelengths (fixed-fixed string)</span>λ<sub>n</sub> = 2L/n &nbsp;&nbsp;→&nbsp;&nbsp; f<sub>n</sub> = nv/(2L), n = 1, 2, 3,...</div>

<h2>Wave Energy and Intensity</h2>
<div class="formula-block"><span class="formula-label">Wave Intensity</span>I = P/A = ½ρω²A²v</div>
<p>Intensity is proportional to the square of the amplitude. For a point source, intensity falls as 1/r² (inverse square law). The decibel scale for sound: β = 10 log₁₀(I/I₀), where I₀ = 10⁻¹² W/m².</p>

<div class="info-box info-box--warn">
<div class="info-box-title" style="color:var(--accent-solar)">⚠ Resonance and Structural Engineering</div>
<p style="margin:0">Resonance — when a system is driven at its natural frequency — causes dramatic amplitude amplification. The Tacoma Narrows Bridge (1940) collapsed due to aeroelastic resonance driven by wind. Modern bridge design explicitly avoids resonance conditions through careful frequency analysis.</p>
</div>
"""
    },
    {
        "slug": "centre-of-mass",
        "num": "13", "icon": "⊕",
        "title": "Centre of Mass & Systems of Particles",
        "subtitle": "From Distributed Bodies to System Dynamics",
        "tags": ["Centre of Mass","Systems","CM Frame"],
        "sim": False,
        "keywords": "centre of mass, systems of particles, CM frame, centre of gravity, extended bodies, mass distribution, two-body problem",
        "description": "Finding and using the centre of mass of discrete and continuous systems — CM motion, the two-body problem, and CM frame transformations.",
        "img": "https://images.unsplash.com/photo-1635070041078-e363dbe005cb?w=1200&q=75&auto=format",
        "img_alt": "Balance and centre of mass concept",
        "content": """
<p>The centre of mass (CM) is the unique point at which a body's mass can be considered concentrated for the purposes of translational dynamics. For any system of particles or any extended body, Newton's laws apply to the motion of the CM as if all external forces acted on a single particle of the system's total mass located there.</p>

<h2>Locating the Centre of Mass</h2>
<div class="formula-block"><span class="formula-label">CM of Discrete System</span>r⃗<sub>CM</sub> = (Σm<sub>i</sub>r⃗<sub>i</sub>) / M</div>
<div class="formula-block"><span class="formula-label">CM of Continuous Body</span>r⃗<sub>CM</sub> = (∫r⃗ dm) / M</div>
<p>For a uniform body, the CM coincides with the geometric centroid. For a uniform rod: CM at midpoint. For a uniform triangle: CM at the intersection of medians (one-third from each side). For a uniform semicircle of radius R: CM at 4R/3π from the straight edge.</p>

<h2>CM Motion Theorem</h2>
<div class="formula-block"><span class="formula-label">Newton's Second Law for the CM</span>F⃗<sub>ext</sub> = M·a⃗<sub>CM</sub></div>
<p>Only external forces affect the CM motion. Internal forces (forces between parts of the system) cancel in pairs (Newton's third law). This is why a rocket can accelerate in empty space — the exhaust gas is part of the system until expelled.</p>

<h2>The Two-Body Problem</h2>
<p>For two gravitationally interacting bodies, the CM moves at constant velocity (or stays at rest). In the CM frame, the two-body problem reduces to an effective one-body problem with reduced mass μ = m₁m₂/(m₁+m₂). Both bodies orbit the common CM; the more massive body has the smaller orbit.</p>

<h2>Worked Example: Exploding Projectile</h2>
<p>A shell fired as a projectile explodes at the top of its trajectory into two fragments. Since gravity is the only external force, the CM of the two fragments continues on the original parabolic trajectory — even though the fragments fly in different directions. This beautifully illustrates the CM theorem.</p>

<div class="info-box info-box--note">
<div class="info-box-title" style="color:var(--accent-plasma)">💡 Centre of Mass vs Centre of Gravity</div>
<p style="margin:0">The centre of gravity (where effective gravitational force acts) coincides with the CM only when the gravitational field is uniform. In a non-uniform field (e.g., on a very large body or near a black hole), they differ — the distinction is important in tidal force analysis.</p>
</div>
"""
    },
    {
        "slug": "statics-and-equilibrium",
        "num": "14", "icon": "⚖",
        "title": "Statics & Equilibrium",
        "subtitle": "Conditions for Static Stability",
        "tags": ["Statics","Equilibrium","Torque"],
        "sim": False,
        "keywords": "statics, static equilibrium, translational equilibrium, rotational equilibrium, stability, torque balance, trusses, beams, stress analysis",
        "description": "Statics and equilibrium conditions — translational and rotational equilibrium, free body diagrams, moment balance, stability, and structural analysis.",
        "img": "https://images.unsplash.com/photo-1545486332-9e0999c535b2?w=1200&q=75&auto=format",
        "img_alt": "Architecture and structural equilibrium",
        "content": """
<p>Statics is the branch of mechanics dealing with bodies in equilibrium — at rest or moving at constant velocity. Equilibrium analysis is the foundation of structural engineering: every bridge, building, and machine relies on components that satisfy the conditions of static equilibrium.</p>

<h2>Conditions for Static Equilibrium</h2>
<p>A body is in static equilibrium if and only if both of the following conditions hold:</p>
<div class="formula-block"><span class="formula-label">Translational Equilibrium</span>ΣF⃗ = 0 &nbsp;&nbsp;(sum of all forces is zero)</div>
<div class="formula-block"><span class="formula-label">Rotational Equilibrium</span>Στ⃗ = 0 &nbsp;&nbsp;(sum of all torques about any axis is zero)</div>

<h2>Solving Statics Problems</h2>
<ol style="margin:0 0 16px 20px;color:var(--text-secondary)">
  <li style="margin-bottom:8px">Draw a free body diagram with all forces and their points of application</li>
  <li style="margin-bottom:8px">Choose a convenient axis for torque calculations (often at the location of an unknown force to eliminate it)</li>
  <li style="margin-bottom:8px">Write ΣF<sub>x</sub> = 0, ΣF<sub>y</sub> = 0, Στ = 0</li>
  <li style="margin-bottom:8px">Solve the resulting equations for the unknowns</li>
</ol>

<h2>Centre of Gravity and Tipping</h2>
<p>An object on a surface is stable as long as its centre of gravity's vertical projection falls within the base of support. When the CG moves outside the base, the object tips. This is why a wide, low-slung object (sports car) is more stable than a tall, narrow one (forklift with raised load).</p>

<h2>Stress and Strain in Static Systems</h2>
<p>In real structures, forces must pass through materials as internal stresses. Beams experience bending moments and shear forces. Trusses carry only axial loads (compression or tension). The method of joints and method of sections are standard techniques for analysing truss forces.</p>

<div class="info-box info-box--fact">
<div class="info-box-title" style="color:#a078ff">🏛 Structural Engineering Application</div>
<p style="margin:0">The Eiffel Tower's lattice structure is optimised for statics — every member carries either tension or compression with minimal bending. The triangular lattice is inherently rigid: a triangle cannot deform without changing the length of its sides, unlike a quadrilateral which can be sheared without resistance.</p>
</div>
"""
    },
    {
        "slug": "fluid-mechanics",
        "num": "15", "icon": "💧",
        "title": "Fluid Mechanics",
        "subtitle": "Pressure, Flow, Bernoulli, and Viscosity",
        "tags": ["Fluids","Bernoulli","Viscosity"],
        "sim": False,
        "keywords": "fluid mechanics, Bernoulli's equation, continuity equation, pressure, buoyancy, Archimedes, viscosity, laminar flow, turbulent flow, Reynolds number",
        "description": "Comprehensive fluid mechanics — hydrostatics, Archimedes' principle, continuity equation, Bernoulli's principle, viscosity, and the Reynolds number.",
        "img": "https://images.unsplash.com/photo-1559827291-72ee739d0d9a?w=1200&q=75&auto=format",
        "img_alt": "Fluid flow and water dynamics in physics",
        "content": """
<p>Fluid mechanics describes the behaviour of liquids and gases at rest and in motion. It underpins aeronautical engineering (how wings generate lift), civil engineering (water supply and hydraulics), meteorology (atmospheric dynamics), and medicine (blood flow through vessels). The governing equations — Bernoulli's principle and the Navier-Stokes equations — are among the most important in all of applied physics.</p>

<h2>Hydrostatics — Pressure in Fluids</h2>
<div class="formula-block"><span class="formula-label">Fluid Pressure at Depth h</span>P = P₀ + ρgh</div>
<p>Pressure in a static fluid increases linearly with depth. It acts equally in all directions (Pascal's law). This is why submarine hulls must withstand enormous pressures, and why hydraulic systems can amplify forces.</p>

<h2>Archimedes' Principle</h2>
<div class="formula-block"><span class="formula-label">Buoyant Force</span>F<sub>b</sub> = ρ<sub>fluid</sub> · V<sub>displaced</sub> · g</div>
<p>Any object partially or fully submerged in a fluid experiences an upward buoyant force equal to the weight of fluid displaced. An object floats if F<sub>b</sub> ≥ mg, i.e., if its average density ≤ fluid density.</p>

<h2>Continuity Equation</h2>
<div class="formula-block"><span class="formula-label">Continuity (incompressible)</span>A₁v₁ = A₂v₂</div>
<p>For an incompressible fluid in a pipe, the volume flow rate is constant. Where the pipe narrows (A decreases), velocity increases.</p>

<h2>Bernoulli's Equation</h2>
<div class="formula-block"><span class="formula-label">Bernoulli's Principle</span>P + ½ρv² + ρgh = constant</div>
<p>Along a streamline in ideal (inviscid, incompressible) flow, the sum of pressure, kinetic energy density, and potential energy density is constant. Where velocity is high, pressure is low (venturi effect). This explains aerofoil lift: air moves faster over the curved upper surface, creating lower pressure above the wing.</p>

<h2>Viscosity and Real Fluids</h2>
<p>Real fluids have internal friction (viscosity η). Laminar flow: smooth layers, v<sub>max</sub> = R²ΔP/(4ηL) (Poiseuille's law). Turbulent flow occurs above a critical Reynolds number:</p>
<div class="formula-block"><span class="formula-label">Reynolds Number</span>Re = ρvL/η</div>
<p>Re < 2300: laminar; Re > 4000: turbulent. Blood flow in major arteries is typically laminar (Re ≈ 1000), but can become turbulent at stenoses — which is why turbulent flow creates detectable heart murmurs.</p>

<div class="info-box info-box--note">
<div class="info-box-title" style="color:var(--accent-plasma)">✈ Aerofoil and Lift</div>
<p style="margin:0">Wing lift is more complex than the naive Bernoulli story. Both the Bernoulli effect and the deflection of air downward (Newton's third law reaction) contribute to lift. The Kutta-Joukowski theorem unifies these with circulation theory — the complete description requires both pressure and momentum considerations.</p>
</div>
"""
    },
    {
        "slug": "elasticity-and-stress",
        "num": "16", "icon": "🔩",
        "title": "Elasticity & Stress-Strain",
        "subtitle": "Material Response to Forces — from Hooke's Law to Fracture",
        "tags": ["Elasticity","Materials","Hooke's Law"],
        "sim": False,
        "keywords": "elasticity, Hooke's law, Young's modulus, stress, strain, bulk modulus, shear modulus, elastic limit, yield strength, materials science",
        "description": "Elasticity, stress, strain, and material properties — Young's modulus, bulk modulus, shear modulus, elastic limits, and energy stored in elastic deformation.",
        "img": "https://images.unsplash.com/photo-1581092580497-e0d23cbdf1dc?w=1200&q=75&auto=format",
        "img_alt": "Material testing and elasticity in structural mechanics",
        "content": """
<p>Elasticity describes how solid materials deform under applied forces and return to their original shape when the force is removed. It bridges classical mechanics and materials science. Engineers rely on precise knowledge of elastic properties to design structures that withstand loads without permanent deformation or catastrophic failure.</p>

<h2>Stress and Strain</h2>
<div class="formula-block"><span class="formula-label">Stress and Strain</span>
σ = F/A (stress, Pa = N/m²)<br/>
ε = ΔL/L₀ (strain, dimensionless)
</div>
<p>Stress is force per unit area; strain is the fractional change in dimension. Both are intensive properties (independent of the amount of material).</p>

<h2>Hooke's Law and Young's Modulus</h2>
<div class="formula-block"><span class="formula-label">Young's Modulus</span>E = σ/ε = (F/A) / (ΔL/L₀)</div>
<p>Young's modulus E measures stiffness in tension or compression. Typical values: steel ≈ 200 GPa, aluminium ≈ 70 GPa, glass ≈ 70 GPa, rubber ≈ 0.01–0.1 GPa, bone ≈ 20 GPa.</p>

<h2>Bulk and Shear Moduli</h2>
<div class="formula-block"><span class="formula-label">Bulk Modulus (volume stress)</span>B = −P / (ΔV/V)</div>
<div class="formula-block"><span class="formula-label">Shear Modulus (shear stress)</span>G = (F/A) / φ</div>
<p>The bulk modulus B resists compression; the shear modulus G resists deformation by shearing forces. Liquids have B but G = 0 (they cannot resist shear).</p>

<h2>Elastic Potential Energy</h2>
<div class="formula-block"><span class="formula-label">Elastic PE stored in a deformed material</span>U = ½Eε²V = ½(F²/kA)</div>
<p>The energy density (J/m³) = ½Eε² = σ²/(2E). For a spring: U = ½kx² (where k = AE/L).</p>

<h2>Beyond the Elastic Limit</h2>
<p>The stress-strain curve shows: elastic region (Hooke's law holds, recoverable deformation), yield point (permanent deformation begins), plastic region (material flows), ultimate tensile strength, and fracture. Understanding these regions is critical for safety factor calculations in engineering design.</p>

<div class="info-box info-box--warn">
<div class="info-box-title" style="color:var(--accent-solar)">⚠ Metal Fatigue</div>
<p style="margin:0">Repeated cycling between stress values well below the yield strength can cause <strong>fatigue failure</strong> — cracks initiate at stress concentrations and grow with each cycle. The Comet aircraft disasters (1954) were caused by fatigue cracks propagating from square window corners. Modern design uses rounded corners to reduce stress concentration factors.</p>
</div>
"""
    },
    {
        "slug": "kinematics",
        "num": "17", "icon": "📐",
        "title": "Kinematics in 1D & 2D",
        "subtitle": "Motion Without Forces — Equations of Motion",
        "tags": ["Kinematics","Vectors","Equations of Motion"],
        "sim": False,
        "keywords": "kinematics, equations of motion, displacement, velocity, acceleration, 1D motion, 2D motion, projectile, SUVAT equations, motion graphs",
        "description": "Complete kinematics — equations of motion, velocity-time graphs, position-time graphs, vector decomposition, and 2D motion analysis.",
        "img": "https://images.unsplash.com/photo-1543286386-713bdd548da4?w=1200&q=75&auto=format",
        "img_alt": "Motion analysis and velocity tracking",
        "content": """
<p>Kinematics is the mathematical description of motion without reference to its causes (forces). It answers the questions: where is the object? How fast is it moving? How is its speed changing? Kinematics provides the language and tools — displacement, velocity, acceleration, and the equations relating them — that are used throughout all of classical mechanics.</p>

<h2>Definitions</h2>
<div class="formula-block"><span class="formula-label">Kinematic Quantities</span>
Displacement: Δx = x<sub>f</sub> − x<sub>i</sub> (vector, m)<br/>
Velocity: v = dx/dt (vector, m/s)<br/>
Acceleration: a = dv/dt = d²x/dt² (vector, m/s²)
</div>
<p>Distinguish carefully: <em>distance</em> (scalar, path length) vs <em>displacement</em> (vector, net change); <em>speed</em> (scalar, |v|) vs <em>velocity</em> (vector).</p>

<h2>SUVAT Equations (Constant Acceleration)</h2>
<div class="table-wrap"><table>
<thead><tr><th>Equation</th><th>Missing Variable</th></tr></thead>
<tbody>
<tr><td>v = u + at</td><td>x</td></tr>
<tr><td>x = ut + ½at²</td><td>v</td></tr>
<tr><td>v² = u² + 2ax</td><td>t</td></tr>
<tr><td>x = ½(u+v)t</td><td>a</td></tr>
<tr><td>x = vt − ½at²</td><td>u</td></tr>
</tbody></table></div>
<p>Where u = initial velocity, v = final velocity, a = acceleration (constant), x = displacement, t = time. Choose the equation that contains your unknowns and lacks the one you don't have.</p>

<h2>Motion Graphs</h2>
<p><strong>Position-time graph:</strong> gradient = velocity; horizontal line = rest; slope of tangent = instantaneous velocity.</p>
<p><strong>Velocity-time graph:</strong> gradient = acceleration; area under graph = displacement; horizontal line = constant velocity (zero acceleration).</p>
<p><strong>Acceleration-time graph:</strong> area under graph = change in velocity.</p>

<h2>2D Kinematics — Vector Decomposition</h2>
<p>Any 2D motion can be decomposed into independent x and y components. Apply SUVAT equations separately to each component. The classic example is projectile motion where a<sub>x</sub> = 0 and a<sub>y</sub> = −g.</p>
<div class="formula-block"><span class="formula-label">2D Velocity Components</span>
v<sub>x</sub>(t) = v<sub>x0</sub> + a<sub>x</sub>t<br/>
v<sub>y</sub>(t) = v<sub>y0</sub> + a<sub>y</sub>t
</div>

<div class="info-box info-box--note">
<div class="info-box-title" style="color:var(--accent-plasma)">💡 Non-Constant Acceleration</div>
<p style="margin:0">SUVAT equations only apply for constant acceleration. For variable acceleration, integration is required: v(t) = ∫a(t)dt and x(t) = ∫v(t)dt. Many real systems have acceleration that varies with position or time (springs, drag forces), requiring calculus or numerical methods.</p>
</div>
"""
    },
    {
        "slug": "damped-oscillations",
        "num": "18", "icon": "📉",
        "title": "Damped & Forced Oscillations",
        "subtitle": "Resonance, Damping, and the Q-Factor",
        "tags": ["Damping","Resonance","Q-Factor"],
        "sim": False,
        "keywords": "damped oscillations, forced oscillations, resonance, Q factor, underdamped, overdamped, critically damped, driving frequency, amplitude resonance",
        "description": "Damped and forced oscillations — types of damping, driven oscillators, resonance phenomena, the quality factor Q, and mechanical resonance in engineering.",
        "img": "https://images.unsplash.com/photo-1509228627152-72ae9ae6848d?w=1200&q=75&auto=format",
        "img_alt": "Oscillation dampening and vibration mechanics",
        "content": """
<p>Real oscillators always lose energy to their environment — springs have friction, pendulums have air resistance, electrical circuits have resistance. Damping modifies the behaviour of oscillators in profound ways. When we add a periodic driving force, the interplay between driving, damping, and natural frequency produces resonance — one of the most important phenomena in physics and engineering.</p>

<h2>The Damped Oscillator Equation</h2>
<div class="formula-block"><span class="formula-label">Damped SHM</span>m(d²x/dt²) + b(dx/dt) + kx = 0</div>
<p>Where b is the damping coefficient. The solution depends on the discriminant b² − 4mk:</p>

<h2>Three Regimes of Damping</h2>
<div class="table-wrap"><table>
<thead><tr><th>Condition</th><th>Regime</th><th>Behaviour</th></tr></thead>
<tbody>
<tr><td>b² < 4mk</td><td>Underdamped</td><td>Oscillates with exponentially decaying amplitude</td></tr>
<tr><td>b² = 4mk</td><td>Critically damped</td><td>Returns to equilibrium fastest without oscillating</td></tr>
<tr><td>b² > 4mk</td><td>Overdamped</td><td>Returns to equilibrium slowly without oscillating</td></tr>
</tbody></table></div>
<div class="formula-block"><span class="formula-label">Underdamped Solution</span>x(t) = Ae<sup>−γt</sup> cos(ω<sub>d</sub>t + φ) &nbsp;&nbsp;where γ = b/2m, ω<sub>d</sub> = √(ω₀² − γ²)</div>

<h2>Quality Factor Q</h2>
<div class="formula-block"><span class="formula-label">Q-Factor</span>Q = ω₀/2γ = ω₀m/b</div>
<p>Q measures how many oscillation cycles occur before energy decays to 1/e² of its initial value. High Q = lightly damped (many oscillations). Examples: pendulum clock Q ≈ 10⁴, quartz crystal resonator Q ≈ 10⁶, atomic transition (laser) Q ≈ 10¹⁴.</p>

<h2>Forced Oscillations and Resonance</h2>
<p>When a damped oscillator is driven by a periodic force F₀cos(ωt):</p>
<div class="formula-block"><span class="formula-label">Steady-State Amplitude</span>A = (F₀/m) / √((ω₀²−ω²)² + (bω/m)²)</div>
<p>Resonance (maximum amplitude) occurs near ω = ω₀. At exact resonance, amplitude is limited only by damping: A<sub>res</sub> = F₀/(bω₀) = QF₀/(mω₀²). A high-Q oscillator has very sharp, high resonance peaks.</p>

<div class="info-box info-box--warn">
<div class="info-box-title" style="color:var(--accent-solar)">⚠ Resonance Disasters</div>
<p style="margin:0">The Tacoma Narrows Bridge (1940), Millennium Bridge London (2000), and the Angers Bridge (1850) all failed due to resonance. The Millennium Bridge was stiffened after pedestrians found their natural walking pace synchronised with the bridge's sway frequency — a feedback resonance. Modern bridge design includes tuned mass dampers to suppress resonance.</p>
</div>
"""
    },
    {
        "slug": "lagrangian-mechanics",
        "num": "19", "icon": "∫",
        "title": "Lagrangian Mechanics",
        "subtitle": "Variational Principles and Generalised Coordinates",
        "tags": ["Advanced","Lagrangian","Variational"],
        "sim": False,
        "keywords": "Lagrangian mechanics, Euler-Lagrange equation, generalised coordinates, variational principle, principle of least action, constraints, holonomic",
        "description": "Lagrangian mechanics — the principle of least action, generalised coordinates, Euler-Lagrange equations, constraints, and Noether's theorem.",
        "img": "https://images.unsplash.com/photo-1509228468518-180dd4864904?w=1200&q=75&auto=format",
        "img_alt": "Advanced theoretical mechanics equations",
        "content": """
<p>Lagrangian mechanics, developed by Joseph-Louis Lagrange in 1788, reformulates classical mechanics using a single scalar function — the Lagrangian — rather than vector forces. This approach elegantly handles constraints, greatly simplifies complex problems, and reveals the deep connection between symmetries and conservation laws through Noether's theorem. It also forms the conceptual bridge to quantum mechanics and quantum field theory.</p>

<h2>The Lagrangian</h2>
<div class="formula-block"><span class="formula-label">The Lagrangian</span>L = T − V &nbsp;&nbsp;(kinetic energy minus potential energy)</div>
<p>Unlike the Hamiltonian (T + V = total energy), the Lagrangian is the difference of KE and PE. It encodes all the dynamics of a system.</p>

<h2>Generalised Coordinates</h2>
<p>Instead of Cartesian coordinates, Lagrangian mechanics uses generalised coordinates q<sub>i</sub> — any set of independent parameters that completely describe the system's configuration. For a pendulum, one generalised coordinate (the angle θ) suffices. For an N-particle system in 3D with k constraints, 3N−k generalised coordinates are needed.</p>

<h2>Euler-Lagrange Equations</h2>
<div class="formula-block"><span class="formula-label">Euler-Lagrange Equation</span>d/dt (∂L/∂q̇<sub>i</sub>) − ∂L/∂q<sub>i</sub> = 0</div>
<p>One equation per generalised coordinate. These are second-order differential equations of motion equivalent to Newton's laws but often far simpler to derive for complex systems.</p>

<h2>The Principle of Least Action</h2>
<p>The equations of motion follow from a variational principle: the actual path taken by a system between two configurations is the one that makes the action S stationary:</p>
<div class="formula-block"><span class="formula-label">Action</span>S = ∫L dt &nbsp;&nbsp;→&nbsp;&nbsp; δS = 0</div>
<p>This variational principle is arguably the most profound formulation of classical mechanics — and it extends directly to quantum mechanics (Feynman's path integral) and field theory.</p>

<h2>Example: Double Pendulum</h2>
<p>The double pendulum is notoriously complex using Newton's laws (coupled differential equations with constraint forces). With Lagrangian mechanics, write T and V in terms of angles θ₁, θ₂ and their time derivatives, form L, and apply Euler-Lagrange. The constraint forces never appear — a major simplification.</p>

<h2>Noether's Theorem</h2>
<p>Every continuous symmetry of the Lagrangian corresponds to a conserved quantity. Time translation symmetry → conservation of energy. Spatial translation symmetry → conservation of momentum. Rotational symmetry → conservation of angular momentum. This is one of the deepest and most beautiful results in all of physics.</p>

<div class="info-box info-box--fact">
<div class="info-box-title" style="color:#a078ff">🔭 From Classical to Quantum</div>
<p style="margin:0">Feynman's formulation of quantum mechanics uses the action S directly: a quantum particle takes all possible paths simultaneously, each weighted by e<sup>iS/ℏ</sup>. In the limit ℏ → 0, the phases cancel everywhere except near the path of stationary action — recovering classical mechanics. The Lagrangian is thus the conceptual bridge between classical and quantum physics.</p>
</div>
"""
    },
    {
        "slug": "hamiltonian-mechanics",
        "num": "20", "icon": "ℋ",
        "title": "Hamiltonian Mechanics",
        "subtitle": "Phase Space, Canonical Equations, and Classical-Quantum Bridge",
        "tags": ["Advanced","Hamiltonian","Phase Space"],
        "sim": False,
        "keywords": "Hamiltonian mechanics, Hamilton's equations, phase space, canonical coordinates, Poisson brackets, canonical transformation, classical mechanics",
        "description": "Hamiltonian mechanics — Hamilton's equations of motion, phase space trajectories, Poisson brackets, canonical transformations, and the connection to quantum mechanics.",
        "img": "https://images.unsplash.com/photo-1509228468518-180dd4864904?w=1200&q=75&auto=format",
        "img_alt": "Phase space and Hamiltonian dynamics",
        "content": """
<p>Hamiltonian mechanics, formulated by William Rowan Hamilton in the 1830s, reformulates classical mechanics in terms of coordinates and momenta — the 'phase space' description. It is equivalent to both Newtonian and Lagrangian mechanics but provides a framework that is geometrically elegant, directly related to quantum mechanics, and essential for statistical mechanics and chaos theory.</p>

<h2>The Hamiltonian</h2>
<div class="formula-block"><span class="formula-label">The Hamiltonian</span>H = T + V = Σp<sub>i</sub>q̇<sub>i</sub> − L</div>
<p>Where p<sub>i</sub> = ∂L/∂q̇<sub>i</sub> are the generalised (canonical) momenta. For most systems (time-independent potentials), H equals the total mechanical energy.</p>

<h2>Hamilton's Equations of Motion</h2>
<div class="formula-block"><span class="formula-label">Hamilton's Equations</span>
dq<sub>i</sub>/dt = ∂H/∂p<sub>i</sub><br/>
dp<sub>i</sub>/dt = −∂H/∂q<sub>i</sub>
</div>
<p>These are 2n first-order equations (for n degrees of freedom), replacing n second-order Lagrange equations. They treat position and momentum on equal footing — a symmetry that becomes the correspondence principle in quantum mechanics.</p>

<h2>Phase Space</h2>
<p>Phase space is the 2n-dimensional space spanned by (q₁...qₙ, p₁...pₙ). Each point in phase space represents a complete state of the system. The system's evolution traces out a trajectory in phase space. Key theorem: <strong>Liouville's theorem</strong> — the phase space volume occupied by an ensemble of systems is conserved in time (the flow is incompressible). This underpins statistical mechanics.</p>

<h2>Poisson Brackets</h2>
<div class="formula-block"><span class="formula-label">Poisson Bracket</span>{f, g} = Σ(∂f/∂q<sub>i</sub> ∂g/∂p<sub>i</sub> − ∂f/∂p<sub>i</sub> ∂g/∂q<sub>i</sub>)</div>
<p>The time evolution of any function f(q,p,t) is df/dt = {f, H} + ∂f/∂t. A quantity is conserved if {f, H} = 0. This directly maps to the quantum commutator [f̂, Ĥ]/(iℏ).</p>

<div class="info-box info-box--note">
<div class="info-box-title" style="color:var(--accent-plasma)">🔗 The Quantum Connection</div>
<p style="margin:0">The translation from classical Hamiltonian mechanics to quantum mechanics is remarkably direct: replace canonical variables with operators (q → q̂, p → p̂) and Poisson brackets with commutators ({A,B} → [Â,B̂]/iℏ). The Hamiltonian becomes the energy operator, and Hamilton's equations become Heisenberg's equations of motion. This 'canonical quantisation' is the most common method for constructing quantum theories.</p>
</div>
"""
    },
    {
        "slug": "rigid-body-motion",
        "num": "21", "icon": "🎳",
        "title": "Rigid Body Motion",
        "subtitle": "Inertia Tensors, Euler Angles, and Gyroscopes",
        "tags": ["Rigid Bodies","Gyroscope","Euler Angles"],
        "sim": False,
        "keywords": "rigid body motion, inertia tensor, Euler angles, principal axes, precession, nutation, gyroscope, Euler equations of motion, angular momentum",
        "description": "Rigid body dynamics — the inertia tensor, principal axes, Euler angles, precession and nutation of gyroscopes, and the Euler equations of rigid body motion.",
        "img": "https://images.unsplash.com/photo-1630839437035-dac17da580d0?w=1200&q=75&auto=format",
        "img_alt": "Spinning top and gyroscopic rigid body motion",
        "content": """
<p>The motion of rigid bodies — solid objects that maintain their shape — is considerably more complex than point particle motion. A rigid body has six degrees of freedom (three translational, three rotational), and the rotational dynamics are described by the inertia tensor rather than a simple scalar moment of inertia. The resulting equations govern everything from spinning tops and gyroscopes to the rotation of planets and spacecraft attitude control.</p>

<h2>The Inertia Tensor</h2>
<p>For rotation about an arbitrary axis, the relationship L = Iω generalises to:</p>
<div class="formula-block"><span class="formula-label">Angular Momentum (tensor form)</span>L⃗ = I·ω⃗ (matrix multiplication)</div>
<p>The inertia tensor I is a 3×3 symmetric matrix. Its components are I<sub>ij</sub> = ∫(r²δ<sub>ij</sub> − r<sub>i</sub>r<sub>j</sub>)dm. L and ω are generally not parallel — this explains the wobbling of an asymmetric rotating body.</p>

<h2>Principal Axes</h2>
<p>Every rigid body has three principal axes about which the inertia tensor is diagonal. These are the eigenvectors of the inertia tensor. For rotation about a principal axis, L is parallel to ω and the motion is simple. Euler's equations describe the rotation in the principal axis frame:</p>
<div class="formula-block"><span class="formula-label">Euler's Equations</span>
I₁(dω₁/dt) + (I₃−I₂)ω₂ω₃ = τ₁<br/>
I₂(dω₂/dt) + (I₁−I₃)ω₃ω₁ = τ₂<br/>
I₃(dω₃/dt) + (I₂−I₁)ω₁ω₂ = τ₃
</div>

<h2>Precession and Nutation</h2>
<p>A spinning gyroscope subject to gravity undergoes precession — the spin axis slowly rotates about the vertical. The precession rate is:</p>
<div class="formula-block"><span class="formula-label">Precession Rate</span>Ω = τ/L = Mgd/(Iω)</div>
<p>Superimposed on precession is nutation — a bobbing of the spin axis. The Earth itself precesses with a period of 26,000 years (due to the Moon and Sun's torque on Earth's equatorial bulge) and nutates with a period of 18.6 years.</p>

<h2>Applications</h2>
<p>Gyroscopes are used in navigation systems (inertial navigation for aircraft, ships, and spacecraft), stabilisation systems (camera stabilisers, ship stabilisers), and attitude control (satellite reaction wheels). Understanding rigid body motion is also essential for robotics, biomechanics, and the analysis of athletic spinning motions.</p>

<div class="info-box info-box--fact">
<div class="info-box-title" style="color:#a078ff">🪃 The Dzhanibekov Effect</div>
<p style="margin:0">Euler's equations predict that rotation about an intermediate principal axis is unstable — the body will flip periodically in free space. This was dramatically demonstrated by Russian cosmonaut Vladimir Dzhanibekov who observed a wing nut spontaneously flipping in microgravity (1985). It is also called the tennis racket theorem and is a consequence of the instability of the intermediate axis of the inertia tensor.</p>
</div>
"""
    },
    {
        "slug": "non-inertial-frames",
        "num": "22", "icon": "🔁",
        "title": "Non-Inertial Reference Frames",
        "subtitle": "Fictitious Forces, Coriolis Effect, and Rotating Frames",
        "tags": ["Reference Frames","Coriolis","Centrifugal"],
        "sim": False,
        "keywords": "non-inertial frames, fictitious forces, Coriolis effect, centrifugal force, rotating reference frame, accelerating frame, Foucault pendulum",
        "description": "Physics in non-inertial reference frames — fictitious forces, the Coriolis effect, centrifugal force, Foucault pendulum, and applications in meteorology and engineering.",
        "img": "https://images.unsplash.com/photo-1465101162946-4377e57745c3?w=1200&q=75&auto=format",
        "img_alt": "Earth rotation and non-inertial reference frames",
        "content": """
<p>Newton's laws hold exactly in inertial (non-accelerating) frames. But observers in accelerating or rotating frames observe apparent forces that have no third-law partner — fictitious forces. These are not 'real' forces in the Newtonian sense, but they are real observable effects for observers in the non-inertial frame. Understanding them is essential for meteorology, engineering on Earth, and spacecraft dynamics.</p>

<h2>Fictitious Forces in Accelerating Frames</h2>
<p>An observer in a frame with acceleration a⃗<sub>0</sub> must add a fictitious force −ma⃗<sub>0</sub> to each object to apply Newton's second law. Example: in an accelerating elevator, objects appear heavier (upward acceleration) or lighter (downward acceleration). In free fall, the fictitious force exactly cancels gravity — weightlessness.</p>

<h2>Rotating Frames — Additional Forces</h2>
<p>In a frame rotating with angular velocity Ω⃗, two fictitious forces appear for a particle with velocity v⃗' (as measured in the rotating frame):</p>
<div class="formula-block"><span class="formula-label">Coriolis Force</span>F⃗<sub>Cor</sub> = −2m(Ω⃗ × v⃗')</div>
<div class="formula-block"><span class="formula-label">Centrifugal Force</span>F⃗<sub>cf</sub> = −mΩ⃗ × (Ω⃗ × r⃗)</div>

<h2>The Coriolis Effect on Earth</h2>
<p>Earth is a rotating frame (Ω = 7.27 × 10⁻⁵ rad/s). The Coriolis force deflects moving objects: to the right in the Northern Hemisphere, to the left in the Southern Hemisphere. Consequences:</p>
<ul style="margin:0 0 16px 20px;color:var(--text-secondary)">
  <li style="margin-bottom:8px">Cyclones rotate anticlockwise in the North, clockwise in the South</li>
  <li style="margin-bottom:8px">Long-range artillery must account for Coriolis deflection</li>
  <li style="margin-bottom:8px">Prevailing wind patterns and ocean currents are shaped by the Coriolis effect</li>
  <li style="margin-bottom:8px">The Foucault pendulum demonstrates Earth's rotation by the slow precession of its swing plane</li>
</ul>

<h2>Centrifugal Force</h2>
<p>The centrifugal force pushes outward from the rotation axis. On Earth, it slightly reduces effective gravity (most at the equator where v = rΩ is maximum) and causes Earth to be slightly oblate (flattened at poles). Earth's equatorial radius exceeds its polar radius by about 21 km.</p>

<h2>Foucault Pendulum</h2>
<p>Foucault's pendulum (1851) demonstrates Earth's rotation directly. The swing plane remains fixed in space while Earth rotates beneath it. At the North Pole, the plane rotates 360° in 24 hours. At latitude λ, the period is 24h/sin λ. At the equator, the Foucault pendulum shows no precession (horizontal component of Ω is perpendicular to the swing).</p>

<div class="info-box info-box--tip">
<div class="info-box-title" style="color:var(--accent-green)">🌍 Equivalence Principle Preview</div>
<p style="margin:0">The observation that a uniform gravitational field is indistinguishable from a uniformly accelerating frame led Einstein to his <strong>equivalence principle</strong> — the cornerstone of General Relativity. In GR, gravity is not a force but the curvature of spacetime, and 'free fall' is the natural inertial motion. The fictitious force perspective thus contains the seed of the deepest theory of gravity we have.</p>
</div>
"""
    },
]

def make_html(t):
    tags = " ".join(f'<span class="tc-tag" style="padding:5px 12px;font-size:0.75rem">{x}</span>' for x in t["tags"])
    sim_badge = '<span class="badge badge-green">Interactive Simulation</span>' if t.get("sim") else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>{t["title"]} — Classical Mechanics | QuantumAtlas</title>
  <meta name="description" content="{t["description"]}"/>
  <meta name="keywords" content="{t["keywords"]}"/>
  <link rel="canonical" href="https://yourdomain.com/topics/classical-mechanics/{t["slug"]}.html"/>
  <meta property="og:title" content="{t["title"]} | QuantumAtlas"/>
  <meta property="og:description" content="{t["description"]}"/>
  <meta property="og:image" content="{t["img"]}"/>
  <script type="application/ld+json">{{
    "@context":"https://schema.org","@type":"Article",
    "headline":"{t["title"]}","description":"{t["description"]}",
    "image":"{t["img"]}",
    "author":{{"@type":"Organization","name":"QuantumAtlas"}},
    "publisher":{{"@type":"Organization","name":"QuantumAtlas","url":"https://yourdomain.com"}},
    "breadcrumb":{{"@type":"BreadcrumbList","itemListElement":[
      {{"@type":"ListItem","position":1,"name":"Home","item":"https://yourdomain.com/"}},
      {{"@type":"ListItem","position":2,"name":"Branches","item":"https://yourdomain.com/theory.html"}},
      {{"@type":"ListItem","position":3,"name":"Classical Mechanics","item":"https://yourdomain.com/branches/classical-mechanics.html"}},
      {{"@type":"ListItem","position":4,"name":"{t["title"]}"}}
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
  <section class="topic-hero">
    <img src="{t["img"]}" alt="{t["img_alt"]}" class="topic-hero-bg-img" loading="eager"/>
    <div class="topic-hero-overlay"></div>
    <div class="container topic-hero-content">
      <nav class="breadcrumb">
        <a href="../../index.html">Home</a><span class="sep">›</span>
        <a href="../../theory.html">Branches</a><span class="sep">›</span>
        <a href="../../branches/classical-mechanics.html">Classical Mechanics</a><span class="sep">›</span>
        <span class="current">{t["title"]}</span>
      </nav>
      <div style="display:flex;gap:10px;flex-wrap:wrap;margin-bottom:18px">
        <span class="badge badge-plasma">Classical Mechanics</span>
        {sim_badge}
        <span class="badge badge-nova">Topic {t["num"]}</span>
      </div>
      <h1 class="topic-hero-title">{t["icon"]} {t["title"]}</h1>
      <p class="topic-hero-sub">{t["subtitle"]}</p>
      <div style="display:flex;gap:8px;flex-wrap:wrap;margin-top:20px">{tags}</div>
    </div>
  </section>
  <div class="container topic-layout">
    <article class="topic-article">
      <div class="ad-container" style="margin-bottom:36px">
        <div style="text-align:center;width:100%">
          <span class="ad-label">Advertisement</span>
          <ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-2633513915753897" data-ad-slot="auto" data-ad-format="auto" data-full-width-responsive="true"></ins>
          <script>(adsbygoogle=window.adsbygoogle||[]).push({{}});</script>
        </div>
      </div>
      <div class="topic-body">{t["content"]}</div>
      <div class="ad-container" style="margin-top:40px">
        <div style="text-align:center;width:100%">
          <span class="ad-label">Advertisement</span>
          <ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-2633513915753897" data-ad-slot="auto" data-ad-format="auto" data-full-width-responsive="true"></ins>
          <script>(adsbygoogle=window.adsbygoogle||[]).push({{}});</script>
        </div>
      </div>
    </article>
    <aside class="topic-sidebar">
      <div class="sidebar-card">
        <h4 style="font-family:var(--font-mono);font-size:0.75rem;text-transform:uppercase;letter-spacing:0.12em;color:var(--accent-plasma);margin-bottom:14px">// Topic Info</h4>
        <div class="sidebar-stat"><span>Branch</span><span>Classical Mechanics</span></div>
        <div class="sidebar-stat"><span>Topic</span><span>{t["num"]} / 22</span></div>
        <div class="sidebar-stat"><span>Level</span><span>Advanced</span></div>
      </div>
      <div class="sidebar-card">
        <h4 style="font-family:var(--font-mono);font-size:0.75rem;text-transform:uppercase;letter-spacing:0.12em;color:var(--accent-plasma);margin-bottom:14px">// All Topics</h4>
        <ul style="list-style:none;display:flex;flex-direction:column;gap:6px">
          <li><a href="newtons-laws.html" style="font-size:0.8rem;color:var(--text-muted);text-decoration:none">01. Newton's Laws</a></li>
          <li><a href="projectile-motion.html" style="font-size:0.8rem;color:var(--text-muted);text-decoration:none">02. Projectile Motion</a></li>
          <li><a href="conservation-of-energy.html" style="font-size:0.8rem;color:var(--text-muted);text-decoration:none">03. Conservation of Energy</a></li>
          <li><a href="linear-momentum.html" style="font-size:0.8rem;color:var(--text-muted);text-decoration:none">04. Linear Momentum</a></li>
          <li><a href="circular-motion.html" style="font-size:0.8rem;color:var(--text-muted);text-decoration:none">05. Circular Motion</a></li>
          <li><a href="gravitational-force.html" style="font-size:0.8rem;color:var(--text-muted);text-decoration:none">06. Gravitational Force</a></li>
          <li><a href="simple-harmonic-motion.html" style="font-size:0.8rem;color:var(--text-muted);text-decoration:none">07. Simple Harmonic Motion</a></li>
          <li><a href="rotational-dynamics.html" style="font-size:0.8rem;color:var(--text-muted);text-decoration:none">08. Rotational Dynamics</a></li>
          <li><a href="work-and-power.html" style="font-size:0.8rem;color:var(--text-muted);text-decoration:none">09. Work & Power</a></li>
          <li><a href="friction-and-drag.html" style="font-size:0.8rem;color:var(--text-muted);text-decoration:none">10. Friction & Drag</a></li>
          <li><a href="keplers-laws.html" style="font-size:0.8rem;color:var(--text-muted);text-decoration:none">11. Kepler's Laws</a></li>
          <li><a href="waves-and-oscillations.html" style="font-size:0.8rem;color:var(--text-muted);text-decoration:none">12. Waves & Oscillations</a></li>
          <li><a href="centre-of-mass.html" style="font-size:0.8rem;color:var(--text-muted);text-decoration:none">13. Centre of Mass</a></li>
          <li><a href="statics-and-equilibrium.html" style="font-size:0.8rem;color:var(--text-muted);text-decoration:none">14. Statics & Equilibrium</a></li>
          <li><a href="fluid-mechanics.html" style="font-size:0.8rem;color:var(--text-muted);text-decoration:none">15. Fluid Mechanics</a></li>
          <li><a href="elasticity-and-stress.html" style="font-size:0.8rem;color:var(--text-muted);text-decoration:none">16. Elasticity & Stress</a></li>
          <li><a href="kinematics.html" style="font-size:0.8rem;color:var(--text-muted);text-decoration:none">17. Kinematics</a></li>
          <li><a href="damped-oscillations.html" style="font-size:0.8rem;color:var(--text-muted);text-decoration:none">18. Damped Oscillations</a></li>
          <li><a href="lagrangian-mechanics.html" style="font-size:0.8rem;color:var(--text-muted);text-decoration:none">19. Lagrangian Mechanics</a></li>
          <li><a href="hamiltonian-mechanics.html" style="font-size:0.8rem;color:var(--text-muted);text-decoration:none">20. Hamiltonian Mechanics</a></li>
          <li><a href="rigid-body-motion.html" style="font-size:0.8rem;color:var(--text-muted);text-decoration:none">21. Rigid Body Motion</a></li>
          <li><a href="non-inertial-frames.html" style="font-size:0.8rem;color:var(--text-muted);text-decoration:none">22. Non-Inertial Frames</a></li>
        </ul>
      </div>
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
</html>"""

os.makedirs('/home/claude/physics-website/topics/classical-mechanics', exist_ok=True)
for t in REMAINING:
    path = f'/home/claude/physics-website/topics/classical-mechanics/{t["slug"]}.html'
    with open(path, 'w') as f:
        f.write(make_html(t))
    print(f"✓ {t['slug']}.html")
print("All 18 remaining topics done.")
