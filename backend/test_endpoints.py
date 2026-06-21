import os
import sys
import asyncio

# Ensure backend folder is in path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from main import read_properties, evaluate_properties, StudentProfile, PropertyItem

async def test_direct_functions():
    print("Testing read_properties directly...")
    props = await read_properties("Ramat Gan")
    print(f"Number of properties returned: {len(props)}")
    for p in props:
        print(f" - ID {p['id']}: {p['title']} in {p['city']}, Rent: {p['rent']} (Source: {p.get('source')})")
        
    print("\nTesting evaluate_properties directly...")
    profile = StudentProfile(
        budget=20000.0,
        income=20000.0,
        city="Ramat Gan",
        zone="Zone A"
    )
    
    # Convert list of dicts to list of PropertyItem objects
    prop_items = []
    for p in props:
        prop_items.append(PropertyItem(**p))
        
    eval_results = evaluate_properties(profile, prop_items)
    print(f"Number of evaluated results: {len(eval_results)}")
    for res in eval_results:
        print(f" - {res['title']}: Total Burn: {res['total_burn']}, Is Safe: {res['is_safe']}")

if __name__ == "__main__":
    asyncio.run(test_direct_functions())
