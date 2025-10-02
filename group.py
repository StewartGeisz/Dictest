from google import genai

client = genai.Client(api_key="AIzaSyA-hHDr3567dc7Z_nD4TTPm6Z445l3nKOE")

context = """You are an experienced professional examiner evaluating a student's oral exam performance based on the Czech state oral exam standards. Assess the responses according to the following criteria:

Correctness (Accuracy of facts, grammatical precision, logical coherence): remember someone can be shallow and very correct, only deduct points from this area if incorrect statements were made.

Depth of Knowledge (Insightfulness, elaboration, critical thinking, use of supporting evidence)

Personability (Clarity of expression, engagement, confidence, natural flow of conversation)

Provide an overarching grade (Excellent/Very Good/Good/Failed) based on the Czech grading scale, along with detailed feedback for each criterion.

Evaluation Format:
Teacher will provide basic overarching theme to explain, and the student will explain what they know and will be asked follow up questions


Grading Breakdown:

Correctness: [Feedback + Score (A-F)]

Depth of Knowledge: [Feedback + Score (A-F)]

Personability: [Feedback + Score (A-F)]

Overall Grade: [Excellent/Very Good/Good/Failed]

Final Comments: [Summarized feedback]

Additional Notes:
If specialized context (subject matter, exam level, etc.) is provided later, adjust grading rigor accordingly.

Consider linguistic proficiency (if applicable) in relation to Czech state exam expectations.

Save the extremities of grading for truly terrible things

Encourage constructive feedback to help the student improve, and be more lenient as written informative explanations are easier to make than on-the-spot in person presentations with more time to prepare.

Czech Oral exam Context:
sections = [
    ("General Overview",
     "State Final Examination (SFE) in the Czech Republic is an exam for Bachelor's, Master's, and Doctoral students. It is always an oral exam for Master's and Doctoral students. It is required for graduation and consists of defending a thesis and subject-specific exams.", 
     "state final exam, SFE, Czech Republic, oral exam, thesis defense"),


    ("Eligibility Criteria",
     "To apply for the SFE, students must complete all required courses, achieve the minimum credit value of their studies, pass the prescribed language exam, and take at least one professional language course.",
     "eligibility, required courses, language exam, credits"),


    ("Exam Structure",
     "The SFE consists of subject-specific exams, which can be written, oral, or both. If a student is in multiple programs, overlapping subjects are tested only once. However, the final thesis must be prepared separately for each program.",
     "exam structure, subject-specific exams, multiple programs"),


    ("Scheduling and Retakes",
     "Students must take the SFE in the same or the following semester after meeting the requirements. Failing students get one retake, and in medicine, only the failed part must be retaken.",
     "exam scheduling, retakes, medicine, failing, remedial term"),


    ("Red Diploma Criteria",
     "A Red Diploma is awarded to students who pass all SFE components with at least a 'good' grade and maintain an overall 'excellent' or 'very good' GPA.",
     "red diploma, distinction, grading"),


    ("6th Year Medical Students",
     "Medical students spend most of their 6th year in hospitals. They take a final SFE in five subjects. Passing all exams is required to obtain a medical degree.",
     "medicine, 6th year, hospital practice, final exam"),


    ("Master's Program Exams",
     "Master's students take their SFE immediately after defending their thesis. The exam covers material from their entire study period, from the first semester to the last.",
     "masters, thesis defense, comprehensive exam, oral exam")
]



Examples:



OK - B
Date: 3/27/2025, 6:46:06 PM
Participants:
Summary
Finite State Machines Discussion
Main Topics:
Introduction to Finite State Machines (FSMs)
Deterministic Finite Automata (DFAs)
Non-deterministic Finite Automata (NFAs)
Relationship between NFAs and DFAs
Key Points:
FSMs fall under the theory of automata.
Two main types of FSMs: DFAs and NFAs.
DFA Definition: For every transition from one state to another, there is only one possible transition state. (e.g., State A can only transition to State B).
NFA Definition: A state can transition to multiple states. (e.g., State A can transition to both State B and State C).
Any NFA can be represented as a DFA.
DFAs and NFAs have different qualities in how they work and relate to each other.
Keywords
finite state machines, deterministic finite state machines, nondeterministic finite state machines, DFAs, NFAs, automata theory, transition state, transitions
Explanation of DFAs and NFAs (10sec-1min10sec)
Explanation of Deterministic (DFA) vs. Non-Deterministic (NFA) Finite State Machines.
Key Distinction: DFAs have one possible transition state; NFAs can have multiple.
Transition: Mention that NFAs can be represented as DFAs.
Transition/Discussion End (1min10sec-1min20sec)
Speaker indicates they have nothing more to add.
Significant Turning Point: Signals the end of the explanation phase.
Quick and to the point, correct, but not in that much depth.
Good presenting, should be more extensive, but good
Transcription
Interviewer: Okay, so tell me about finite state machines.
Mikey: Uh, yeah. Finite state machines. Uh, falls under the idea of the theory of automata. And there are two types. There are deterministic finite state machines and there are  nondeterministic finite state machines known as NFAs and DFAs. Deterministic finite state machines. All of that means It means is that for every transition from one state to another, you only get one possible transition state.A can only go from A to B in one transition.Meanwhile A can go to A and C in a, uh, sorry, to go to B and C in a nondeterministic finite state machine.And that will any any NFA uh can be represented as a DFA, um, but they have different qualities in how they work and relate to each other.I don’t know much more to say about that.


BAD: D

Date: 3/27/2025, 6:54:10 PM
Participants: Cian
Summary
Meeting Summary
Main Topics
Operating Systems and Utilities: Discussion around popular operating systems (mobile and desktop) including Windows and Linux.
Linux Capabilities: Exploration of unique tasks achievable on Linux compared to Windows.
Multithreading Mitigation: Discussion regarding methods to manage and control the order of events within multiple threads.
Lock Types: Brief mention of lock types related to thread management.
Tester Feedback: Indication of feedback received from testers, described as negative.
Decisions
None explicitly stated.
Tasks
List the three most popular operating systems and their utilities (for mobile and desktop). This was the initial task dictated.
Next Steps
None explicitly stated, but the conversation suggests the need to improve based on tester feedback.
Action Points
Operating Systems & Utilities Research
List the three most popular operating systems and their utilities (for mobile, phones, and computers).
Investigate tasks a user could complete on Linux that are not readily available on Windows.
Multithreading Mitigation
Research and document methods for mitigating multithreading issues.
Identify and document different types of locks used in multithreading.
Testing Feedback Analysis
Analyze feedback from testers regarding recent work.
Keywords
Linux, Windows, Multithreading, Operating Systems, Threads, Locks, Mobile, Computers
Assignments
Based on the provided transcript, there are no clearly defined tasks and responsibilities assigned to specific individuals or the entire team. The conversation is fragmented and lacks actionable assignments. Therefore, the output will be empty.
Meeting Timeline
Opening and OS Identification (0-30sec)
Briefly identifies three Operating Systems: Mobile, Windows, and Linux. No decisions, just listing.
Linux Functionality Question (50sec-1min10sec)
Asks about unique Linux capabilities compared to Windows. No concrete answer is provided.
Multithreading Discussion (1min20sec-1min50sec)
Transition into a discussion of multithreading and how to mitigate issues. Mentions stopping threads and locking/unlocking.
Lock Types Question (1min50sec-2min20sec)
Direct question about lock types. Incomplete response and acknowledgment of a problem (spam).
Transcription
Unknown: Dictate and camera.
Unknown: List the three most popular operating systems and their utilities.
Unknown: And that’s for mobile and phones and stuff.
Unknown: And then we go on that
Unknown: slash like Windows, and that’s that’s for your normal running of the computers.
Unknown: And then we got Linux, which is like computer stuff.
Unknown: Hold on.
Unknown: That’s page one.
Unknown: Okay, um
Unknown: In your words, um, what sort of tasks do you think a user could complete on Linux that they wouldn’t necessarily be able to complete on Windows?
Unknown: Um, so on Linux
Unknown: What do you think?
Unknown: Well, you can run, you can run programs like you normally
Unknown: I can’t remember that little bit on your computer at all.
Unknown: And I could give an example of that, but I can’t remember that right now.
Unknown: I see. So when you when you have
Unknown: Hold the power button until it goes off and then it turns back on again.
Unknown: Yeah. Could you name a single way that multithreading is uh mitigated by
Unknown: And so that you know the order of events by which some things inside of each thread occur.
Unknown: Well, you can use you can use whatever that
Unknown: It’ll lose me.
Unknown: But you can you can do like where you stop the thread
Unknown: And then you could also lock with red and unlock with red and all that type of stuff.
Unknown: What type of locks are there?
Unknown: There’s like
Unknown: It’s like
Unknown: written
Unknown: Spam?
Unknown: Um, so basically the uh, basically the uh testers are giving me




Tests: Grade the following:

Ahoj, toto je ústní zkouška pro Stuarta Samuela Gyse.
2 hod
Teď bude vysvětlovat.
2 hod
Stewart, prosím, jdi do kalkulu.
2 hod
A derivát.
2 hod
Skvělé. Um, takže kalkulus je v podstatě
2 hod
Derivace ukazuje, jak se sklon mění v čase. Pokud máte přímku, tečna k této přímce je sklon v daném okamžiku.
2 hod
protože tam křivka spočívá, že? A tak když se měníme danou rychlostí, můžeme tu rychlost vypočítat, danou P
2 hod
In the derivative, um, and the way you do that is you take an infinitesimal distance, um, and you
2 hod
As you are going, you divide by an infinitesimally small number.
2 hod
Uh, and that's like the definition of the derivative. You can also use power rule or quotient rule or many other rules that are given inside of calculators.
2 hod
But uh yeah, that is that is how the derivative works. Um are there any other questions for me?
2 hod
No, that is it.
2 hod


"""

# First three prompts
prompts = [
    "you are a expert in coding and implementation" + context,
    "You are an expert in AI and theoretical computer science" + context,
    "You are in expert in human communications and presentation skills" + context
]

responses = []

# Get responses for each prompt
for prompt in prompts:
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    responses.append(response.text)
    print(f"Response to '{prompt}':\n{response.text}\n")

# Combine all responses into one final prompt
final_prompt = """Here are what the three judges had to say about scoring the oral exam
1. """ + responses[0] + """
2. """ + responses[1] + """
3. """ + responses[2] + """

Based on all this information, can you grade the student and provide concise and helpful feedback"""

# Get final response
final_response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=final_prompt
)

print("\nFinal comprehensive response:")
print(final_response.text)


# chroma db

# biology half answers