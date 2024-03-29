stock_symbols = {
    "AAPL": ["Apple Inc.", "Apple"],
    "MSFT": ["Microsoft Corporation", "Microsoft"],
    "TSLA": ["Tesla, Inc.", "Tesla Motors", "Tesla"],
    "GOOGL": ["Alphabet Inc.", "Google"],
    "AMZN": ["Amazon.com, Inc.", "Amazon"],
    "NVDA": ["NVIDIA Corporation", "NVIDIA", "nVidia"],
    "AMD": ["Advanced Micro Devices, Inc.", "AMD"],
    "INTC": ["Intel Corporation", "Intel"],
    "META": ["Meta Platforms, Inc.", "Meta", "Facebook"],
    "ORCL": ["Oracle Corporation", "Oracle"],
    "PG": ["Procter & Gamble Co.", "Procter & Gamble", "P&G"],
    "KO": ["The Coca-Cola Company", "Coca-Cola", "Coke"],
    "JNJ": ["Johnson & Johnson", "J&J"],
    "PFE": ["Pfizer Inc.", "Pfizer"],
    "JPM": ["JPMorgan Chase & Co.", "JPMorgan", "Chase"],
    "V": ["Visa Inc.", "Visa"],
    "XOM": ["Exxon Mobil Corporation", "ExxonMobil", "Exxon", "Mobil"],
    "NEE": ["NextEra Energy, Inc.", "NextEra Energy", "Florida Power & Light"],
    "MMM": ["3M Company", "3M"],
    "AIR": ["AAR Corp.", "AAR"]
}


stocks_info = {
    "AAPL": {
        "Symbol": "AAPL",
        "Company Name": ["Apple Inc.", "Apple"],
        "Founder": ["Steve Jobs", "Steve Wozniak", "Ronald Wayne"],
        "Important People": ["Tim Cook", "Jonathan Ive", "Phil Schiller", "Craig Federighi", "Eddy Cue"],
        "Important Projects": ["iPhone", "Iphone", "iphone", "MacBook", "Macbook", "macbook", "iPad", "Ipad", "ipad", "Apple Watch", "Apple watch", "apple watch", "iOS", "Ios", "ios", "macOS", "Macos", "macos", "Apple TV", "Apple tv", "apple tv"],
    },
    "MSFT": {
        "Symbol": "MSFT",
        "Company Name": ["Microsoft Corporation", "Microsoft"],
        "Founder": ["Bill Gates", "Paul Allen"],
        "Important People": ["Satya Nadella", "Bill Gates", "Brad Smith", "Panos Panay", "Phil Spencer"],
        "Important Projects": ["Windows", "windows", "Office", "office", "Azure", "azure", "Xbox", "xbox", "Surface", "surface", "LinkedIn", "linkedin", "GitHub", "github", "Minecraft", "minecraft", "Teams", "teams", "Edge", "edge"],
    },
    "TSLA": {
        "Symbol": "TSLA",
        "Company Name": ["Tesla, Inc.", "Tesla Motors", "Tesla"],
        "Founder": ["Elon Musk", "JB Straubel", "Ian Wright", "Marc Tarpenning", "Martin Eberhard"],
        "Important People": ["Elon Musk", "JB Straubel", "Franz von Holzhausen", "Drew Baglino"],
        "Important Projects": ["Model S", "Model s", "model s", "Model 3", "Model 3", "model 3", "Model X", "Model x", "model x", "Model Y", "Model y", "model y", "Cybertruck", "cybertruck", "Roadster", "roadster", "Semi", "semi", "Autopilot", "autopilot", "Gigafactory", "gigafactory", "Solar Roof", "solar roof", "Powerwall", "powerwall"],
    },
    "GOOGL": {
        "Symbol": "GOOGL",
        "Company Name": ["Alphabet Inc.", "Google"],
        "Founder": ["Larry Page", "Sergey Brin"],
        "Important People": ["Sundar Pichai", "Larry Page", "Sergey Brin", "Ruth Porat", "John Hennessy"],
        "Important Projects": ["Google Search", "Google search", "google search", "Android", "android", "YouTube", "youtube", "Google Cloud", "Google cloud", "google cloud", "Waymo", "waymo", "Google Maps", "Google maps", "google maps", "Pixel", "pixel", "Google Assistant", "Google assistant", "google assistant", "DeepMind", "deepmind"],
    },
    "AMZN": {
        "Symbol": "AMZN",
        "Company Name": ["Amazon.com, Inc.", "Amazon"],
        "Founder": ["Jeff Bezos"],
        "Important People": ["Andy Jassy", "Jeff Bezos", "Werner Vogels"],
        "Important Projects": ["Amazon Web Services", "Amazon web services", "amazon web services", "AWS", "aws", "Kindle", "kindle", "Echo", "echo", "Alexa", "alexa", "Amazon Prime", "Amazon prime", "amazon prime", "Fire Tablet", "Fire tablet", "fire tablet", "Fire TV", "Fire tv", "fire tv", "Amazon Fresh", "Amazon fresh", "amazon fresh", "Amazon Music", "Amazon music", "amazon music"],
    },
    "NVDA": {
        "Symbol": "NVDA",
        "Company Name": ["NVIDIA Corporation", "NVIDIA", "nVidia"],
        "Founder": ["Jensen Huang", "Chris Malachowsky", "Curtis Priem"],
        "Important People": ["Jensen Huang", "Colette Kress", "Tim Teter"],
        "Important Projects": ["GeForce", "geforce", "GeForce GTX", "GeForce RTX", "CUDA", "cuda", "Tegra", "tegra", "Shield", "shield", "NVIDIA AI", "nvidia ai", "Deep Learning", "deep learning", "DLSS", "dlss", "Ray Tracing", "ray tracing"],
        },
    "AMD": {
        "Symbol": "AMD",
        "Company Name": ["Advanced Micro Devices, Inc.", "AMD"],
        "Founder": ["Jerry Sanders"],
        "Important People": ["Lisa Su", "Mark Papermaster", "Rick Bergman", "Devinder Kumar"],
        "Important Projects": ["Ryzen", "ryzen", "RYZEN", "Epyc", "epyc", "EPYC", "Radeon", "radeon", "RADEON", "Threadripper", "threadripper", "THREADRIPPER", "Zen", "zen", "ZEN", "Radeon Instinct", "radeon instinct", "Navi", "navi", "NAVI", "RDNA", "rdna", "RDNA2", "rdna2"],
    },
    "INTC": {
        "Symbol": "INTC",
        "Company Name": ["Intel Corporation", "Intel"],
        "Founder": ["Robert Noyce", "Gordon Moore"],
        "Important People": ["Pat Gelsinger", "Robert Swan", "George Davis", "Sandra Rivera", "Raja Koduri"],
        "Important Projects": ["Core", "core", "Xeon", "xeon", "XEON", "Pentium", "pentium", "PENTIUM", "Atom", "atom", "ATOM", "Itanium", "itanium", "ITANIUM", "Optane", "optane", "OPTANE", "Iris", "iris", "IRIS", "Thunderbolt", "thunderbolt", "THUNDERBOLT", "FPGA", "fpga", "Arc", "arc", "ARC"],
    },
    "META": {
        "Symbol": "META",
        "Company Name": ["Meta Platforms, Inc.", "Meta", "Facebook"],
        "Founder": ["Mark Zuckerberg"],
        "Important People": ["Mark Zuckerberg", "Sheryl Sandberg", "Mike Schroepfer"],
        "Important Projects": ["Facebook", "facebook", "FACEBOOK", "Instagram", "instagram", "INSTAGRAM", "WhatsApp", "whatsapp", "WHATSAPP", "Oculus", "oculus", "OCULUS", "Portal", "portal", "PORTAL", "Novi", "novi", "NOVI", "Libra", "libra", "LIBRA", "Messenger", "messenger", "MESSENGER"],
    },
    "ORCL": {
        "Symbol": "ORCL",
        "Company Name": ["Oracle Corporation", "Oracle"],
        "Founder": ["Larry Ellison", "Bob Miner", "Ed Oates"],
        "Important People": ["Larry Ellison", "Safra Catz", "Mark Hurd"],
        "Important Projects": ["Oracle Database", "oracle database", "Oracle Cloud", "oracle cloud", "Java", "java", "MySQL", "mysql", "PeopleSoft", "peoplesoft", "Siebel", "siebel", "JD Edwards", "jd edwards", "Fusion Middleware", "fusion middleware", "Oracle E-Business Suite", "oracle e-business suite", "NetSuite", "netsuite"],
    },
    "PG": {
        "Symbol": "PG",
        "Company Name": ["Procter & Gamble Co.", "Procter & Gamble", "P&G"],
        "Founder": ["William Procter", "James Gamble"],
        "Important People": ["David S. Taylor", "Jon R. Moeller", "R. Alexandra Keith"],
        "Important Projects": ["Tide", "tide", "Pampers", "pampers", "Gillette", "gillette", "Oral-B", "oral-b", "Bounty", "bounty", "Charmin", "charmin", "Pantene", "pantene", "Head & Shoulders", "head & shoulders", "Olay", "olay", "Always", "always", "Febreze", "febreze", "Crest", "crest", "Dawn", "dawn"],
    },
    "KO": {
        "Symbol": "KO",
        "Company Name": ["The Coca-Cola Company", "Coca-Cola", "Coke"],
        "Founder": ["Asa Griggs Candler"],
        "Important People": ["James Quincey", "Brian Smith", "John Murphy"],
        "Important Projects": ["Coca-Cola", "coca-cola", "Coke", "coke", "Diet Coke", "diet coke", "Coca-Cola Zero Sugar", "coca-cola zero sugar", "Fanta", "fanta", "Sprite", "sprite", "Dasani", "dasani", "Smartwater", "smartwater", "Minute Maid", "minute maid", "Simply Orange", "simply orange", "Powerade", "powerade"],
    },
    "JNJ": {
        "Symbol": "JNJ",
        "Company Name": ["Johnson & Johnson", "J&J"],
        "Founder": ["Robert Wood Johnson I", "James Wood Johnson", "Edward Mead Johnson"],
        "Important People": ["Alex Gorsky", "Joaquin Duato"],
        "Important Projects": ["Tylenol", "tylenol", "Band-Aid", "band-aid", "Neutrogena", "neutrogena", "Johnson's Baby", "johnson's baby", "Listerine", "listerine", "Aveeno", "aveeno", "Acuvue", "acuvue", "Janssen Pharmaceuticals", "janssen pharmaceuticals", "DePuy Synthes", "depuy synthes", "Ethicon", "ethicon"],
    },
    "PFE": {
        "Symbol": "PFE",
        "Company Name": ["Pfizer Inc.", "Pfizer"],
        "Founder": ["Charles Pfizer", "Charles F. Erhart"],
        "Important People": ["Albert Bourla", "Mikael Dolsten", "Angela Hwang"],
        "Important Projects": ["Viagra", "viagra", "Lyrica", "lyrica", "Prevnar", "prevnar", "Xeljanz", "xeljanz", "Ibrance", "ibrance", "Eliquis", "eliquis", "Comirnaty", "comirnaty", "COVID-19 Vaccine", "covid-19 vaccine", "BNT162b2", "bnt162b2", "Zoloft", "zoloft", "Lipitor", "lipitor"],
    },
    "JPM": {
        "Symbol": "JPM",
        "Company Name": ["JPMorgan Chase & Co.", "JPMorgan", "Chase"],
        "Founder": ["J. P. Morgan"],
        "Important People": ["Jamie Dimon", "Daniel Pinto", "Marianne Lake"],
        "Important Projects": ["Chase Bank", "chase bank", "J.P. Morgan Asset Management", "j.p. morgan asset management", "JPMorgan Wealth Management", "jpmorgan wealth management", "Chase Mobile", "chase mobile", "J.P. Morgan Securities", "j.p. morgan securities", "Chase Paymentech", "chase paymentech"],
    },
    "V": {
        "Symbol": "V",
        "Company Name": ["Visa Inc.", "Visa"],
        "Founder": ["Dee Hock"],
        "Important People": ["Al Kelly", "Ryan McInerney"],
        "Important Projects": ["Visa Credit Cards", "visa credit cards", "Visa Debit Cards", "visa debit cards", "Visa Payment System", "visa payment system", "VisaNet", "visanet"],
    },
    "XOM": {
        "Symbol": "XOM",
        "Company Name": ["Exxon Mobil Corporation", "ExxonMobil", "Exxon", "Mobil"],
        "Founder": ["John D. Rockefeller"],
        "Important People": ["Darren Woods", "Andrew P. Swiger", "Neil A. Chapman"],
        "Important Projects": ["Exxon", "exxon", "Mobil", "mobil", "Esso", "esso", "XTO Energy", "xto energy", "Imperial Oil", "imperial oil", "Synergy Fuel Technology", "synergy fuel technology"],
    },
    "NEE": {
        "Symbol": "NEE",
        "Company Name": ["NextEra Energy, Inc.", "NextEra Energy", "Florida Power & Light"],
        "Founder": ["N/A"],
        "Important People": ["James L. Robo", "Rebecca Kujawa", "John Ketchum"],
        "Important Projects": ["Wind Energy", "wind energy", "Solar Energy", "solar energy", "Nuclear Energy", "nuclear energy"],
    },
    "MMM": {
        "Symbol": "MMM",
        "Company Name": ["3M Company", "3M"],
        "Founder": ["Henry S. Bryan", "Hermon W. Cable", "John Dwan", "William A. McGonagle"],
        "Important People": ["Mike Roman", "Hak Cheol Shin"],
        "Important Projects": ["Post-it Notes", "post-it notes", "Scotch Tape", "scotch tape", "Command", "command", "Filtrete", "filtrete", "Nexcare", "nexcare", "Littmann", "littmann"],
    },
    "AIR": {
        "Symbol": "AIR",
        "Company Name": ["AAR Corp.", "AAR"],
        "Founder": ["Ira A. Eichner"],
        "Important People": ["John M. Holmes", "Sean Gillen"],
        "Important Projects": ["Aviation Services", "aviation services", "MRO Services", "mro services", "Parts Supply", "parts supply", "Logistics", "logistics"],
    }
}