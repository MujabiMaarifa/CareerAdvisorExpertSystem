from pyswip import Prolog

class CareerAdvisor:
    #class constructor to initialize user object
    def __init__(self, kb_file="main.pl"):
        self.prolog = Prolog()
        self.prolog.consult(kb_file)

    #set user's profile
    
    def set_user_skills(self, skills):
        for skill in skills:
            self.prolog.assertz(f"has_skill({skill})")

    def set_user_traits(self, traits):
        for trait in traits:
            self.prolog.assertz(f"has_trait({trait})")

    def set_user_interests(self, interests):
        for interest in interests:
            self.prolog.assertz(f"has_interest({interest})")

    def set_user_education(self, education):
        self.prolog.assertz(f"has_education({education})")

    #function to apply forward chaining 
    def forward_chaining(self):
        qualified = set()
        for res in self.prolog.query("requires(Career, Skill), has_skill(Skill)"):
            qualified.add(res["Career"])
        return list(qualified)

    #function to apply backward chaining
    def backward_chaining(self, career):
        query = f"recommend({career})"
        result = list(self.prolog.query(query))
        return bool(result)

    # ---------- Hybrid recommendation ----------
    def hybrid_recommendation(self):
        potential = self.forward_chaining()
        final_recommend = []
        for career in potential:
            if self.backward_chaining(career):
                final_recommend.append(career)
        return final_recommend

