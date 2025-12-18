/*Domain facts*/

/* ---- Careers ---- */
%career(_)

career(software_engineer).
career(data_scientist).
career(network_engineer).
career(cybersecurity_analyst).
career(ai_engineer).
career(web_developer).
career(database_administrator).
career(nurse).
career(doctor).
career(lawyer).
career(architect).
career(teacher).

/* ---- Skills ---- */
%skill(user_skill)

skill(programming).
skill(problem_solving).
skill(mathematics).
skill(networking).
skill(statistics).
skill(machine_learning).
skill(web_design).
skill(database_management).
skill(system_security).
skill(communication).
skill(teaching_explaining).
skill(critical_thinking).
skill(drawing).
skill(medical_knowledge).


/* ---- Interests ---- */
%interest(user_interest)

interest(technology).
interest(data_analysis).
interest(research).
interest(design).
interest(networks).
interest(security).
interest(teaching).
interest(house_planning).
interest(patient_care).

/* ---- Personality Traits ---- */
%trait(personal_trait)

trait(analytical).
trait(logical).
trait(creative).
trait(detail_oriented).
trait(curious).
trait(caring).
trait(teaching).

/* ---- Education ---- */
%education(education_level)

education_level(diploma).
education_level(bachelors).
education_level(masters).
education_level(phd).

/* ---- Career Requirements ---- */
%career_requires(career, skill/interest)

requires(software_engineer, programming).
requires(software_engineer, problem_solving).

requires(data_scientist, statistics).
requires(data_scientist, programming).

requires(network_engineer, networking).

requires(cybersecurity_analyst, system_security).

requires(ai_engineer, machine_learning).
requires(ai_engineer, mathematics).

requires(web_developer, web_design).

requires(database_administrator, database_management).

requires(nurse, patient_care).
requires(nurse, communication).
requires(nurse, medical_knowledge).

requires(architect, mathematics).
requires(architect, drawing).
requires(architect, house_planning).

requires(teacher, communication).
requires(teacher, critical_thinking).
requires(teacher, logical).
requires(teacher, teaching_explaining).

%dynamicUserFacts
:- dynamic has_skill/1.
:- dynamic has_interest/1.
:- dynamic has_trait/1.
:- dynamic has_education/1.

%inferenceRules
/* User qualifies for a skill-based career */
qualified(Career) :-
    requires(Career, Skill),
    has_skill(Skill).

/*  Strong qualification (multiple skills) */
strongly_qualified(Career) :-
    requires(Career, Skill1),
    requires(Career, Skill2),
    Skill1 \= Skill2, %uniqueskills
    has_skill(Skill1),
    has_skill(Skill2).

/* interestbasedsuitability */
interested_in(Career) :-
    career(Career),
    requires(Career, Skill),
    skill_interest_match(Skill, Interest),
    has_interest(Interest).

/* trait based suitability*/
personality_fit(Career) :-
    career(Career),
    career_trait(Career, Trait),
    has_trait(Trait).

/* education based filtering */
education_fit(Career) :-
    has_education(bachelors),
    career(Career).

/* final recommendation rule */
recommend(Career) :-
    strongly_qualified(Career),
    interested_in(Career),
    personality_fit(Career),
    education_fit(Career).


/* ---- Skill to Interest Mapping ---- */
skill_interest_match(programming, technology).
skill_interest_match(statistics, data_analysis).
skill_interest_match(machine_learning, research).
skill_interest_match(networking, networks).
skill_interest_match(system_security, security).
skill_interest_match(web_design, design).
skill_interest_match(database_management, data_analysis).
skill_interest_match(medical_knowledge, patient_care).
skill_interest_match(drawing, house_planning).
skill_interest_match(teaching_explaining, teaching).

/* ---- Career to Trait Mapping ---- */
career_trait(software_engineer, logical).
career_trait(data_scientist, analytical).
career_trait(data_scientist, curious).
career_trait(ai_engineer, analytical).
career_trait(network_engineer, detail_oriented).
career_trait(cybersecurity_analyst, detail_oriented).
career_trait(web_developer, creative).
career_trait(database_administrator, logical).
career_trait(nurse, caring).
career_trait(teacher, teaching).

/* automatically assign rules */
%trigger rule1 qualified(Career)
infer_qualified :-
    qualified(C),
    \+ inferred_qualified(C),
    assertz(inferred_qualified(C)).

:- dynamic inferred_qualified/1.

/* priority assigning->requires(C)- is assigned priority if the rules might be triggered at the same time */
score(Career, Score) :- 
    findall(1, (requires(Career, S), has_skill(S)), SkillScore),
    length(SkillScore, SkillCount),

    findall(1, (career_trait(Career, T), has_trait(T)), TraitScore),
    length(TraitScore, TraitCount),

    Score is SkillCount * 2 + TraitCount.

/* Select best career */
best_career(Career) :-
    career(Career),
    score(Career, Score),
    \+ (career(Other),
        score(Other, OtherScore),
        OtherScore > Score).

