import periodictable

class ChemistryEngine:
    def __init__(self):
        print("🧪 Level 5 Chemistry Engine Active!")
    def analyze_molecule(self, formula_text):
        try:
            molecule = periodictable.formula(formula_text)
            total_mass = molecule.mass

            print(f"\n=====================================")
            print(f"🔬 ANALYSIS FOR: {formula_text}")
            print(f"=====================================")
            print(f"Total Molar Mass: {total_mass:.3f} g/mol\n")
            print("Element Breakdown:")
            for element, count in molecule.atoms.items():
                element_total_mass = element.mass * count
                mass_percentage = (element_total_mass / total_mass) * 100
                print(f"🔹 {element.name:<10} ({element.symbol}): Count = {count:<3} | "
                      f"Mass % = {mass_percentage:.2f}%")
            print(f"=====================================")
        except Exception as e:
            print(f"Error analyzing molecule '{formula_text}': {e}")

engine = ChemistryEngine()

while True:
    user_input = input("\nEnter a formula (e.g., H20, NaCl, C6H12O6) or 'quit': ").strip()
    if user_input.lower() == 'quit':
        print("Engine shutting down. Arriverderci! 👋")
        break
    if not user_input:
        print("Please enter a valid chemical formula.")
        continue
    engine.analyze_molecule(user_input)
