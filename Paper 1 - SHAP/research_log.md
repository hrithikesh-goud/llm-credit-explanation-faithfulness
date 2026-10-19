## Paper 1: SHAP (Lundberg & Lee, 2017)

1. What problem does SHAP solve?
Answer:Basically an ML model like XGBOOST directly gives the outcome for example a person applied for a loan and gets refusal, XGBOOST model gives an output like refused but will not give the clear explaination, why loan application got refused

But SHAP actually gives the score for each feature for making the output one way or the other with a clear explaination.

2. How does it work (one simple sentence)?
Answer: Loan Rejection Reasons - features(Late payments,long period loan,age)
Decison - Accepted or Refused
So SHAP checks whether the decision changes with or without feature.
So SHAP actually gives score for each feature for making the decision

3. Why does my project need it?
Answer: So basically LLM gives a reason for suppose loan rejection and SHAP will also gives a reason for the same loan rejection, So here my work is to compare the both reasons and if LLM reasons are different from SHAP then LLM have given the wrong explaination.
I can consider SHAP's reason because SHAP checks inside the model that made the decision, But LLM only checks the applicant details.  



## Paper 2: LIME (Ribeiro, Singh & Guestrin, 2016)

1. What did the paper do?
Answer:The paper it invented LIME which is a new tool and that will explain why a model made a decision for any kind of a model.
LIME model has been tested to classify text and image.
It has given an explaination and let people to decide whether to trust or not.

2. What is its limitation compared with SHAP?
Answer: LIME actually uses random changes to the input and gives different outputs everytime, but SHAP will give the same output based on the model that made decision.

3. How does it connect to my project?
Answer:In my project SHAP will give the output that is used to check the LLM, But LIME will give different outputs everytime.I chose SHAP because it gives the consistent reasons everytime.


## Paper 3: Faithfulness (Jacovi & Goldberg, 2020)
Plausible - Sounds believable to a person.
Faithful - It will match the real reason.

1. What did the paper do?
Answer: The paper told the given explainations must be checked for truth, And shouldn't only check whether it sounded good or not.

2. What is the difference between plausible and faithful?
Answer: Imagine a student comes to a lecture late, And the professor asked why
Then the student replied, There was heavy traffic today
Plausible - Yes, Sounds like believable.
Faithful - No,The actual reason was he overslept.    

3. How does it connect to my project?
Answer:The LLM might give the wrong answer like the student just told there was alot of traffic,But SHAP gives the exact and real reason.
So my projects checks whether the LLM explaination is faithful by comparing with SHAP.



## Paper 4: Unfaithful LLM explanations (Turpin et al., 2023)

1. What did the paper do?
Answer:They basically asked the LLM to answer a question and explain it step by step and they secretly mentioned a hint that pushes the LLM towards the particular answer.

2. What did they find?
Answer:The LLM actually followed the hint and pushes the answer towards that particular answer and never mentions about the hint in the eplaination.

3. How does it connect to my project?
Answer:If the LLM is hiding the real reason or hint for a simple question, It might give the wrong explaination or false reason for a customer whose loan got refused,So my projects checks the LLM's explanation with SHAP and confirm whether LLM has given the true output.



## Paper 5: TalkToModel (Slack et al., 2023)

1. What did the paper do?
Answer:They built a chatbot that will let people ask questions to an ML model and the chatbot will give explaination in plain and simple english.

2. How does it work (the translator idea)?
Answer:The Chatbot checks with real explaination tools like SHAP and then only it will give the output in simple english.

3. How does it connect to my project, and what's my gap?
Answer:This is similar to my LLM with SHAP method, My gap is it didn't measure how frequently the LLM's justification is wrong for the loan decisions.