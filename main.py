from pyswip import Prolog

class CareerAdvisor:
    #class constructor to initialize user object
    def __init__(self, kb_file="main.pl"):
        self.prolog = Prolog()
        self.prolog.consult(kb_file)

    #clear the user skills to avoid conflicts 
     def clear_user_facts(self):
        self.prolog.retractall("has_skill(_)") 
        self.prolog.retractall("has_trait(_)") 
        self.prolog.retractall("has_interest(_)") 
        self.prolog.retractall("has_education(_)")

    #set user's profile
    
    def set_user_skills(self, skills):
        self.clear_user_facts()
        for skill in skills:
            self.prolog.assertz(f"has_skill({skill})")

    def set_user_traits(self, traits):
        self.clear_user_facts()
        for trait in traits:
            self.prolog.assertz(f"has_trait({trait})")

    def set_user_interests(self, interests):
        self.clear_user_facts()
        for interest in interests:
            self.prolog.assertz(f"has_interest({interest})")

    def set_user_education(self, education):
        self.clear_user_facts()
        self.prolog.assertz(f"has_education({education})")

    #function to apply forward chaining 
    def forward_chaining(self):
        qualified = set()
        for res in self.prolog.query("requires(Career, Skill), has_skill(Skill)"):
            qualified.add(res["Career"])
        return list(qualified)

    #function to apply backward chaining
    def backward_chaining(self, career):
        try:
            query = f"recommend({career})"
            result = list(self.prolog.query(query))
            return bool(result)
        except Exception as e:
            print(f"Backward chaining error {career}: {e}")

    # hybrid implementation
    def hybrid_recommendation(self):
        potential = self.forward_chaining()
        final_recommend = []
        for career in potential:
            if self.backward_chaining(career):
                final_recommend.append(career)
        return final_recommend

