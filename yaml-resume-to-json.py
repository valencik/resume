import json
import jsonschema
import yaml
 
# Load the JSON Resume schema from current directory or GitHub
try:
   schema = open("schema.json").read()
except:
   import requests
   schema = requests.get("https://raw.githubusercontent.com/jsonresume/resume-schema/master/schema.json").text

# Load the resume and parse as YAML data
data = yaml.load(open("resume.yaml", mode='r'))
 
# Validate the resume against the schema
try:
    v = jsonschema.Draft3Validator(json.loads(schema))
    # Lazily report all errors in the instance
    for error in sorted(v.iter_errors(data), key=str):
        print(error.message)
    # Write out the pretty printed JSON
    with open('resume.json', mode='w') as resume_out:
        json.dump(data, resume_out, sort_keys=True, indent=4)
except jsonschema.ValidationError as e:
    print(e.message)
