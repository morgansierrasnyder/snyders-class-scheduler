# Snyder's Class Scheduler

**Description**: This application will print a class schedule ordering that is consistent with the rules of class prerequisites (i.e. you cannot take a course before you take its prerequisite)

## Dependencies

Python 2

## Getting Started

1. Download and unzip snyders_class_scheduler.zip
2. Open Terminal or Command Prompt, and navigate to the top level directory
3. Ensure the application has permission to run as an executable by entering:
```
	$ chmod +x scheduler
```
3. Attempt to run the scheduler on one of the test files:
```
	$ ./scheduler test/premed.json
```

## Usage

Now, you can run the scheduler on any JSON file containing correctly formatted class data, by passing the filepath/filename as the argument to the ./scheduler command. Only one file at a time, please!

The JSON input files should follow this general format:

```
[
    {
        "name": "Class 1",
        "prerequisites": []
    },
    {
        "name": "Class 2",
        "prerequisites": ["Class 1"]
    }
]
```
## Security

Depending on the source of your data files, you may require data validation.

If you created the files, they are surely flawless.

If you didn't, it may be good to check that they are correctly formatted, contain valid prerequisites, and do not contain cyclical dependencies. To do so, turn on the data validation flags at the top of src/scheduler_script.py by setting them to 1:

```
FORMAT_CHECK = 1 # If 1, check for correct format of JSON datastructure
EXIST_CHECK = 1 # If 1, check for invalid prerequisites in JSON
CYCLE_CHECK = 1 # If 1, check for cyclical relationships in JSON
```

Please note that turning on these flags will increase the runtime of the application.

## Testing

1. Navigate to the test/ directory
2. Run $ python scheduler_tests.py to launch the SchedulerTests

In addition, there is a collection of both valid and invalid JSON data files in the test/ directory that can be used to test the command line output empirically.

## Performance Analysis

The scheduling algorithm used in this application is a recursive depth-first search over all connected components of the class "tree":
```
For each class:
	If this class was already scheduled, continue
	If this class has prerequisites, recurse to schedule those first
	schedule this class
```

Given that the input data uses adjacency lists to store information about prerequisties, the runtime of this solution is

**O(V + E)**

where V represents the number of classes, and E represents the number of class <> prerequisite relationships

## Known issues

Checking for cyclical dependencies with the CYCLE_CHECK flag on is only supported for first order cycles. For example, when Class 1 has prerequisite Class 2 and Class 2 has prerequisite Class 1.

Cycle checking at any depth will be supported in version 2.0!

## Getting help

Email me at m.sierrasnyder@gmail.com!

## Credits and references

1. Clever
2. Guido van Rossum
3. Siddhartha Gautama
