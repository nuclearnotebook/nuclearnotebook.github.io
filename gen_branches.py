#!/usr/bin/env python3
"""Generate all 17 remaining branch pages"""
import os

BRANCHES = [
    ("quantum-mechanics","Quantum Mechanics","Modern","badge-nova","24","6","https://images.unsplash.com/photo-1518770660439-4636190af475?w=1200&q=75&auto=format","Wave functions, Schrödinger equation, uncertainty principle, entanglement, and the foundations of quantum field theory.","#7b2fff","quantum mechanics, wave function, Schrödinger equation, uncertainty principle, quantum entanglement, quantum field theory, particle wave duality",["Wave-Particle Duality","Schrödinger Equation","Uncertainty Principle","Quantum Tunnelling","Superposition","Entanglement","Quantum Operators","Spin and Angular Momentum","Hydrogen Atom","Perturbation Theory","Variational Methods","Identical Particles","Quantum Statistics","Path Integrals","Measurement Problem","Bell's Theorem","Quantum Cryptography","Density Matrix","Quantum Harmonic Oscillator","Many-Body Quantum Systems","Decoherence","Relativistic QM","Quantum Field Basics","The Standard Model Preview"]),
    ("thermodynamics","Thermodynamics","Classical","badge-solar","20","4","https://images.unsplash.com/photo-1580863822022-ee0af1be97b3?w=1200&q=75&auto=format","The four laws of thermodynamics, heat and work, entropy, Carnot cycle, and thermodynamic potentials.","#ff6b1a","thermodynamics, first law, second law, entropy, Carnot engine, heat engines, thermodynamic cycles, heat transfer, temperature, internal energy",["Zeroth Law & Temperature","First Law of Thermodynamics","Heat and Work","Internal Energy","Second Law & Entropy","Carnot Cycle","Heat Engines & Refrigerators","Third Law of Thermodynamics","Thermodynamic Potentials","Maxwell Relations","Phase Transitions","Clausius-Clapeyron Equation","Ideal Gas Law","Real Gas Models","Heat Transfer: Conduction","Heat Transfer: Convection","Heat Transfer: Radiation","Thermodynamic Equilibrium","Irreversible Processes","Exergy and Efficiency"]),
    ("statistical-mechanics","Statistical Mechanics","Modern","badge-nova","18","3","https://images.unsplash.com/photo-1461749280684-dccba630e2f6?w=1200&q=75&auto=format","Microstates, macrostates, Boltzmann distribution, partition functions, and quantum statistics.","#7b2fff","statistical mechanics, Boltzmann distribution, partition function, entropy, microstates, Fermi-Dirac statistics, Bose-Einstein statistics, canonical ensemble",["Microstates and Macrostates","Boltzmann Entropy","Canonical Ensemble","Partition Function","Boltzmann Distribution","Grand Canonical Ensemble","Fermi-Dirac Statistics","Bose-Einstein Statistics","Maxwell-Boltzmann Statistics","Equipartition Theorem","Ideal Gas from Statistics","Blackbody Radiation","Bose-Einstein Condensation","Ising Model","Phase Transitions in Statistics","Fluctuations and Correlations","Non-Equilibrium Statistical Mechanics","Entropy and Information Theory"]),
    ("electromagnetism","Electromagnetism","Classical","badge-plasma","22","7","https://images.unsplash.com/photo-1511871893393-82e9c16b81e3?w=1200&q=75&auto=format","Maxwell's equations, electric and magnetic fields, electromagnetic induction, circuits, and radiation.","#00d4ff","electromagnetism, Maxwell's equations, electric field, magnetic field, electromagnetic induction, Faraday's law, Gauss's law, Ampere's law, EM waves",["Electric Charge and Coulomb's Law","Electric Fields","Gauss's Law","Electric Potential","Capacitors and Dielectrics","Current and Resistance","DC Circuits","Magnetic Fields","Magnetic Force on Charges","Ampere's Law","Faraday's Law","Lenz's Law","Inductance","AC Circuits","Maxwell's Equations","Electromagnetic Waves","Poynting Vector","Electromagnetic Radiation","Polarisation","Dispersion and Refraction","Antennas and Radiation","Magnetism in Matter"]),
    ("relativity","Relativity","Modern","badge-nova","20","5","https://images.unsplash.com/photo-1502134249126-9f3755a50d78?w=1200&q=75&auto=format","Special and general relativity, Lorentz transformations, spacetime curvature, and black hole physics.","#7b2fff","special relativity, general relativity, Lorentz transformation, time dilation, length contraction, spacetime, E=mc2, black holes, gravitational waves",["Galilean Relativity","Postulates of Special Relativity","Lorentz Transformations","Time Dilation","Length Contraction","Relativistic Momentum","Mass-Energy Equivalence","Relativistic Kinematics","The Twin Paradox","Spacetime and Minkowski Diagrams","Tensors in Relativity","General Relativity: Equivalence Principle","Geodesics and Curved Spacetime","Schwarzschild Metric","Black Holes","Gravitational Time Dilation","Gravitational Waves","Cosmological Models","Big Bang Theory","Dark Energy and Accelerating Universe"]),
    ("optics","Optics","Classical","badge-plasma","20","5","https://images.unsplash.com/photo-1507413245164-6160d8298b31?w=1200&q=75&auto=format","Geometric and wave optics, reflection, refraction, diffraction, interference, and lasers.","#00d4ff","optics, reflection, refraction, Snell's law, diffraction, interference, polarisation, lasers, lenses, mirrors, optical instruments",["Nature of Light","Reflection and Mirrors","Refraction and Snell's Law","Total Internal Reflection","Lenses and Lens Equations","Optical Instruments","Interference","Young's Double Slit","Diffraction","Diffraction Gratings","Polarisation","Malus's Law","Dispersion and Prisms","Coherence","Lasers","Holography","Fibre Optics","Non-linear Optics","Photonics","Quantum Optics"]),
    ("acoustics","Acoustics","Applied","badge-solar","16","4","https://images.unsplash.com/photo-1445375011782-2384686778a0?w=1200&q=75&auto=format","Sound waves, resonance, standing waves, Doppler effect, and musical physics.","#ff6b1a","acoustics, sound waves, Doppler effect, resonance, standing waves, decibels, speed of sound, ultrasound, musical acoustics, noise",["Nature of Sound","Speed of Sound","Sound Intensity and Decibels","Doppler Effect","Reflection and Echoes","Interference of Sound","Resonance and Natural Frequency","Standing Waves in Tubes","Musical Instruments","Musical Scales","The Human Ear","Ultrasound","Infrasound","Architectural Acoustics","Noise Pollution and Control","Acoustic Metamaterials"]),
    ("nuclear-physics","Nuclear Physics","Modern","badge-nova","18","3","https://images.unsplash.com/photo-1564327767484-ea27b4b7add7?w=1200&q=75&auto=format","Nuclear structure, radioactive decay, fission, fusion, and nuclear forces.","#7b2fff","nuclear physics, radioactivity, nuclear fission, nuclear fusion, binding energy, radioactive decay, alpha beta gamma radiation, nuclear reactor",["Nuclear Structure","Nuclear Binding Energy","Radioactive Decay","Alpha Decay","Beta Decay","Gamma Decay","Half-Life","Decay Chains","Nuclear Reactions","Nuclear Fission","Chain Reactions","Nuclear Reactors","Nuclear Fusion","The Liquid Drop Model","Shell Model","Nuclear Forces","Nuclear Astrophysics","Medical Applications"]),
    ("atomic-physics","Atomic Physics","Modern","badge-green","18","3","https://images.unsplash.com/photo-1559757148-5c350d0d3c56?w=1200&q=75&auto=format","Bohr model, quantum atomic structure, emission spectra, and atomic clocks.","#00ff88","atomic physics, Bohr model, hydrogen atom, electron transitions, atomic spectra, spectroscopy, lasers, atomic clocks, quantum numbers",["Atomic Models — Thomson to Bohr","Bohr Model of Hydrogen","Quantum Numbers","Electron Orbitals","Multi-Electron Atoms","Pauli Exclusion Principle","Aufbau Principle","Emission and Absorption Spectra","Hydrogen Spectrum","Zeeman Effect","Stark Effect","Electron Spin","Spin-Orbit Coupling","Fine and Hyperfine Structure","Atomic Transitions","Lasers and Stimulated Emission","Atomic Clocks","Laser Cooling and Traps"]),
    ("molecular-physics","Molecular Physics","Modern","badge-nova","16","2","https://images.unsplash.com/photo-1628595351029-c2bf17511435?w=1200&q=75&auto=format","Molecular bonding, vibrational modes, spectroscopy, and chemical bonding theory.","#7b2fff","molecular physics, molecular bonds, covalent bonds, ionic bonds, molecular vibrations, molecular spectroscopy, van der Waals forces, LCAO",["Types of Chemical Bonds","Ionic and Covalent Bonding","LCAO and Molecular Orbital Theory","Molecular Hydrogen","Diatomic Molecules","Polyatomic Molecules","Rotational States","Vibrational States","Ro-Vibrational Coupling","Infrared Spectroscopy","Raman Spectroscopy","Van der Waals Interactions","Hydrogen Bonding","Intermolecular Forces","Molecular Energy Levels","Photodissociation"]),
    ("condensed-matter","Condensed Matter Physics","Applied","badge-solar","20","4","https://images.unsplash.com/photo-1532187643603-ba119ca4109e?w=1200&q=75&auto=format","Crystal structures, band theory, semiconductors, superconductivity, and the quantum Hall effect.","#ff6b1a","condensed matter physics, crystal structure, band theory, semiconductors, superconductivity, quantum Hall effect, Bose-Einstein condensate, magnetism",["Crystal Structures","Bravais Lattices","X-Ray Diffraction","Phonons","Free Electron Model","Band Theory","Insulators Semiconductors Metals","Doping and pn Junctions","Transistors","Hall Effect","Superconductivity","Meissner Effect","Cooper Pairs","BCS Theory","Quantum Hall Effect","Fractional Quantum Hall Effect","Magnetism","Ferromagnetism","Topological Insulators","Graphene and 2D Materials"]),
    ("astrophysics","Astrophysics & Cosmology","Modern","badge-nova","25","5","https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?w=1200&q=75&auto=format","Stellar evolution, black holes, dark matter, and the large-scale structure of the universe.","#7b2fff","astrophysics, cosmology, stellar evolution, black holes, dark matter, dark energy, Big Bang, neutron stars, galaxies, cosmic microwave background",["The Sun and Stellar Structure","Stellar Evolution","Hertzsprung-Russell Diagram","White Dwarfs","Neutron Stars","Black Holes","Supernovae","The Milky Way","Galaxies","Active Galactic Nuclei","Dark Matter","The Expanding Universe","Hubble's Law","Big Bang Theory","Cosmic Microwave Background","Dark Energy","Inflation Theory","Large-Scale Structure","Gravitational Lensing","Exoplanets","Stellar Nucleosynthesis","Gamma-Ray Bursts","Gravitational Wave Astronomy","Multi-Messenger Astronomy","The Fate of the Universe"]),
    ("particle-physics","Particle Physics","Modern","badge-nova","20","3","https://images.unsplash.com/photo-1579389083078-4e7018379f7e?w=1200&q=75&auto=format","The Standard Model, quarks, leptons, bosons, and the Higgs mechanism.","#7b2fff","particle physics, Standard Model, quarks, leptons, bosons, Higgs boson, quantum chromodynamics, electroweak theory, particle accelerators",["Elementary Particles Overview","Quarks and Leptons","Gauge Bosons","The Standard Model","Quantum Electrodynamics","Quantum Chromodynamics","Electroweak Unification","The Higgs Mechanism","Feynman Diagrams","Particle Accelerators","The LHC","CP Violation","Neutrino Oscillations","Antimatter","Conservation Laws","Symmetry in Particle Physics","Beyond the Standard Model","Supersymmetry","Grand Unified Theories","String Theory Overview"]),
    ("geophysics","Geophysics","Applied","badge-solar","16","2","https://images.unsplash.com/photo-1523821741446-edb2b68bb7a0?w=1200&q=75&auto=format","Seismology, Earth's interior structure, geomagnetism, and plate tectonics.","#ff6b1a","geophysics, seismology, seismic waves, Earth's interior, geomagnetism, plate tectonics, gravity anomalies, earthquake physics, Earth's structure",["Earth's Internal Structure","Seismic Waves","Earthquakes","Seismometers","P and S Waves","Earth's Core","Earth's Mantle","Plate Tectonics","Convection in the Mantle","Geomagnetism","Earth's Magnetic Field","Magnetic Reversals","Gravity Anomalies","Isostasy","Geothermal Heat","Volcanoes and Physics"]),
    ("biophysics","Biophysics","Interdisciplinary","badge-green","16","2","https://images.unsplash.com/photo-1532187863486-abf9dbad1b69?w=1200&q=75&auto=format","Physics of living systems: membrane biophysics, motor proteins, neural signals, and medical imaging.","#00ff88","biophysics, membrane biophysics, ion channels, motor proteins, DNA mechanics, neural signals, medical imaging, MRI, biophotonics",["Physics of the Cell","Cell Membranes and Lipid Bilayers","Ion Channels and Membrane Potential","Action Potentials","Motor Proteins","DNA Mechanics","Protein Folding","Diffusion and Transport","Viscoelasticity in Biology","Biophotonics","Microscopy Techniques","Medical Imaging: X-Ray","Medical Imaging: MRI","Medical Imaging: Ultrasound","Radiation Biophysics","Biophysics of Hearing"]),
    ("plasma-physics","Plasma Physics","Applied","badge-solar","16","3","https://images.unsplash.com/photo-1504711434969-e33886168f5c?w=1200&q=75&auto=format","Ionized gas dynamics, magnetic confinement, plasma waves, and nuclear fusion.","#ff6b1a","plasma physics, ionized gas, magnetic confinement, plasma waves, tokamak, nuclear fusion, solar wind, magnetohydrodynamics, Debye length",["What is Plasma","Debye Shielding","Plasma Frequency","Motion in Magnetic Fields","Plasma Waves","Magnetohydrodynamics","Magnetic Confinement","Tokamaks","Inertial Confinement","Nuclear Fusion Energy","Solar Wind","Magnetosphere","Aurora","Plasma Instabilities","Plasma Diagnostics","Astrophysical Plasmas"]),
    ("chaos-theory","Chaos Theory","Interdisciplinary","badge-nova","16","4","https://images.unsplash.com/photo-1465101162946-4377e57745c3?w=1200&q=75&auto=format","Nonlinear dynamics, fractals, strange attractors, and the butterfly effect.","#7b2fff","chaos theory, nonlinear dynamics, fractals, strange attractors, Lorenz attractor, butterfly effect, bifurcation, Lyapunov exponents, logistic map",["Introduction to Nonlinear Dynamics","Deterministic Chaos","Sensitivity to Initial Conditions","The Butterfly Effect","Lyapunov Exponents","Phase Space and Attractors","Strange Attractors","The Lorenz Attractor","Bifurcations","The Logistic Map","Period Doubling","Fractals","The Mandelbrot Set","Self-Similarity","Chaos in Physical Systems","Applications of Chaos Theory"]),
]

def make_branch(b):
    slug, name, cat, badge, topics_n, sims_n, img, desc, color, keywords, topic_list = b
    topic_cards = ""
    for i, t in enumerate(topic_list):
        num = str(i+1).zfill(2)
        topic_cards += f"""
        <a href="../topics/{slug}/{t.lower().replace(' ','-').replace("'","").replace('/','').replace('&','').replace(',','').replace(':','').replace('—','')}.html" class="tc" style="text-decoration:none">
          <span style="font-family:var(--font-mono);font-size:0.65rem;color:var(--text-muted)">{num} / {topics_n}</span>
          <h3 style="font-size:0.95rem;color:var(--text-primary);margin:0">{t}</h3>
          <div style="display:flex;justify-content:space-between;align-items:center;border-top:1px solid var(--border-dim);padding-top:8px;margin-top:auto">
            <span style="font-family:var(--font-display);font-size:0.7rem;color:var(--accent-plasma)">Read →</span>
          </div>
        </a>"""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>{name} — All Topics | QuantumAtlas</title>
  <meta name="description" content="Explore all {name} topics on QuantumAtlas — {desc}"/>
  <meta name="keywords" content="{keywords}"/>
  <link rel="canonical" href="https://yourdomain.com/branches/{slug}.html"/>
  <meta property="og:title" content="{name} — All Topics | QuantumAtlas"/>
  <meta property="og:description" content="{desc}"/>
  <meta property="og:image" content="{img}"/>
  <script type="application/ld+json">{{
    "@context":"https://schema.org","@type":"CollectionPage",
    "name":"{name} Topics","description":"{desc}",
    "url":"https://yourdomain.com/branches/{slug}.html",
    "breadcrumb":{{"@type":"BreadcrumbList","itemListElement":[
      {{"@type":"ListItem","position":1,"name":"Home","item":"https://yourdomain.com/"}},
      {{"@type":"ListItem","position":2,"name":"Branches","item":"https://yourdomain.com/theory.html"}},
      {{"@type":"ListItem","position":3,"name":"{name}"}}
    ]}}
  }}</script>
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-4X0M6RM0F6"></script>
  <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-4X0M6RM0F6',{{page_title:document.title,page_location:window.location.href}});</script>
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-2633513915753897" crossorigin="anonymous"></script>
  <meta name="google-adsense-account" content="ca-pub-2633513915753897">
  <link rel="stylesheet" href="../css/global.css"/>
  <link rel="stylesheet" href="../css/nav.css"/>
  <style>
    .branch-hero{{padding:130px 0 70px;position:relative;overflow:hidden}}
    .branch-hero-bg{{position:absolute;inset:0;background:linear-gradient(135deg,rgba(5,8,16,0) 0%,rgba(5,8,16,0.9) 100%)}}
    .branch-hero img.bg{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:0.1}}
    .topics-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}}
    .tc{{background:var(--gradient-card);border:1px solid var(--border-dim);border-radius:var(--radius-md);padding:18px;display:flex;flex-direction:column;gap:8px;transition:var(--transition);position:relative;overflow:hidden}}
    .tc::after{{content:'';position:absolute;left:0;top:0;bottom:0;width:3px;background:var(--gradient-plasma);transform:scaleY(0);transform-origin:bottom;transition:transform 0.3s ease}}
    .tc:hover{{transform:translateY(-3px);border-color:var(--border-glow);box-shadow:var(--shadow-hover)}}
    .tc:hover::after{{transform:scaleY(1)}}
    @media(max-width:900px){{.topics-grid{{grid-template-columns:repeat(2,1fr)}}}}
    @media(max-width:560px){{.topics-grid{{grid-template-columns:1fr}}}}
  </style>
</head>
<body>
<div id="nav-placeholder"></div>
<main>
  <section class="branch-hero">
    <img src="{img}" alt="{name}" class="bg" loading="eager"/>
    <div class="branch-hero-bg"></div>
    <div class="container" style="position:relative;z-index:2">
      <nav class="breadcrumb">
        <a href="../index.html">Home</a><span class="sep">›</span>
        <a href="../theory.html">Branches</a><span class="sep">›</span>
        <span class="current">{name}</span>
      </nav>
      <span class="badge {badge}" style="margin-bottom:16px">{cat}</span>
      <h1><span class="gradient-text">{name}</span></h1>
      <p style="max-width:620px;font-size:1.05rem;margin-top:12px;color:var(--text-secondary)">{desc}</p>
      <div style="display:flex;gap:24px;flex-wrap:wrap;margin-top:24px;font-family:var(--font-mono);font-size:0.8rem;color:var(--text-muted)">
        <span>📄 <strong style="color:var(--text-primary)">{topics_n} Topics</strong></span>
        <span>🎮 <strong style="color:var(--text-primary)">{sims_n} Simulations</strong></span>
      </div>
    </div>
  </section>
  <section class="section--sm">
    <div class="container">
      <div class="ad-container" style="margin-bottom:36px">
        <div style="text-align:center;width:100%">
          <span class="ad-label">Advertisement</span>
          <ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-2633513915753897" data-ad-slot="auto" data-ad-format="auto" data-full-width-responsive="true"></ins>
          <script>(adsbygoogle=window.adsbygoogle||[]).push({{}});</script>
        </div>
      </div>
      <div class="topics-grid reveal">{topic_cards}</div>
      <div class="ad-container" style="margin-top:48px">
        <div style="text-align:center;width:100%">
          <span class="ad-label">Advertisement</span>
          <ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-2633513915753897" data-ad-slot="auto" data-ad-format="auto" data-full-width-responsive="true"></ins>
          <script>(adsbygoogle=window.adsbygoogle||[]).push({{}});</script>
        </div>
      </div>
    </div>
  </section>
</main>
<div id="footer-placeholder"></div>
<script src="../js/components.js"></script>
</body>
</html>"""

os.makedirs('/home/claude/physics-website/branches', exist_ok=True)
for b in BRANCHES:
    path = f'/home/claude/physics-website/branches/{b[0]}.html'
    with open(path,'w') as f:
        f.write(make_branch(b))
    print(f"✓ branches/{b[0]}.html")
print("All 17 branch pages done.")
