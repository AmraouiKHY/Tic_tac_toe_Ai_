% Symptoms for different medical conditions

symptom(flu, fever).
symptom(flu, headache).
symptom(flu, sore_throat).
symptom(flu, cough).
symptom(flu, fatigue).

symptom(cold, sore_throat).
symptom(cold, cough).
symptom(cold, runny_nose).
symptom(cold, sneezing).
symptom(cold, congestion).

symptom(pneumonia, fever).
symptom(pneumonia, cough).
symptom(pneumonia, chest_pain).
symptom(pneumonia, difficulty_breathing).
symptom(pneumonia, fatigue).

symptom(asthma, wheezing).
symptom(asthma, shortness_of_breath).
symptom(asthma, chest_tightness).
symptom(asthma, coughing).



% Rules for diagnosing medical conditions

diagnose(flu) :-
    symptom(flu, fever),
    symptom(flu, headache),
    symptom(flu, sore_throat),
    symptom(flu, cough),
    symptom(flu, fatigue).

diagnose(cold) :-
    symptom(cold, sore_throat),
    symptom(cold, cough),
    symptom(cold, runny_nose),
    symptom(cold, sneezing),
    symptom(cold, congestion).

diagnose(pneumonia) :-
    symptom(pneumonia, fever),
    symptom(pneumonia, cough),
    symptom(pneumonia, chest_pain),
    symptom(pneumonia, difficulty_breathing),
    symptom(pneumonia, fatigue).

diagnose(asthma) :-
    symptom(asthma, wheezing),
    symptom(asthma, shortness_of_breath),
    symptom(asthma, chest_tightness),
    symptom(asthma, coughing).

has_symptoms(X, Symptoms) :-
    diagnose(X),
    forall(member(Symptom, Symptoms), symptom(X, Symptom)).