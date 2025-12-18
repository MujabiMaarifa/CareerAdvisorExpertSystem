from pyswip import Prolog

class CareerAdvisor:
    def __init__(self, kb_file="main.pl"):
        self.prolog = Prolog()
        self.prolog.consult(kb_file)

    # clear all user facts at once
    def clear_user_facts(self):
        self.prolog.retractall("has_skill(_)") 
        self.prolog.retractall("has_trait(_)") 
        self.prolog.retractall("has_interest(_)") 
        self.prolog.retractall("has_education(_)")

    def set_user_profile(self, skills=[], traits=[], interests=[], education=None):
        self.clear_user_facts()
        for skill in skills:
            self.prolog.assertz(f"has_skill({skill})")
        for trait in traits:
            self.prolog.assertz(f"has_trait({trait})")
        for interest in interests:
            self.prolog.assertz(f"has_interest({interest})")
        if education:
            self.prolog.assertz(f"has_education({education})")


    # Forward chaining: career requires all skills
    def forward_chaining(self):
        qualified = set()
        for res in self.prolog.query("strongly_qualified(Career)"):
            qualified.add(res["Career"])
        for res in self.prolog.query("qualified(Career)"):
            qualified.add(res["Career"])
        return list(qualified)

    # Backward chaining
    def backward_chaining(self, career):
        try:
            result = list(self.prolog.query(f"recommend({career})"))
            return bool(result)
        except Exception as e:
            print(f"Backward chaining error {career}: {e}")
            return False

    # Hybrid
    def hybrid_recommendation(self):
        potential = set()

        query = list(self.prolog.query("strongly_qualified(Career)"))
        for res in query:
            potential.add(res["Career"])
        result = list(self.prolog.query("qualified(Career)"))
        for res in result:
            potential.add(res["Career"])

        final = []
        for career in potential:
            if self.backward_chaining(career):
                final.append(career)
        return final
