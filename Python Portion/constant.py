# this file is used for constants values
import pygsheets

# variables for where to split text into phrases
split = [", ", ". ", " and ", " but "]

# hardcode derogatory words in


blacklist = {
    "Racism" : "",
    "Albeism" : {
        "Impairment, Special Need, Deficit | Disability",
        "Wheelchair bound, Confined to a wheelchair, Handicapped, Differently abled, Lame, Crip, Cripple, Gimp, Spastic, Spaz, Physically challenged, Handicapped, Wheelz, Speed Racer, Speedy | Wheelchair user, Disabled, People with Disabilities or PWDs, has [insert disability], Physically disabled",
        } 
}

synonym = {
    "Impairment, Deficit" : "Disability",
    "Special Need" : "Disability",
    "Deficit" : "Disability",
    "Wheelchair bound, Confined to a wheelchair, Handicapped, Differently abled, Lame, Crip, Cripple, Gimp, Spastic, Spaz, Physically challenged, Handicapable, Wheelz, Speed Racer, Speedy" : "Wheelchair user, Disabled, People with Disabilities or PWDs, has [insert disability], Physically disabled",
    "Retarded, Feeble-minded, Slow/Delayed, Developmental delay,  Mentally deficient, Stupid, Dumb,  Dimwitted, Idiot" : "Person with a Developmental Disability, Person with an Intellectual Disability,  Person with Down Syndrome, Intellectually Disabled, Developmentally Disabled",
    "Psychotic, Mad, Crazy, Demented, Mental, Loony, Nutjob, Nutso, Whacko, Psychopath, Crazed, Psycho, Deranged, Lunatic" : "Psychiatric disability/diagnosis, psychosocial disability, person with [specific diagnosis/disability]",
    "Aspie, Person with autism" : "Autistic, Neurodivergent",
    "Midget" : "Dwarf, little person",
    "Patient" : "*(Refer to them by name or identity choice)",
    "Nuthouse, Loony Bin" : "Asylum, Institution",
    "Normal, Whole, Able-Bodied, Healthy" : "Nondisabled, Neurotypical *(for non-autistic)",
    "Deaf-and-Dumb, Hearing Impaired" : "Deaf, Hard of Hearing",
    "Mute" : "Doesn't communicate verbally, Doesn't speak verbally", 
    "High functioning, Low Functioning" : "*(Most autistic people say they have moments of both and prefer no functioning labels)", 
    "Visually impaired" : "Blind, Low vision", 
    "Special needs" : "Accommodations, Modifications", 
    "Epileptic fit" : "Seizure",
    "Sufferers, Suffers from, Afflicted, Stricken with" : "has [disability]",
    "Victim" : "Survivor *(unless a victim of murder)"
    ""
}