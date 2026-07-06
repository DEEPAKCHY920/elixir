import os

TREATMENTS = {
    "acne-treatment": {
        "title": "Acne Treatment",
        "category": "Skin Care & Facials",
        "tagline": "Rebalance your skin's natural oil production, eliminate blemishes, and clear pores with clinical precision.",
        "form_value": "Skin Rejuvenation",
        "pricing": "₹4,500 / session",
        "duration": "45 Mins",
        "sessions": "4-6 Sessions",
        "meta_desc": "Get clear, spot-free skin with our expert Acne Treatment at Elixir Clinic. Blending salicylic peels, light therapy, and medical extraction protocols.",
        "overview": "<p>Acne is a complex inflammatory condition triggered by excess sebum production, follicle congestion, and bacteria. At Elixir Clinic, we approach acne treatment through an intensive multi-step clinical system that targets the underlying causes. By utilizing medical-grade salicylic acid chemical peels, focused blue light therapy, and professional sterile extractions, we reduce active lesions, soothe redness, and prevent future breakouts.</p><p>We also evaluate the skin's dosha balance (typically Pitta-Kapha excess) to recommend botanical cleansers such as neem and turmeric to maintain skin barrier health after your clinical session.</p>",
        "benefits": [
            {"title": "Clear Active Breakouts", "desc": "Eliminates acne-causing bacteria and unclogs deeply congested pores.", "icon": "spa"},
            {"title": "Reduce Scars & Redness", "desc": "Soothes dermal inflammation and fades post-acne dark marks (PIH).", "icon": "healing"},
            {"title": "Regulate Sebum Control", "desc": "Reduces excess oil production to prevent future follicle blockages.", "icon": "water_drop"}
        ],
        "procedure": [
            {"step": "01", "title": "Double Cleanse & Prep", "desc": "Skin is deeply cleansed with botanical extracts to remove dirt, followed by a clarifying tonic."},
            {"step": "02", "title": "Clinical Treatment", "desc": "A customized salicylic chemical peel is applied, followed by sterile extractions and healing blue LED therapy."},
            {"step": "03", "title": "Barrier Support", "desc": "A calming zinc-infused recovery mask and hydrating sunscreen are applied to protect the barrier."}
        ],
        "recovery": "<p>Acne treatment has virtually zero downtime. You may experience mild redness for 2-4 hours post-session. We recommend avoiding direct makeup for 24 hours and using a gentle, non-comedogenic cleanser. Always apply a broad-spectrum SPF 50+ sunscreen daily, as your skin will be more sensitive to UV light.</p>",
        "faqs": [
            {"q": "How many sessions will I need?", "a": "Most patients see significant clearing after 3 sessions, but we recommend a course of 4 to 6 sessions spaced 2 weeks apart for optimal results."},
            {"q": "Does the extraction process hurt?", "a": "You may feel mild pinching during extractions, but our trained medical experts perform them using sterile tools and cooling agents to minimize discomfort."},
            {"q": "Will my acne return after treatment?", "a": "Our treatments clear current breakouts and regulate oil. To prevent recurrence, we provide a customized home-care routine combining clinical active ingredients and Ayurvedic botanicals."}
        ]
    },
    "hydra-facial": {
        "title": "Hydra Facial",
        "category": "Skin Care & Facials",
        "tagline": "Drench your skin in medical-grade hydration, deep pore suction, and botanical serum infusions.",
        "form_value": "Skin Rejuvenation",
        "pricing": "₹15,000 / session",
        "duration": "60 Mins",
        "sessions": "1 Session / Month",
        "meta_desc": "Experience the ultimate skin glow with our Hydra Facial at Elixir Clinic. Instantly cleanse, exfoliate, extract, and hydrate with high-performance serum infusions.",
        "overview": "<p>The Hydra Facial is a revolutionary, non-invasive skin resurfacing treatment that delivers immediate, visible results with absolutely no downtime. Utilizing patented vortex-fusion technology, the device cleanses, exfoliates, and extracts impurities from deep within pores while simultaneously infusing the skin with essential nutrients like antioxidants, peptides, and hyaluronic acid.</p><p>This treatment is ideal for all skin types, addressing concerns like fine lines, large pores, hyperpigmentation, and dull skin to restore a plump, dewy glow.</p>",
        "benefits": [
            {"title": "Instant Radiance", "desc": "Delivers a visible, red-carpet glow and deep cellular hydration immediately.", "icon": "sparkles"},
            {"title": "Deep Extraction", "desc": "Uses vortex-suction to effortlessly remove blackheads, whiteheads, and sebum.", "icon": "clean_hands"},
            {"title": "Fine Line Plumping", "desc": "Infuses concentrated hyaluronic acid to minimize fine lines and dehydration creases.", "icon": "add_circle"}
        ],
        "procedure": [
            {"step": "01", "title": "Cleansing & Peeling", "desc": "A gentle exfoliating tip cleanses the skin surface and sweeps away dead cells."},
            {"step": "02", "title": "Extract & Hydrate", "desc": "Vortex-suction removes impurities from pores, while nourishing moisturizers soothe the skin."},
            {"step": "03", "title": "Fuse & Protect", "desc": "The skin is saturated with antioxidant serums and peptides to maximize shine and barrier strength."}
        ],
        "recovery": "<p>There is absolutely no downtime associated with a Hydra Facial. You can immediately return to your normal daily activities. We advise keeping the skin clean, avoiding heavy makeup for the rest of the day, and applying sunscreen to maintain your fresh glow.</p>",
        "faqs": [
            {"q": "Who is a good candidate for Hydra Facial?", "a": "Hydra Facial is suitable for all skin types, including sensitive skin. It helps with dryness, oily congestion, and general anti-aging maintenance."},
            {"q": "How often should I get a Hydra Facial?", "a": "We recommend one session per month to maintain optimal hydration, clear pores, and keep your skin glowing continuously."},
            {"q": "Can I combine this with other treatments?", "a": "Yes, Hydra Facial is an excellent base treatment and can be safely combined with Botox, fillers, or laser therapies, often during the same clinic visit."}
        ]
    },
    "chemical-peel": {
        "title": "Chemical Peel",
        "category": "Skin Care & Facials",
        "tagline": "Resurface your skin texture, fade hyperpigmentation, and smooth scars with medical acid peeling.",
        "form_value": "Skin Rejuvenation",
        "pricing": "₹8,500 / session",
        "duration": "30 Mins",
        "sessions": "3-5 Sessions",
        "meta_desc": "Reveal smooth, radiant skin with professional Chemical Peels at Elixir Clinic. Tailored glycolic, lactic, and salicylic acid formulas for clinical resurfacing.",
        "overview": "<p>Chemical Peels use medical-grade exfoliating solutions to dissolve the chemical bonds holding dead, damaged cells to the skin's surface. By encouraging the outer layer of skin to peel away, this treatment reveals a fresh, smooth, and evenly pigmented layer underneath.</p><p>At Elixir Clinic, our dermatologists customize peel formulations—ranging from gentle glycolic and lactic acids to deeper TCA and salicylic formulas—to address your specific concerns like sun damage, pigmentation, acne scars, and fine lines.</p>",
        "benefits": [
            {"title": "Even Skin Tone", "desc": "Fades dark spots, melasma, sun damage, and post-inflammatory pigmentation.", "icon": "grain"},
            {"title": "Texture Resurfacing", "desc": "Smooths rough skin patches, dry build-up, and shallow acne scars.", "icon": "auto_fix_high"},
            {"title": "Boost Collagen", "desc": "Triggers the natural healing response in deeper layers to stimulate collagen synthesis.", "icon": "favorite"}
        ],
        "procedure": [
            {"step": "01", "title": "Skin Degreasing", "desc": "The skin is prepped and thoroughly degreased to ensure even absorption of the peeling agents."},
            {"step": "02", "title": "Peel Application", "desc": "The customized chemical solution is applied and carefully monitored by our medical team."},
            {"step": "03", "title": "Neutralization & Soothe", "desc": "The peel is deactivated, followed by a cooling compress, barrier repair cream, and physical sunscreen."}
        ],
        "recovery": "<p>Depending on the depth of the peel, recovery ranges from 2 to 7 days. You may experience mild flaking or peeling resembling a light sunburn. Do not peel or scratch loose skin. Avoid heat, heavy workouts, and direct sun exposure for 48 hours, and apply physical mineral SPF daily.</p>",
        "faqs": [
            {"q": "Will my skin literally peel off?", "a": "For light and medium peels, you will experience mild flaking or shedding. Deep peels produce more noticeable peeling. We customize the depth based on your lifestyle and comfort."},
            {"q": "Does a chemical peel burn?", "a": "You will feel a warm, tingling, or stinging sensation during the application, which subsides as soon as the neutralizer is applied."},
            {"q": "Can chemical peels treat body areas?", "a": "Yes! We frequently perform peels on the back, neck, chest, and hands to clear acne, sun spots, and dry textures."}
        ]
    },
    "laser-hair-removal": {
        "title": "Laser Hair Removal",
        "category": "Laser Treatments",
        "tagline": "Permanently eliminate unwanted body and facial hair using FDA-approved cooled-tip lasers.",
        "form_value": "Laser Treatments",
        "pricing": "₹12,500 / session",
        "duration": "45 Mins",
        "sessions": "6-8 Sessions",
        "meta_desc": "Get permanently smooth skin with FDA-approved Laser Hair Removal at Elixir Clinic. Safe, virtually painless cooled-tip technology for all skin types.",
        "overview": "<p>Unwanted body hair can be a constant maintenance hassle. Our Laser Hair Removal treatment offers a permanent, hygienic solution. Using advanced, FDA-approved laser devices with integrated cooled-tip technologies, we target hair follicles precisely at the root without damaging the surrounding skin tissue.</p><p>The laser energy is absorbed by the pigment (melanin) in the hair, converting to heat and destroying the follicle to prevent regrowth. This method is safe for all skin tones and body areas, including the face, underarms, bikini line, legs, and back.</p>",
        "benefits": [
            {"title": "Permanent Reduction", "desc": "Achieves up to 90% permanent hair reduction after completing the recommended sessions.", "icon": "check_circle"},
            {"title": "Virtually Painless", "desc": "Features advanced contact cooling to soothe the skin surface, ensuring maximum comfort.", "icon": "spa"},
            {"title": "No More Ingrowns", "desc": "Eliminates the risk of painful ingrown hairs, razor bumps, and skin irritation.", "icon": "shield"}
        ],
        "procedure": [
            {"step": "01", "title": "Grid Mapping & Gel", "desc": "The treatment area is shaved, mapped into grids, and covered with a chilled conducting gel."},
            {"step": "02", "title": "Laser Treatment", "desc": "The laser applicator is passed over the grid, emitting precise pulses targeted at active follicles."},
            {"step": "03", "title": "Calming Gel", "desc": "The conducting gel is cleaned off, and a soothing aloe vera cream and sunscreen are applied."}
        ],
        "recovery": "<p>There is no downtime. You can return to work immediately. You may experience mild redness or goosebump-like sensations for a few hours. Avoid hot showers, saunas, and swimming pools for 24 hours. Do not pluck or wax between sessions—only shaving is allowed.</p>",
        "faqs": [
            {"q": "Why do I need multiple sessions?", "a": "Hair grows in cycles. Lasers only destroy follicles in the active growth phase (anagen). Multiple sessions ensure we catch all hairs as they enter this phase."},
            {"q": "Is laser hair removal safe for dark skin?", "a": "Yes! We use specialized Nd:YAG laser settings that bypass the skin's surface pigment to target the deep hair roots safely, preventing burns or pigment issues."},
            {"q": "Does it work on blonde or grey hair?", "a": "Because the laser relies on melanin to locate the hair root, it is less effective on white, grey, blonde, or red hair. A consultation will help determine suitability."}
        ]
    },
    "prp-therapy": {
        "title": "PRP Therapy",
        "category": "Anti-Aging & Injectables",
        "tagline": "Harness your own blood platelets to organically stimulate collagen, heal tissue, and restore skin glow.",
        "form_value": "Anti-Aging Treatment",
        "pricing": "₹18,000 / session",
        "duration": "60 Mins",
        "sessions": "3-4 Sessions",
        "meta_desc": "Revitalize your skin and hair naturally with PRP Therapy at Elixir Clinic. Platelet-Rich Plasma micro-infusions for collagen growth and cellular repair.",
        "overview": "<p>Platelet-Rich Plasma (PRP) Therapy is a completely organic treatment that uses your body's own growth factors to stimulate skin rejuvenation and hair regrowth. We draw a small amount of your blood and place it in a high-speed centrifuge to separate the plasma containing a highly concentrated amount of platelets.</p><p>This growth-factor-rich plasma is then micro-injected back into your face (Vampire Facial) or scalp, triggering rapid tissue healing, collagen production, cell growth, and improved blood supply.</p>",
        "benefits": [
            {"title": "100% Natural Rejuvenation", "desc": "Uses your own cells, eliminating any risk of allergic reactions or chemical side effects.", "icon": "favorite"},
            {"title": "Boost Collagen & Elastin", "desc": "Plumps fine lines, improves skin elasticity, and refines crepey textures.", "icon": "psychology_alt"},
            {"title": "Strengthens Hair Roots", "desc": "Feeds dormant follicles on the scalp to combat thinning and boost hair density.", "icon": "face"}
        ],
        "procedure": [
            {"step": "01", "title": "Blood Draw & Numbing", "desc": "A small blood sample is collected, and a topical numbing cream is applied to the target area."},
            {"step": "02", "title": "Centrifugation", "desc": "The blood is spun to separate and isolate the concentrated Platelet-Rich Plasma layer."},
            {"step": "03", "title": "Micro-Injection", "desc": "The PRP is carefully injected or microneedled into the face or scalp using fine sterile needles."}
        ],
        "recovery": "<p>Downtime is minimal (24-48 hours). You may experience mild swelling, bruising, or tiny red pinpricks at the injection sites. Do not wash your face or scalp for 12 hours post-treatment to allow the plasma to absorb completely. Avoid intense heat and workouts for 48 hours.</p>",
        "faqs": [
            {"q": "Is PRP painful?", "a": "We apply a strong medical numbing cream for 45 minutes before the procedure, making the micro-injections very tolerable. You may feel a slight warm sensation afterward."},
            {"q": "When will I see skin results?", "a": "Collagen production takes time. While you will see an immediate glow in 2 weeks, the peak structural improvements in volume and lines develop over 3 to 6 months."},
            {"q": "Can I combine PRP with Microneedling?", "a": "Yes! This combination is highly recommended for scarring, stretch marks, and facial rejuvenation. The PRP is absorbed deep through the micro-channels."}
        ]
    },
    "microneedling": {
        "title": "Microneedling",
        "category": "Skin Care & Facials",
        "tagline": "Trigger cellular skin remodeling and fade acne scars using advanced micro-channeling devices.",
        "form_value": "Skin Rejuvenation",
        "pricing": "₹10,000 / session",
        "duration": "45 Mins",
        "sessions": "3-5 Sessions",
        "meta_desc": "Fade acne scars, stretch marks, and fine lines with professional Microneedling at Elixir Clinic. Safe collagen induction therapy with sterile devices.",
        "overview": "<p>Microneedling, also known as Collagen Induction Therapy, is a minimally invasive clinical procedure designed to trigger the skin's natural healing response. Using an FDA-approved device equipped with fine sterile micro-needles, we create thousands of microscopic, controlled micro-channels in the outer layers of the skin.</p><p>These micro-injuries prompt the body to produce new collagen and elastin fibers, restructuring acne scars, smoothing fine lines, minimizing large pores, and allowing deeper penetration of medical serums.</p>",
        "benefits": [
            {"title": "Acne Scar Remodeling", "desc": "Breaks down stubborn fibrous scar tissue and encourages flat, smooth skin growth.", "icon": "healing"},
            {"title": "Minimize Large Pores", "desc": "Tightens the skin matrix surrounding pores, making them appear significantly smaller.", "icon": "auto_fix_high"},
            {"title": "Enhanced Product Absorption", "desc": "Allows active serums (hyaluronic acid, vitamin C) to penetrate up to 300% deeper.", "icon": "water_drop"}
        ],
        "procedure": [
            {"step": "01", "title": "Cleanse & Numb", "desc": "The face is cleaned, and a premium numbing cream is applied for 30-40 minutes to ensure comfort."},
            {"step": "02", "title": "Active Micro-Needling", "desc": "A sterile needle cartridge is used over the face, infused with active hyaluronic acid glide serums."},
            {"step": "03", "title": "Recovery Mask", "desc": "A cooling hyaluronic mask is applied to calm redness, followed by barrier repair creams."}
        ],
        "recovery": "<p>Downtime is 24 to 48 hours. Your skin will look like it has a mild sunburn. Avoid touching your face, sweating, makeup, and active acids (retinoids, vitamin C) for 48 hours. Keep the skin highly hydrated and use a gentle physical sunscreen daily.</p>",
        "faqs": [
            {"q": "Does microneedling hurt?", "a": "Because of the topical numbing cream, the treatment is virtually painless. You may feel a sandpaper-like scratching sensation in boney areas like the forehead."},
            {"q": "How many sessions are needed for acne scars?", "a": "For deep acne scars, we recommend a series of 4 to 6 sessions spaced 4 weeks apart to allow the new collagen structure to build fully."},
            {"q": "Is it safe for active acne?", "a": "No. Microneedling cannot be done over active, inflammatory acne pustules, as it can spread bacteria. We treat active acne first using chemical peels."}
        ]
    },
    "anti-aging-treatment": {
        "title": "Anti-Aging Treatment",
        "category": "Anti-Aging & Injectables",
        "tagline": "Rebuild your skin's structural integrity, lift sagging contours, and smooth expression wrinkles.",
        "form_value": "Anti-Aging Treatment",
        "pricing": "Consultation Required",
        "duration": "90 Mins",
        "sessions": "Varies by Plan",
        "meta_desc": "Turn back the clock with custom Anti-Aging Treatments at Elixir Clinic. Tailored plans combining medical lasers, radiofrequency lifting, and skin boosters.",
        "overview": "<p>As the skin ages, it loses collagen, elastin, and fat volume, leading to sagging, fine lines, and wrinkles. At Elixir Clinic, our Anti-Aging Treatments are not one-size-fits-all. We design customized, multi-modality rejuvenation blueprints that address your unique facial structural changes.</p><p>Your plan may combine advanced Radiofrequency (RF) skin tightening, micro-focused ultrasound lifting, dermal boosters, and medical-grade lasers to rebuild structural support from the inside out, returning natural contours and volume.</p>",
        "benefits": [
            {"title": "Lift Sagging Contours", "desc": "Lifts cheeks, defines jawlines, and tightens loose skin around the neck.", "icon": "check_circle"},
            {"title": "Smooth Fine Lines", "desc": "Plumps crow's feet, laugh lines, forehead wrinkles, and crepiness.", "icon": "sparkles"},
            {"title": "Restore Skin Volume", "desc": "Replenishes lost dermal hydration and stimulates natural cellular renewal.", "icon": "add_circle"}
        ],
        "procedure": [
            {"step": "01", "title": "3D Skin Scan Analysis", "desc": "We use advanced medical sensors to analyze deep volume loss and structural collagen density."},
            {"step": "02", "title": "Clinical Rejuvenation", "desc": "We administer custom lifting energy therapies, followed by dermal hydration injections or lasers."},
            {"step": "03", "title": "Soothing Lift Mask", "desc": "A cold collagen-infused recovery mask is applied to lock in hydration and reduce redness."}
        ],
        "recovery": "<p>Downtime varies depending on the modalities used. Energy-based lifting has zero downtime, while combination skin resurfacing may require 2-4 days of recovery. We provide a customized aftercare kit with peptides and barrier creams.</p>",
        "faqs": [
            {"q": "What age should I start anti-aging treatments?", "a": "Preventative treatments like skin boosters and light energy lifting can start in your late 20s or early 30s. Deeper restorative treatments are common in 40s and beyond."},
            {"q": "Are the results natural-looking?", "a": "Yes! Our philosophy is 'Precise Care'. We focus on rebuilding your own collagen and restoring natural volumes, avoiding overfilled or artificial looks."},
            {"q": "How long do the anti-aging results last?", "a": "Lifting and collagen-building results can last between 12 to 18 months. We recommend simple maintenance sessions once or twice a year."}
        ]
    },
    "botox": {
        "title": "Botox",
        "category": "Anti-Aging & Injectables",
        "tagline": "Soften dynamic expression lines, wrinkles, and crow's feet with targeted micro-injections.",
        "form_value": "Anti-Aging Treatment",
        "pricing": "₹350 / unit",
        "duration": "20 Mins",
        "sessions": "Repeat every 4-6 Months",
        "meta_desc": "Smooth dynamic wrinkles instantly with safe, professional Botox injections at Elixir Clinic. Tailored by board-certified dermatologists for natural results.",
        "overview": "<p>Botox is a purified protein that temporarily relaxes the specific facial muscles responsible for dynamic expression wrinkles. When we frown, smile, or squint, our muscles contract, pulling the skin and creating lines. Over time, these dynamic lines become permanent creases.</p><p>By administering microscopic, precise injections of Botox, we soften dynamic wrinkles—such as forehead lines, frown lines (11s), and crow's feet—resulting in a refreshed, rested, and naturally youthful look.</p>",
        "benefits": [
            {"title": "Smooth Forehead & Eyes", "desc": "Erases forehead furrows, frown lines, and squint creases around the eyes.", "icon": "check_circle"},
            {"title": "Prevent Deep Creases", "desc": "Prevents temporary dynamic lines from converting into permanent, deep skin cracks.", "icon": "shield"},
            {"title": "Fast & Convenient", "desc": "Often called a 'lunchtime procedure' taking under 20 minutes with zero downtime.", "icon": "schedule"}
        ],
        "procedure": [
            {"step": "01", "title": "Expression Mapping", "desc": "Our doctor analyzes your muscle movements to determine precise injection points."},
            {"step": "02", "title": "Micro-Injections", "desc": "Botox is injected into target muscles using an ultra-fine needle (feels like a small pinprick)."},
            {"step": "03", "title": "Ice Press", "desc": "A cold compress is applied to prevent swelling, and you are ready to resume your day."}
        ],
        "recovery": "<p>There is no downtime. You may experience tiny red bumps at the injection sites, which disappear in 15-30 minutes. Do not lie down flat, massage the face, or exercise for 4 hours post-injection to prevent the product from migrating.</p>",
        "faqs": [
            {"q": "Will Botox make my face look frozen?", "a": "Not at all. We practice conservative, precise dosing to preserve your natural facial expressions and emotions, while simply smoothing away the harsh wrinkles."},
            {"q": "How long does it take to see results?", "a": "You will begin to see muscle relaxation in 3 to 5 days, with the final, smoothed results appearing in 10 to 14 days."},
            {"q": "How often do I need to get Botox?", "a": "Botox naturally breaks down and wears off in 4 to 6 months. We recommend scheduled maintenance sessions to keep your skin smooth and wrinkle-free."}
        ]
    },
    "dermal-fillers": {
        "title": "Dermal Fillers",
        "category": "Anti-Aging & Injectables",
        "tagline": "Restore lost facial volume, sculpt jawlines, and plump lips with hyaluronic acid fillers.",
        "form_value": "Anti-Aging Treatment",
        "pricing": "From ₹28,000 / syringe",
        "duration": "45 Mins",
        "sessions": "Lasts 9-18 Months",
        "meta_desc": "Restore youthful volumes and define facial contours with premium Hyaluronic Acid Dermal Fillers at Elixir Clinic. Safe, immediate, natural-looking results.",
        "overview": "<p>Dermal Fillers are gel-like substances formulated from Hyaluronic Acid (a sugar molecule found naturally in our body that binds water). As we age, our facial bones recede and fat pads shrink, causing cheeks to deflate and sag, lips to thin, and shadows to form around the nose and mouth (nasolabial folds).</p><p>We inject fillers deep into target areas to restore youthfulness, sculpt chin and jaw profiles, and plump lips, yielding an immediate lifting effect.</p>",
        "benefits": [
            {"title": "Immediate Lift & Volume", "desc": "Visible improvements are seen instantly right after the clinical session.", "icon": "sparkles"},
            {"title": "Sculpt Facial Features", "desc": "Enhances cheekbones, projects chins, and sharpens jawlines for balanced profile harmony.", "icon": "check_circle"},
            {"title": "Reversible & Safe", "desc": "Made of hyaluronic acid, which can be easily dissolved if needed, ensuring complete control.", "icon": "shield"}
        ],
        "procedure": [
            {"step": "01", "title": "Assessment & Mapping", "desc": "The face structure is mapped, identifying volume loss, followed by sterilizing and numbing."},
            {"step": "02", "title": "Filler Injection", "desc": "The filler is injected precisely into the targeted structural layers using fine needles or cannulas."},
            {"step": "03", "title": "Molding & Cold Pack", "desc": "The doctor gently molds the product to ensure smooth contours, followed by a cold compress."}
        ],
        "recovery": "<p>Recovery is quick. You can return to normal activities immediately. Some swelling, tenderness, and bruising at the injection sites are common and resolve in 3 to 7 days. Avoid heavy heat (saunas) and intense workouts for 48 hours.</p>",
        "faqs": [
            {"q": "Do dermal fillers hurt?", "a": "Our premium fillers contain built-in lidocaine (numbing agent) and we apply a topical numbing cream beforehand, making the discomfort very minor."},
            {"q": "How long do fillers last?", "a": "Depending on the area treated and the thickness of the filler gel, results last between 9 months (lips) to 18 months (cheeks/jawline)."},
            {"q": "What is the difference between Botox and Fillers?", "a": "Botox relaxes muscles to smooth dynamic expression lines (e.g. forehead). Fillers restore lost volume and lift sagging tissues (e.g. cheeks, lips)."}
        ]
    },
    "skin-brightening": {
        "title": "Skin Brightening",
        "category": "Skin Care & Facials",
        "tagline": "Fade stubborn hyperpigmentation, brighten dull tones, and boost overall skin glow.",
        "form_value": "Skin Rejuvenation",
        "pricing": "₹7,500 / session",
        "duration": "45 Mins",
        "sessions": "4-6 Sessions",
        "meta_desc": "Get a glowing, even skin tone with professional Skin Brightening treatments at Elixir Clinic. Target hyperpigmentation, melasma, and sunspots.",
        "overview": "<p>A bright, even complexion represents cellular health. Skin Brightening treatments at Elixir Clinic target stubborn pigment fields (melanin build-up) caused by sun exposure, hormonal fluctuations (melasma), and post-inflammatory marks. By combining skin-brightening peels, vitamin C infusions, and advanced light therapy, we regulate melanin production.</p><p>We also look at Bhrajaka Pitta dosha balance to recommend cooling, brightening botanicals like saffron and sandalwood for home care protection.</p>",
        "benefits": [
            {"title": "Fade Hyperpigmentation", "desc": "Visibly reduces dark spots, sun freckles, melasma, and stubborn post-acne marks.", "icon": "grain"},
            {"title": "Evens Out Complexion", "desc": "Restores a uniform color and glow across the face, neck, and body.", "icon": "sparkles"},
            {"title": "Inhibit Melanin Production", "desc": "Regulates pigment cells to prevent new discoloration from forming.", "icon": "shield"}
        ],
        "procedure": [
            {"step": "01", "title": "Micro-Exfoliation", "desc": "The skin is cleansed and gently exfoliated to allow brightening serums to absorb deeply."},
            {"step": "02", "title": "Active Brightening Peel", "desc": "A customized brightening peel containing vitamin C, kojic, or arbutin is applied."},
            {"step": "03", "title": "Infusion Mask", "desc": "A soothing, vitamin-rich brightening mask is applied to calm and hydrate the skin."}
        ],
        "recovery": "<p>There is minimal downtime. You may experience mild flaking for 2-3 days post-treatment. Sun protection is critical: wear SPF 50+ daily, avoid direct sun exposure for 5 days, and do not use harsh scrubs or acids for 48 hours.</p>",
        "faqs": [
            {"q": "Will skin brightening lighten my natural skin tone?", "a": "No, our treatments do not alter your genetic skin tone. They are designed to eliminate excess pigment, dark patches, and sunspots to restore your healthiest, original, even complexion."},
            {"q": "How many sessions are recommended?", "a": "For mild dullness, 3 sessions yield great results. For stubborn melasma or deep sun damage, we recommend a series of 6 sessions spaced 2 weeks apart."},
            {"q": "Is the result permanent?", "a": "Pigment correction is highly durable, but UV rays can trigger new spots. Consistent sunscreen use and maintaining your prescribed skincare routine are essential for long-term brightness."}
        ]
    },
    "carbon-laser-facial": {
        "title": "Carbon Laser Facial",
        "category": "Laser Treatments",
        "tagline": "Deeply detoxify pores, reduce oily shine, and stimulate collagen with the Hollywood Peel.",
        "form_value": "Laser Treatments",
        "pricing": "₹9,500 / session",
        "duration": "45 Mins",
        "sessions": "3-5 Sessions",
        "meta_desc": "Experience the famous Carbon Laser Facial (Hollywood Peel) at Elixir Clinic. Instantly purify pores, exfoliate dead skin, and reduce oiliness.",
        "overview": "<p>The Carbon Laser Facial, often called the 'Hollywood Peel', is a highly effective, fast treatment designed to purify pores and boost skin glow. We apply a thin layer of liquid carbon cream to the face, which penetrates deep into the pores, bonding with dead skin cells, oil, and impurities.</p><p>We then pass a specialized Q-Switched Nd:YAG laser over the face. The laser light is highly attracted to the black carbon particles, instantly vaporizing the carbon along with all the debris, deeply cleaning the pores and stimulating collagen.</p>",
        "benefits": [
            {"title": "Deep Pore Detox", "desc": "Vaporizes carbon particles to instantly pull dirt, oil, and dead skin out of pores.", "icon": "clean_hands"},
            {"title": "Oil Control", "desc": "Dramatically reduces excess sebum production, leaving a clean matte finish.", "icon": "water_drop"},
            {"title": "Instant Exfoliation", "desc": "Improves skin texture immediately, leaving it smooth and ready for makeup.", "icon": "sparkles"}
        ],
        "procedure": [
            {"step": "01", "title": "Carbon Paste Prep", "desc": "A thin layer of liquid medical carbon is applied to the face and allowed to dry for 10-15 minutes."},
            {"step": "02", "title": "Laser Vaporization", "desc": "The laser is passed over the face, producing a clicking sound as it vaporizes the carbon paste."},
            {"step": "03", "title": "Cooling Hydration", "desc": "The skin is cleaned, and a cooling aloe compress, hydrating serums, and sunscreen are applied."},
        ],
        "recovery": "<p>There is zero downtime. You can apply makeup and return to your routine immediately. You may experience slight skin warmth or mild pinkness for an hour. Keep the skin hydrated and always wear sunscreen.</p>",
        "faqs": [
            {"q": "Does the carbon laser facial hurt?", "a": "No, the treatment is very comfortable. You will feel a mild warm tingling sensation and a slight snap, but no pain. Numbing cream is not required."},
            {"q": "Is this good for acne?", "a": "Yes! The laser heat kills acne bacteria and shrinks oil glands, making it excellent for managing inflammatory breakouts and oily skin."},
            {"q": "Can I get this before an event?", "a": "Absolutely! The Carbon Laser Facial produces immediate exfoliating and glowing results, making it the perfect pre-event skin pick-me-up."}
        ]
    },
    "skin-tightening": {
        "title": "Skin Tightening",
        "category": "Laser Treatments",
        "tagline": "Firm loose skin and contour your face using advanced Radiofrequency and Ultrasound energy.",
        "form_value": "Laser Treatments",
        "pricing": "₹12,000 / session",
        "duration": "50 Mins",
        "sessions": "4-6 Sessions",
        "meta_desc": "Tighten loose skin and contour your face with non-surgical Radiofrequency Skin Tightening at Elixir Clinic. Rebuild collagen structure safely.",
        "overview": "<p>Loss of firmness and sagging skin are caused by the breakdown of structural collagen fibers. Our non-surgical Skin Tightening treatment uses advanced Radiofrequency (RF) and focused ultrasound energy to deliver controlled thermal energy deep into the subcutaneous layers of the skin.</p><p>This heat immediately contracts existing collagen fibers, producing an instant firming effect, while simultaneously stimulating fibroblasts to synthesize new, thick collagen over the following months.</p>",
        "benefits": [
            {"title": "Lift & Firm Skin", "desc": "Restores tone to sagging jowls, cheeks, under-eye areas, and the neck.", "icon": "check_circle"},
            {"title": "Rebuild Collagen", "desc": "Stimulates long-term production of thick, young collagen for firm skin.", "icon": "favorite"},
            {"title": "Completely Non-Surgical", "desc": "No needles, no incisions, and no downtime required for a tight contour.", "icon": "shield"}
        ],
        "procedure": [
            {"step": "01", "title": "Prep & Conducting Gel", "desc": "The skin is cleaned, and a specialized conducting gel is applied to the treatment area."},
            {"step": "02", "title": "Energy Application", "desc": "The RF handpiece is massaged over the area in circular motions, raising the deep tissue temperature."},
            {"step": "03", "title": "Cool Down & Cleanse", "desc": "The gel is wiped off, followed by a cooling compress and hydrating recovery serums."}
        ],
        "recovery": "<p>There is no downtime. You can immediately return to work. Your skin will look slightly flushed, like you had a warm workout, which fades in 1-2 hours. Avoid cold water washing for 4 hours to let the thermal stimulation work.</p>",
        "faqs": [
            {"q": "What does the treatment feel like?", "a": "It feels like a warm, soothing hot stone massage. Most patients find the treatment very relaxing and comfortable."},
            {"q": "When will I see the results?", "a": "You will notice an immediate tightening due to collagen contraction. The maximum firming and lifting results appear gradually over 2 to 3 months as new collagen matures."},
            {"q": "Which areas can be tightened?", "a": "We frequently treat the jowls, jawline, neck, under-eye bags, and abdomen to tighten loose post-pregnancy or post-weight loss skin."}
        ]
    },
    "hair-loss-treatment": {
        "title": "Hair Loss Treatment",
        "category": "Hair & Body",
        "tagline": "Stop hair thinning, nourish follicles, and stimulate natural regrowth using medical-grade therapies.",
        "form_value": "Hair Restoration",
        "pricing": "₹12,000 / session",
        "duration": "60 Mins",
        "sessions": "4-6 Sessions",
        "meta_desc": "Combat hair thinning and promote regrowth with advanced Hair Loss Treatments at Elixir Clinic. Scalp nourishment and clinical PRP solutions.",
        "overview": "<p>Hair loss and thinning can be triggered by stress, genetics (DHT activity), or nutritional deficiencies. At Elixir Clinic, our Hair Loss Treatments are structured to halt hair fall and revitalize dormant roots. We utilize custom therapies like Platelet-Rich Plasma (PRP) scalp micro-infusions, follicle-stimulating growth factor cocktails, and low-level laser therapy (LLLT).</p><p>We also evaluate the scalp's Vata-Pitta dosha profile to prescribe nourishing organic hair oils (Bhringraj, Brahmi, Amla) to maintain scalp health between clinical sessions.</p>",
        "benefits": [
            {"title": "Stop Excessive Hair Fall", "desc": "Nourishes follicle roots to reduce shedding and stabilize active hair fall.", "icon": "shield"},
            {"title": "Stimulate Dormant Roots", "desc": "Awakens inactive hair roots to promote thicker, denser growth.", "icon": "face"},
            {"title": "Improve Scalp Circulation", "desc": "Increases blood flow and nutrient delivery directly to the hair follicles.", "icon": "favorite"}
        ],
        "procedure": [
            {"step": "01", "title": "Scalp Prep & Sanitization", "desc": "The scalp is thoroughly cleaned, parted into sections, and sanitized."},
            {"step": "02", "title": "Nourishing Infusion", "desc": "Platelet-rich growth factors or clinical growth serums are micro-infused into the root layer."},
            {"step": "03", "title": "Laser Stimulation", "desc": "Low-level laser light therapy is applied to boost cellular energy and blood flow in follicles."}
        ],
        "recovery": "<p>There is minimal downtime. You may feel a slight tenderness on the scalp for 12-24 hours. Do not wash your hair or apply hair products for 12 hours after the session. Avoid intense sweating and swimming pools for 48 hours.</p>",
        "faqs": [
            {"q": "Can hair loss treatments grow hair on bald areas?", "a": "These treatments work by strengthening and thickening active follicles that are thinning. They cannot grow hair on completely bald areas where the follicle has died. A transplant is recommended for bald areas."},
            {"q": "How many sessions are required?", "a": "We recommend a course of 4 to 6 sessions spaced 3 weeks apart. Hair growth is a slow process, and visible changes in density take 3 to 4 months."},
            {"q": "Is the treatment suitable for women?", "a": "Yes! Female pattern hair thinning responds exceptionally well to scalp nourishment, growth factors, and PRP therapies."}
        ]
    },
    "hair-transplant": {
        "title": "Hair Transplant",
        "category": "Hair & Body",
        "tagline": "Permanently restore your hairline and crown density with advanced FUE follicle transplants.",
        "form_value": "Hair Restoration",
        "pricing": "From ₹85,000",
        "duration": "4-6 Hours",
        "sessions": "1 Procedure",
        "meta_desc": "Restore your hairline permanently with advanced FUE Hair Transplants at Elixir Clinic. Safe, minimally invasive follicle extraction with natural outcomes.",
        "overview": "<p>For areas with advanced hair thinning or complete baldness, a Hair Transplant provides a permanent, natural-looking restoration. At Elixir Clinic, we specialize in the Follicular Unit Extraction (FUE) method. This minimally invasive procedure involves extracting healthy individual hair follicles from a donor zone (usually the back of the scalp) and grafting them into the thinning or bald recipient areas.</p><p>Once transplanted, the hair follicles continue to grow naturally for a lifetime, blending seamlessly with your existing hair.</p>",
        "benefits": [
            {"title": "Permanent Hair Growth", "desc": "The transplanted hair is genetically resistant to hair loss, ensuring lifetime growth.", "icon": "check_circle"},
            {"title": "Natural Hairline Design", "desc": "Our surgeons map and implant grafts matching the natural angle and density of your hair.", "icon": "face"},
            {"title": "Minimally Invasive FUE", "desc": "Leaves no linear scars, ensuring a quick healing process and minimal discomfort.", "icon": "shield"}
        ],
        "procedure": [
            {"step": "01", "title": "Donor Mapping & Numbing", "desc": "The hairline is mapped, donor area shaved, and local anesthesia is administered for comfort."},
            {"step": "02", "title": "Follicle Extraction", "desc": "Healthy follicles are extracted individually from the donor zone using a micro-punch tool."},
            {"step": "03", "title": "Graft Implantation", "desc": "Micro-channels are made in the recipient area, and the extracted grafts are carefully implanted."}
        ],
        "recovery": "<p>Recovery takes 7 to 10 days. Tiny scabs will form around the implanted grafts and flake off naturally in a week. We provide a post-op kit with gentle washing sprays and antibiotics. Avoid heavy lifting and intense exercise for 2 weeks.</p>",
        "faqs": [
            {"q": "Does a hair transplant hurt?", "a": "The procedure is performed under local anesthesia. You will feel the initial numbing injections, but once the scalp is numb, you will feel no pain during the transplant."},
            {"q": "When will I see the full results?", "a": "Transplanted hair will shed in 3-4 weeks (this is normal). New growth begins in 3 months, with the final dense results visible in 9 to 12 months."},
            {"q": "Are the results permanent?", "a": "Yes! The hair follicles taken from the donor zone are genetically resistant to DHT (the hormone responsible for balding), meaning they will continue to grow permanently."}
        ]
    },
    "tattoo-removal": {
        "title": "Tattoo Removal",
        "category": "Laser Treatments",
        "tagline": "Safe, clean tattoo clearance using advanced multi-wavelength Q-Switched laser technology.",
        "form_value": "Laser Treatments",
        "pricing": "From ₹3,500 / session",
        "duration": "20 Mins",
        "sessions": "6-10 Sessions",
        "meta_desc": "Clear unwanted tattoos safely with advanced Laser Tattoo Removal at Elixir Clinic. Multi-wavelength Nd:YAG lasers for all ink colors.",
        "overview": "<p>Unwanted tattoos no longer have to be permanent. Our Laser Tattoo Removal treatment offers a safe, clinically proven method to fade and clear ink pigments. We use advanced Q-Switched lasers that emit rapid, high-energy light pulses targeted at the tattoo ink.</p><p>The ink particles absorb the laser energy, breaking down into microscopic fragments. Over the following weeks, your body's lymphatic system naturally sweeps these tiny ink fragments away, gradually fading the tattoo with each session.</p>",
        "benefits": [
            {"title": "Safe Ink Clearance", "desc": "Targets tattoo pigments directly, minimizing the risk of damage to the surrounding skin.", "icon": "shield"},
            {"title": "Multi-Color Targeting", "desc": "Uses multiple laser wavelengths to target different ink colors, including dark and bright inks.", "icon": "grain"},
            {"title": "Scar-Free Healing", "desc": "Encourages clean skin clearance without leaving textured scars or thermal damage.", "icon": "healing"}
        ],
        "procedure": [
            {"step": "01", "title": "Numbing & Prep", "desc": "The tattoo is cleaned, and a cooling numbing gel is applied to minimize discomfort."},
            {"step": "02", "title": "Laser Pulses", "desc": "The laser is passed over the tattoo, shattering the ink particles (produces a popping sound)."},
            {"step": "03", "title": "Post-Care Dressing", "desc": "A soothing antibiotic ointment is applied, and the area is covered with a sterile bandage."}
        ],
        "recovery": "<p>Recovery takes 5 to 7 days. The treated area may look slightly frosted, blistered, or scabbed, which is a normal healing reaction. Keep the area clean and dry. Apply healing ointment daily, do not scratch scabs, and protect the area from sun exposure.</p>",
        "faqs": [
            {"q": "Can a tattoo be completely removed?", "a": "Yes, most tattoos can be faded to the point of complete clearance. The number of sessions depends on tattoo size, ink depth, and ink colors used."},
            {"q": "How many sessions are needed?", "a": "Tattoo removal is a gradual process. Most tattoos require 6 to 10 sessions spaced 6 to 8 weeks apart to allow the lymphatic system to clear the shattered ink."},
            {"q": "What does the laser feel like?", "a": "It is often described as feeling like a rubber band snapping against the skin. We use cooling air systems and numbing creams to ensure the treatment is tolerable."}
        ]
    }
}

TEMPLATE_PATH = "treatment-template.html"
OUTPUT_DIR = "treatments"

def main():
    if not os.path.exists(TEMPLATE_PATH):
        print(f"Error: Template file '{TEMPLATE_PATH}' not found. Please create it first.")
        return

    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        template_content = f.read()

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"Directory '{OUTPUT_DIR}' checked/created.")

    for slug, data in TREATMENTS.items():
        # Generate Benefits Cards
        benefits_html = ""
        for index, benefit in enumerate(data["benefits"]):
            delay_attr = f' style="transition-delay: {index * 0.1}s;"' if index > 0 else ''
            benefits_html += f'''            <!-- Benefit {index + 1} -->
            <div class="glass-card p-8 rounded-3xl bg-white border border-glass-border flex gap-4 items-start group hover:-translate-y-1 transition-all duration-300 reveal-on-scroll"{delay_attr}>
                <div class="w-10 h-10 rounded-xl bg-primary/10 text-primary flex items-center justify-center shrink-0 group-hover:scale-110 transition-transform">
                    <span class="material-symbols-outlined text-lg">{benefit["icon"]}</span>
                </div>
                <div class="space-y-1.5">
                    <h4 class="font-bold text-deep-navy text-xs uppercase tracking-wider font-navigation">{benefit["title"]}</h4>
                    <p class="text-[10px] text-on-surface-variant leading-relaxed">{benefit["desc"]}</p>
                </div>
            </div>\n'''

        # Generate Procedure Cards
        procedure_html = ""
        for index, step in enumerate(data["procedure"]):
            delay_attr = f' style="transition-delay: {index * 0.1}s;"' if index > 0 else ''
            procedure_html += f'''            <!-- Step {step["step"]} -->
            <div class="glass-card p-8 rounded-3xl bg-white border border-glass-border relative hover:-translate-y-1 transition-all duration-300 reveal-on-scroll"{delay_attr}>
                <span class="absolute top-6 right-8 font-display-lg text-4xl font-extrabold text-primary/10 leading-none">{step["step"]}</span>
                <div class="space-y-4">
                    <div class="w-10 h-10 rounded-full bg-primary/10 text-primary flex items-center justify-center font-bold text-xs">
                        {step["step"]}
                    </div>
                    <div class="space-y-1.5">
                        <h4 class="font-bold text-deep-navy text-xs uppercase tracking-wider font-navigation">{step["title"]}</h4>
                        <p class="text-[10px] text-on-surface-variant leading-relaxed">{step["desc"]}</p>
                    </div>
                </div>
            </div>\n'''

        # Generate FAQs HTML
        faqs_html = ""
        for index, faq in enumerate(data["faqs"]):
            faqs_html += f'''            <!-- FAQ Item {index + 1} -->
            <div class="glass-card rounded-2xl border border-glass-border bg-white/60 overflow-hidden">
                <button onclick="toggleFaq({index})" class="w-full px-6 py-4 text-left flex justify-between items-center gap-4 hover:bg-slate-50/50 transition-colors">
                    <h4 class="font-bold text-deep-navy text-xs uppercase tracking-wider font-navigation">{faq["q"]}</h4>
                    <span id="faq-icon-{index}" class="material-symbols-outlined text-primary text-sm transition-transform duration-300">expand_more</span>
                </button>
                <div id="faq-content-{index}" class="hidden opacity-0 -translate-y-2 transition-all duration-300 px-6 pb-5 border-t border-glass-border/30 pt-4">
                    <p class="text-[11px] text-on-surface-variant leading-relaxed font-body-md">{faq["a"]}</p>
                </div>
            </div>\n'''

        # Substitute all variables in template
        page_html = template_content
        page_html = page_html.replace("{{TITLE}}", data["title"])
        page_html = page_html.replace("{{CATEGORY}}", data["category"].upper())
        page_html = page_html.replace("{{TAGLINE}}", data["tagline"])
        page_html = page_html.replace("{{METADESC}}", data["meta_desc"])
        page_html = page_html.replace("{{FORM_VALUE}}", data["form_value"])
        page_html = page_html.replace("{{OVERVIEW}}", data["overview"])
        page_html = page_html.replace("{{PRICING}}", data["pricing"])
        page_html = page_html.replace("{{DURATION}}", data["duration"])
        page_html = page_html.replace("{{SESSIONS}}", data["sessions"])
        page_html = page_html.replace("{{BENEFITS_CARDS}}", benefits_html.strip())
        page_html = page_html.replace("{{PROCEDURE_CARDS}}", procedure_html.strip())
        page_html = page_html.replace("{{RECOVERY_GUIDELINES}}", data["recovery"])
        page_html = page_html.replace("{{FAQS_ACCORDIONS}}", faqs_html.strip())

        output_path = os.path.join(OUTPUT_DIR, f"{slug}.html")
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(page_html)

        print(f"Generated: {output_path}")

    print("Generation complete! 15 unique SEO pages have been compiled successfully.")

if __name__ == "__main__":
    main()
