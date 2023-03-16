## Engineering Project

### BPMN Diagram

#### Files Architecture:

##### Classes:

![bpmn.png](resources/img/bpmn_classes.png)

- 📄 [process.py](classes%2FBPMN%2Fprocess.py)
- 📄 [lane.py](classes%2FBPMN%2Flane.py)
- 📄 [bpmn_element.py](classes%2FBPMN%2Fbpmn_element.py)
- 📄 [bpmn_diagram.py](classes%2FBPMN%2Fbpmn_diagram.py)

- 📁 Flow:
    - 📄 [flow_object.py](classes%2FBPMN%2Fflow%2Fflow_object.py)

    - 📁 gateway:

        - 📄 [parallel_gateway.py](classes%2FBPMN%2Fflow%2Fgateway%2Fparallel_gateway.py)
        - 📄 [inclusive_gateway.py](classes%2FBPMN%2Fflow%2Fgateway%2Finclusive_gateway.py)
        - 📄 [gateway.py](classes%2FBPMN%2Fflow%2Fgateway%2Fgateway.py)
        - 📄 [exclusive_gateway.py](classes%2FBPMN%2Fflow%2Fgateway%2Fexclusive_gateway.py)
        - 📄 [event_based_gateway.py](classes%2FBPMN%2Fflow%2Fgateway%2Fevent_based_gateway.py)

    - 📁 event:

        - 📄 [start_event.py](classes%2FBPMN%2Fflow%2Fevent%2Fstart_event.py)
        - 📄 [intermediate_event.py](classes%2FBPMN%2Fflow%2Fevent%2Fintermediate_event.py)
        - 📄 [event.py](classes%2FBPMN%2Fflow%2Fevent%2Fevent.py)
        - 📄 [end_event.py](classes%2FBPMN%2Fflow%2Fevent%2Fend_event.py)
    - 📁 activity:
        - 📄 [task.py](classes%2FBPMN%2Fflow%2Factivity%2Ftask.py)
        - 📄 [activity.py](classes%2FBPMN%2Fflow%2Factivity%2Factivity.py)

- 📁 Connecting:
    - 📄 [sequence_flow.py](classes%2FBPMN%2Fconnecting%2Fsequence_flow.py)
    - 📄 [message_flow.py](classes%2FBPMN%2Fconnecting%2Fmessage_flow.py)
    - 📄 [connection_flow.py](classes%2FBPMN%2Fconnecting%2Fconnection_flow.py)
    - 📄 [association.py](classes%2FBPMN%2Fconnecting%2Fassociation.py)

### Petri Network

![petri.png](resources/img/petri_classes.png)

- 📄 [arc.py](classes%2FPETRI%2Farc.py)
- 📄 [petri_net.py](classes%2FPETRI%2Fpetri_net.py)
- 📄 [place.py](classes%2FPETRI%2Fplace.py)
- 📄 [transition.py](classes%2FPETRI%2Ftransition.py)

## Tests

``` shell
./tests.sh
```


## Ressources

- https://scholar.cu.edu.eg/?q=imanhelal/files/is333_mis_lab8_2013.pdf
