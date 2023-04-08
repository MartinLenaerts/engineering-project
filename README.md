## Engineering Project

## Installation

```
pip install -r requirement.txt
```

## Usages 

### With `Python`

```
usage: main.py [-h] [-f FILENAME] [-o {png,txt}] [--keep]

Script to translate bpmn diagram to petri net

options:
  -h, --help            show this help message and exit
  -f FILENAME, --filename FILENAME
                        BPMN file to translate (.bpmn file), if this argument
                        is not given, all the files in the folder
                        "resources/bpmn_diagrams" will be translated
  -o {png,txt}, --output {png,txt}
                        output type (png or txt)
  --keep                Save the output file(s) in the same location as the
                        .bpmn file. if this argument is not given, the file(s)
                        will be saved here: "cache/petri_output"
```

### With `Docker`

```
docker-compose up --build
```

## Tests

``` shell
make test
```

or if you want the code coverage 

``` shell
make test-coverage
```


## Examples
<div style="background: white">

|                                              bpmn                                              |                                              petri                                              |
|:----------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------:|
| ![start_decision_tasks_ends.png](resources%2Fimg%2Fbpmn_parts%2Fstart_decision_tasks_ends.png) | ![start_decision_tasks_ends.png](resources%2Fimg%2Fpetri_parts%2Fstart_decision_tasks_ends.png) |
|     ![start_fork_tasks_ends.png](resources%2Fimg%2Fbpmn_parts%2Fstart_fork_tasks_ends.png)     |     ![start_fork_tasks_ends.png](resources%2Fimg%2Fpetri_parts%2Fstart_fork_tasks_ends.png)     |
|            ![start_task_end.png](resources%2Fimg%2Fbpmn_parts%2Fstart_task_end.png)            |            ![start_task_end.png](resources%2Fimg%2Fpetri_parts%2Fstart_task_end.png)            |
|      ![starts_join_task_end.png](resources%2Fimg%2Fbpmn_parts%2Fstarts_join_task_end.png)      |      ![starts_join_task_end.png](resources%2Fimg%2Fpetri_parts%2Fstarts_join_task_end.png)      |
|     ![starts_merge_task_end.png](resources%2Fimg%2Fbpmn_parts%2Fstarts_merge_task_end.png)     |     ![starts_merge_task_end.png](resources%2Fimg%2Fpetri_parts%2Fstarts_merge_task_end.png)     |
|     ![starts_processes_ends.png](resources%2Fimg%2Fbpmn_parts%2Fstarts_processes_ends.png)     |     ![starts_processes_ends.png](resources%2Fimg%2Fpetri_parts%2Fstarts_processes_ends.png)     |

</div>

### BPMN Diagram

#### Files Architecture:

##### Classes:

![bpmn.png](resources/img/bpmn_classes.png)

### Petri Network

![petri.png](resources/img/petri_classes.png)

## Ressources

![mapping_table.png](resources%2Fimg%2Fmapping_table.png)

- https://www.researchgate.net/publication/27467826_Formal_Semantics_and_Automated_Analysis_of_BPMN_Process_Models
- http://didattica.cs.unicam.it/old/lib/exe/fetch.php?media=didattica:magistrale:ebpm:ay_1819:slide_11_-_mapping_from_bpmn_to_petrinets.pdf

