# Open roles shown on the Scout jobs site.
# To add a role: add a dict to ROLES. To close a role: delete it (or set "active": False).
# Then run: python3 _build/build.py

CAL = "https://calendar.app.google/RUinGAqwi7AAYC8A8"

GETCRUX_ABOUT = {
    "lead": "GetCrux is an AI creative strategist for performance marketers.",
    "paras": [
        "Ad creative is now the biggest lever on ad platforms, but most teams can't tell why an ad works, so they guess and copy their last winner. GetCrux finds the winning patterns across 100+ parameters, like hooks, messaging, storyline, music and pacing, and recommends exactly what to launch next.",
        "It's backed by Y Combinator and used by growth and creative teams at Fortune 1000 companies, fast-growing YC startups, and consumer apps across the US.",
    ],
}

ROLES = [
    {
        "slug": "getcrux-founding-ae",
        "active": True,
        "title": "Founding Account Executive",
        "company": "GetCrux",
        "location": "Remote (US)",
        "tag": "Founding AE",
        "card_comp": "$240K - $320K OTE",
        "card_blurb": "YC-backed AI creative strategist for performance marketers. 3X growth in 3 months, and inbound is outpacing the founders.",
        "facts": [
            ("OTE", "$240K - $320K", "50/50 split, 3-month ramp"),
            ("Base", "$120K - $160K", "plus 0.1% - 0.25% equity"),
            ("Experience", "3 - 10 years", "mid-market or enterprise AE"),
            ("Stage", "YC-backed seed", "$2.6M+ raised"),
        ],
        "callout": ("Pipeline is already there.", "GetCrux grew 3X in 3 months, and inbound is bringing in more leads than the founders can manage."),
        "about_title": "About GetCrux",
        "about": GETCRUX_ABOUT,
        "opportunity": {
            "lead": "Help GetCrux close faster and get to $10M ARR next year.",
            "paras": ["You'd work directly with the co-founders to run deals end to end, sharpen the ICP and positioning, and turn a strong top of funnel into revenue."],
        },
        "own": [
            ("The full funnel.", "Discovery, demo, team alignment, pilot, and conversion."),
            ("Sourcing.", "Find new opportunities through creative targeting, account-based marketing, events, and conferences."),
            ("Enterprise deals.", "Multi-thread larger deals alongside the founders."),
            ("Pilots.", "Partner with customer success and engineering to make pilots land."),
            ("Upsell.", "Spot expansion opportunities across the existing customer base."),
            ("ICP and positioning.", "Shape who GetCrux sells to and how, with the founders and GTM team."),
        ],
        "must": [
            "3 - 10 years as a mid-market or enterprise AE at a seed to Series C startup",
            "Full-cycle closing, including pipeline you sourced yourself",
            "US work authorization (no visa sponsorship)",
        ],
        "bonus": [
            "You've been a founding AE before",
            "You've sold martech, adtech, or marketing intelligence to growth or performance marketers or e-commerce buyers",
        ],
        "steps": [
            ("Intro chat", "With Atharva, co-founder"),
            ("Deep dive", "With Atharva"),
            ("Founder deep dive", "With both co-founders"),
            ("In-person meeting", "With the co-founders"),
        ],
    },
    {
        "slug": "getcrux-founding-csm",
        "active": True,
        "title": "Founding Customer Success Manager",
        "company": "GetCrux",
        "location": "Remote (US)",
        "tag": "Founding CSM",
        "card_comp": "$125K - $175K base + equity",
        "card_blurb": "Take over customer success from the founders and build it from scratch, with a portfolio including Rocket Money, Wise, SoFi and Noom.",
        "facts": [
            ("Base", "$125K - $175K", "plus competitive equity"),
            ("Experience", "4+ years", "customer success or account management"),
            ("Portfolio", "Rocket Money, Wise, SoFi", "and several Fortune 1000s"),
            ("Stage", "YC-backed seed", "$2.6M+ raised"),
        ],
        "callout": ("Momentum.", "GetCrux 3X'd revenue in 3 months and is on its way to $10M ARR next year."),
        "about_title": "About GetCrux",
        "about": GETCRUX_ABOUT,
        "opportunity": {
            "lead": "Be GetCrux's first CSM, taking over from the founders and building the function from scratch.",
            "paras": ["You'd manage a portfolio of some of the fastest-growing teams around, including Rocket Money, Wise, SoFi, Noom, Remitly, Rappi, GenDigital and SanDisk, plus several Fortune 1000 companies."],
        },
        "own": [
            ("Retention.", "Help customers hit their growth and creative KPIs: surface creative insights, build testing plans, research new concepts, and generate AI creatives."),
            ("Onboarding.", "Work with the GTM and product teams to understand new customers' goals and set up the right workflows."),
            ("Expansion.", "Find ways to deepen each account and work with the AEs to close expansion deals."),
            ("The customer's voice.", "Track usage and issues, stay on top of ad platform best practices and AI developments, and help shape the roadmap."),
            ("Presence.", "Help build GetCrux's name through content, events, dinners, and product launches."),
        ],
        "must": [
            "4+ years in customer success or account management at martech, adtech, or e-commerce startups or agencies",
            "Mid-market or enterprise CSM experience in martech, adtech, marketing, or adjacent spaces like e-commerce and social",
            "A track record owning onboarding, retention, and expansion against NRR/GRR targets",
            "You speak marketers' language with growth and creative teams",
            "US work authorization (no visa sponsorship)",
        ],
        "bonus": [
            "You've been a founding CSM or built the function from scratch at a seed to Series C startup",
            "Agency background, or you've worked as a growth marketer or creative strategist",
        ],
        "steps": [
            ("Intro chat", "With Atharva, co-founder (15 min)"),
            ("Role assessment", "Build a weekly or monthly ad-performance report for a customer in GetCrux (45 - 60 min)"),
            ("CEO chat", "With Himank, co-founder and CEO (15 min)"),
            ("In-person meeting", "With the co-founders (30 - 60 min)"),
        ],
    },
    {
        "slug": "turtles-head-of-customer-support",
        "active": True,
        "title": "Head of Customer Support",
        "company": "Turtles",
        "location": "Remote (US or Canada)",
        "tag": "Leadership",
        "card_comp": "$130K - $170K base + bonus",
        "card_blurb": "Scale a world-class, friendly support team from 20 to 50+ at a profitable AI marketplace platform growing 4x a year.",
        "facts": [
            ("Base", "$130K - $170K", "plus a meaningful annual bonus"),
            ("Team", "20 today", "expected to more than double next year"),
            ("Experience", "4+ years", "including leading a support team"),
            ("Company", "Profitable", "9-figure revenue pace"),
        ],
        "callout": ("Growing fast.", "Turtles has grown 4x+ in the last year, is profitable, and believes it can do it again."),
        "about_title": "About Turtles",
        "about": {
            "lead": "Turtles is the AI platform for marketplaces.",
            "paras": [
                "The world's fastest-growing marketplaces run on Turtles, helping 30M+ US shoppers discover products they love across curated, passion-driven communities. Turtles also helps brands like Nike, LEGO, and Jimmy Choo find millions of new fans.",
                "It's a team of about 65 across New York (SoHo), Helsinki, and Hong Kong. People who like solving hard problems quickly, with lots of autonomy, do well here.",
            ],
        },
        "opportunity": {
            "lead": "Scale a world-class support team from 20 people to 50+, without losing what makes it great.",
            "paras": [
                "Turtles takes pride in friendly, high-quality support and wants to keep that culture as the team more than doubles, not turn into a call center. AI and automation are part of the plan, with the goal of better service faster, not just cutting costs or deflecting customers.",
            ],
        },
        "own": [
            ("Scaling the team.", "Hire and grow the team, and build a layer of team leads and managers."),
            ("Culture and quality.", "Keep support friendly and world-class as volume grows."),
            ("AI and automation.", "Roll out and improve tools like Intercom Fin to serve customers better and faster."),
            ("Performance.", "Own SLAs, response times, and CSAT. Your bonus is tied to them."),
        ],
        "must": [
            "You've led and scaled a support operation through rapid growth, for example from 10 - 20 people to 50",
            "4+ years in customer support or operations, including time as a manager or head of support",
            "Experience in B2C, direct-to-consumer, or e-commerce",
            "You've hired or promoted team leads or managers",
            "Work authorization without visa sponsorship",
        ],
        "bonus": [
            "A background in general operations leadership",
            "You've rolled out AI or automation in a support team (Intercom Fin, Zendesk AI, Ada)",
        ],
        "steps": [
            ("Intro call", "Culture and values (30 min)"),
            ("Hiring manager interview", "Experience and role expectations (45 min)"),
            ("Role assessment", "Skills and judgment for the role (2 hours)"),
            ("Final round", "Meet with leadership (1 hour)"),
        ],
    },
    {
        "slug": "mending-delivery-client-success",
        "active": True,
        "title": "Delivery and Client Success Expert",
        "company": "Mending",
        "location": "New York, hybrid",
        "tag": "Senior IC or team lead",
        "card_comp": "$115K - $160K base + equity",
        "card_blurb": "Part commercial, part implementation: grow and launch accounts for a startup bringing direct primary care to employers.",
        "facts": [
            ("Base", "$115K - $160K", "plus competitive equity"),
            ("OTE", "Coming Q1 2027", "and you'll help set it"),
            ("Experience", "6+ years", "customer success or account management"),
            ("The mix", "60 / 40", "commercial / implementation"),
        ],
        "callout": ("Shape the role.", "Mending is open to a senior IC or a team lead, and will scope management to your experience: IC to start, or leading the existing team on day one."),
        "about_title": "About Mending",
        "about": {
            "lead": "Mending builds the technology and infrastructure behind Direct Primary Care (DPC).",
            "paras": [
                "Mending helps employers, health plans, TPAs, brokers, and DPC practices work together at scale. Its data platform brings DPC into health plans to lower costs, improve access, and deliver better outcomes, and its Mending Access program lets employees of participating employers start seeing a DPC provider.",
                "The team is a mix of healthcare nerds, engineers, designers, DPC doctors, and health tech operators, based in New York.",
            ],
        },
        "opportunity": {
            "lead": "Implement and grow Mending's signed accounts.",
            "paras": [
                "About 60% of the role is commercial: each signed TPA brings dozens of employer groups to sell into, so you'll build relationships with benefits teams, account managers, and brokers to land new employers and get their employees using Mending Access.",
                "The other 40% is implementation, from a simple data feed with weekly check-ins to launches with governance and compliance teams. You could pitch a 1,000-person employer in the morning and run a 25-person implementation call in the afternoon.",
            ],
        },
        "own": [
            ("Land and expand.", "Work with brokers, benefits consultants, TPA account managers, and health plan administrators to bring in new employer groups and grow member adoption."),
            ("Key relationships.", "Own renewals and Mending's most important client relationships."),
            ("Implementations.", "Run launches end to end for health plan and TPA partners, as their first non-sales point of contact."),
            ("Reporting.", "Run business reviews and own reporting with existing partners."),
            ("How client success runs.", "Keep building the function alongside sales, network, engineering, and data teams."),
        ],
        "must": [
            "6+ years in customer success or account management, ideally in health tech",
            "You've owned onboarding and implementation end to end as an AM or CSM where product use drove revenue",
            "Experience with land-and-expand through channels or partners, like TPAs and brokers",
            "You build client reporting and make the value case to client executives",
            "US work authorization (no visa sponsorship)",
        ],
        "bonus": [
            "Early-stage (seed to Series A) experience, or health tech, especially employee benefits",
            "You've built CS processes from scratch (HubSpot, playbooks) or managed a CS team",
        ],
        "steps": [
            ("Hiring manager interview", "With Bin, Head of Ops (30 min)"),
            ("Co-founder interview", "With Jeff, co-founder (30 min)"),
            ("Live case", "Commercial problem solving and implementation (45 min)"),
            ("Values interview", "How you work and what you value (30 min)"),
        ],
    },
    {
        "slug": "dealops-founding-ae",
        "active": True,
        "title": "Founding Account Executive",
        "company": "Dealops",
        "location": "San Francisco, in person",
        "tag": "First GTM hire",
        "card_comp": "$250K - $280K OTE",
        "card_blurb": "Be the first GTM hire, own the full sales cycle, and build the playbook with the CEO.",
        "facts": [
            ("OTE", "$250K - $280K", "50/50 split"),
            ("Base", "$125K - $140K", "plus competitive equity"),
            ("Experience", "3 - 5 years", "quota-carrying AE"),
            ("Visa", "Transfers OK", "e.g. OPT, H-1B transfer"),
        ],
        "callout": ("Moving fast.", "The CEO is running a hiring sprint and aims to make an offer soon."),
        "about_title": None,
        "about": None,
        "opportunity": {
            "lead": "You'd be Dealops' first GTM hire, owning the full sales cycle and working directly with the CEO to define how the company sells.",
            "paras": ["That means shaping the ICP, messaging, outbound strategy, qualification, and how deals get run and won. This isn't a \"follow the playbook\" role. You build the playbook."],
        },
        "own": [
            ("Full-cycle sales.", "Source, qualify, run discovery, solution, negotiate, and close."),
            ("Pipeline.", "Build target lists, run outbound experiments, and iterate on messaging every week."),
            ("Complex buying committees.", "Win over RevOps, Finance, Sales leadership, and Legal/Security."),
            ("The GTM machine.", "Talk track, qualification criteria, deal process, tooling, and handoffs."),
            ("Product partnership.", "Feed market insight into the roadmap and help turn pilots into repeatable wins."),
        ],
        "must": [
            "3 - 5 years as a quota-carrying AE at a fast-growing, VC-backed B2B SaaS or AI startup",
            "Strong quota attainment and full-cycle closing of complex deals",
            "Mid-market or enterprise deals closed at $50K - $100K+ ACV",
            "Solid fundamentals: MEDDPICC or similar, mutual account plans, multithreading, working champions vs. buyers",
        ],
        "bonus": [
            "150%+ quota attainment, or you've been a founding AE before",
            "You've sold billing, CPQ, ERP, invoicing, or contract/legal tech to finance and RevOps leaders",
        ],
        "steps": [
            ("Hiring manager call", "30 minutes"),
            ("Take-home and review", "30 minutes"),
            ("Onsite", "2 - 3 hours. Walk through your account strategy and prospecting plan."),
        ],
    },
]
