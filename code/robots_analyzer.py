import pandas as pd
from tqdm import tqdm
from datetime import date


def main():
    input_file = "data/june_2025/robots_txt_2025-06-19_agents.csv"
    output_file = "data/june_2025/disallowed_bots.csv"

    robots_texts = pd.read_csv(input_file)

    results = []
    today = str(date.today())

    for _, row in tqdm(robots_texts.iterrows(), total=len(robots_texts)):
        website = row['Website']
        robots_text = row['robots']

        # Skip if robots_text is not a string
        if not isinstance(robots_text, str):
            continue
        
        bots = []
        lines = robots_text.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            if line.startswith('User-agent:'):
                bot = line.split('User-agent:')[1].strip()
                # Check next line for Disallow: /
                if i+1 < len(lines) and lines[i+1].strip() == 'Disallow: /':
                    bots.append(bot)
        
        if bots:  # Only add rows with found bots
            for bot in bots:
                results.append({
                    'Date': today,
                    'Website': website,
                    'Disallowed Bot': bot
                })
    
    # Create and save DataFrame
    df = pd.DataFrame(results)
    df.to_csv(output_file, index=False)
    print(f"Saved results to {output_file}")

if __name__ == "__main__":
    main()