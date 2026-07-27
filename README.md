# CS2 Player Trust Score Tool

A web application where a user pastes a Steam profile URL and receives a trust score for that CS2 player. The score tells you whether a player is trustworthy or suspicious based on publicly available Steam data. The output is a simple Green (trustworthy), Yellow (suspicious), or Red (high risk) score with clear reasoning.

# What the tool analyzes

- VAC ban history

- Hours played vs account age

- Inventory value vs account age
 
- Friends network
 
- Playtime patterns

# How it works

User pastes a Steam profile URL → app extracts the Steam ID → calls Steam Web API → analyzes the data → displays trust score with breakdown of why it scored that way.

# Design Decisions

1. Why "Hours vs Rank" became "Hours vs Account age." Steam's Web API doesn't expose CS2 rank data through any public endpoint. Changed to hours played ÷ days since account creation, which on its own does not distinguish a legitimate heavy player from a farmed account, making it a single contributor among several others rather than a direct red flag.

2. Why missing data is excluded, not guessed. If data can't be retrieved (private profile, rate limit, failed request), it's left out of the weighted score entirely and listed in the detailed breakdown.

# Setup Instructions 

(*To be completed*)

# Known Limitations

- Uses **public data only**, which does not provide a definitive verdict on any player, and should be read as a set of indicators, not proof of wrongdoing.

- The hours vs account-age signal cannot guarantee a way to distinguish a legitimate hardcore player from a farmed or boosted account on its own.

- Friends network analysis only works if the friend list itself is public.
