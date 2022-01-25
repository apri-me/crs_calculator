def conv_celpip_first_clb(speaking, listening, reading, writing):
    the_dict = {
        '10 - 12': 'CLB 10 or more',
        '9': 'CLB 9',
        '8': 'CLB 8',
        '7': 'CLB 7',
        '6': 'CLB 6',
        '5': 'CLB 4 or 5',
        '4': 'CLB 4 or 5',
        'M, 0 - 3': 'Less than CLB 4',
    }
    return [the_dict[speaking], the_dict[listening], the_dict[reading], the_dict[writing]]


def conv_ielts_first_clb(speaking, listening, reading, writing):
    speaking_dict = {
        '7.5 - 9.0': 'CLB 10 or more',
        '7.0': 'CLB 9',
        '6.5': 'CLB 8',
        '6.0': 'CLB 7',
        '5.5': 'CLB 6',
        '5.0': 'CLB 4 or 5',
        '4.0 - 4.5': 'CLB 4 or 5',
        '0 - 3.5': 'Less than CLB 4',
    }
    listening_dict = {
        '8.5 - 9.0': 'CLB 10 or more',
        '8.0': 'CLB 9',
        '7.5': 'CLB 8',
        '6.0 - 7.0': 'CLB 7',
        '5.5': 'CLB 6',
        '5.0': 'CLB 4 or 5',
        '4.5': 'CLB 4 or 5',
        '0 - 4.0': 'Less than CLB 4',
    }
    reading_dict = {
        '8.0 - 9.0': 'CLB 10 or more',
        '7.0 - 7.5': 'CLB 9',
        '6.5': 'CLB 8',
        '6.0': 'CLB 7',
        '5.0 - 5.5': 'CLB 6',
        '4.0 - 4.5': 'CLB 4 or 5',
        '3.5': 'CLB 4 or 5',
        '0 - 3.0': 'Less than CLB 4',
    }
    writing_dict = {
        '7.5 - 9.0': 'CLB 10 or more',
        '7.0': 'CLB 9',
        '6.5': 'CLB 8',
        '6.0': 'CLB 7',
        '5.5': 'CLB 6',
        '5.0': 'CLB 4 or 5',
        '4.0 - 4.5': 'CLB 4 or 5',
        '0 - 3.5': 'Less than CLB 4',
    }

    return [speaking_dict[speaking], listening_dict[listening], reading_dict[reading], writing_dict[writing]]


def conv_tef_first_clb(speaking, listening, reading, writing):
    speaking_dict = {
        '393-450': 'CLB 10 or more',
        '371-392': 'CLB 9',
        '349-370': 'CLB 8',
        '310-348': 'CLB 7',
        '271-309': 'CLB 6',
        '226-270': 'CLB 4 or 5',
        '181-225': 'CLB 4 or 5',
        '0 - 180': 'Less than CLB 4',
    }
    listening_dict = {
        '316-360': 'CLB 10 or more',
        '298-315': 'CLB 9',
        '280-297': 'CLB 8',
        '249-279': 'CLB 7',
        '217-248': 'CLB 6',
        '181-216': 'CLB 4 or 5',
        '145-180': 'CLB 4 or 5',
        '0 - 144': 'Less than CLB 4',
    }
    reading_dict = {
        '263-300': 'CLB 10 or more',
        '248-262': 'CLB 9',
        '233-247': 'CLB 8',
        '207-232': 'CLB 7',
        '181-206': 'CLB 6',
        '151-180': 'CLB 4 or 5',
        '121-150': 'CLB 4 or 5',
        '0 - 120': 'Less than CLB 4',
    }
    writing_dict = {
        '393-450': 'CLB 10 or more',
        '371-392': 'CLB 9',
        '349-370': 'CLB 8',
        '310-348': 'CLB 7',
        '271-309': 'CLB 6',
        '226-270': 'CLB 4 or 5',
        '181-225': 'CLB 4 or 5',
        '0 - 180': 'Less than CLB 4',
    }
    return [speaking_dict[speaking], listening_dict[listening], reading_dict[reading], writing_dict[writing]]

def conv_tcf_first_clb(speaking, listening, reading, writing):
    speaking_dict = {
        '16-20': 'CLB 10 or more',
        '14-15': 'CLB 9',
        '12-13': 'CLB 8',
        '10-11': 'CLB 7',
        '7-9': 'CLB 6',
        '6': 'CLB 4 or 5',
        '4-5': 'CLB 4 or 5',
        '0-3': 'Less than CLB 4',
    }
    listening_dict = {
        '549-699': 'CLB 10 or more',
        '523-548': 'CLB 9',
        '503-522': 'CLB 8',
        '458-502': 'CLB 7',
        '398-457': 'CLB 6',
        '369-397': 'CLB 4 or 5',
        '331-368': 'CLB 4 or 5',
        '0-330': 'Less than CLB 4',
    }
    reading_dict = {
        '549-699': 'CLB 10 or more',
        '524-548': 'CLB 9',
        '499-523': 'CLB 8',
        '453-498': 'CLB 7',
        '406-452': 'CLB 6',
        '375-405': 'CLB 4 or 5',
        '342-374': 'CLB 4 or 5',
        '0-341': 'Less than CLB 4',
    }
    writing_dict = {
        '16-20': 'CLB 10 or more',
        '14-15': 'CLB 9',
        '12-13': 'CLB 8',
        '10-11': 'CLB 7',
        '7-9': 'CLB 6',
        '6': 'CLB 4 or 5',
        '4-5': 'CLB 4 or 5',
        '0-3': 'Less than CLB 4',
    }
    return [speaking_dict[speaking], listening_dict[listening], reading_dict[reading], writing_dict[writing]]




def cal_first_clb(olp):
    olp_type = olp[0]
    speaking = olp[1]
    listening = olp[2]
    reading = olp[3]
    writing = olp[4]

    if (olp_type == "CELPIP-G"):
        return conv_celpip_first_clb(speaking, listening, reading, writing)
    elif (olp_type == "IELTS"):
        return conv_ielts_first_clb(speaking, listening, reading, writing)
    elif (olp_type == "TEF Canada"):
        return conv_tef_first_clb(speaking, listening, reading, writing)
    else:
        return conv_tcf_first_clb(speaking, listening, reading, writing)


def conv_celpip_sec_clb(speaking, listening, reading, writing):
    the_dict = {
        '10 - 12': 'CLB 9 or more',
        '9': 'CLB 9 or more',
        '8': 'CLB 7 or 8',
        '7': 'CLB 7 or 8',
        '6': 'CLB 5 or 6',
        '5': 'CLB 5 or 6',
        '4': 'CLB 4 or less',
        'M, 0 - 3': 'CLB 4 or less',
    }
    return [the_dict[speaking], the_dict[listening], the_dict[reading], the_dict[writing]]


def conv_ielts_sec_clb(speaking, listening, reading, writing):
    speaking_dict = {
        '7.5 - 9.0': 'CLB 9 or more',
        '7.0': 'CLB 9 or more',
        '6.5': 'CLB 7 or 8',
        '6.0': 'CLB 7 or 8',
        '5.5': 'CLB 5 or 6',
        '5.0': 'CLB 5 or 6',
        '4.0 - 4.5': 'CLB 4 or less',
        '0 - 3.5': 'CLB 4 or less',
    }
    listening_dict = {
        '8.5 - 9.0': 'CLB 9 or more',
        '8.0': 'CLB 9 or more',
        '7.5': 'CLB 7 or 8',
        '6.0 - 7.0': 'CLB 7 or 8',
        '5.5': 'CLB 5 or 6',
        '5.0': 'CLB 5 or 6',
        '4.5': 'CLB 4 or less',
        '0 - 4.0': 'CLB 4 or less',
    }
    reading_dict = {
        '8.0 - 9.0': 'CLB 9 or more',
        '7.0 - 7.5': 'CLB 9 or more',
        '6.5': 'CLB 7 or 8',
        '6.0': 'CLB 7 or 8',
        '5.0 - 5.5': 'CLB 5 or 6',
        '4.0 - 4.5': 'CLB 5 or 6',
        '3.5': 'CLB 4 or less',
        '0 - 3.0': 'CLB 4 or less',
    }
    writing_dict = {
        '7.5 - 9.0': 'CLB 9 or more',
        '7.0': 'CLB 9 or more',
        '6.5': 'CLB 7 or 8',
        '6.0': 'CLB 7 or 8',
        '5.5': 'CLB 5 or 6',
        '5.0': 'CLB 5 or 6',
        '4.0 - 4.5': 'CLB 4 or less',
        '0 - 3.5': 'CLB 4 or less',
    }

    return [speaking_dict[speaking], listening_dict[listening], reading_dict[reading], writing_dict[writing]]


def conv_tef_sec_clb(speaking, listening, reading, writing):
    speaking_dict = {
        '393-450': 'CLB 9 or more',
        '371-392': 'CLB 9 or more',
        '349-370': 'CLB 7 or 8',
        '310-348': 'CLB 7 or 8',
        '271-309': 'CLB 5 or 6',
        '226-270': 'CLB 5 or 6',
        '181-225': 'CLB 4 or less',
        '0 - 180': 'CLB 4 or less',
    }
    listening_dict = {
        '316-360': 'CLB 9 or more',
        '298-315': 'CLB 9 or more',
        '280-297': 'CLB 7 or 8',
        '249-279': 'CLB 7 or 8',
        '217-248': 'CLB 5 or 6',
        '181-216': 'CLB 5 or 6',
        '145-180': 'CLB 4 or less',
        '0 - 144': 'CLB 4 or less',
    }
    reading_dict = {
        '263-300': 'CLB 9 or more',
        '248-262': 'CLB 9 or more',
        '233-247': 'CLB 7 or 8',
        '207-232': 'CLB 7 or 8',
        '181-206': 'CLB 5 or 6',
        '151-180': 'CLB 5 or 6',
        '121-150': 'CLB 4 or less',
        '0 - 120': 'CLB 4 or less',
    }
    writing_dict = {
        '393-450': 'CLB 9 or more',
        '371-392': 'CLB 9 or more',
        '349-370': 'CLB 7 or 8',
        '310-348': 'CLB 7 or 8',
        '271-309': 'CLB 5 or 6',
        '226-270': 'CLB 5 or 6',
        '181-225': 'CLB 4 or less',
        '0 - 180': 'CLB 4 or less',
    }
    return [speaking_dict[speaking], listening_dict[listening], reading_dict[reading], writing_dict[writing]]


def conv_tcf_sec_clb(speaking, listening, reading, writing):
    speaking_dict = {
        '16-20': 'CLB 9 or more',
        '14-15': 'CLB 9 or more',
        '12-13': 'CLB 7 or 8',
        '10-11': 'CLB 7 or 8',
        '7-9': 'CLB 5 or 6',
        '6': 'CLB 5 or 6',
        '4-5': 'CLB 4 or less',
        '0-3': 'CLB 4 or less',
    }
    listening_dict = {
        '549-699': 'CLB 9 or more',
        '523-548': 'CLB 9 or more',
        '503-522': 'CLB 7 or 8',
        '458-502': 'CLB 7 or 8',
        '398-457': 'CLB 5 or 6',
        '369-397': 'CLB 5 or 6',
        '331-368': 'CLB 4 or less',
        '0-330': 'CLB 4 or less',
    }
    reading_dict = {
        '549-699': 'CLB 9 or more',
        '524-548': 'CLB 9 or more',
        '499-523': 'CLB 7 or 8',
        '453-498': 'CLB 7 or 8',
        '406-452': 'CLB 5 or 6',
        '375-405': 'CLB 5 or 6',
        '342-374': 'CLB 4 or less',
        '0-341': 'CLB 4 or less',
    }
    writing_dict = {
        '16-20': 'CLB 9 or more',
        '14-15': 'CLB 9 or more',
        '12-13': 'CLB 7 or 8',
        '10-11': 'CLB 7 or 8',
        '7-9': 'CLB 5 or 6',
        '6': 'CLB 5 or 6',
        '4-5': 'CLB 4 or less',
        '0-3': 'CLB 4 or less',
    }
    return [speaking_dict[speaking], listening_dict[listening], reading_dict[reading], writing_dict[writing]]


def cal_second_clb(olp):
    if olp:
        olp_type = olp[0]
        speaking = olp[1]
        listening = olp[2]
        reading = olp[3]
        writing = olp[4]

        if (olp_type == "CELPIP-G"):
            return conv_celpip_sec_clb(speaking, listening, reading, writing)
        elif (olp_type == "IELTS"):
            return conv_ielts_sec_clb(speaking, listening, reading, writing)
        elif (olp_type == "TEF Canada"):
            return conv_tef_sec_clb(speaking, listening, reading, writing)
        else:
            return conv_tcf_sec_clb(speaking, listening, reading, writing)

def cal_have_spouse(marital_status, ):
    marital_dict = {
        'Annulled Marriage': 0,
        'Common-law': 1,
        'Divorced / Seperated': 0,
        'Legally Seperated': 0,
        'Married': 1,
        'Never Married / Single': 0,
        'Widowed': 0,
    }
    return marital_dict[marital_status]


def cal_age_points(age, have_spouse):
    age_dict = {
        '17 years of age or less': (0, 0),
        '18 years of age': (99, 90),
        '19 years of age': (105, 95),
        '20 years of age': (110, 100),
        '21 years of age': (110, 100),
        '22 years of age': (110, 100),
        '23 years of age': (110, 100),
        '24 years of age': (110, 100),
        '25 years of age': (110, 100),
        '26 years of age': (110, 100),
        '27 years of age': (110, 100),
        '28 years of age': (110, 100),
        '29 years of age': (110, 100),
        '30 years of age': (105, 95),
        '31 years of age': (99, 90),
        '32 years of age': (94, 85),
        '33 years of age': (88, 80),
        '34 years of age': (83, 75),
        '35 years of age': (77, 70),
        '36 years of age': (72, 65),
        '37 years of age': (66, 60),
        '38 years of age': (61, 55),
        '39 years of age': (55, 50),
        '40 years of age': (50, 45),
        '41 years of age': (39, 35),
        '42 years of age': (28, 25),
        '43 years of age': (17, 15),
        '44 years of age': (6, 5),
        '45 years of age or more': (0, 0)
    }
    return age_dict[age][have_spouse]



def cal_loe_points(loe, have_spouse):
    loe_dict = {
        "None, or less than secondary school (high school)": (0, 0),
        "None, or less than secondary school (high school)": (30, 28),
        "One-year program at a university, college, trade or technical school, or other institute": (90, 84),
        "Two-year program at a university, college, trade or technical school, or other institute": (98, 91),
        "Bachelor's degree (three or more year program at a university, college, trade or technical school, or other institute)": (120, 112),
        "Two or more certificates, diplomas, or degrees. One must be for a program of three or more years": (128, 119),
        "Master's degree, or professional degree needed to practice in a licensed profession (see Help)": (135, 126),
        "Doctoral level university degree (PhD)": (150, 140),
    }
    return loe_dict[loe][have_spouse]



def cal_firstlang_skill_points(clb, have_spouse):
    clb_dict = {
        "Less than CLB 4": (0, 0),
        "CLB 4 or 5": (6, 6),
        "CLB 6": (9, 8),
        "CLB 7": (17, 16),
        "CLB 8": (23, 22),
        "CLB 9": (31, 29),
        "CLB 10 or more": (34, 32)
    }
    return clb_dict[clb][have_spouse]



def cal_secondlang_skill_points(clb):
    clb_dict = {
        "CLB 4 or less": 0,
        "CLB 5 or 6": 1,
        "CLB 7 or 8": 3,
        "CLB 9 or more": 6
    }
    return clb_dict[clb]



def cal_olp_points(first_clb, second_clb, have_spouse):
    first_lang =  0
    for clb in first_clb:
        first_lang += cal_firstlang_skill_points(clb, have_spouse)
    
    second_lang = 0
    if second_clb:
        for clb in second_clb:
            second_lang += cal_secondlang_skill_points(clb)
    
    return first_lang + second_lang
    

def cal_cwe_points(years, have_spouse):
    cwe_dict = {
        "None or less than a year": (0, 0),
        "1 year": (40, 35),
        "2 years": (53, 46),
        "3 years": (64, 56),
        "4 years": (72, 63),
        "5 years or more": (80, 70)
    }
    return cwe_dict[years][have_spouse]
    

def cal_core_capital_points(age, loe, first_clb, second_clb, cwe_years, have_spouse):
    age_pts = cal_age_points(age, have_spouse)
    loe_pts = cal_loe_points(loe, have_spouse)
    olp_pts = cal_olp_points(first_clb, second_clb, have_spouse)
    cwe_pts = cal_cwe_points(cwe_years, have_spouse)

    print(loe_pts)
    return age_pts + loe_pts + olp_pts + cwe_pts


def cal_sp_loe_points(loe):
    loe_dict = {
        "None, or less than secondary school (high school)": 0,
        "Secondary diploma (high school graduation)": 2,
        "One-year program at a university, college, trade or technical school, or other institute": 6,
        "Two-year program at a university, college, trade or technical school, or other institute": 7,
        "Bachelor's degree (three or more year program at a university, college, trade or technical school, or other institute)": 8,
        "Two or more certificates, diplomas, or degrees. One must be for a program of three or more years": 9,
        "Master's degree, or professional degree needed to practice in a licensed profession (see Help)": 10,
        "Doctoral level university degree (PhD)": 10,
    }
    return loe_dict[loe]


def cal_sp_olp_points(clb):
    total = 0
    clb_dict = {
        "CLB 4 or less": 0,
        "CLB 5 or 6": 1,
        "CLB 7 or 8": 3,
        "CLB 9 or more": 5,
    }
    for c in clb:
        total += clb_dict[c]
    return total


def cal_sp_cwe_points(years):
    cwe_dict = {
        "None or less than a year": 0,
        "1 year": 5,
        "2 years": 7,
        "3 years": 8,
        "4 years": 9,
        "5 years or more": 10
    }
    return cwe_dict[years]


def cal_spouse_points(loe, clb, cwe_years):
    loe_pts = cal_sp_loe_points(loe)
    olp_pts = cal_sp_olp_points(clb)
    cwe_pts = cal_sp_cwe_points(cwe_years)
    return loe_pts + olp_pts + cwe_pts

def cal_psd_form_edu(loe):
    loe_dict = {
        "None, or less than secondary school (high school)": (0, 0),
        "Secondary diploma (high school graduation)": (0, 0),
        "One-year program at a university, college, trade or technical school, or other institute": (25, 13),
        "Two-year program at a university, college, trade or technical school, or other institute": (25, 13),
        "Bachelor's degree (three or more year program at a university, college, trade or technical school, or other institute)": (50, 25),
        "Two or more certificates, diplomas, or degrees. One must be for a program of three or more years": (50, 25),
        "Master's degree, or professional degree needed to practice in a licensed profession (see Help)": (50, 25),
        "Doctoral level university degree (PhD)": (50, 25),
    }
    return loe_dict[loe]


def cal_olp_psd_points(psd, clb):
    for c in clb:
        if c in ["Less than CLB 4", "CLB 4 or 5", "CLB 6"]:
            return 0
    for c in clb:
        if c in ["CLB 7", "CLB 8"]:
            return psd[1]
    return psd[0]


def cal_cwe_psd_points(psd, years):
    if ( years == "None or less than a year" ):
        return 0
    if ( years == "1 year"):
        return psd[1]
    return psd[0]

def cal_edu_transferability_points(psd, clb, cwe_years):
    olp_psd_pts = cal_olp_psd_points(psd, clb)
    cwe_psd_pts = cal_cwe_psd_points(psd, cwe_years)
    total = olp_psd_pts + cwe_psd_pts
    return 50 if total > 50 else total

def cal_olp_fwe_points(fwe_years, clb):
    fwe_dict = {
        "None or less than a year": (0, 0),
        "1 year": (25, 13),
        "2 years": (25, 13),
        "3 years or more": (50, 25),
    }
    for c in clb:
        if c in ["Less than CLB 4", "CLB 4 or 5", "CLB 6"]:
            return 0
    for c in clb:
        if c in ["CLB 7", "CLB 8"]:
            return fwe_dict[fwe_years][1]
    return fwe_dict[fwe_years][0]

def cal_cwe_fwe_points(fwe_years, cwe_years):
    fwe_dict = {
        "None or less than a year": (0, 0),
        "1 year": (25, 13),
        "2 years": (25, 13),
        "3 years or more": (50, 25),
    }
    if (cwe_years == "None or less than a year"):
        return 0
    if (cwe_years == "1 year"):
        return fwe_dict[fwe_years][1]
    return fwe_dict[fwe_years][0]


def cal_work_transferability_points(fwe_years, clb, cwe_years):
    olp_fwe_pts = cal_olp_fwe_points(fwe_years, clb)
    cwe_fwe_pts = cal_cwe_fwe_points(fwe_years, cwe_years)
    total = olp_fwe_pts + cwe_fwe_pts
    return 50 if total > 50 else total


def cal_cq_pts(clb):
    for c in clb:
        if c in ["Less than CLB 4"]:
            return 0
    for c in clb:
        if c in ["CLB 4 or 5", "CLB 6"]:
            return 25
    return 50


def cal_skill_transferability_points(loe, clb, cwe_years, fwe_years, have_cq):
    psd = cal_psd_form_edu(loe)
    # Education
    edu = cal_edu_transferability_points(psd, clb, cwe_years)
    # Work Experience
    work = cal_work_transferability_points(fwe_years, clb, cwe_years)
    cq_pts = 0
    if have_cq:
        cq_pts = cal_cq_pts(clb)
    total = edu + work + cq_pts
    return 100 if total > 100 else total

def cal_sib(have_sib):
    return 15 if have_sib else 0

def cal_nomination(nomination):
    return 600 if nomination else 0

def cal_noc_pts(noc_skill_type):
    if not noc_skill_type:
        return 0
    noc_dict = {
        "NOC Skill Type 00": 200,
        "NOC Skill Level A or B or  any Type 0 other than 00": 50,
        "NOC Skill Level C or D": 0,
    }
    return noc_dict[noc_skill_type]

def clb_fr_high(fr_clb):
    for clb in fr_clb:
        if clb in ["Less than CLB 4", "CLB 4 or 5", "CLB 6", "CLB 4 or less", "CLB 5 or 6"]:
            return False
    return True


def clb_eng_high(eng_clb):
    if not eng_clb:
        return False
    for clb in eng_clb:
        if clb in ["Less than CLB 4", "CLB 4 or 5", "CLB 4 or less"]:
            return False
    return True


def cal_add_fr_eng(eng_clb, fr_clb):
    if not clb_fr_high(fr_clb):
        return 0
    if clb_eng_high(eng_clb):
        return 50
    return 25
    

def cal_add_olp_pts(first_clb, first_type, second_clb):
    if not second_clb:
        if first_type in ['TEF Canada', 'TCF Canada']:
            return cal_add_fr_eng([], first_clb)
        return 0
    if first_type in ['CELPIP-G', 'IELTS']:
        return cal_add_fr_eng(first_clb, second_clb)
    return cal_add_fr_eng(second_clb, first_clb)

def cal_add_psd_pts(psd):
    if not psd:
        return 0
    psd_dict = {
        "Secondary (high school) or less": 0,
        "One- or two-year diploma or certificate": 15,
        "Degree, diploma or certificate of three years or longer OR a Master’s, professional or doctoral degree of at least one academic year": 30,
    }
    return psd_dict[psd]

def cal_additional_points(have_sib, noc_skill_type, nomination, first_clb, first_type, second_clb, psd):
    total = 0
    total += cal_sib(have_sib)
    total += cal_nomination(nomination)
    total += cal_noc_pts(noc_skill_type)
    total += cal_add_olp_pts(first_clb, first_type, second_clb)
    total += cal_add_psd_pts(psd)
    print(cal_noc_pts(noc_skill_type))
    return 600 if total > 600 else total
        

def calculate_crs(age, loe, first_olp, cwe_years, marital_status,
        fwe_years, have_cq, have_sib, nomination, psd=None, noc_skill_type=None, second_olp=None, sp_loe=None, sp_olp=None, sp_cwe_years=None):
    first_clb = cal_first_clb(first_olp)
    second_clb = cal_second_clb(second_olp)
    sp_clb = cal_second_clb(sp_olp)
    have_spouse = cal_have_spouse(marital_status)

    # A. Core/ human capital factors
    # age: Age
    # loe: Level of education
    # olp: Official languages proficiency
    # cwe: Canadian work experience

    core_capital_points = cal_core_capital_points(age, loe, first_clb, second_clb, cwe_years, have_spouse)

    # B. Spouse or common-law partner factors 
    # sp_loe: spouse's level of education
    # sp_clb: spuses's clb
    # sp_cwe_years

    spouse_points = 0
    if (have_spouse):
        spouse_points = cal_spouse_points(sp_loe, sp_clb, sp_cwe_years)
    
    # C. Skill Transferability factors (Maximum 100 points)
    #   Education (max 50)
    # olp_psd: With good/strong official languages proficiency and a post-secondary degree (50)
    # cwe_psd: With Canadian work experience and a post-secondary degree(50)
    #   Foreign work experience (max 50)
    # olp_fwe: With good/strong official languages proficiency (Canadian Language Benchmark [CLB] level 7 or higher) and foreign work experience (50)
    # cwe_fwe: With Canadian work experience and foreign work experience (50)
    #   Certificate of qualification (for people in trade occupations) (max 50)
    # olp_cq: With good/strong official languages proficiency and a certificate of qualification (50)

    skill_transferability_points = cal_skill_transferability_points(loe, first_clb, cwe_years, fwe_years, have_cq)

    # D. Additional points (Maximum 600 points)

    # fle: french language skills (50)
    # pec: Post-secondary education in Canada (30)
    # ae: Arranged employment (200)
    # pn: PN nomination (600)

    additional_points = cal_additional_points(have_sib, noc_skill_type, nomination, first_clb, first_olp[0], second_clb, psd)
    return [core_capital_points, spouse_points, skill_transferability_points, additional_points]


if __name__ == "__main__":

    crs_input1 = {
        'age': '20 years of age',
        'loe': "Doctoral level university degree (PhD)",
        'first_olp': ['IELTS', '6.5', '7.5', '6.0', '7.0'],
        'second_olp': ["TCF Canada", '10-11', '458-502', '342-374', '10-11'],
        'cwe_years': '2 years',
        'marital_status': 'Married',
        'sp_loe': 'One-year program at a university, college, trade or technical school, or other institute',
        'sp_olp': ['IELTS', '6.5', '7.5', '6.0', '7.0'], 
        'sp_cwe_years': '2 years', 
        'fwe_years': '2 years', 
        'have_cq': True, 
        'psd': "Secondary (high school) or less",
        'have_sib': True,
        'noc_skill_type': 'NOC Skill Type 00',
        'nomination': True,
    }

    crs_input2 = {
        'age': '32 years of age',
        'loe': "Two-year program at a university, college, trade or technical school, or other institute",
        'first_olp': ['TEF Canada', '371-392', '298-315', '248-262', '310-348'],
        #'second_olp': ["TCF Canada", '10-11', '458-502', '342-374', '10-11'],
        'cwe_years': 'None or less than a year',
        'marital_status': 'Widowed',
        # 'sp_loe': 'One-year degree, diploma or certificate from  a university, college, trade or technical school, or other institute',
        # 'sp_olp': ['IELTS', '6.5', '7.5', '6.0', '7.0'], 
        # 'sp_cwe_years': '2 years', 
        'fwe_years': '3 years or more', 
        'have_cq': False, 
        'psd': "One- or two-year diploma or certificate",
        'have_sib': True,
        # 'noc_skill_type': 'NOC Skill Type 00',
        'nomination': False,
    }

    crs_input3 = {
        'age': '24 years of age',
        'loe': "Bachelor's degree (three or more year program at a university, college, trade or technical school, or other institute)",
        'first_olp': ['TEF Canada', '349-370', '280-297', '233-247', '371-392'],
        'second_olp': ["CELPIP-G", '8', '7', '9', '4'],
        'cwe_years': '4 years',
        'marital_status': 'Never Married / Single',
        # 'sp_loe': 'One-year degree, diploma or certificate from  a university, college, trade or technical school, or other institute',
        # 'sp_olp': ['IELTS', '6.5', '7.5', '6.0', '7.0'], 
        # 'sp_cwe_years': '2 years', 
        'fwe_years': '1 year', 
        'have_cq': True, 
        # 'psd': "Secondary (high school) or less",
        'have_sib': False,
        'noc_skill_type': 'NOC Skill Level A or B or  any Type 0 other than 00',
        'nomination': False,
    }

    crs_input4 = {
        'age': '45 years of age or more',
        'loe': "Two or more certificates, diplomas, or degrees. One must be for a program of three or more years",
        'first_olp': ['IELTS', '7.0', '7.5', '7.0 - 7.5', '7.0'],
        'second_olp': ["TEF Canada", '393-450', '298-315', '233-247', '310-348'],
        'cwe_years': '5 years or more',
        'marital_status': 'Divorced / Seperated',
        # 'sp_loe': 'One-year degree, diploma or certificate from  a university, college, trade or technical school, or other institute',
        # 'sp_olp': ['IELTS', '6.5', '7.5', '6.0', '7.0'], 
        # 'sp_cwe_years': '2 years', 
        'fwe_years': '3 years or more', 
        'have_cq': True, 
        'psd': "Degree, diploma or certificate of three years or longer OR a Master’s, professional or doctoral degree of at least one academic year",
        'have_sib': False,
        # 'noc_skill_type': 'NOC Skill Level A or B or  any Type 0 other than 00',
        'nomination': False,
    }

    crs_input5 = {
        'age': '17 years of age or less',
        'loe': "One-year program at a university, college, trade or technical school, or other institute",
        'first_olp': ['CELPIP-G', '9', '7', '8', '10 - 12'],
        # 'second_olp': ["TEF Canada", '393-450', '298-315', '233-247', '310-348'],
        'cwe_years': '3 years',
        'marital_status': 'Common-law',
        'sp_loe': 'Doctoral level university degree (PhD)',
        'sp_olp': ['IELTS', '7.0', '8.0', '6.5', '6.5'], 
        'sp_cwe_years': '3 years', 
        'fwe_years': '2 years', 
        'have_cq': False, 
        'psd': "One- or two-year diploma or certificate",
        'have_sib': False,
        'noc_skill_type': 'NOC Skill Level C or D',
        'nomination': True,
    }

    crs = calculate_crs(**crs_input5)
    print(crs)
    tot = 0
    for c in crs:
        tot += c
    print(tot)
    
