import streamlit as st

st.title ('Smart Placement Assistant')
st.write ('Check your placement eligibility and skill match.')

companies = [
    {'name': 'Deloitte',
     'min_cgpa': 7.5,
     'max_backlogs': 0,
     'skills': ['Python', 'Excel', 'Communication']},
    {'name': 'EY',
     'min_cgpa': 7.0,
     'max_backlogs': 1,
     'skills': ['Excel', 'Communication']},
    {'name': 'KPMG',
     'min_cgpa': 8.0,
     'max_backlogs': 0,
     'skills': ['Excel', 'Python', 'SQL']},
    {'name': 'TCS',
     'min_cgpa': 6.5,
     'max_backlogs': 2,
     'skills': ['Python', 'Communication']}]
st.header('Student Profile')


name = st.text_input("Enter your name: ")
course = st.text_input("Enter your course: ")
cgpa = st.number_input("Enter your CGPA: ", min_value=0.0, max_value=10.0, step=0.1)
backlogs = st.number_input("Enter the number of backlogs: ", min_value=0, step=1)
skills = st.text_input("Enter your skills (comma-separated): ")
skills = [
    skill.strip()
    for skill in skills.split(",")
]
student = {
    'name': name,
        'course': course,
        'cgpa': cgpa,
        'backlogs': backlogs,
        'skills': skills
    }

   



if st.button("Check Eligibility"):

    st.header("Eligibility Results")

    eligible_companies = []

    for company in companies:

        if (
            student['cgpa'] >= company['min_cgpa']
            and student['backlogs'] <= company['max_backlogs']
        ):
            eligible_companies.append(company)
            st.success(f"{company['name']} - Eligible ✓")

        else:
            st.error(f"{company['name']} - Not Eligible ✗")

    st.header("Skill Match Results")

    for company in eligible_companies:

        required_skills = company['skills']

        matching_skills = []
        missing_skills = []

        for skill in required_skills:

            if skill in student['skills']:
                matching_skills.append(skill)
            else:
                missing_skills.append(skill)

        match_percentage = (
            len(matching_skills) / len(required_skills)
        ) * 100

        st.subheader(company['name'])

        st.write(
            f"**Skill Match Percentage: {match_percentage:.2f}%**"
        )

        if matching_skills:
            st.write(
                "Matching Skills:",
                ", ".join(matching_skills)
            )

        if missing_skills:
            st.write(
                "Skills to improve:",
                ", ".join(missing_skills)
            )
    st.header('**Placement Report**')
    st.write('**Student**: ', {name})
    st.write('**Course**: ', {course})
    st.write('**CGPA**: ', {cgpa})
    st.write('**Backlogs**: ', {backlogs})
    st.write(f'**Skills**: {','.join(skills)}')
    st.subheader('**Eligible Companies**: ')

    if eligible_companies:

        for company in eligible_companies:
            st.write('✓', company['name'])
    else:
            st.write('✗ No eligible companies found.')

st.divider()
st.header('Company Requirements')

for company in companies:
    with st.expander(company['name']):
         st.write(f'**Minimum CGPA**', company['min_cgpa'])
         st.write(f'**Maximum Backlogs**', company['max_backlogs'])
         st.write(f'**Required Skills**',','.join(company['skills']))