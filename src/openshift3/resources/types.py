
# XXX This code file has been automatically generated. Do not edit it.

from .base import Resource, register_model


@register_model
class versioned_Event(Resource):

    __kind__ = '*versioned.Event'

    __fields__ = {
    }

    __types__ = {
    }

    __required__ = set()


    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class types_UID(Resource):

    __kind__ = 'types.UID'

    __fields__ = {
    }

    __types__ = {
    }

    __required__ = set()


    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class unversioned_APIResource(Resource):

    """APIResource specifies the name of a resource and whether it is
    namespaced."""

    __kind__ = 'unversioned.APIResource'

    __fields__ = {
        'name': 'name',
        'namespaced': 'namespaced',
        'kind': 'kind',
    }

    __types__ = {
    }

    __required__ = set([
        'kind',
        'name',
        'namespaced',
    ])

    name = None # string (required)
    namespaced = None # boolean (required)
    kind = None # string (required)

    def __init__(self, *, kind, name, namespaced, **_kwargs_):

        self.kind = 'APIResource'

        self.kind = kind
        self.name = name
        self.namespaced = namespaced

        super().__init__(**_kwargs_)

@register_model
class unversioned_APIResourceList(Resource):

    """APIResourceList is a list of APIResource, it is used to expose the
    name of the resources supported in a specific group and version,
    and if the resource is namespaced."""

    __kind__ = 'unversioned.APIResourceList'

    __fields__ = {
        'api_version': 'apiVersion',
        'resources': 'resources',
        'group_version': 'groupVersion',
        'kind': 'kind',
    }

    __types__ = {
        'resources': 'unversioned.APIResource',
    }

    __required__ = set([
        'group_version',
        'resources',
    ])

    api_version = None # string
    resources = None # array (required)
    group_version = None # string (required)
    kind = None # string

    def __init__(self, *, group_version, resources, **_kwargs_):

        self.kind = 'APIResource'

        self.group_version = group_version
        self.resources = resources

        super().__init__(**_kwargs_)

@register_model
class unversioned_LabelSelector(Resource):

    """A label selector is a label query over a set of resources. The result
    of matchLabels and matchExpressions are ANDed. An empty label
    selector matches all objects. A null label selector matches no
    objects."""

    __kind__ = 'unversioned.LabelSelector'

    __fields__ = {
        'match_expressions': 'matchExpressions',
        'match_labels': 'matchLabels',
    }

    __types__ = {
        'match_expressions': 'unversioned.LabelSelectorRequirement',
    }

    __required__ = set()

    match_expressions = None # array
    match_labels = None # object

    def __init__(self, **_kwargs_):
        self.match_expressions = []

        super().__init__(**_kwargs_)

@register_model
class unversioned_LabelSelectorRequirement(Resource):

    """A label selector requirement is a selector that contains values, a
    key, and an operator that relates the key and values."""

    __kind__ = 'unversioned.LabelSelectorRequirement'

    __fields__ = {
        'operator': 'operator',
        'values': 'values',
        'key': 'key',
    }

    __types__ = {
    }

    __required__ = set([
        'key',
        'operator',
    ])

    operator = None # string (required)
    values = None # array
    key = None # string (required)

    def __init__(self, *, key, operator, **_kwargs_):
        self.values = []

        self.key = key
        self.operator = operator

        super().__init__(**_kwargs_)

@register_model
class unversioned_ListMeta(Resource):

    """ListMeta describes metadata that synthetic resources must have,
    including lists and various status objects. A resource may have
    only one of {ObjectMeta, ListMeta}."""

    __kind__ = 'unversioned.ListMeta'

    __fields__ = {
        'resource_version': 'resourceVersion',
        'self_link': 'selfLink',
    }

    __types__ = {
    }

    __required__ = set()

    resource_version = None # string
    self_link = None # string

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class unversioned_Patch(Resource):

    """Patch is provided to give a concrete name and type to the Kubernetes
    PATCH request body."""

    __kind__ = 'unversioned.Patch'

    __fields__ = {
    }

    __types__ = {
    }

    __required__ = set()


    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class unversioned_Status(Resource):

    """Status is a return value for calls that don't return other objects."""

    __kind__ = 'unversioned.Status'

    __fields__ = {
        'details': 'details',
        'api_version': 'apiVersion',
        'reason': 'reason',
        'metadata': 'metadata',
        'message': 'message',
        'status': 'status',
        'code': 'code',
        'kind': 'kind',
    }

    __types__ = {
        'details': 'unversioned.StatusDetails',
        'metadata': 'unversioned.ListMeta',
    }

    __required__ = set()

    details = None # unversioned.StatusDetails
    api_version = None # string
    reason = None # string
    metadata = None # unversioned.ListMeta
    message = None # string
    status = None # string
    code = None # integer
    kind = None # string

    def __init__(self, **_kwargs_):

        self.kind = 'ListMeta'

        super().__init__(**_kwargs_)

@register_model
class unversioned_StatusCause(Resource):

    """StatusCause provides more information about an api.Status failure,
    including cases when multiple errors are encountered."""

    __kind__ = 'unversioned.StatusCause'

    __fields__ = {
        'field': 'field',
        'reason': 'reason',
        'message': 'message',
    }

    __types__ = {
    }

    __required__ = set()

    field = None # string
    reason = None # string
    message = None # string

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class unversioned_StatusDetails(Resource):

    """StatusDetails is a set of additional properties that MAY be set by the
    server to provide additional information about a response. The
    Reason field of a Status object defines what attributes will be
    set. Clients must ignore fields that do not match the defined type
    of each attribute, and should assume that any attribute may be
    empty, invalid, or under defined."""

    __kind__ = 'unversioned.StatusDetails'

    __fields__ = {
        'name': 'name',
        'retry_after_seconds': 'retryAfterSeconds',
        'causes': 'causes',
        'group': 'group',
        'kind': 'kind',
    }

    __types__ = {
        'causes': 'unversioned.StatusCause',
    }

    __required__ = set()

    name = None # string
    retry_after_seconds = None # integer
    causes = None # array
    group = None # string
    kind = None # string

    def __init__(self, **_kwargs_):
        self.causes = []

        self.kind = 'StatusCause'

        super().__init__(**_kwargs_)

@register_model
class v1_AWSElasticBlockStoreVolumeSource(Resource):

    """Represents a Persistent Disk resource in AWS.  An AWS EBS disk must
    exist before mounting to a container. The disk must also be in the
    same AWS zone as the kubelet. An AWS EBS disk can only be mounted
    as read/write once. AWS EBS volumes support ownership management
    and SELinux relabeling."""

    __kind__ = 'v1.AWSElasticBlockStoreVolumeSource'

    __fields__ = {
        'read_only': 'readOnly',
        'volume_id': 'volumeID',
        'partition': 'partition',
        'fs_type': 'fsType',
    }

    __types__ = {
    }

    __required__ = set([
        'volume_id',
    ])

    read_only = None # boolean
    volume_id = None # string (required)
    partition = None # integer
    fs_type = None # string

    def __init__(self, *, volume_id, **_kwargs_):

        self.volume_id = volume_id

        super().__init__(**_kwargs_)

@register_model
class v1_AttachedVolume(Resource):

    """AttachedVolume describes a volume attached to a node"""

    __kind__ = 'v1.AttachedVolume'

    __fields__ = {
        'name': 'name',
        'device_path': 'devicePath',
    }

    __types__ = {
    }

    __required__ = set([
        'device_path',
        'name',
    ])

    name = None # string (required)
    device_path = None # string (required)

    def __init__(self, *, device_path, name, **_kwargs_):

        self.device_path = device_path
        self.name = name

        super().__init__(**_kwargs_)

@register_model
class v1_AzureFileVolumeSource(Resource):

    """AzureFile represents an Azure File Service mount on the host and bind
    mount to the pod."""

    __kind__ = 'v1.AzureFileVolumeSource'

    __fields__ = {
        'share_name': 'shareName',
        'read_only': 'readOnly',
        'secret_name': 'secretName',
    }

    __types__ = {
    }

    __required__ = set([
        'secret_name',
        'share_name',
    ])

    share_name = None # string (required)
    read_only = None # boolean
    secret_name = None # string (required)

    def __init__(self, *, secret_name, share_name, **_kwargs_):

        self.secret_name = secret_name
        self.share_name = share_name

        super().__init__(**_kwargs_)

@register_model
class v1_Binding(Resource):

    """Binding ties one object to another. For example, a pod is bound to a
    node by a scheduler."""

    __kind__ = 'v1.Binding'

    __fields__ = {
        'target': 'target',
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'kind': 'kind',
    }

    __types__ = {
        'target': 'v1.ObjectReference',
        'metadata': 'v1.ObjectMeta',
    }

    __required__ = set([
        'target',
    ])

    target = None # v1.ObjectReference (required)
    metadata = None # v1.ObjectMeta
    api_version = None # string
    kind = None # string

    def __init__(self, *, target, **_kwargs_):

        self.kind = 'ObjectMeta'

        self.target = target

        super().__init__(**_kwargs_)

@register_model
class v1_Capabilities(Resource):

    """Adds and removes POSIX capabilities from running containers."""

    __kind__ = 'v1.Capabilities'

    __fields__ = {
        'drop': 'drop',
        'add': 'add',
    }

    __types__ = {
        'add': 'v1.Capability',
    }

    __required__ = set()

    drop = None # array
    add = None # array

    def __init__(self, **_kwargs_):
        self.drop = []
        self.add = []

        super().__init__(**_kwargs_)

@register_model
class v1_Capability(Resource):

    __kind__ = 'v1.Capability'

    __fields__ = {
    }

    __types__ = {
    }

    __required__ = set()


    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_CephFSVolumeSource(Resource):

    """Represents a Ceph Filesystem mount that lasts the lifetime of a pod
    Cephfs volumes do not support ownership management or SELinux
    relabeling."""

    __kind__ = 'v1.CephFSVolumeSource'

    __fields__ = {
        'monitors': 'monitors',
        'secret_file': 'secretFile',
        'read_only': 'readOnly',
        'user': 'user',
        'path': 'path',
        'secret_ref': 'secretRef',
    }

    __types__ = {
        'secret_ref': 'v1.LocalObjectReference',
    }

    __required__ = set([
        'monitors',
    ])

    monitors = None # array (required)
    secret_file = None # string
    read_only = None # boolean
    user = None # string
    path = None # string
    secret_ref = None # v1.LocalObjectReference

    def __init__(self, *, monitors, **_kwargs_):

        self.monitors = monitors

        super().__init__(**_kwargs_)

@register_model
class v1_CinderVolumeSource(Resource):

    """Represents a cinder volume resource in Openstack. A Cinder volume must
    exist before mounting to a container. The volume must also be in
    the same region as the kubelet. Cinder volumes support ownership
    management and SELinux relabeling."""

    __kind__ = 'v1.CinderVolumeSource'

    __fields__ = {
        'read_only': 'readOnly',
        'volume_id': 'volumeID',
        'fs_type': 'fsType',
    }

    __types__ = {
    }

    __required__ = set([
        'volume_id',
    ])

    read_only = None # boolean
    volume_id = None # string (required)
    fs_type = None # string

    def __init__(self, *, volume_id, **_kwargs_):

        self.volume_id = volume_id

        super().__init__(**_kwargs_)

@register_model
class v1_ComponentCondition(Resource):

    """Information about the condition of a component."""

    __kind__ = 'v1.ComponentCondition'

    __fields__ = {
        'message': 'message',
        'type': 'type',
        'error': 'error',
        'status': 'status',
    }

    __types__ = {
    }

    __required__ = set([
        'status',
        'type',
    ])

    message = None # string
    type = None # string (required)
    error = None # string
    status = None # string (required)

    def __init__(self, *, status, type, **_kwargs_):

        self.status = status
        self.type = type

        super().__init__(**_kwargs_)

@register_model
class v1_ComponentStatus(Resource):

    """ComponentStatus (and ComponentStatusList) holds the cluster validation
    info."""

    __kind__ = 'v1.ComponentStatus'

    __fields__ = {
        'conditions': 'conditions',
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'kind': 'kind',
    }

    __types__ = {
        'conditions': 'v1.ComponentCondition',
        'metadata': 'v1.ObjectMeta',
    }

    __required__ = set()

    conditions = None # array
    metadata = None # v1.ObjectMeta
    api_version = None # string
    kind = None # string

    def __init__(self, **_kwargs_):
        self.conditions = []

        self.kind = 'ObjectMeta'

        super().__init__(**_kwargs_)

@register_model
class v1_ComponentStatusList(Resource):

    """Status of all the conditions for the component as a list of
    ComponentStatus objects."""

    __kind__ = 'v1.ComponentStatusList'

    __fields__ = {
        'items': 'items',
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'kind': 'kind',
    }

    __types__ = {
        'items': 'v1.ComponentStatus',
        'metadata': 'unversioned.ListMeta',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    metadata = None # unversioned.ListMeta
    api_version = None # string
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'ListMeta'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_ConfigMap(Resource):

    """ConfigMap holds configuration data for pods to consume."""

    __kind__ = 'v1.ConfigMap'

    __fields__ = {
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'data': 'data',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
    }

    __required__ = set()

    metadata = None # v1.ObjectMeta
    api_version = None # string
    data = None # object
    kind = None # string

    def __init__(self, **_kwargs_):

        self.kind = 'ObjectMeta'

        super().__init__(**_kwargs_)

@register_model
class v1_ConfigMapKeySelector(Resource):

    """Selects a key from a ConfigMap."""

    __kind__ = 'v1.ConfigMapKeySelector'

    __fields__ = {
        'name': 'name',
        'key': 'key',
    }

    __types__ = {
    }

    __required__ = set([
        'key',
    ])

    name = None # string
    key = None # string (required)

    def __init__(self, *, key, **_kwargs_):

        self.key = key

        super().__init__(**_kwargs_)

@register_model
class v1_ConfigMapList(Resource):

    """ConfigMapList is a resource containing a list of ConfigMap objects."""

    __kind__ = 'v1.ConfigMapList'

    __fields__ = {
        'items': 'items',
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'kind': 'kind',
    }

    __types__ = {
        'items': 'v1.ConfigMap',
        'metadata': 'unversioned.ListMeta',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    metadata = None # unversioned.ListMeta
    api_version = None # string
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'ListMeta'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_ConfigMapVolumeSource(Resource):

    """Adapts a ConfigMap into a volume.  The contents of the target
    ConfigMap's Data field will be presented in a volume as files
    using the keys in the Data field as the file names, unless the
    items element is populated with specific mappings of keys to
    paths. ConfigMap volumes support ownership management and SELinux
    relabeling."""

    __kind__ = 'v1.ConfigMapVolumeSource'

    __fields__ = {
        'name': 'name',
        'items': 'items',
    }

    __types__ = {
        'items': 'v1.KeyToPath',
    }

    __required__ = set()

    name = None # string
    items = None # array

    def __init__(self, **_kwargs_):
        self.items = []

        super().__init__(**_kwargs_)

@register_model
class v1_Container(Resource):

    """A single application container that you want to run within a pod."""

    __kind__ = 'v1.Container'

    __fields__ = {
        'name': 'name',
        'ports': 'ports',
        'stdin_once': 'stdinOnce',
        'command': 'command',
        'stdin': 'stdin',
        'liveness_probe': 'livenessProbe',
        'readiness_probe': 'readinessProbe',
        'args': 'args',
        'env': 'env',
        'lifecycle': 'lifecycle',
        'termination_message_path': 'terminationMessagePath',
        'image_pull_policy': 'imagePullPolicy',
        'resources': 'resources',
        'volume_mounts': 'volumeMounts',
        'security_context': 'securityContext',
        'tty': 'tty',
        'working_dir': 'workingDir',
        'image': 'image',
    }

    __types__ = {
        'readiness_probe': 'v1.Probe',
        'env': 'v1.EnvVar',
        'lifecycle': 'v1.Lifecycle',
        'security_context': 'v1.SecurityContext',
        'liveness_probe': 'v1.Probe',
        'volume_mounts': 'v1.VolumeMount',
        'ports': 'v1.ContainerPort',
        'resources': 'v1.ResourceRequirements',
    }

    __required__ = set([
        'name',
    ])

    name = None # string (required)
    ports = None # array
    stdin_once = None # boolean
    command = None # array
    stdin = None # boolean
    liveness_probe = None # v1.Probe
    readiness_probe = None # v1.Probe
    args = None # array
    env = None # array
    lifecycle = None # v1.Lifecycle
    termination_message_path = None # string
    image_pull_policy = None # string
    resources = None # v1.ResourceRequirements
    volume_mounts = None # array
    security_context = None # v1.SecurityContext
    tty = None # boolean
    working_dir = None # string
    image = None # string

    def __init__(self, *, name, **_kwargs_):
        self.ports = []
        self.command = []
        self.args = []
        self.env = []
        self.volume_mounts = []

        self.name = name

        super().__init__(**_kwargs_)

@register_model
class v1_ContainerImage(Resource):

    """Describe a container image"""

    __kind__ = 'v1.ContainerImage'

    __fields__ = {
        'names': 'names',
        'size_bytes': 'sizeBytes',
    }

    __types__ = {
    }

    __required__ = set([
        'names',
    ])

    names = None # array (required)
    size_bytes = None # integer

    def __init__(self, *, names, **_kwargs_):

        self.names = names

        super().__init__(**_kwargs_)

@register_model
class v1_ContainerPort(Resource):

    """ContainerPort represents a network port in a single container."""

    __kind__ = 'v1.ContainerPort'

    __fields__ = {
        'name': 'name',
        'protocol': 'protocol',
        'host_port': 'hostPort',
        'container_port': 'containerPort',
        'host_ip': 'hostIP',
    }

    __types__ = {
    }

    __required__ = set([
        'container_port',
    ])

    name = None # string
    protocol = None # string
    host_port = None # integer
    container_port = None # integer (required)
    host_ip = None # string

    def __init__(self, *, container_port, **_kwargs_):

        self.container_port = container_port

        super().__init__(**_kwargs_)

@register_model
class v1_ContainerState(Resource):

    """ContainerState holds a possible state of container. Only one of its
    members may be specified. If none of them is specified, the
    default one is ContainerStateWaiting."""

    __kind__ = 'v1.ContainerState'

    __fields__ = {
        'waiting': 'waiting',
        'terminated': 'terminated',
        'running': 'running',
    }

    __types__ = {
        'waiting': 'v1.ContainerStateWaiting',
        'terminated': 'v1.ContainerStateTerminated',
        'running': 'v1.ContainerStateRunning',
    }

    __required__ = set()

    waiting = None # v1.ContainerStateWaiting
    terminated = None # v1.ContainerStateTerminated
    running = None # v1.ContainerStateRunning

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_ContainerStateRunning(Resource):

    """ContainerStateRunning is a running state of a container."""

    __kind__ = 'v1.ContainerStateRunning'

    __fields__ = {
        'started_at': 'startedAt',
    }

    __types__ = {
    }

    __required__ = set()

    started_at = None # string

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_ContainerStateTerminated(Resource):

    """ContainerStateTerminated is a terminated state of a container."""

    __kind__ = 'v1.ContainerStateTerminated'

    __fields__ = {
        'reason': 'reason',
        'finished_at': 'finishedAt',
        'container_id': 'containerID',
        'exit_code': 'exitCode',
        'message': 'message',
        'started_at': 'startedAt',
        'signal': 'signal',
    }

    __types__ = {
    }

    __required__ = set([
        'exit_code',
    ])

    reason = None # string
    finished_at = None # string
    container_id = None # string
    exit_code = None # integer (required)
    message = None # string
    started_at = None # string
    signal = None # integer

    def __init__(self, *, exit_code, **_kwargs_):

        self.exit_code = exit_code

        super().__init__(**_kwargs_)

@register_model
class v1_ContainerStateWaiting(Resource):

    """ContainerStateWaiting is a waiting state of a container."""

    __kind__ = 'v1.ContainerStateWaiting'

    __fields__ = {
        'reason': 'reason',
        'message': 'message',
    }

    __types__ = {
    }

    __required__ = set()

    reason = None # string
    message = None # string

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_ContainerStatus(Resource):

    """ContainerStatus contains details for the current status of this
    container."""

    __kind__ = 'v1.ContainerStatus'

    __fields__ = {
        'name': 'name',
        'ready': 'ready',
        'image_id': 'imageID',
        'state': 'state',
        'container_id': 'containerID',
        'image': 'image',
        'last_state': 'lastState',
        'restart_count': 'restartCount',
    }

    __types__ = {
        'last_state': 'v1.ContainerState',
        'state': 'v1.ContainerState',
    }

    __required__ = set([
        'image',
        'image_id',
        'name',
        'ready',
        'restart_count',
    ])

    name = None # string (required)
    ready = None # boolean (required)
    image_id = None # string (required)
    state = None # v1.ContainerState
    container_id = None # string
    image = None # string (required)
    last_state = None # v1.ContainerState
    restart_count = None # integer (required)

    def __init__(self, *, image, image_id, name, ready, restart_count, **_kwargs_):

        self.image = image
        self.image_id = image_id
        self.name = name
        self.ready = ready
        self.restart_count = restart_count

        super().__init__(**_kwargs_)

@register_model
class v1_DaemonEndpoint(Resource):

    """DaemonEndpoint contains information about a single Daemon endpoint."""

    __kind__ = 'v1.DaemonEndpoint'

    __fields__ = {
        'port': 'Port',
    }

    __types__ = {
    }

    __required__ = set([
        'port',
    ])

    port = None # integer (required)

    def __init__(self, *, port, **_kwargs_):

        self.port = port

        super().__init__(**_kwargs_)

@register_model
class v1_DeleteOptions(Resource):

    """DeleteOptions may be provided when deleting an API object"""

    __kind__ = 'v1.DeleteOptions'

    __fields__ = {
        'preconditions': 'preconditions',
        'api_version': 'apiVersion',
        'grace_period_seconds': 'gracePeriodSeconds',
        'orphan_dependents': 'orphanDependents',
        'kind': 'kind',
    }

    __types__ = {
        'preconditions': 'v1.Preconditions',
    }

    __required__ = set()

    preconditions = None # v1.Preconditions
    api_version = None # string
    grace_period_seconds = None # integer
    orphan_dependents = None # boolean
    kind = None # string

    def __init__(self, **_kwargs_):

        self.kind = 'Preconditions'

        super().__init__(**_kwargs_)

@register_model
class v1_DeprecatedDownwardAPIVolumeFile(Resource):

    """DeprecatedDownwardAPIVolumeFile represents information to create the
    file containing the pod field This type is deprecated and should
    be replaced by use of the downwardAPI volume source."""

    __kind__ = 'v1.DeprecatedDownwardAPIVolumeFile'

    __fields__ = {
        'name': 'name',
        'field_ref': 'fieldRef',
        'resource_field_ref': 'resourceFieldRef',
    }

    __types__ = {
        'field_ref': 'v1.ObjectFieldSelector',
        'resource_field_ref': 'v1.ResourceFieldSelector',
    }

    __required__ = set([
        'name',
    ])

    name = None # string (required)
    field_ref = None # v1.ObjectFieldSelector
    resource_field_ref = None # v1.ResourceFieldSelector

    def __init__(self, *, name, **_kwargs_):

        self.name = name

        super().__init__(**_kwargs_)

@register_model
class v1_DeprecatedDownwardAPIVolumeSource(Resource):

    """DeprecatedDownwardAPIVolumeSource represents a volume containing
    downward API info. This type is deprecated and should be replaced
    by use of the downwardAPI volume source."""

    __kind__ = 'v1.DeprecatedDownwardAPIVolumeSource'

    __fields__ = {
        'items': 'items',
    }

    __types__ = {
        'items': 'v1.DeprecatedDownwardAPIVolumeFile',
    }

    __required__ = set()

    items = None # array

    def __init__(self, **_kwargs_):
        self.items = []

        super().__init__(**_kwargs_)

@register_model
class v1_DownwardAPIVolumeFile(Resource):

    """DownwardAPIVolumeFile represents information to create the file
    containing the pod field"""

    __kind__ = 'v1.DownwardAPIVolumeFile'

    __fields__ = {
        'path': 'path',
        'field_ref': 'fieldRef',
        'resource_field_ref': 'resourceFieldRef',
    }

    __types__ = {
        'field_ref': 'v1.ObjectFieldSelector',
        'resource_field_ref': 'v1.ResourceFieldSelector',
    }

    __required__ = set([
        'path',
    ])

    path = None # string (required)
    field_ref = None # v1.ObjectFieldSelector
    resource_field_ref = None # v1.ResourceFieldSelector

    def __init__(self, *, path, **_kwargs_):

        self.path = path

        super().__init__(**_kwargs_)

@register_model
class v1_DownwardAPIVolumeSource(Resource):

    """DownwardAPIVolumeSource represents a volume containing downward API
    info. Downward API volumes support ownership management and
    SELinux relabeling."""

    __kind__ = 'v1.DownwardAPIVolumeSource'

    __fields__ = {
        'items': 'items',
    }

    __types__ = {
        'items': 'v1.DownwardAPIVolumeFile',
    }

    __required__ = set()

    items = None # array

    def __init__(self, **_kwargs_):
        self.items = []

        super().__init__(**_kwargs_)

@register_model
class v1_EmptyDirVolumeSource(Resource):

    """Represents an empty directory for a pod. Empty directory volumes
    support ownership management and SELinux relabeling."""

    __kind__ = 'v1.EmptyDirVolumeSource'

    __fields__ = {
        'medium': 'medium',
    }

    __types__ = {
    }

    __required__ = set()

    medium = None # string

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_EndpointAddress(Resource):

    """EndpointAddress is a tuple that describes single IP address."""

    __kind__ = 'v1.EndpointAddress'

    __fields__ = {
        'hostname': 'hostname',
        'ip': 'ip',
        'target_ref': 'targetRef',
    }

    __types__ = {
        'target_ref': 'v1.ObjectReference',
    }

    __required__ = set([
        'ip',
    ])

    hostname = None # string
    ip = None # string (required)
    target_ref = None # v1.ObjectReference

    def __init__(self, *, ip, **_kwargs_):

        self.ip = ip

        super().__init__(**_kwargs_)

@register_model
class v1_EndpointPort(Resource):

    """EndpointPort is a tuple that describes a single port."""

    __kind__ = 'v1.EndpointPort'

    __fields__ = {
        'name': 'name',
        'protocol': 'protocol',
        'port': 'port',
    }

    __types__ = {
    }

    __required__ = set([
        'port',
    ])

    name = None # string
    protocol = None # string
    port = None # integer (required)

    def __init__(self, *, port, **_kwargs_):

        self.port = port

        super().__init__(**_kwargs_)

@register_model
class v1_EndpointSubset(Resource):

    """EndpointSubset is a group of addresses with a common set of ports. The
    expanded set of endpoints is the Cartesian product of Addresses x
    Ports. For example, given:   {     Addresses: [{"ip":
    "10.10.1.1"}, {"ip": "10.10.2.2"}],     Ports:     [{"name": "a",
    "port": 8675}, {"name": "b", "port": 309}]   } The resulting set
    of endpoints can be viewed as:     a: [ 10.10.1.1:8675,
    10.10.2.2:8675 ],     b: [ 10.10.1.1:309, 10.10.2.2:309 ]"""

    __kind__ = 'v1.EndpointSubset'

    __fields__ = {
        'addresses': 'addresses',
        'ports': 'ports',
        'not_ready_addresses': 'notReadyAddresses',
    }

    __types__ = {
        'addresses': 'v1.EndpointAddress',
        'not_ready_addresses': 'v1.EndpointAddress',
        'ports': 'v1.EndpointPort',
    }

    __required__ = set()

    addresses = None # array
    ports = None # array
    not_ready_addresses = None # array

    def __init__(self, **_kwargs_):
        self.addresses = []
        self.ports = []
        self.not_ready_addresses = []

        super().__init__(**_kwargs_)

@register_model
class v1_Endpoints(Resource):

    """Endpoints is a collection of endpoints that implement the actual
    service. Example:   Name: "mysvc",   Subsets: [     {
    Addresses: [{"ip": "10.10.1.1"}, {"ip": "10.10.2.2"}],
    Ports: [{"name": "a", "port": 8675}, {"name": "b", "port": 309}]
    },     {       Addresses: [{"ip": "10.10.3.3"}],       Ports:
    [{"name": "a", "port": 93}, {"name": "b", "port": 76}]     },  ]"""

    __kind__ = 'v1.Endpoints'

    __fields__ = {
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'subsets': 'subsets',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
        'subsets': 'v1.EndpointSubset',
    }

    __required__ = set([
        'subsets',
    ])

    metadata = None # v1.ObjectMeta
    api_version = None # string
    subsets = None # array (required)
    kind = None # string

    def __init__(self, *, subsets, **_kwargs_):

        self.kind = 'EndpointSubset'

        self.subsets = subsets

        super().__init__(**_kwargs_)

@register_model
class v1_EndpointsList(Resource):

    """EndpointsList is a list of endpoints."""

    __kind__ = 'v1.EndpointsList'

    __fields__ = {
        'items': 'items',
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'kind': 'kind',
    }

    __types__ = {
        'items': 'v1.Endpoints',
        'metadata': 'unversioned.ListMeta',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    metadata = None # unversioned.ListMeta
    api_version = None # string
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'ListMeta'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_EnvVar(Resource):

    """EnvVar represents an environment variable present in a Container."""

    __kind__ = 'v1.EnvVar'

    __fields__ = {
        'name': 'name',
        'value': 'value',
        'value_from': 'valueFrom',
    }

    __types__ = {
        'value_from': 'v1.EnvVarSource',
    }

    __required__ = set([
        'name',
    ])

    name = None # string (required)
    value = None # string
    value_from = None # v1.EnvVarSource

    def __init__(self, *, name, **_kwargs_):

        self.name = name

        super().__init__(**_kwargs_)

@register_model
class v1_EnvVarSource(Resource):

    """EnvVarSource represents a source for the value of an EnvVar."""

    __kind__ = 'v1.EnvVarSource'

    __fields__ = {
        'secret_key_ref': 'secretKeyRef',
        'field_ref': 'fieldRef',
        'config_map_key_ref': 'configMapKeyRef',
        'resource_field_ref': 'resourceFieldRef',
    }

    __types__ = {
        'secret_key_ref': 'v1.SecretKeySelector',
        'field_ref': 'v1.ObjectFieldSelector',
        'resource_field_ref': 'v1.ResourceFieldSelector',
        'config_map_key_ref': 'v1.ConfigMapKeySelector',
    }

    __required__ = set()

    secret_key_ref = None # v1.SecretKeySelector
    field_ref = None # v1.ObjectFieldSelector
    config_map_key_ref = None # v1.ConfigMapKeySelector
    resource_field_ref = None # v1.ResourceFieldSelector

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_Event(Resource):

    """Event is a report of an event somewhere in the cluster."""

    __kind__ = 'v1.Event'

    __fields__ = {
        'first_timestamp': 'firstTimestamp',
        'api_version': 'apiVersion',
        'type': 'type',
        'reason': 'reason',
        'count': 'count',
        'last_timestamp': 'lastTimestamp',
        'metadata': 'metadata',
        'kind': 'kind',
        'source': 'source',
        'message': 'message',
        'involved_object': 'involvedObject',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
        'source': 'v1.EventSource',
        'involved_object': 'v1.ObjectReference',
    }

    __required__ = set([
        'involved_object',
        'metadata',
    ])

    first_timestamp = None # string
    api_version = None # string
    type = None # string
    reason = None # string
    count = None # integer
    last_timestamp = None # string
    metadata = None # v1.ObjectMeta (required)
    kind = None # string
    source = None # v1.EventSource
    message = None # string
    involved_object = None # v1.ObjectReference (required)

    def __init__(self, *, involved_object, metadata, **_kwargs_):

        self.kind = 'ObjectReference'

        self.involved_object = involved_object
        self.metadata = metadata

        super().__init__(**_kwargs_)

@register_model
class v1_EventList(Resource):

    """EventList is a list of events."""

    __kind__ = 'v1.EventList'

    __fields__ = {
        'items': 'items',
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'kind': 'kind',
    }

    __types__ = {
        'items': 'v1.Event',
        'metadata': 'unversioned.ListMeta',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    metadata = None # unversioned.ListMeta
    api_version = None # string
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'ListMeta'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_EventSource(Resource):

    """EventSource contains information for an event."""

    __kind__ = 'v1.EventSource'

    __fields__ = {
        'component': 'component',
        'host': 'host',
    }

    __types__ = {
    }

    __required__ = set()

    component = None # string
    host = None # string

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_ExecAction(Resource):

    """ExecAction describes a "run in container" action."""

    __kind__ = 'v1.ExecAction'

    __fields__ = {
        'command': 'command',
    }

    __types__ = {
    }

    __required__ = set()

    command = None # array

    def __init__(self, **_kwargs_):
        self.command = []

        super().__init__(**_kwargs_)

@register_model
class v1_FCVolumeSource(Resource):

    """Represents a Fibre Channel volume. Fibre Channel volumes can only be
    mounted as read/write once. Fibre Channel volumes support
    ownership management and SELinux relabeling."""

    __kind__ = 'v1.FCVolumeSource'

    __fields__ = {
        'target_ww_ns': 'targetWWNs',
        'read_only': 'readOnly',
        'fs_type': 'fsType',
        'lun': 'lun',
    }

    __types__ = {
    }

    __required__ = set([
        'lun',
        'target_ww_ns',
    ])

    target_ww_ns = None # array (required)
    read_only = None # boolean
    fs_type = None # string
    lun = None # integer (required)

    def __init__(self, *, lun, target_ww_ns, **_kwargs_):

        self.lun = lun
        self.target_ww_ns = target_ww_ns

        super().__init__(**_kwargs_)

@register_model
class v1_FSGroupStrategyOptions(Resource):

    """FSGroupStrategyOptions defines the strategy type and options used to
    create the strategy."""

    __kind__ = 'v1.FSGroupStrategyOptions'

    __fields__ = {
        'type': 'type',
        'ranges': 'ranges',
    }

    __types__ = {
        'ranges': 'v1.IDRange',
    }

    __required__ = set()

    type = None # string
    ranges = None # array

    def __init__(self, **_kwargs_):
        self.ranges = []

        super().__init__(**_kwargs_)

@register_model
class v1_FSType(Resource):

    __kind__ = 'v1.FSType'

    __fields__ = {
    }

    __types__ = {
    }

    __required__ = set()


    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_FinalizerName(Resource):

    __kind__ = 'v1.FinalizerName'

    __fields__ = {
    }

    __types__ = {
    }

    __required__ = set()


    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_FlexVolumeSource(Resource):

    """FlexVolume represents a generic volume resource that is
    provisioned/attached using a exec based plugin. This is an alpha
    feature and may change in future."""

    __kind__ = 'v1.FlexVolumeSource'

    __fields__ = {
        'read_only': 'readOnly',
        'options': 'options',
        'driver': 'driver',
        'fs_type': 'fsType',
        'secret_ref': 'secretRef',
    }

    __types__ = {
        'secret_ref': 'v1.LocalObjectReference',
    }

    __required__ = set([
        'driver',
    ])

    read_only = None # boolean
    options = None # object
    driver = None # string (required)
    fs_type = None # string
    secret_ref = None # v1.LocalObjectReference

    def __init__(self, *, driver, **_kwargs_):

        self.driver = driver

        super().__init__(**_kwargs_)

@register_model
class v1_FlockerVolumeSource(Resource):

    """Represents a Flocker volume mounted by the Flocker agent. Flocker
    volumes do not support ownership management or SELinux relabeling."""

    __kind__ = 'v1.FlockerVolumeSource'

    __fields__ = {
        'dataset_name': 'datasetName',
    }

    __types__ = {
    }

    __required__ = set([
        'dataset_name',
    ])

    dataset_name = None # string (required)

    def __init__(self, *, dataset_name, **_kwargs_):

        self.dataset_name = dataset_name

        super().__init__(**_kwargs_)

@register_model
class v1_GCEPersistentDiskVolumeSource(Resource):

    """Represents a Persistent Disk resource in Google Compute Engine.  A GCE
    PD must exist before mounting to a container. The disk must also
    be in the same GCE project and zone as the kubelet. A GCE PD can
    only be mounted as read/write once or read-only many times. GCE
    PDs support ownership management and SELinux relabeling."""

    __kind__ = 'v1.GCEPersistentDiskVolumeSource'

    __fields__ = {
        'read_only': 'readOnly',
        'partition': 'partition',
        'fs_type': 'fsType',
        'pd_name': 'pdName',
    }

    __types__ = {
    }

    __required__ = set([
        'pd_name',
    ])

    read_only = None # boolean
    partition = None # integer
    fs_type = None # string
    pd_name = None # string (required)

    def __init__(self, *, pd_name, **_kwargs_):

        self.pd_name = pd_name

        super().__init__(**_kwargs_)

@register_model
class v1_GitRepoVolumeSource(Resource):

    """Represents a volume that is populated with the contents of a git
    repository. Git repo volumes do not support ownership management.
    Git repo volumes support SELinux relabeling."""

    __kind__ = 'v1.GitRepoVolumeSource'

    __fields__ = {
        'repository': 'repository',
        'directory': 'directory',
        'revision': 'revision',
    }

    __types__ = {
    }

    __required__ = set([
        'repository',
    ])

    repository = None # string (required)
    directory = None # string
    revision = None # string

    def __init__(self, *, repository, **_kwargs_):

        self.repository = repository

        super().__init__(**_kwargs_)

@register_model
class v1_GlusterfsVolumeSource(Resource):

    """Represents a Glusterfs mount that lasts the lifetime of a pod.
    Glusterfs volumes do not support ownership management or SELinux
    relabeling."""

    __kind__ = 'v1.GlusterfsVolumeSource'

    __fields__ = {
        'path': 'path',
        'endpoints': 'endpoints',
        'read_only': 'readOnly',
    }

    __types__ = {
    }

    __required__ = set([
        'endpoints',
        'path',
    ])

    path = None # string (required)
    endpoints = None # string (required)
    read_only = None # boolean

    def __init__(self, *, endpoints, path, **_kwargs_):

        self.endpoints = endpoints
        self.path = path

        super().__init__(**_kwargs_)

@register_model
class v1_HTTPGetAction(Resource):

    """HTTPGetAction describes an action based on HTTP Get requests."""

    __kind__ = 'v1.HTTPGetAction'

    __fields__ = {
        'path': 'path',
        'http_headers': 'httpHeaders',
        'scheme': 'scheme',
        'port': 'port',
        'host': 'host',
    }

    __types__ = {
        'http_headers': 'v1.HTTPHeader',
    }

    __required__ = set([
        'port',
    ])

    path = None # string
    http_headers = None # array
    scheme = None # string
    port = None # string (required)
    host = None # string

    def __init__(self, *, port, **_kwargs_):
        self.http_headers = []

        self.port = port

        super().__init__(**_kwargs_)

@register_model
class v1_HTTPHeader(Resource):

    """HTTPHeader describes a custom header to be used in HTTP probes"""

    __kind__ = 'v1.HTTPHeader'

    __fields__ = {
        'name': 'name',
        'value': 'value',
    }

    __types__ = {
    }

    __required__ = set([
        'name',
        'value',
    ])

    name = None # string (required)
    value = None # string (required)

    def __init__(self, *, name, value, **_kwargs_):

        self.name = name
        self.value = value

        super().__init__(**_kwargs_)

@register_model
class v1_Handler(Resource):

    """Handler defines a specific action that should be taken"""

    __kind__ = 'v1.Handler'

    __fields__ = {
        'http_get': 'httpGet',
        'tcp_socket': 'tcpSocket',
        'exec': 'exec',
    }

    __types__ = {
        'http_get': 'v1.HTTPGetAction',
        'exec': 'v1.ExecAction',
        'tcp_socket': 'v1.TCPSocketAction',
    }

    __required__ = set()

    http_get = None # v1.HTTPGetAction
    tcp_socket = None # v1.TCPSocketAction
    exec = None # v1.ExecAction

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_HostPathVolumeSource(Resource):

    """Represents a host path mapped into a pod. Host path volumes do not
    support ownership management or SELinux relabeling."""

    __kind__ = 'v1.HostPathVolumeSource'

    __fields__ = {
        'path': 'path',
    }

    __types__ = {
    }

    __required__ = set([
        'path',
    ])

    path = None # string (required)

    def __init__(self, *, path, **_kwargs_):

        self.path = path

        super().__init__(**_kwargs_)

@register_model
class v1_IDRange(Resource):

    """IDRange provides a min/max of an allowed range of IDs."""

    __kind__ = 'v1.IDRange'

    __fields__ = {
        'max': 'max',
        'min': 'min',
    }

    __types__ = {
    }

    __required__ = set()

    max = None # integer
    min = None # integer

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_ISCSIVolumeSource(Resource):

    """Represents an ISCSI disk. ISCSI volumes can only be mounted as
    read/write once. ISCSI volumes support ownership management and
    SELinux relabeling."""

    __kind__ = 'v1.ISCSIVolumeSource'

    __fields__ = {
        'target_portal': 'targetPortal',
        'read_only': 'readOnly',
        'iqn': 'iqn',
        'iscsi_interface': 'iscsiInterface',
        'fs_type': 'fsType',
        'lun': 'lun',
    }

    __types__ = {
    }

    __required__ = set([
        'iqn',
        'lun',
        'target_portal',
    ])

    target_portal = None # string (required)
    read_only = None # boolean
    iqn = None # string (required)
    iscsi_interface = None # string
    fs_type = None # string
    lun = None # integer (required)

    def __init__(self, *, iqn, lun, target_portal, **_kwargs_):

        self.iqn = iqn
        self.lun = lun
        self.target_portal = target_portal

        super().__init__(**_kwargs_)

@register_model
class v1_KeyToPath(Resource):

    """Maps a string key to a path within a volume."""

    __kind__ = 'v1.KeyToPath'

    __fields__ = {
        'path': 'path',
        'key': 'key',
    }

    __types__ = {
    }

    __required__ = set([
        'key',
        'path',
    ])

    path = None # string (required)
    key = None # string (required)

    def __init__(self, *, key, path, **_kwargs_):

        self.key = key
        self.path = path

        super().__init__(**_kwargs_)

@register_model
class v1_Lifecycle(Resource):

    """Lifecycle describes actions that the management system should take in
    response to container lifecycle events. For the PostStart and
    PreStop lifecycle handlers, management of the container blocks
    until the action is complete, unless the container process fails,
    in which case the handler is aborted."""

    __kind__ = 'v1.Lifecycle'

    __fields__ = {
        'pre_stop': 'preStop',
        'post_start': 'postStart',
    }

    __types__ = {
        'pre_stop': 'v1.Handler',
        'post_start': 'v1.Handler',
    }

    __required__ = set()

    pre_stop = None # v1.Handler
    post_start = None # v1.Handler

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_LimitRange(Resource):

    """LimitRange sets resource usage limits for each kind of resource in a
    Namespace."""

    __kind__ = 'v1.LimitRange'

    __fields__ = {
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'spec': 'spec',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
        'spec': 'v1.LimitRangeSpec',
    }

    __required__ = set()

    metadata = None # v1.ObjectMeta
    api_version = None # string
    spec = None # v1.LimitRangeSpec
    kind = None # string

    def __init__(self, **_kwargs_):

        self.kind = 'LimitRangeSpec'

        super().__init__(**_kwargs_)

@register_model
class v1_LimitRangeItem(Resource):

    """LimitRangeItem defines a min/max usage limit for any resource that
    matches on kind."""

    __kind__ = 'v1.LimitRangeItem'

    __fields__ = {
        'default_request': 'defaultRequest',
        'max_limit_request_ratio': 'maxLimitRequestRatio',
        'type': 'type',
        'min': 'min',
        'max': 'max',
        'default': 'default',
    }

    __types__ = {
    }

    __required__ = set()

    default_request = None # object
    max_limit_request_ratio = None # object
    type = None # string
    min = None # object
    max = None # object
    default = None # object

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_LimitRangeList(Resource):

    """LimitRangeList is a list of LimitRange items."""

    __kind__ = 'v1.LimitRangeList'

    __fields__ = {
        'items': 'items',
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'kind': 'kind',
    }

    __types__ = {
        'items': 'v1.LimitRange',
        'metadata': 'unversioned.ListMeta',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    metadata = None # unversioned.ListMeta
    api_version = None # string
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'ListMeta'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_LimitRangeSpec(Resource):

    """LimitRangeSpec defines a min/max usage limit for resources that match
    on kind."""

    __kind__ = 'v1.LimitRangeSpec'

    __fields__ = {
        'limits': 'limits',
    }

    __types__ = {
        'limits': 'v1.LimitRangeItem',
    }

    __required__ = set([
        'limits',
    ])

    limits = None # array (required)

    def __init__(self, *, limits, **_kwargs_):

        self.limits = limits

        super().__init__(**_kwargs_)

@register_model
class v1_LoadBalancerIngress(Resource):

    """LoadBalancerIngress represents the status of a load-balancer ingress
    point: traffic intended for the service should be sent to an
    ingress point."""

    __kind__ = 'v1.LoadBalancerIngress'

    __fields__ = {
        'hostname': 'hostname',
        'ip': 'ip',
    }

    __types__ = {
    }

    __required__ = set()

    hostname = None # string
    ip = None # string

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_LoadBalancerStatus(Resource):

    """LoadBalancerStatus represents the status of a load-balancer."""

    __kind__ = 'v1.LoadBalancerStatus'

    __fields__ = {
        'ingress': 'ingress',
    }

    __types__ = {
        'ingress': 'v1.LoadBalancerIngress',
    }

    __required__ = set()

    ingress = None # array

    def __init__(self, **_kwargs_):
        self.ingress = []

        super().__init__(**_kwargs_)

@register_model
class v1_LocalObjectReference(Resource):

    """LocalObjectReference contains enough information to let you locate the
    referenced object inside the same namespace."""

    __kind__ = 'v1.LocalObjectReference'

    __fields__ = {
        'name': 'name',
    }

    __types__ = {
    }

    __required__ = set()

    name = None # string

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_NFSVolumeSource(Resource):

    """Represents an NFS mount that lasts the lifetime of a pod. NFS volumes
    do not support ownership management or SELinux relabeling."""

    __kind__ = 'v1.NFSVolumeSource'

    __fields__ = {
        'path': 'path',
        'read_only': 'readOnly',
        'server': 'server',
    }

    __types__ = {
    }

    __required__ = set([
        'path',
        'server',
    ])

    path = None # string (required)
    read_only = None # boolean
    server = None # string (required)

    def __init__(self, *, path, server, **_kwargs_):

        self.path = path
        self.server = server

        super().__init__(**_kwargs_)

@register_model
class v1_Namespace(Resource):

    """Namespace provides a scope for Names. Use of multiple namespaces is
    optional."""

    __kind__ = 'v1.Namespace'

    __fields__ = {
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'spec': 'spec',
        'status': 'status',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
        'spec': 'v1.NamespaceSpec',
        'status': 'v1.NamespaceStatus',
    }

    __required__ = set()

    metadata = None # v1.ObjectMeta
    api_version = None # string
    spec = None # v1.NamespaceSpec
    status = None # v1.NamespaceStatus
    kind = None # string

    def __init__(self, **_kwargs_):

        self.kind = 'NamespaceStatus'

        super().__init__(**_kwargs_)

@register_model
class v1_NamespaceList(Resource):

    """NamespaceList is a list of Namespaces."""

    __kind__ = 'v1.NamespaceList'

    __fields__ = {
        'items': 'items',
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'kind': 'kind',
    }

    __types__ = {
        'items': 'v1.Namespace',
        'metadata': 'unversioned.ListMeta',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    metadata = None # unversioned.ListMeta
    api_version = None # string
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'ListMeta'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_NamespaceSpec(Resource):

    """NamespaceSpec describes the attributes on a Namespace."""

    __kind__ = 'v1.NamespaceSpec'

    __fields__ = {
        'finalizers': 'finalizers',
    }

    __types__ = {
        'finalizers': 'v1.FinalizerName',
    }

    __required__ = set()

    finalizers = None # array

    def __init__(self, **_kwargs_):
        self.finalizers = []

        super().__init__(**_kwargs_)

@register_model
class v1_NamespaceStatus(Resource):

    """NamespaceStatus is information about the current status of a
    Namespace."""

    __kind__ = 'v1.NamespaceStatus'

    __fields__ = {
        'phase': 'phase',
    }

    __types__ = {
    }

    __required__ = set()

    phase = None # string

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_Node(Resource):

    """Node is a worker node in Kubernetes, formerly known as minion. Each
    node will have a unique identifier in the cache (i.e. in etcd)."""

    __kind__ = 'v1.Node'

    __fields__ = {
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'spec': 'spec',
        'status': 'status',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
        'spec': 'v1.NodeSpec',
        'status': 'v1.NodeStatus',
    }

    __required__ = set()

    metadata = None # v1.ObjectMeta
    api_version = None # string
    spec = None # v1.NodeSpec
    status = None # v1.NodeStatus
    kind = None # string

    def __init__(self, **_kwargs_):

        self.kind = 'NodeStatus'

        super().__init__(**_kwargs_)

@register_model
class v1_NodeAddress(Resource):

    """NodeAddress contains information for the node's address."""

    __kind__ = 'v1.NodeAddress'

    __fields__ = {
        'type': 'type',
        'address': 'address',
    }

    __types__ = {
    }

    __required__ = set([
        'address',
        'type',
    ])

    type = None # string (required)
    address = None # string (required)

    def __init__(self, *, address, type, **_kwargs_):

        self.address = address
        self.type = type

        super().__init__(**_kwargs_)

@register_model
class v1_NodeCondition(Resource):

    """NodeCondition contains condition infromation for a node."""

    __kind__ = 'v1.NodeCondition'

    __fields__ = {
        'last_transition_time': 'lastTransitionTime',
        'reason': 'reason',
        'type': 'type',
        'last_heartbeat_time': 'lastHeartbeatTime',
        'message': 'message',
        'status': 'status',
    }

    __types__ = {
    }

    __required__ = set([
        'status',
        'type',
    ])

    last_transition_time = None # string
    reason = None # string
    type = None # string (required)
    last_heartbeat_time = None # string
    message = None # string
    status = None # string (required)

    def __init__(self, *, status, type, **_kwargs_):

        self.status = status
        self.type = type

        super().__init__(**_kwargs_)

@register_model
class v1_NodeDaemonEndpoints(Resource):

    """NodeDaemonEndpoints lists ports opened by daemons running on the Node."""

    __kind__ = 'v1.NodeDaemonEndpoints'

    __fields__ = {
        'kubelet_endpoint': 'kubeletEndpoint',
    }

    __types__ = {
        'kubelet_endpoint': 'v1.DaemonEndpoint',
    }

    __required__ = set()

    kubelet_endpoint = None # v1.DaemonEndpoint

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_NodeList(Resource):

    """NodeList is the whole list of all Nodes which have been registered
    with master."""

    __kind__ = 'v1.NodeList'

    __fields__ = {
        'items': 'items',
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'kind': 'kind',
    }

    __types__ = {
        'items': 'v1.Node',
        'metadata': 'unversioned.ListMeta',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    metadata = None # unversioned.ListMeta
    api_version = None # string
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'ListMeta'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_NodeSpec(Resource):

    """NodeSpec describes the attributes that a node is created with."""

    __kind__ = 'v1.NodeSpec'

    __fields__ = {
        'external_id': 'externalID',
        'provider_id': 'providerID',
        'pod_cidr': 'podCIDR',
        'unschedulable': 'unschedulable',
    }

    __types__ = {
    }

    __required__ = set()

    external_id = None # string
    provider_id = None # string
    pod_cidr = None # string
    unschedulable = None # boolean

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_NodeStatus(Resource):

    """NodeStatus is information about the current status of a node."""

    __kind__ = 'v1.NodeStatus'

    __fields__ = {
        'daemon_endpoints': 'daemonEndpoints',
        'capacity': 'capacity',
        'volumes_in_use': 'volumesInUse',
        'conditions': 'conditions',
        'addresses': 'addresses',
        'phase': 'phase',
        'allocatable': 'allocatable',
        'volumes_attached': 'volumesAttached',
        'images': 'images',
        'node_info': 'nodeInfo',
    }

    __types__ = {
        'volumes_in_use': 'v1.UniqueVolumeName',
        'addresses': 'v1.NodeAddress',
        'node_info': 'v1.NodeSystemInfo',
        'volumes_attached': 'v1.AttachedVolume',
        'daemon_endpoints': 'v1.NodeDaemonEndpoints',
        'conditions': 'v1.NodeCondition',
        'images': 'v1.ContainerImage',
    }

    __required__ = set()

    daemon_endpoints = None # v1.NodeDaemonEndpoints
    capacity = None # object
    volumes_in_use = None # array
    conditions = None # array
    addresses = None # array
    phase = None # string
    allocatable = None # object
    volumes_attached = None # array
    images = None # array
    node_info = None # v1.NodeSystemInfo

    def __init__(self, **_kwargs_):
        self.volumes_in_use = []
        self.conditions = []
        self.addresses = []
        self.volumes_attached = []
        self.images = []

        super().__init__(**_kwargs_)

@register_model
class v1_NodeSystemInfo(Resource):

    """NodeSystemInfo is a set of ids/uuids to uniquely identify the node."""

    __kind__ = 'v1.NodeSystemInfo'

    __fields__ = {
        'boot_id': 'bootID',
        'os_image': 'osImage',
        'operating_system': 'operatingSystem',
        'kernel_version': 'kernelVersion',
        'architecture': 'architecture',
        'container_runtime_version': 'containerRuntimeVersion',
        'machine_id': 'machineID',
        'system_uuid': 'systemUUID',
        'kube_proxy_version': 'kubeProxyVersion',
        'kubelet_version': 'kubeletVersion',
    }

    __types__ = {
    }

    __required__ = set([
        'architecture',
        'boot_id',
        'container_runtime_version',
        'kernel_version',
        'kube_proxy_version',
        'kubelet_version',
        'machine_id',
        'operating_system',
        'os_image',
        'system_uuid',
    ])

    boot_id = None # string (required)
    os_image = None # string (required)
    operating_system = None # string (required)
    kernel_version = None # string (required)
    architecture = None # string (required)
    container_runtime_version = None # string (required)
    machine_id = None # string (required)
    system_uuid = None # string (required)
    kube_proxy_version = None # string (required)
    kubelet_version = None # string (required)

    def __init__(self, *, architecture, boot_id, container_runtime_version, kernel_version, kube_proxy_version, kubelet_version, machine_id, operating_system, os_image, system_uuid, **_kwargs_):

        self.architecture = architecture
        self.boot_id = boot_id
        self.container_runtime_version = container_runtime_version
        self.kernel_version = kernel_version
        self.kube_proxy_version = kube_proxy_version
        self.kubelet_version = kubelet_version
        self.machine_id = machine_id
        self.operating_system = operating_system
        self.os_image = os_image
        self.system_uuid = system_uuid

        super().__init__(**_kwargs_)

@register_model
class v1_ObjectFieldSelector(Resource):

    """ObjectFieldSelector selects an APIVersioned field of an object."""

    __kind__ = 'v1.ObjectFieldSelector'

    __fields__ = {
        'field_path': 'fieldPath',
        'api_version': 'apiVersion',
    }

    __types__ = {
    }

    __required__ = set([
        'field_path',
    ])

    field_path = None # string (required)
    api_version = None # string

    def __init__(self, *, field_path, **_kwargs_):

        self.field_path = field_path

        super().__init__(**_kwargs_)

@register_model
class v1_ObjectMeta(Resource):

    """ObjectMeta is metadata that all persisted resources must have, which
    includes all objects users must create."""

    __kind__ = 'v1.ObjectMeta'

    __fields__ = {
        'name': 'name',
        'finalizers': 'finalizers',
        'self_link': 'selfLink',
        'uid': 'uid',
        'generate_name': 'generateName',
        'annotations': 'annotations',
        'namespace': 'namespace',
        'generation': 'generation',
        'deletion_timestamp': 'deletionTimestamp',
        'creation_timestamp': 'creationTimestamp',
        'owner_references': 'ownerReferences',
        'labels': 'labels',
        'deletion_grace_period_seconds': 'deletionGracePeriodSeconds',
        'resource_version': 'resourceVersion',
    }

    __types__ = {
        'owner_references': 'v1.OwnerReference',
    }

    __required__ = set()

    name = None # string
    finalizers = None # array
    self_link = None # string
    uid = None # string
    generate_name = None # string
    annotations = None # object
    namespace = None # string
    generation = None # integer
    deletion_timestamp = None # string
    creation_timestamp = None # string
    owner_references = None # array
    labels = None # object
    deletion_grace_period_seconds = None # integer
    resource_version = None # string

    def __init__(self, **_kwargs_):
        self.finalizers = []
        self.owner_references = []

        super().__init__(**_kwargs_)

@register_model
class v1_ObjectReference(Resource):

    """ObjectReference contains enough information to let you inspect or
    modify the referred object."""

    __kind__ = 'v1.ObjectReference'

    __fields__ = {
        'name': 'name',
        'field_path': 'fieldPath',
        'api_version': 'apiVersion',
        'uid': 'uid',
        'resource_version': 'resourceVersion',
        'namespace': 'namespace',
        'kind': 'kind',
    }

    __types__ = {
    }

    __required__ = set()

    name = None # string
    field_path = None # string
    api_version = None # string
    uid = None # string
    resource_version = None # string
    namespace = None # string
    kind = None # string

    def __init__(self, **_kwargs_):

        self.kind = 'ObjectReference'

        super().__init__(**_kwargs_)

@register_model
class v1_OwnerReference(Resource):

    """OwnerReference contains enough information to let you identify an
    owning object. Currently, an owning object must be in the same
    namespace, so there is no namespace field."""

    __kind__ = 'v1.OwnerReference'

    __fields__ = {
        'name': 'name',
        'api_version': 'apiVersion',
        'uid': 'uid',
        'controller': 'controller',
        'kind': 'kind',
    }

    __types__ = {
    }

    __required__ = set([
        'api_version',
        'kind',
        'name',
        'uid',
    ])

    name = None # string (required)
    api_version = None # string (required)
    uid = None # string (required)
    controller = None # boolean
    kind = None # string (required)

    def __init__(self, *, api_version, kind, name, uid, **_kwargs_):

        self.kind = 'OwnerReference'

        self.api_version = api_version
        self.kind = kind
        self.name = name
        self.uid = uid

        super().__init__(**_kwargs_)

@register_model
class v1_PersistentVolume(Resource):

    """PersistentVolume (PV) is a storage resource provisioned by an
    administrator. It is analogous to a node. More info:
    http://releases.k8s.io/release-1.3/docs/user-guide/persistent-
    volumes.md"""

    __kind__ = 'v1.PersistentVolume'

    __fields__ = {
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'spec': 'spec',
        'status': 'status',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
        'spec': 'v1.PersistentVolumeSpec',
        'status': 'v1.PersistentVolumeStatus',
    }

    __required__ = set()

    metadata = None # v1.ObjectMeta
    api_version = None # string
    spec = None # v1.PersistentVolumeSpec
    status = None # v1.PersistentVolumeStatus
    kind = None # string

    def __init__(self, **_kwargs_):

        self.kind = 'PersistentVolumeStatus'

        super().__init__(**_kwargs_)

@register_model
class v1_PersistentVolumeAccessMode(Resource):

    __kind__ = 'v1.PersistentVolumeAccessMode'

    __fields__ = {
    }

    __types__ = {
    }

    __required__ = set()


    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_PersistentVolumeClaim(Resource):

    """PersistentVolumeClaim is a user's request for and claim to a
    persistent volume"""

    __kind__ = 'v1.PersistentVolumeClaim'

    __fields__ = {
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'spec': 'spec',
        'status': 'status',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
        'spec': 'v1.PersistentVolumeClaimSpec',
        'status': 'v1.PersistentVolumeClaimStatus',
    }

    __required__ = set()

    metadata = None # v1.ObjectMeta
    api_version = None # string
    spec = None # v1.PersistentVolumeClaimSpec
    status = None # v1.PersistentVolumeClaimStatus
    kind = None # string

    def __init__(self, **_kwargs_):

        self.kind = 'PersistentVolumeClaimStatus'

        super().__init__(**_kwargs_)

@register_model
class v1_PersistentVolumeClaimList(Resource):

    """PersistentVolumeClaimList is a list of PersistentVolumeClaim items."""

    __kind__ = 'v1.PersistentVolumeClaimList'

    __fields__ = {
        'items': 'items',
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'kind': 'kind',
    }

    __types__ = {
        'items': 'v1.PersistentVolumeClaim',
        'metadata': 'unversioned.ListMeta',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    metadata = None # unversioned.ListMeta
    api_version = None # string
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'ListMeta'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_PersistentVolumeClaimSpec(Resource):

    """PersistentVolumeClaimSpec describes the common attributes of storage
    devices and allows a Source for provider-specific attributes"""

    __kind__ = 'v1.PersistentVolumeClaimSpec'

    __fields__ = {
        'access_modes': 'accessModes',
        'volume_name': 'volumeName',
        'selector': 'selector',
        'resources': 'resources',
    }

    __types__ = {
        'selector': 'unversioned.LabelSelector',
        'resources': 'v1.ResourceRequirements',
    }

    __required__ = set()

    access_modes = None # array
    volume_name = None # string
    selector = None # unversioned.LabelSelector
    resources = None # v1.ResourceRequirements

    def __init__(self, **_kwargs_):
        self.access_modes = []

        super().__init__(**_kwargs_)

@register_model
class v1_PersistentVolumeClaimStatus(Resource):

    """PersistentVolumeClaimStatus is the current status of a persistent
    volume claim."""

    __kind__ = 'v1.PersistentVolumeClaimStatus'

    __fields__ = {
        'access_modes': 'accessModes',
        'phase': 'phase',
        'capacity': 'capacity',
    }

    __types__ = {
        'access_modes': 'v1.PersistentVolumeAccessMode',
    }

    __required__ = set()

    access_modes = None # array
    phase = None # string
    capacity = None # object

    def __init__(self, **_kwargs_):
        self.access_modes = []

        super().__init__(**_kwargs_)

@register_model
class v1_PersistentVolumeClaimVolumeSource(Resource):

    """PersistentVolumeClaimVolumeSource references the user's PVC in the
    same namespace. This volume finds the bound PV and mounts that
    volume for the pod. A PersistentVolumeClaimVolumeSource is,
    essentially, a wrapper around another type of volume that is owned
    by someone else (the system)."""

    __kind__ = 'v1.PersistentVolumeClaimVolumeSource'

    __fields__ = {
        'claim_name': 'claimName',
        'read_only': 'readOnly',
    }

    __types__ = {
    }

    __required__ = set([
        'claim_name',
    ])

    claim_name = None # string (required)
    read_only = None # boolean

    def __init__(self, *, claim_name, **_kwargs_):

        self.claim_name = claim_name

        super().__init__(**_kwargs_)

@register_model
class v1_PersistentVolumeList(Resource):

    """PersistentVolumeList is a list of PersistentVolume items."""

    __kind__ = 'v1.PersistentVolumeList'

    __fields__ = {
        'items': 'items',
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'kind': 'kind',
    }

    __types__ = {
        'items': 'v1.PersistentVolume',
        'metadata': 'unversioned.ListMeta',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    metadata = None # unversioned.ListMeta
    api_version = None # string
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'ListMeta'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_PersistentVolumeSpec(Resource):

    """PersistentVolumeSpec is the specification of a persistent volume."""

    __kind__ = 'v1.PersistentVolumeSpec'

    __fields__ = {
        'flocker': 'flocker',
        'flex_volume': 'flexVolume',
        'aws_elastic_block_store': 'awsElasticBlockStore',
        'capacity': 'capacity',
        'host_path': 'hostPath',
        'iscsi': 'iscsi',
        'cinder': 'cinder',
        'nfs': 'nfs',
        'azure_file': 'azureFile',
        'rbd': 'rbd',
        'gce_persistent_disk': 'gcePersistentDisk',
        'fc': 'fc',
        'persistent_volume_reclaim_policy': 'persistentVolumeReclaimPolicy',
        'cephfs': 'cephfs',
        'access_modes': 'accessModes',
        'claim_ref': 'claimRef',
        'glusterfs': 'glusterfs',
        'vsphere_volume': 'vsphereVolume',
    }

    __types__ = {
        'flocker': 'v1.FlockerVolumeSource',
        'flex_volume': 'v1.FlexVolumeSource',
        'aws_elastic_block_store': 'v1.AWSElasticBlockStoreVolumeSource',
        'host_path': 'v1.HostPathVolumeSource',
        'iscsi': 'v1.ISCSIVolumeSource',
        'cinder': 'v1.CinderVolumeSource',
        'nfs': 'v1.NFSVolumeSource',
        'azure_file': 'v1.AzureFileVolumeSource',
        'rbd': 'v1.RBDVolumeSource',
        'gce_persistent_disk': 'v1.GCEPersistentDiskVolumeSource',
        'fc': 'v1.FCVolumeSource',
        'cephfs': 'v1.CephFSVolumeSource',
        'access_modes': 'v1.PersistentVolumeAccessMode',
        'claim_ref': 'v1.ObjectReference',
        'glusterfs': 'v1.GlusterfsVolumeSource',
        'vsphere_volume': 'v1.VsphereVirtualDiskVolumeSource',
    }

    __required__ = set()

    flocker = None # v1.FlockerVolumeSource
    flex_volume = None # v1.FlexVolumeSource
    aws_elastic_block_store = None # v1.AWSElasticBlockStoreVolumeSource
    capacity = None # object
    host_path = None # v1.HostPathVolumeSource
    iscsi = None # v1.ISCSIVolumeSource
    cinder = None # v1.CinderVolumeSource
    nfs = None # v1.NFSVolumeSource
    azure_file = None # v1.AzureFileVolumeSource
    rbd = None # v1.RBDVolumeSource
    gce_persistent_disk = None # v1.GCEPersistentDiskVolumeSource
    fc = None # v1.FCVolumeSource
    persistent_volume_reclaim_policy = None # string
    cephfs = None # v1.CephFSVolumeSource
    access_modes = None # array
    claim_ref = None # v1.ObjectReference
    glusterfs = None # v1.GlusterfsVolumeSource
    vsphere_volume = None # v1.VsphereVirtualDiskVolumeSource

    def __init__(self, **_kwargs_):
        self.access_modes = []

        super().__init__(**_kwargs_)

@register_model
class v1_PersistentVolumeStatus(Resource):

    """PersistentVolumeStatus is the current status of a persistent volume."""

    __kind__ = 'v1.PersistentVolumeStatus'

    __fields__ = {
        'phase': 'phase',
        'message': 'message',
        'reason': 'reason',
    }

    __types__ = {
    }

    __required__ = set()

    phase = None # string
    message = None # string
    reason = None # string

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_Pod(Resource):

    """Pod is a collection of containers that can run on a host. This
    resource is created by clients and scheduled onto hosts."""

    __kind__ = 'v1.Pod'

    __fields__ = {
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'spec': 'spec',
        'status': 'status',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
        'spec': 'v1.PodSpec',
        'status': 'v1.PodStatus',
    }

    __required__ = set()

    metadata = None # v1.ObjectMeta
    api_version = None # string
    spec = None # v1.PodSpec
    status = None # v1.PodStatus
    kind = None # string

    def __init__(self, **_kwargs_):

        self.kind = 'PodStatus'

        super().__init__(**_kwargs_)

@register_model
class v1_PodCondition(Resource):

    """PodCondition contains details for the current condition of this pod."""

    __kind__ = 'v1.PodCondition'

    __fields__ = {
        'last_transition_time': 'lastTransitionTime',
        'reason': 'reason',
        'type': 'type',
        'last_probe_time': 'lastProbeTime',
        'message': 'message',
        'status': 'status',
    }

    __types__ = {
    }

    __required__ = set([
        'status',
        'type',
    ])

    last_transition_time = None # string
    reason = None # string
    type = None # string (required)
    last_probe_time = None # string
    message = None # string
    status = None # string (required)

    def __init__(self, *, status, type, **_kwargs_):

        self.status = status
        self.type = type

        super().__init__(**_kwargs_)

@register_model
class v1_PodList(Resource):

    """PodList is a list of Pods."""

    __kind__ = 'v1.PodList'

    __fields__ = {
        'items': 'items',
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'kind': 'kind',
    }

    __types__ = {
        'items': 'v1.Pod',
        'metadata': 'unversioned.ListMeta',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    metadata = None # unversioned.ListMeta
    api_version = None # string
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'ListMeta'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_PodSecurityContext(Resource):

    """PodSecurityContext holds pod-level security attributes and common
    container settings. Some fields are also present in
    container.securityContext.  Field values of
    container.securityContext take precedence over field values of
    PodSecurityContext."""

    __kind__ = 'v1.PodSecurityContext'

    __fields__ = {
        'run_as_user': 'runAsUser',
        'se_linux_options': 'seLinuxOptions',
        'fs_group': 'fsGroup',
        'run_as_non_root': 'runAsNonRoot',
        'supplemental_groups': 'supplementalGroups',
    }

    __types__ = {
        'se_linux_options': 'v1.SELinuxOptions',
    }

    __required__ = set()

    run_as_user = None # integer
    se_linux_options = None # v1.SELinuxOptions
    fs_group = None # integer
    run_as_non_root = None # boolean
    supplemental_groups = None # array

    def __init__(self, **_kwargs_):
        self.supplemental_groups = []

        super().__init__(**_kwargs_)

@register_model
class v1_PodSpec(Resource):

    """PodSpec is a description of a pod."""

    __kind__ = 'v1.PodSpec'

    __fields__ = {
        'service_account': 'serviceAccount',
        'active_deadline_seconds': 'activeDeadlineSeconds',
        'node_name': 'nodeName',
        'subdomain': 'subdomain',
        'host_pid': 'hostPID',
        'containers': 'containers',
        'image_pull_secrets': 'imagePullSecrets',
        'node_selector': 'nodeSelector',
        'dns_policy': 'dnsPolicy',
        'service_account_name': 'serviceAccountName',
        'security_context': 'securityContext',
        'host_ipc': 'hostIPC',
        'host': 'host',
        'host_network': 'hostNetwork',
        'restart_policy': 'restartPolicy',
        'termination_grace_period_seconds': 'terminationGracePeriodSeconds',
        'hostname': 'hostname',
        'volumes': 'volumes',
    }

    __types__ = {
        'image_pull_secrets': 'v1.LocalObjectReference',
        'volumes': 'v1.Volume',
        'security_context': 'v1.PodSecurityContext',
        'containers': 'v1.Container',
    }

    __required__ = set([
        'containers',
    ])

    service_account = None # string
    active_deadline_seconds = None # integer
    node_name = None # string
    subdomain = None # string
    host_pid = None # boolean
    containers = None # array (required)
    image_pull_secrets = None # array
    node_selector = None # object
    dns_policy = None # string
    service_account_name = None # string
    security_context = None # v1.PodSecurityContext
    host_ipc = None # boolean
    host = None # string
    host_network = None # boolean
    restart_policy = None # string
    termination_grace_period_seconds = None # integer
    hostname = None # string
    volumes = None # array

    def __init__(self, *, containers, **_kwargs_):
        self.image_pull_secrets = []
        self.volumes = []

        self.containers = containers

        super().__init__(**_kwargs_)

@register_model
class v1_PodStatus(Resource):

    """PodStatus represents information about the status of a pod. Status may
    trail the actual state of a system."""

    __kind__ = 'v1.PodStatus'

    __fields__ = {
        'message': 'message',
        'pod_ip': 'podIP',
        'reason': 'reason',
        'conditions': 'conditions',
        'phase': 'phase',
        'container_statuses': 'containerStatuses',
        'host_ip': 'hostIP',
        'start_time': 'startTime',
    }

    __types__ = {
        'conditions': 'v1.PodCondition',
        'container_statuses': 'v1.ContainerStatus',
    }

    __required__ = set()

    message = None # string
    pod_ip = None # string
    reason = None # string
    conditions = None # array
    phase = None # string
    container_statuses = None # array
    host_ip = None # string
    start_time = None # string

    def __init__(self, **_kwargs_):
        self.conditions = []
        self.container_statuses = []

        super().__init__(**_kwargs_)

@register_model
class v1_PodTemplate(Resource):

    """PodTemplate describes a template for creating copies of a predefined
    pod."""

    __kind__ = 'v1.PodTemplate'

    __fields__ = {
        'template': 'template',
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
        'template': 'v1.PodTemplateSpec',
    }

    __required__ = set()

    template = None # v1.PodTemplateSpec
    metadata = None # v1.ObjectMeta
    api_version = None # string
    kind = None # string

    def __init__(self, **_kwargs_):

        self.kind = 'PodTemplateSpec'

        super().__init__(**_kwargs_)

@register_model
class v1_PodTemplateList(Resource):

    """PodTemplateList is a list of PodTemplates."""

    __kind__ = 'v1.PodTemplateList'

    __fields__ = {
        'items': 'items',
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'kind': 'kind',
    }

    __types__ = {
        'items': 'v1.PodTemplate',
        'metadata': 'unversioned.ListMeta',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    metadata = None # unversioned.ListMeta
    api_version = None # string
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'ListMeta'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_PodTemplateSpec(Resource):

    """PodTemplateSpec describes the data a pod should have when created from
    a template"""

    __kind__ = 'v1.PodTemplateSpec'

    __fields__ = {
        'metadata': 'metadata',
        'spec': 'spec',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
        'spec': 'v1.PodSpec',
    }

    __required__ = set()

    metadata = None # v1.ObjectMeta
    spec = None # v1.PodSpec

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_Preconditions(Resource):

    """Preconditions must be fulfilled before an operation (update, delete,
    etc.) is carried out."""

    __kind__ = 'v1.Preconditions'

    __fields__ = {
        'uid': 'uid',
    }

    __types__ = {
        'uid': 'types.UID',
    }

    __required__ = set()

    uid = None # types.UID

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_Probe(Resource):

    """Probe describes a health check to be performed against a container to
    determine whether it is alive or ready to receive traffic."""

    __kind__ = 'v1.Probe'

    __fields__ = {
        'failure_threshold': 'failureThreshold',
        'exec': 'exec',
        'tcp_socket': 'tcpSocket',
        'timeout_seconds': 'timeoutSeconds',
        'http_get': 'httpGet',
        'period_seconds': 'periodSeconds',
        'initial_delay_seconds': 'initialDelaySeconds',
        'success_threshold': 'successThreshold',
    }

    __types__ = {
        'http_get': 'v1.HTTPGetAction',
        'tcp_socket': 'v1.TCPSocketAction',
        'exec': 'v1.ExecAction',
    }

    __required__ = set()

    failure_threshold = None # integer
    exec = None # v1.ExecAction
    tcp_socket = None # v1.TCPSocketAction
    timeout_seconds = None # integer
    http_get = None # v1.HTTPGetAction
    period_seconds = None # integer
    initial_delay_seconds = None # integer
    success_threshold = None # integer

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_RBDVolumeSource(Resource):

    """Represents a Rados Block Device mount that lasts the lifetime of a
    pod. RBD volumes support ownership management and SELinux
    relabeling."""

    __kind__ = 'v1.RBDVolumeSource'

    __fields__ = {
        'monitors': 'monitors',
        'pool': 'pool',
        'user': 'user',
        'keyring': 'keyring',
        'secret_ref': 'secretRef',
        'read_only': 'readOnly',
        'fs_type': 'fsType',
        'image': 'image',
    }

    __types__ = {
        'secret_ref': 'v1.LocalObjectReference',
    }

    __required__ = set([
        'image',
        'monitors',
    ])

    monitors = None # array (required)
    pool = None # string
    user = None # string
    keyring = None # string
    secret_ref = None # v1.LocalObjectReference
    read_only = None # boolean
    fs_type = None # string
    image = None # string (required)

    def __init__(self, *, image, monitors, **_kwargs_):

        self.image = image
        self.monitors = monitors

        super().__init__(**_kwargs_)

@register_model
class v1_ReplicationController(Resource):

    """ReplicationController represents the configuration of a replication
    controller."""

    __kind__ = 'v1.ReplicationController'

    __fields__ = {
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'spec': 'spec',
        'status': 'status',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
        'spec': 'v1.ReplicationControllerSpec',
        'status': 'v1.ReplicationControllerStatus',
    }

    __required__ = set()

    metadata = None # v1.ObjectMeta
    api_version = None # string
    spec = None # v1.ReplicationControllerSpec
    status = None # v1.ReplicationControllerStatus
    kind = None # string

    def __init__(self, **_kwargs_):

        self.kind = 'ReplicationControllerStatus'

        super().__init__(**_kwargs_)

@register_model
class v1_ReplicationControllerList(Resource):

    """ReplicationControllerList is a collection of replication controllers."""

    __kind__ = 'v1.ReplicationControllerList'

    __fields__ = {
        'items': 'items',
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'kind': 'kind',
    }

    __types__ = {
        'items': 'v1.ReplicationController',
        'metadata': 'unversioned.ListMeta',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    metadata = None # unversioned.ListMeta
    api_version = None # string
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'ListMeta'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_ReplicationControllerSpec(Resource):

    """ReplicationControllerSpec is the specification of a replication
    controller."""

    __kind__ = 'v1.ReplicationControllerSpec'

    __fields__ = {
        'selector': 'selector',
        'template': 'template',
        'replicas': 'replicas',
    }

    __types__ = {
        'template': 'v1.PodTemplateSpec',
    }

    __required__ = set()

    selector = None # object
    template = None # v1.PodTemplateSpec
    replicas = None # integer

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_ReplicationControllerStatus(Resource):

    """ReplicationControllerStatus represents the current status of a
    replication controller."""

    __kind__ = 'v1.ReplicationControllerStatus'

    __fields__ = {
        'observed_generation': 'observedGeneration',
        'replicas': 'replicas',
        'fully_labeled_replicas': 'fullyLabeledReplicas',
    }

    __types__ = {
    }

    __required__ = set([
        'replicas',
    ])

    observed_generation = None # integer
    replicas = None # integer (required)
    fully_labeled_replicas = None # integer

    def __init__(self, *, replicas, **_kwargs_):

        self.replicas = replicas

        super().__init__(**_kwargs_)

@register_model
class v1_ResourceFieldSelector(Resource):

    """ResourceFieldSelector represents container resources (cpu, memory) and
    their output format"""

    __kind__ = 'v1.ResourceFieldSelector'

    __fields__ = {
        'resource': 'resource',
        'container_name': 'containerName',
        'divisor': 'divisor',
    }

    __types__ = {
    }

    __required__ = set([
        'resource',
    ])

    resource = None # string (required)
    container_name = None # string
    divisor = None # string

    def __init__(self, *, resource, **_kwargs_):

        self.resource = resource

        super().__init__(**_kwargs_)

@register_model
class v1_ResourceQuota(Resource):

    """ResourceQuota sets aggregate quota restrictions enforced per namespace"""

    __kind__ = 'v1.ResourceQuota'

    __fields__ = {
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'spec': 'spec',
        'status': 'status',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
        'spec': 'v1.ResourceQuotaSpec',
        'status': 'v1.ResourceQuotaStatus',
    }

    __required__ = set()

    metadata = None # v1.ObjectMeta
    api_version = None # string
    spec = None # v1.ResourceQuotaSpec
    status = None # v1.ResourceQuotaStatus
    kind = None # string

    def __init__(self, **_kwargs_):

        self.kind = 'ResourceQuotaStatus'

        super().__init__(**_kwargs_)

@register_model
class v1_ResourceQuotaList(Resource):

    """ResourceQuotaList is a list of ResourceQuota items."""

    __kind__ = 'v1.ResourceQuotaList'

    __fields__ = {
        'items': 'items',
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'kind': 'kind',
    }

    __types__ = {
        'items': 'v1.ResourceQuota',
        'metadata': 'unversioned.ListMeta',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    metadata = None # unversioned.ListMeta
    api_version = None # string
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'ListMeta'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_ResourceQuotaScope(Resource):

    __kind__ = 'v1.ResourceQuotaScope'

    __fields__ = {
    }

    __types__ = {
    }

    __required__ = set()


    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_ResourceQuotaSpec(Resource):

    """ResourceQuotaSpec defines the desired hard limits to enforce for
    Quota."""

    __kind__ = 'v1.ResourceQuotaSpec'

    __fields__ = {
        'hard': 'hard',
        'scopes': 'scopes',
    }

    __types__ = {
        'scopes': 'v1.ResourceQuotaScope',
    }

    __required__ = set()

    hard = None # object
    scopes = None # array

    def __init__(self, **_kwargs_):
        self.scopes = []

        super().__init__(**_kwargs_)

@register_model
class v1_ResourceQuotaStatus(Resource):

    """ResourceQuotaStatus defines the enforced hard limits and observed use."""

    __kind__ = 'v1.ResourceQuotaStatus'

    __fields__ = {
        'hard': 'hard',
        'used': 'used',
    }

    __types__ = {
    }

    __required__ = set()

    hard = None # object
    used = None # object

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_ResourceRequirements(Resource):

    """ResourceRequirements describes the compute resource requirements."""

    __kind__ = 'v1.ResourceRequirements'

    __fields__ = {
        'limits': 'limits',
        'requests': 'requests',
    }

    __types__ = {
    }

    __required__ = set()

    limits = None # object
    requests = None # object

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_RunAsUserStrategyOptions(Resource):

    """RunAsUserStrategyOptions defines the strategy type and any options
    used to create the strategy."""

    __kind__ = 'v1.RunAsUserStrategyOptions'

    __fields__ = {
        'uid_range_min': 'uidRangeMin',
        'uid': 'uid',
        'type': 'type',
        'uid_range_max': 'uidRangeMax',
    }

    __types__ = {
    }

    __required__ = set()

    uid_range_min = None # integer
    uid = None # integer
    type = None # string
    uid_range_max = None # integer

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_SELinuxContextStrategyOptions(Resource):

    """SELinuxContextStrategyOptions defines the strategy type and any
    options used to create the strategy."""

    __kind__ = 'v1.SELinuxContextStrategyOptions'

    __fields__ = {
        'se_linux_options': 'seLinuxOptions',
        'type': 'type',
    }

    __types__ = {
        'se_linux_options': 'v1.SELinuxOptions',
    }

    __required__ = set()

    se_linux_options = None # v1.SELinuxOptions
    type = None # string

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_SELinuxOptions(Resource):

    """SELinuxOptions are the labels to be applied to the container"""

    __kind__ = 'v1.SELinuxOptions'

    __fields__ = {
        'level': 'level',
        'user': 'user',
        'role': 'role',
        'type': 'type',
    }

    __types__ = {
    }

    __required__ = set()

    level = None # string
    user = None # string
    role = None # string
    type = None # string

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_Scale(Resource):

    """Scale represents a scaling request for a resource."""

    __kind__ = 'v1.Scale'

    __fields__ = {
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'spec': 'spec',
        'status': 'status',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
        'spec': 'v1.ScaleSpec',
        'status': 'v1.ScaleStatus',
    }

    __required__ = set()

    metadata = None # v1.ObjectMeta
    api_version = None # string
    spec = None # v1.ScaleSpec
    status = None # v1.ScaleStatus
    kind = None # string

    def __init__(self, **_kwargs_):

        self.kind = 'ScaleStatus'

        super().__init__(**_kwargs_)

@register_model
class v1_ScaleSpec(Resource):

    """ScaleSpec describes the attributes of a scale subresource."""

    __kind__ = 'v1.ScaleSpec'

    __fields__ = {
        'replicas': 'replicas',
    }

    __types__ = {
    }

    __required__ = set()

    replicas = None # integer

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_ScaleStatus(Resource):

    """ScaleStatus represents the current status of a scale subresource."""

    __kind__ = 'v1.ScaleStatus'

    __fields__ = {
        'selector': 'selector',
        'replicas': 'replicas',
    }

    __types__ = {
    }

    __required__ = set([
        'replicas',
    ])

    selector = None # string
    replicas = None # integer (required)

    def __init__(self, *, replicas, **_kwargs_):

        self.replicas = replicas

        super().__init__(**_kwargs_)

@register_model
class v1_Secret(Resource):

    """Secret holds secret data of a certain type. The total bytes of the
    values in the Data field must be less than MaxSecretSize bytes."""

    __kind__ = 'v1.Secret'

    __fields__ = {
        'api_version': 'apiVersion',
        'data': 'data',
        'metadata': 'metadata',
        'string_data': 'stringData',
        'type': 'type',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
    }

    __required__ = set()

    api_version = None # string
    data = None # object
    metadata = None # v1.ObjectMeta
    string_data = None # object
    type = None # string
    kind = None # string

    def __init__(self, **_kwargs_):

        self.kind = 'ObjectMeta'

        super().__init__(**_kwargs_)

@register_model
class v1_SecretKeySelector(Resource):

    """SecretKeySelector selects a key of a Secret."""

    __kind__ = 'v1.SecretKeySelector'

    __fields__ = {
        'name': 'name',
        'key': 'key',
    }

    __types__ = {
    }

    __required__ = set([
        'key',
    ])

    name = None # string
    key = None # string (required)

    def __init__(self, *, key, **_kwargs_):

        self.key = key

        super().__init__(**_kwargs_)

@register_model
class v1_SecretList(Resource):

    """SecretList is a list of Secret."""

    __kind__ = 'v1.SecretList'

    __fields__ = {
        'items': 'items',
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'kind': 'kind',
    }

    __types__ = {
        'items': 'v1.Secret',
        'metadata': 'unversioned.ListMeta',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    metadata = None # unversioned.ListMeta
    api_version = None # string
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'ListMeta'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_SecretVolumeSource(Resource):

    """Adapts a Secret into a volume.  The contents of the target Secret's
    Data field will be presented in a volume as files using the keys
    in the Data field as the file names. Secret volumes support
    ownership management and SELinux relabeling."""

    __kind__ = 'v1.SecretVolumeSource'

    __fields__ = {
        'items': 'items',
        'secret_name': 'secretName',
    }

    __types__ = {
        'items': 'v1.KeyToPath',
    }

    __required__ = set()

    items = None # array
    secret_name = None # string

    def __init__(self, **_kwargs_):
        self.items = []

        super().__init__(**_kwargs_)

@register_model
class v1_SecurityContext(Resource):

    """SecurityContext holds security configuration that will be applied to a
    container. Some fields are present in both SecurityContext and
    PodSecurityContext.  When both are set, the values in
    SecurityContext take precedence."""

    __kind__ = 'v1.SecurityContext'

    __fields__ = {
        'run_as_user': 'runAsUser',
        'se_linux_options': 'seLinuxOptions',
        'privileged': 'privileged',
        'run_as_non_root': 'runAsNonRoot',
        'capabilities': 'capabilities',
        'read_only_root_filesystem': 'readOnlyRootFilesystem',
    }

    __types__ = {
        'se_linux_options': 'v1.SELinuxOptions',
        'capabilities': 'v1.Capabilities',
    }

    __required__ = set()

    run_as_user = None # integer
    se_linux_options = None # v1.SELinuxOptions
    privileged = None # boolean
    run_as_non_root = None # boolean
    capabilities = None # v1.Capabilities
    read_only_root_filesystem = None # boolean

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_SecurityContextConstraints(Resource):

    """SecurityContextConstraints governs the ability to make requests that
    affect the SecurityContext that will be applied to a container."""

    __kind__ = 'v1.SecurityContextConstraints'

    __fields__ = {
        'allow_host_dir_volume_plugin': 'allowHostDirVolumePlugin',
        'required_drop_capabilities': 'requiredDropCapabilities',
        'allow_host_network': 'allowHostNetwork',
        'allowed_capabilities': 'allowedCapabilities',
        'allow_host_ipc': 'allowHostIPC',
        'fs_group': 'fsGroup',
        'default_add_capabilities': 'defaultAddCapabilities',
        'allow_host_ports': 'allowHostPorts',
        'allow_host_pid': 'allowHostPID',
        'kind': 'kind',
        'se_linux_context': 'seLinuxContext',
        'metadata': 'metadata',
        'users': 'users',
        'allow_privileged_container': 'allowPrivilegedContainer',
        'volumes': 'volumes',
        'run_as_user': 'runAsUser',
        'api_version': 'apiVersion',
        'supplemental_groups': 'supplementalGroups',
        'read_only_root_filesystem': 'readOnlyRootFilesystem',
        'groups': 'groups',
        'seccomp_profiles': 'seccompProfiles',
        'priority': 'priority',
    }

    __types__ = {
        'se_linux_context': 'v1.SELinuxContextStrategyOptions',
        'run_as_user': 'v1.RunAsUserStrategyOptions',
        'required_drop_capabilities': 'v1.Capability',
        'fs_group': 'v1.FSGroupStrategyOptions',
        'default_add_capabilities': 'v1.Capability',
        'metadata': 'v1.ObjectMeta',
        'allowed_capabilities': 'v1.Capability',
        'supplemental_groups': 'v1.SupplementalGroupsStrategyOptions',
        'volumes': 'v1.FSType',
    }

    __required__ = set([
        'allow_host_dir_volume_plugin',
        'allow_host_ipc',
        'allow_host_network',
        'allow_host_pid',
        'allow_host_ports',
        'allow_privileged_container',
        'allowed_capabilities',
        'default_add_capabilities',
        'priority',
        'read_only_root_filesystem',
        'required_drop_capabilities',
        'volumes',
    ])

    allow_host_dir_volume_plugin = None # boolean (required)
    required_drop_capabilities = None # array (required)
    allow_host_network = None # boolean (required)
    allowed_capabilities = None # array (required)
    allow_host_ipc = None # boolean (required)
    fs_group = None # v1.FSGroupStrategyOptions
    default_add_capabilities = None # array (required)
    allow_host_ports = None # boolean (required)
    allow_host_pid = None # boolean (required)
    kind = None # string
    se_linux_context = None # v1.SELinuxContextStrategyOptions
    metadata = None # v1.ObjectMeta
    users = None # array
    allow_privileged_container = None # boolean (required)
    volumes = None # array (required)
    run_as_user = None # v1.RunAsUserStrategyOptions
    api_version = None # string
    supplemental_groups = None # v1.SupplementalGroupsStrategyOptions
    read_only_root_filesystem = None # boolean (required)
    groups = None # array
    seccomp_profiles = None # array
    priority = None # integer (required)

    def __init__(self, *, allow_host_dir_volume_plugin, allow_host_ipc, allow_host_network, allow_host_pid, allow_host_ports, allow_privileged_container, allowed_capabilities, default_add_capabilities, priority, read_only_root_filesystem, required_drop_capabilities, volumes, **_kwargs_):
        self.users = []
        self.groups = []
        self.seccomp_profiles = []

        self.kind = 'FSType'

        self.allow_host_dir_volume_plugin = allow_host_dir_volume_plugin
        self.allow_host_ipc = allow_host_ipc
        self.allow_host_network = allow_host_network
        self.allow_host_pid = allow_host_pid
        self.allow_host_ports = allow_host_ports
        self.allow_privileged_container = allow_privileged_container
        self.allowed_capabilities = allowed_capabilities
        self.default_add_capabilities = default_add_capabilities
        self.priority = priority
        self.read_only_root_filesystem = read_only_root_filesystem
        self.required_drop_capabilities = required_drop_capabilities
        self.volumes = volumes

        super().__init__(**_kwargs_)

@register_model
class v1_SecurityContextConstraintsList(Resource):

    """SecurityContextConstraintsList is a list of SecurityContextConstraints
    objects"""

    __kind__ = 'v1.SecurityContextConstraintsList'

    __fields__ = {
        'items': 'items',
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'kind': 'kind',
    }

    __types__ = {
        'items': 'v1.SecurityContextConstraints',
        'metadata': 'unversioned.ListMeta',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    metadata = None # unversioned.ListMeta
    api_version = None # string
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'ListMeta'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_Service(Resource):

    """Service is a named abstraction of software service (for example,
    mysql) consisting of local port (for example 3306) that the proxy
    listens on, and the selector that determines which pods will
    answer requests sent through the proxy."""

    __kind__ = 'v1.Service'

    __fields__ = {
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'spec': 'spec',
        'status': 'status',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
        'spec': 'v1.ServiceSpec',
        'status': 'v1.ServiceStatus',
    }

    __required__ = set()

    metadata = None # v1.ObjectMeta
    api_version = None # string
    spec = None # v1.ServiceSpec
    status = None # v1.ServiceStatus
    kind = None # string

    def __init__(self, **_kwargs_):

        self.kind = 'ServiceStatus'

        super().__init__(**_kwargs_)

@register_model
class v1_ServiceAccount(Resource):

    """ServiceAccount binds together: * a name, understood by users, and
    perhaps by peripheral systems, for an identity * a principal that
    can be authenticated and authorized * a set of secrets"""

    __kind__ = 'v1.ServiceAccount'

    __fields__ = {
        'image_pull_secrets': 'imagePullSecrets',
        'secrets': 'secrets',
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'kind': 'kind',
    }

    __types__ = {
        'image_pull_secrets': 'v1.LocalObjectReference',
        'secrets': 'v1.ObjectReference',
        'metadata': 'v1.ObjectMeta',
    }

    __required__ = set()

    image_pull_secrets = None # array
    secrets = None # array
    metadata = None # v1.ObjectMeta
    api_version = None # string
    kind = None # string

    def __init__(self, **_kwargs_):
        self.image_pull_secrets = []
        self.secrets = []

        self.kind = 'ObjectMeta'

        super().__init__(**_kwargs_)

@register_model
class v1_ServiceAccountList(Resource):

    """ServiceAccountList is a list of ServiceAccount objects"""

    __kind__ = 'v1.ServiceAccountList'

    __fields__ = {
        'items': 'items',
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'kind': 'kind',
    }

    __types__ = {
        'items': 'v1.ServiceAccount',
        'metadata': 'unversioned.ListMeta',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    metadata = None # unversioned.ListMeta
    api_version = None # string
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'ListMeta'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_ServiceList(Resource):

    """ServiceList holds a list of services."""

    __kind__ = 'v1.ServiceList'

    __fields__ = {
        'items': 'items',
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'kind': 'kind',
    }

    __types__ = {
        'items': 'v1.Service',
        'metadata': 'unversioned.ListMeta',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    metadata = None # unversioned.ListMeta
    api_version = None # string
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'ListMeta'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_ServicePort(Resource):

    """ServicePort contains information on service's port."""

    __kind__ = 'v1.ServicePort'

    __fields__ = {
        'name': 'name',
        'protocol': 'protocol',
        'port': 'port',
        'node_port': 'nodePort',
        'target_port': 'targetPort',
    }

    __types__ = {
    }

    __required__ = set([
        'port',
    ])

    name = None # string
    protocol = None # string
    port = None # integer (required)
    node_port = None # integer
    target_port = None # string

    def __init__(self, *, port, **_kwargs_):

        self.port = port

        super().__init__(**_kwargs_)

@register_model
class v1_ServiceSpec(Resource):

    """ServiceSpec describes the attributes that a user creates on a service."""

    __kind__ = 'v1.ServiceSpec'

    __fields__ = {
        'cluster_ip': 'clusterIP',
        'session_affinity': 'sessionAffinity',
        'ports': 'ports',
        'type': 'type',
        'external_i_ps': 'externalIPs',
        'deprecated_public_i_ps': 'deprecatedPublicIPs',
        'selector': 'selector',
        'portal_ip': 'portalIP',
        'load_balancer_source_ranges': 'loadBalancerSourceRanges',
        'load_balancer_ip': 'loadBalancerIP',
    }

    __types__ = {
        'ports': 'v1.ServicePort',
    }

    __required__ = set([
        'ports',
    ])

    cluster_ip = None # string
    session_affinity = None # string
    ports = None # array (required)
    type = None # string
    external_i_ps = None # array
    deprecated_public_i_ps = None # array
    selector = None # object
    portal_ip = None # string
    load_balancer_source_ranges = None # array
    load_balancer_ip = None # string

    def __init__(self, *, ports, **_kwargs_):
        self.external_i_ps = []
        self.deprecated_public_i_ps = []
        self.load_balancer_source_ranges = []

        self.ports = ports

        super().__init__(**_kwargs_)

@register_model
class v1_ServiceStatus(Resource):

    """ServiceStatus represents the current status of a service."""

    __kind__ = 'v1.ServiceStatus'

    __fields__ = {
        'load_balancer': 'loadBalancer',
    }

    __types__ = {
        'load_balancer': 'v1.LoadBalancerStatus',
    }

    __required__ = set()

    load_balancer = None # v1.LoadBalancerStatus

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_SupplementalGroupsStrategyOptions(Resource):

    """SupplementalGroupsStrategyOptions defines the strategy type and
    options used to create the strategy."""

    __kind__ = 'v1.SupplementalGroupsStrategyOptions'

    __fields__ = {
        'type': 'type',
        'ranges': 'ranges',
    }

    __types__ = {
        'ranges': 'v1.IDRange',
    }

    __required__ = set()

    type = None # string
    ranges = None # array

    def __init__(self, **_kwargs_):
        self.ranges = []

        super().__init__(**_kwargs_)

@register_model
class v1_TCPSocketAction(Resource):

    """TCPSocketAction describes an action based on opening a socket"""

    __kind__ = 'v1.TCPSocketAction'

    __fields__ = {
        'port': 'port',
    }

    __types__ = {
    }

    __required__ = set([
        'port',
    ])

    port = None # string (required)

    def __init__(self, *, port, **_kwargs_):

        self.port = port

        super().__init__(**_kwargs_)

@register_model
class v1_UniqueVolumeName(Resource):

    __kind__ = 'v1.UniqueVolumeName'

    __fields__ = {
    }

    __types__ = {
    }

    __required__ = set()


    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_Volume(Resource):

    """Volume represents a named volume in a pod that may be accessed by any
    container in the pod."""

    __kind__ = 'v1.Volume'

    __fields__ = {
        'flex_volume': 'flexVolume',
        'flocker': 'flocker',
        'aws_elastic_block_store': 'awsElasticBlockStore',
        'empty_dir': 'emptyDir',
        'host_path': 'hostPath',
        'iscsi': 'iscsi',
        'cinder': 'cinder',
        'fc': 'fc',
        'gce_persistent_disk': 'gcePersistentDisk',
        'name': 'name',
        'azure_file': 'azureFile',
        'nfs': 'nfs',
        'metadata': 'metadata',
        'persistent_volume_claim': 'persistentVolumeClaim',
        'git_repo': 'gitRepo',
        'rbd': 'rbd',
        'glusterfs': 'glusterfs',
        'config_map': 'configMap',
        'cephfs': 'cephfs',
        'downward_api': 'downwardAPI',
        'vsphere_volume': 'vsphereVolume',
        'secret': 'secret',
    }

    __types__ = {
        'flex_volume': 'v1.FlexVolumeSource',
        'flocker': 'v1.FlockerVolumeSource',
        'aws_elastic_block_store': 'v1.AWSElasticBlockStoreVolumeSource',
        'empty_dir': 'v1.EmptyDirVolumeSource',
        'host_path': 'v1.HostPathVolumeSource',
        'iscsi': 'v1.ISCSIVolumeSource',
        'cinder': 'v1.CinderVolumeSource',
        'nfs': 'v1.NFSVolumeSource',
        'metadata': 'v1.DeprecatedDownwardAPIVolumeSource',
        'azure_file': 'v1.AzureFileVolumeSource',
        'persistent_volume_claim': 'v1.PersistentVolumeClaimVolumeSource',
        'rbd': 'v1.RBDVolumeSource',
        'gce_persistent_disk': 'v1.GCEPersistentDiskVolumeSource',
        'config_map': 'v1.ConfigMapVolumeSource',
        'fc': 'v1.FCVolumeSource',
        'cephfs': 'v1.CephFSVolumeSource',
        'git_repo': 'v1.GitRepoVolumeSource',
        'glusterfs': 'v1.GlusterfsVolumeSource',
        'vsphere_volume': 'v1.VsphereVirtualDiskVolumeSource',
        'downward_api': 'v1.DownwardAPIVolumeSource',
        'secret': 'v1.SecretVolumeSource',
    }

    __required__ = set([
        'name',
    ])

    flex_volume = None # v1.FlexVolumeSource
    flocker = None # v1.FlockerVolumeSource
    aws_elastic_block_store = None # v1.AWSElasticBlockStoreVolumeSource
    empty_dir = None # v1.EmptyDirVolumeSource
    host_path = None # v1.HostPathVolumeSource
    iscsi = None # v1.ISCSIVolumeSource
    cinder = None # v1.CinderVolumeSource
    fc = None # v1.FCVolumeSource
    gce_persistent_disk = None # v1.GCEPersistentDiskVolumeSource
    name = None # string (required)
    azure_file = None # v1.AzureFileVolumeSource
    nfs = None # v1.NFSVolumeSource
    metadata = None # v1.DeprecatedDownwardAPIVolumeSource
    persistent_volume_claim = None # v1.PersistentVolumeClaimVolumeSource
    git_repo = None # v1.GitRepoVolumeSource
    rbd = None # v1.RBDVolumeSource
    glusterfs = None # v1.GlusterfsVolumeSource
    config_map = None # v1.ConfigMapVolumeSource
    cephfs = None # v1.CephFSVolumeSource
    downward_api = None # v1.DownwardAPIVolumeSource
    vsphere_volume = None # v1.VsphereVirtualDiskVolumeSource
    secret = None # v1.SecretVolumeSource

    def __init__(self, *, name, **_kwargs_):

        self.name = name

        super().__init__(**_kwargs_)

@register_model
class v1_VolumeMount(Resource):

    """VolumeMount describes a mounting of a Volume within a container."""

    __kind__ = 'v1.VolumeMount'

    __fields__ = {
        'name': 'name',
        'mount_path': 'mountPath',
        'read_only': 'readOnly',
        'sub_path': 'subPath',
    }

    __types__ = {
    }

    __required__ = set([
        'mount_path',
        'name',
    ])

    name = None # string (required)
    mount_path = None # string (required)
    read_only = None # boolean
    sub_path = None # string

    def __init__(self, *, mount_path, name, **_kwargs_):

        self.mount_path = mount_path
        self.name = name

        super().__init__(**_kwargs_)

@register_model
class v1_VsphereVirtualDiskVolumeSource(Resource):

    """Represents a vSphere volume resource."""

    __kind__ = 'v1.VsphereVirtualDiskVolumeSource'

    __fields__ = {
        'volume_path': 'volumePath',
        'fs_type': 'fsType',
    }

    __types__ = {
    }

    __required__ = set([
        'volume_path',
    ])

    volume_path = None # string (required)
    fs_type = None # string

    def __init__(self, *, volume_path, **_kwargs_):

        self.volume_path = volume_path

        super().__init__(**_kwargs_)
__all__ = ['versioned_Event', 'types_UID', 'unversioned_APIResource', 'unversioned_APIResourceList', 'unversioned_LabelSelector', 'unversioned_LabelSelectorRequirement', 'unversioned_ListMeta', 'unversioned_Patch', 'unversioned_Status', 'unversioned_StatusCause', 'unversioned_StatusDetails', 'v1_AWSElasticBlockStoreVolumeSource', 'v1_AttachedVolume', 'v1_AzureFileVolumeSource', 'v1_Binding', 'v1_Capabilities', 'v1_Capability', 'v1_CephFSVolumeSource', 'v1_CinderVolumeSource', 'v1_ComponentCondition', 'v1_ComponentStatus', 'v1_ComponentStatusList', 'v1_ConfigMap', 'v1_ConfigMapKeySelector', 'v1_ConfigMapList', 'v1_ConfigMapVolumeSource', 'v1_Container', 'v1_ContainerImage', 'v1_ContainerPort', 'v1_ContainerState', 'v1_ContainerStateRunning', 'v1_ContainerStateTerminated', 'v1_ContainerStateWaiting', 'v1_ContainerStatus', 'v1_DaemonEndpoint', 'v1_DeleteOptions', 'v1_DeprecatedDownwardAPIVolumeFile', 'v1_DeprecatedDownwardAPIVolumeSource', 'v1_DownwardAPIVolumeFile', 'v1_DownwardAPIVolumeSource', 'v1_EmptyDirVolumeSource', 'v1_EndpointAddress', 'v1_EndpointPort', 'v1_EndpointSubset', 'v1_Endpoints', 'v1_EndpointsList', 'v1_EnvVar', 'v1_EnvVarSource', 'v1_Event', 'v1_EventList', 'v1_EventSource', 'v1_ExecAction', 'v1_FCVolumeSource', 'v1_FSGroupStrategyOptions', 'v1_FSType', 'v1_FinalizerName', 'v1_FlexVolumeSource', 'v1_FlockerVolumeSource', 'v1_GCEPersistentDiskVolumeSource', 'v1_GitRepoVolumeSource', 'v1_GlusterfsVolumeSource', 'v1_HTTPGetAction', 'v1_HTTPHeader', 'v1_Handler', 'v1_HostPathVolumeSource', 'v1_IDRange', 'v1_ISCSIVolumeSource', 'v1_KeyToPath', 'v1_Lifecycle', 'v1_LimitRange', 'v1_LimitRangeItem', 'v1_LimitRangeList', 'v1_LimitRangeSpec', 'v1_LoadBalancerIngress', 'v1_LoadBalancerStatus', 'v1_LocalObjectReference', 'v1_NFSVolumeSource', 'v1_Namespace', 'v1_NamespaceList', 'v1_NamespaceSpec', 'v1_NamespaceStatus', 'v1_Node', 'v1_NodeAddress', 'v1_NodeCondition', 'v1_NodeDaemonEndpoints', 'v1_NodeList', 'v1_NodeSpec', 'v1_NodeStatus', 'v1_NodeSystemInfo', 'v1_ObjectFieldSelector', 'v1_ObjectMeta', 'v1_ObjectReference', 'v1_OwnerReference', 'v1_PersistentVolume', 'v1_PersistentVolumeAccessMode', 'v1_PersistentVolumeClaim', 'v1_PersistentVolumeClaimList', 'v1_PersistentVolumeClaimSpec', 'v1_PersistentVolumeClaimStatus', 'v1_PersistentVolumeClaimVolumeSource', 'v1_PersistentVolumeList', 'v1_PersistentVolumeSpec', 'v1_PersistentVolumeStatus', 'v1_Pod', 'v1_PodCondition', 'v1_PodList', 'v1_PodSecurityContext', 'v1_PodSpec', 'v1_PodStatus', 'v1_PodTemplate', 'v1_PodTemplateList', 'v1_PodTemplateSpec', 'v1_Preconditions', 'v1_Probe', 'v1_RBDVolumeSource', 'v1_ReplicationController', 'v1_ReplicationControllerList', 'v1_ReplicationControllerSpec', 'v1_ReplicationControllerStatus', 'v1_ResourceFieldSelector', 'v1_ResourceQuota', 'v1_ResourceQuotaList', 'v1_ResourceQuotaScope', 'v1_ResourceQuotaSpec', 'v1_ResourceQuotaStatus', 'v1_ResourceRequirements', 'v1_RunAsUserStrategyOptions', 'v1_SELinuxContextStrategyOptions', 'v1_SELinuxOptions', 'v1_Scale', 'v1_ScaleSpec', 'v1_ScaleStatus', 'v1_Secret', 'v1_SecretKeySelector', 'v1_SecretList', 'v1_SecretVolumeSource', 'v1_SecurityContext', 'v1_SecurityContextConstraints', 'v1_SecurityContextConstraintsList', 'v1_Service', 'v1_ServiceAccount', 'v1_ServiceAccountList', 'v1_ServiceList', 'v1_ServicePort', 'v1_ServiceSpec', 'v1_ServiceStatus', 'v1_SupplementalGroupsStrategyOptions', 'v1_TCPSocketAction', 'v1_UniqueVolumeName', 'v1_Volume', 'v1_VolumeMount', 'v1_VsphereVirtualDiskVolumeSource']

@register_model
class versioned_Event(Resource):

    __kind__ = '*versioned.Event'

    __fields__ = {
    }

    __types__ = {
    }

    __required__ = set()


    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class patch_Object(Resource):

    """represents an object patch, which may be any of: JSON patch (RFC
    6902), JSON merge patch (RFC 7396), or the Kubernetes strategic
    merge patch"""

    __kind__ = 'patch.Object'

    __fields__ = {
    }

    __types__ = {
    }

    __required__ = set()


    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class runtime_RawExtension(Resource):

    """this may be any JSON object with a 'kind' and 'apiVersion' field; and
    is preserved unmodified by processing"""

    __kind__ = 'runtime.RawExtension'

    __fields__ = {
    }

    __types__ = {
    }

    __required__ = set()


    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class types_UID(Resource):

    __kind__ = 'types.UID'

    __fields__ = {
    }

    __types__ = {
    }

    __required__ = set()


    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class unversioned_APIResource(Resource):

    """APIResource specifies the name of a resource and whether it is
    namespaced."""

    __kind__ = 'unversioned.APIResource'

    __fields__ = {
        'name': 'name',
        'namespaced': 'namespaced',
        'kind': 'kind',
    }

    __types__ = {
    }

    __required__ = set([
        'kind',
        'name',
        'namespaced',
    ])

    name = None # string (required)
    namespaced = None # boolean (required)
    kind = None # string (required)

    def __init__(self, *, kind, name, namespaced, **_kwargs_):

        self.kind = 'APIResource'

        self.kind = kind
        self.name = name
        self.namespaced = namespaced

        super().__init__(**_kwargs_)

@register_model
class unversioned_APIResourceList(Resource):

    """APIResourceList is a list of APIResource, it is used to expose the
    name of the resources supported in a specific group and version,
    and if the resource is namespaced."""

    __kind__ = 'unversioned.APIResourceList'

    __fields__ = {
        'api_version': 'apiVersion',
        'resources': 'resources',
        'group_version': 'groupVersion',
        'kind': 'kind',
    }

    __types__ = {
        'resources': 'unversioned.APIResource',
    }

    __required__ = set([
        'group_version',
        'resources',
    ])

    api_version = None # string
    resources = None # array (required)
    group_version = None # string (required)
    kind = None # string

    def __init__(self, *, group_version, resources, **_kwargs_):

        self.kind = 'APIResource'

        self.group_version = group_version
        self.resources = resources

        super().__init__(**_kwargs_)

@register_model
class unversioned_LabelSelector(Resource):

    """A label selector is a label query over a set of resources. The result
    of matchLabels and matchExpressions are ANDed. An empty label
    selector matches all objects. A null label selector matches no
    objects."""

    __kind__ = 'unversioned.LabelSelector'

    __fields__ = {
        'match_expressions': 'matchExpressions',
        'match_labels': 'matchLabels',
    }

    __types__ = {
        'match_expressions': 'unversioned.LabelSelectorRequirement',
    }

    __required__ = set()

    match_expressions = None # array
    match_labels = None # object

    def __init__(self, **_kwargs_):
        self.match_expressions = []

        super().__init__(**_kwargs_)

@register_model
class unversioned_LabelSelectorRequirement(Resource):

    """A label selector requirement is a selector that contains values, a
    key, and an operator that relates the key and values."""

    __kind__ = 'unversioned.LabelSelectorRequirement'

    __fields__ = {
        'operator': 'operator',
        'values': 'values',
        'key': 'key',
    }

    __types__ = {
    }

    __required__ = set([
        'key',
        'operator',
    ])

    operator = None # string (required)
    values = None # array
    key = None # string (required)

    def __init__(self, *, key, operator, **_kwargs_):
        self.values = []

        self.key = key
        self.operator = operator

        super().__init__(**_kwargs_)

@register_model
class unversioned_ListMeta(Resource):

    """ListMeta describes metadata that synthetic resources must have,
    including lists and various status objects. A resource may have
    only one of {ObjectMeta, ListMeta}."""

    __kind__ = 'unversioned.ListMeta'

    __fields__ = {
        'resource_version': 'resourceVersion',
        'self_link': 'selfLink',
    }

    __types__ = {
    }

    __required__ = set()

    resource_version = None # string
    self_link = None # string

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class unversioned_Patch(Resource):

    """Patch is provided to give a concrete name and type to the Kubernetes
    PATCH request body."""

    __kind__ = 'unversioned.Patch'

    __fields__ = {
    }

    __types__ = {
    }

    __required__ = set()


    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class unversioned_Status(Resource):

    """Status is a return value for calls that don't return other objects."""

    __kind__ = 'unversioned.Status'

    __fields__ = {
        'details': 'details',
        'api_version': 'apiVersion',
        'reason': 'reason',
        'metadata': 'metadata',
        'message': 'message',
        'status': 'status',
        'code': 'code',
        'kind': 'kind',
    }

    __types__ = {
        'details': 'unversioned.StatusDetails',
        'metadata': 'unversioned.ListMeta',
    }

    __required__ = set()

    details = None # unversioned.StatusDetails
    api_version = None # string
    reason = None # string
    metadata = None # unversioned.ListMeta
    message = None # string
    status = None # string
    code = None # integer
    kind = None # string

    def __init__(self, **_kwargs_):

        self.kind = 'ListMeta'

        super().__init__(**_kwargs_)

@register_model
class unversioned_StatusCause(Resource):

    """StatusCause provides more information about an api.Status failure,
    including cases when multiple errors are encountered."""

    __kind__ = 'unversioned.StatusCause'

    __fields__ = {
        'field': 'field',
        'reason': 'reason',
        'message': 'message',
    }

    __types__ = {
    }

    __required__ = set()

    field = None # string
    reason = None # string
    message = None # string

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class unversioned_StatusDetails(Resource):

    """StatusDetails is a set of additional properties that MAY be set by the
    server to provide additional information about a response. The
    Reason field of a Status object defines what attributes will be
    set. Clients must ignore fields that do not match the defined type
    of each attribute, and should assume that any attribute may be
    empty, invalid, or under defined."""

    __kind__ = 'unversioned.StatusDetails'

    __fields__ = {
        'name': 'name',
        'retry_after_seconds': 'retryAfterSeconds',
        'causes': 'causes',
        'group': 'group',
        'kind': 'kind',
    }

    __types__ = {
        'causes': 'unversioned.StatusCause',
    }

    __required__ = set()

    name = None # string
    retry_after_seconds = None # integer
    causes = None # array
    group = None # string
    kind = None # string

    def __init__(self, **_kwargs_):
        self.causes = []

        self.kind = 'StatusCause'

        super().__init__(**_kwargs_)

@register_model
class v1_AWSElasticBlockStoreVolumeSource(Resource):

    """Represents a Persistent Disk resource in AWS.  An AWS EBS disk must
    exist before mounting to a container. The disk must also be in the
    same AWS zone as the kubelet. An AWS EBS disk can only be mounted
    as read/write once. AWS EBS volumes support ownership management
    and SELinux relabeling."""

    __kind__ = 'v1.AWSElasticBlockStoreVolumeSource'

    __fields__ = {
        'read_only': 'readOnly',
        'volume_id': 'volumeID',
        'partition': 'partition',
        'fs_type': 'fsType',
    }

    __types__ = {
    }

    __required__ = set([
        'volume_id',
    ])

    read_only = None # boolean
    volume_id = None # string (required)
    partition = None # integer
    fs_type = None # string

    def __init__(self, *, volume_id, **_kwargs_):

        self.volume_id = volume_id

        super().__init__(**_kwargs_)

@register_model
class v1_AppliedClusterResourceQuota(Resource):

    """AppliedClusterResourceQuota mirrors ClusterResourceQuota at a project
    scope, for projection into a project.  It allows a project-admin
    to know which ClusterResourceQuotas are applied to his project and
    their associated usage."""

    __kind__ = 'v1.AppliedClusterResourceQuota'

    __fields__ = {
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'spec': 'spec',
        'status': 'status',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
        'spec': 'v1.ClusterResourceQuotaSpec',
        'status': 'v1.ClusterResourceQuotaStatus',
    }

    __required__ = set([
        'metadata',
        'spec',
    ])

    metadata = None # v1.ObjectMeta (required)
    api_version = None # string
    spec = None # v1.ClusterResourceQuotaSpec (required)
    status = None # v1.ClusterResourceQuotaStatus
    kind = None # string

    def __init__(self, *, metadata, spec, **_kwargs_):

        self.kind = 'ClusterResourceQuotaStatus'

        self.metadata = metadata
        self.spec = spec

        super().__init__(**_kwargs_)

@register_model
class v1_AppliedClusterResourceQuotaList(Resource):

    """AppliedClusterResourceQuotaList is a collection of
    AppliedClusterResourceQuotas"""

    __kind__ = 'v1.AppliedClusterResourceQuotaList'

    __fields__ = {
        'items': 'items',
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'kind': 'kind',
    }

    __types__ = {
        'items': 'v1.AppliedClusterResourceQuota',
        'metadata': 'unversioned.ListMeta',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    metadata = None # unversioned.ListMeta
    api_version = None # string
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'ListMeta'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_AzureFileVolumeSource(Resource):

    """AzureFile represents an Azure File Service mount on the host and bind
    mount to the pod."""

    __kind__ = 'v1.AzureFileVolumeSource'

    __fields__ = {
        'share_name': 'shareName',
        'read_only': 'readOnly',
        'secret_name': 'secretName',
    }

    __types__ = {
    }

    __required__ = set([
        'secret_name',
        'share_name',
    ])

    share_name = None # string (required)
    read_only = None # boolean
    secret_name = None # string (required)

    def __init__(self, *, secret_name, share_name, **_kwargs_):

        self.secret_name = secret_name
        self.share_name = share_name

        super().__init__(**_kwargs_)

@register_model
class v1_BinaryBuildSource(Resource):

    """BinaryBuildSource describes a binary file to be used for the Docker
    and Source build strategies, where the file will be extracted and
    used as the build source."""

    __kind__ = 'v1.BinaryBuildSource'

    __fields__ = {
        'as_file': 'asFile',
    }

    __types__ = {
    }

    __required__ = set()

    as_file = None # string

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_Build(Resource):

    """Build encapsulates the inputs needed to produce a new deployable
    image, as well as the status of the execution and a reference to
    the Pod which executed the build."""

    __kind__ = 'v1.Build'

    __fields__ = {
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'spec': 'spec',
        'status': 'status',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
        'spec': 'v1.BuildSpec',
        'status': 'v1.BuildStatus',
    }

    __required__ = set()

    metadata = None # v1.ObjectMeta
    api_version = None # string
    spec = None # v1.BuildSpec
    status = None # v1.BuildStatus
    kind = None # string

    def __init__(self, **_kwargs_):

        self.kind = 'BuildStatus'

        super().__init__(**_kwargs_)

@register_model
class v1_BuildConfig(Resource):

    """BuildConfig is a template which can be used to create new builds."""

    __kind__ = 'v1.BuildConfig'

    __fields__ = {
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'spec': 'spec',
        'status': 'status',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
        'spec': 'v1.BuildConfigSpec',
        'status': 'v1.BuildConfigStatus',
    }

    __required__ = set([
        'spec',
        'status',
    ])

    metadata = None # v1.ObjectMeta
    api_version = None # string
    spec = None # v1.BuildConfigSpec (required)
    status = None # v1.BuildConfigStatus (required)
    kind = None # string

    def __init__(self, *, spec, status, **_kwargs_):

        self.kind = 'BuildConfigStatus'

        self.spec = spec
        self.status = status

        super().__init__(**_kwargs_)

@register_model
class v1_BuildConfigList(Resource):

    """BuildConfigList is a collection of BuildConfigs."""

    __kind__ = 'v1.BuildConfigList'

    __fields__ = {
        'items': 'items',
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'kind': 'kind',
    }

    __types__ = {
        'items': 'v1.BuildConfig',
        'metadata': 'unversioned.ListMeta',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    metadata = None # unversioned.ListMeta
    api_version = None # string
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'ListMeta'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_BuildConfigSpec(Resource):

    """BuildConfigSpec describes when and how builds are created"""

    __kind__ = 'v1.BuildConfigSpec'

    __fields__ = {
        'output': 'output',
        'run_policy': 'runPolicy',
        'strategy': 'strategy',
        'triggers': 'triggers',
        'service_account': 'serviceAccount',
        'post_commit': 'postCommit',
        'resources': 'resources',
        'source': 'source',
        'completion_deadline_seconds': 'completionDeadlineSeconds',
        'revision': 'revision',
    }

    __types__ = {
        'output': 'v1.BuildOutput',
        'strategy': 'v1.BuildStrategy',
        'triggers': 'v1.BuildTriggerPolicy',
        'resources': 'v1.ResourceRequirements',
        'revision': 'v1.SourceRevision',
        'source': 'v1.BuildSource',
        'post_commit': 'v1.BuildPostCommitSpec',
    }

    __required__ = set([
        'strategy',
        'triggers',
    ])

    output = None # v1.BuildOutput
    run_policy = None # string
    strategy = None # v1.BuildStrategy (required)
    triggers = None # array (required)
    service_account = None # string
    post_commit = None # v1.BuildPostCommitSpec
    resources = None # v1.ResourceRequirements
    source = None # v1.BuildSource
    completion_deadline_seconds = None # integer
    revision = None # v1.SourceRevision

    def __init__(self, *, strategy, triggers, **_kwargs_):

        self.strategy = strategy
        self.triggers = triggers

        super().__init__(**_kwargs_)

@register_model
class v1_BuildConfigStatus(Resource):

    """BuildConfigStatus contains current state of the build config object."""

    __kind__ = 'v1.BuildConfigStatus'

    __fields__ = {
        'last_version': 'lastVersion',
    }

    __types__ = {
    }

    __required__ = set([
        'last_version',
    ])

    last_version = None # integer (required)

    def __init__(self, *, last_version, **_kwargs_):

        self.last_version = last_version

        super().__init__(**_kwargs_)

@register_model
class v1_BuildList(Resource):

    """BuildList is a collection of Builds."""

    __kind__ = 'v1.BuildList'

    __fields__ = {
        'items': 'items',
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'kind': 'kind',
    }

    __types__ = {
        'items': 'v1.Build',
        'metadata': 'unversioned.ListMeta',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    metadata = None # unversioned.ListMeta
    api_version = None # string
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'ListMeta'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_BuildLog(Resource):

    """BuildLog is the (unused) resource associated with the build log
    redirector"""

    __kind__ = 'v1.BuildLog'

    __fields__ = {
        'api_version': 'apiVersion',
        'kind': 'kind',
    }

    __types__ = {
    }

    __required__ = set()

    api_version = None # string
    kind = None # string

    def __init__(self, **_kwargs_):

        self.kind = 'BuildLog'

        super().__init__(**_kwargs_)

@register_model
class v1_BuildOutput(Resource):

    """BuildOutput is input to a build strategy and describes the Docker
    image that the strategy should produce."""

    __kind__ = 'v1.BuildOutput'

    __fields__ = {
        'to': 'to',
        'push_secret': 'pushSecret',
    }

    __types__ = {
        'to': 'v1.ObjectReference',
        'push_secret': 'v1.LocalObjectReference',
    }

    __required__ = set()

    to = None # v1.ObjectReference
    push_secret = None # v1.LocalObjectReference

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_BuildPostCommitSpec(Resource):

    """A BuildPostCommitSpec holds a build post commit hook specification.
    The hook executes a command in a temporary container running the
    build output image, immediately after the last layer of the image
    is committed and before the image is pushed to a registry. The
    command is executed with the current working directory ($PWD) set
    to the image's WORKDIR.  The build will be marked as failed if the
    hook execution fails. It will fail if the script or command return
    a non-zero exit code, or if there is any other error related to
    starting the temporary container.  There are five different ways
    to configure the hook. As an example, all forms below are
    equivalent and will execute `rake test --verbose`.  1. Shell
    script:         "postCommit": {          "script": "rake test
    --verbose",        }      The above is a convenient form which is
    equivalent to:         "postCommit": {          "command":
    ["/bin/sh", "-ic"],          "args":    ["rake test --verbose"]
    }  2. A command as the image entrypoint:         "postCommit": {
    "commit": ["rake", "test", "--verbose"]        }      Command
    overrides the image entrypoint in the exec form, as documented in
    Docker:
    https://docs.docker.com/engine/reference/builder/#entrypoint.  3.
    Pass arguments to the default entrypoint:         "postCommit": {
    "args": ["rake", "test", "--verbose"]               }      This
    form is only useful if the image entrypoint can handle arguments.
    4. Shell script with arguments:         "postCommit": {
    "script": "rake test $1",          "args":   ["--verbose"]
    }      This form is useful if you need to pass arguments that
    would otherwise be     hard to quote properly in the shell script.
    In the script, $0 will be     "/bin/sh" and $1, $2, etc, are the
    positional arguments from Args.  5. Command with arguments:
    "postCommit": {          "command": ["rake", "test"],
    "args":    ["--verbose"]        }      This form is equivalent to
    appending the arguments to the Command slice.  It is invalid to
    provide both Script and Command simultaneously. If none of the
    fields are specified, the hook is not executed."""

    __kind__ = 'v1.BuildPostCommitSpec'

    __fields__ = {
        'command': 'command',
        'args': 'args',
        'script': 'script',
    }

    __types__ = {
    }

    __required__ = set()

    command = None # array
    args = None # array
    script = None # string

    def __init__(self, **_kwargs_):
        self.command = []
        self.args = []

        super().__init__(**_kwargs_)

@register_model
class v1_BuildRequest(Resource):

    """BuildRequest is the resource used to pass parameters to build
    generator"""

    __kind__ = 'v1.BuildRequest'

    __fields__ = {
        'binary': 'binary',
        'from_': 'from',
        'api_version': 'apiVersion',
        'triggered_by': 'triggeredBy',
        'triggered_by_image': 'triggeredByImage',
        'env': 'env',
        'metadata': 'metadata',
        'last_version': 'lastVersion',
        'revision': 'revision',
        'kind': 'kind',
    }

    __types__ = {
        'binary': 'v1.BinaryBuildSource',
        'from_': 'v1.ObjectReference',
        'env': 'v1.EnvVar',
        'triggered_by': 'v1.BuildTriggerCause',
        'triggered_by_image': 'v1.ObjectReference',
        'metadata': 'v1.ObjectMeta',
        'revision': 'v1.SourceRevision',
    }

    __required__ = set([
        'triggered_by',
    ])

    binary = None # v1.BinaryBuildSource
    from_ = None # v1.ObjectReference
    api_version = None # string
    triggered_by = None # array (required)
    triggered_by_image = None # v1.ObjectReference
    env = None # array
    metadata = None # v1.ObjectMeta
    last_version = None # integer
    revision = None # v1.SourceRevision
    kind = None # string

    def __init__(self, *, triggered_by, **_kwargs_):
        self.env = []

        self.kind = 'SourceRevision'

        self.triggered_by = triggered_by

        super().__init__(**_kwargs_)

@register_model
class v1_BuildSource(Resource):

    """BuildSource is the SCM used for the build."""

    __kind__ = 'v1.BuildSource'

    __fields__ = {
        'binary': 'binary',
        'type': 'type',
        'source_secret': 'sourceSecret',
        'secrets': 'secrets',
        'context_dir': 'contextDir',
        'git': 'git',
        'images': 'images',
        'dockerfile': 'dockerfile',
    }

    __types__ = {
        'binary': 'v1.BinaryBuildSource',
        'secrets': 'v1.SecretBuildSource',
        'git': 'v1.GitBuildSource',
        'images': 'v1.ImageSource',
        'source_secret': 'v1.LocalObjectReference',
    }

    __required__ = set([
        'type',
    ])

    binary = None # v1.BinaryBuildSource
    type = None # string (required)
    source_secret = None # v1.LocalObjectReference
    secrets = None # array
    context_dir = None # string
    git = None # v1.GitBuildSource
    images = None # array
    dockerfile = None # string

    def __init__(self, *, type, **_kwargs_):
        self.secrets = []
        self.images = []

        self.type = type

        super().__init__(**_kwargs_)

@register_model
class v1_BuildSpec(Resource):

    """BuildSpec has the information to represent a build and also additional
    information about a build"""

    __kind__ = 'v1.BuildSpec'

    __fields__ = {
        'output': 'output',
        'service_account': 'serviceAccount',
        'revision': 'revision',
        'triggered_by': 'triggeredBy',
        'resources': 'resources',
        'post_commit': 'postCommit',
        'source': 'source',
        'completion_deadline_seconds': 'completionDeadlineSeconds',
        'strategy': 'strategy',
    }

    __types__ = {
        'output': 'v1.BuildOutput',
        'revision': 'v1.SourceRevision',
        'triggered_by': 'v1.BuildTriggerCause',
        'resources': 'v1.ResourceRequirements',
        'source': 'v1.BuildSource',
        'strategy': 'v1.BuildStrategy',
        'post_commit': 'v1.BuildPostCommitSpec',
    }

    __required__ = set([
        'strategy',
        'triggered_by',
    ])

    output = None # v1.BuildOutput
    service_account = None # string
    revision = None # v1.SourceRevision
    triggered_by = None # array (required)
    resources = None # v1.ResourceRequirements
    post_commit = None # v1.BuildPostCommitSpec
    source = None # v1.BuildSource
    completion_deadline_seconds = None # integer
    strategy = None # v1.BuildStrategy (required)

    def __init__(self, *, strategy, triggered_by, **_kwargs_):

        self.strategy = strategy
        self.triggered_by = triggered_by

        super().__init__(**_kwargs_)

@register_model
class v1_BuildStatus(Resource):

    """BuildStatus contains the status of a build"""

    __kind__ = 'v1.BuildStatus'

    __fields__ = {
        'cancelled': 'cancelled',
        'output_docker_image_reference': 'outputDockerImageReference',
        'reason': 'reason',
        'duration': 'duration',
        'start_timestamp': 'startTimestamp',
        'phase': 'phase',
        'message': 'message',
        'completion_timestamp': 'completionTimestamp',
        'config': 'config',
    }

    __types__ = {
        'duration': 'time.Duration',
        'config': 'v1.ObjectReference',
    }

    __required__ = set([
        'phase',
    ])

    cancelled = None # boolean
    output_docker_image_reference = None # string
    reason = None # string
    duration = None # time.Duration
    start_timestamp = None # string
    phase = None # string (required)
    message = None # string
    completion_timestamp = None # string
    config = None # v1.ObjectReference

    def __init__(self, *, phase, **_kwargs_):

        self.phase = phase

        super().__init__(**_kwargs_)

@register_model
class v1_BuildStrategy(Resource):

    """BuildStrategy contains the details of how to perform a build."""

    __kind__ = 'v1.BuildStrategy'

    __fields__ = {
        'custom_strategy': 'customStrategy',
        'docker_strategy': 'dockerStrategy',
        'type': 'type',
        'jenkins_pipeline_strategy': 'jenkinsPipelineStrategy',
        'source_strategy': 'sourceStrategy',
    }

    __types__ = {
        'custom_strategy': 'v1.CustomBuildStrategy',
        'source_strategy': 'v1.SourceBuildStrategy',
        'docker_strategy': 'v1.DockerBuildStrategy',
        'jenkins_pipeline_strategy': 'v1.JenkinsPipelineBuildStrategy',
    }

    __required__ = set([
        'type',
    ])

    custom_strategy = None # v1.CustomBuildStrategy
    docker_strategy = None # v1.DockerBuildStrategy
    type = None # string (required)
    jenkins_pipeline_strategy = None # v1.JenkinsPipelineBuildStrategy
    source_strategy = None # v1.SourceBuildStrategy

    def __init__(self, *, type, **_kwargs_):

        self.type = type

        super().__init__(**_kwargs_)

@register_model
class v1_BuildTriggerCause(Resource):

    """BuildTriggerCause holds information about a triggered build. It is
    used for displaying build trigger data for each build and build
    configuration in oc describe. It is also used to describe which
    triggers led to the most recent update in the build configuration."""

    __kind__ = 'v1.BuildTriggerCause'

    __fields__ = {
        'image_change_build': 'imageChangeBuild',
        'message': 'message',
        'github_web_hook': 'githubWebHook',
        'generic_web_hook': 'genericWebHook',
    }

    __types__ = {
        'github_web_hook': 'v1.GitHubWebHookCause',
        'image_change_build': 'v1.ImageChangeCause',
        'generic_web_hook': 'v1.GenericWebHookCause',
    }

    __required__ = set()

    image_change_build = None # v1.ImageChangeCause
    message = None # string
    github_web_hook = None # v1.GitHubWebHookCause
    generic_web_hook = None # v1.GenericWebHookCause

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_BuildTriggerPolicy(Resource):

    """BuildTriggerPolicy describes a policy for a single trigger that
    results in a new Build."""

    __kind__ = 'v1.BuildTriggerPolicy'

    __fields__ = {
        'generic': 'generic',
        'github': 'github',
        'type': 'type',
        'image_change': 'imageChange',
    }

    __types__ = {
        'generic': 'v1.WebHookTrigger',
        'github': 'v1.WebHookTrigger',
        'image_change': 'v1.ImageChangeTrigger',
    }

    __required__ = set([
        'type',
    ])

    generic = None # v1.WebHookTrigger
    github = None # v1.WebHookTrigger
    type = None # string (required)
    image_change = None # v1.ImageChangeTrigger

    def __init__(self, *, type, **_kwargs_):

        self.type = type

        super().__init__(**_kwargs_)

@register_model
class v1_Capabilities(Resource):

    """Adds and removes POSIX capabilities from running containers."""

    __kind__ = 'v1.Capabilities'

    __fields__ = {
        'drop': 'drop',
        'add': 'add',
    }

    __types__ = {
        'add': 'v1.Capability',
    }

    __required__ = set()

    drop = None # array
    add = None # array

    def __init__(self, **_kwargs_):
        self.drop = []
        self.add = []

        super().__init__(**_kwargs_)

@register_model
class v1_Capability(Resource):

    __kind__ = 'v1.Capability'

    __fields__ = {
    }

    __types__ = {
    }

    __required__ = set()


    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_CephFSVolumeSource(Resource):

    """Represents a Ceph Filesystem mount that lasts the lifetime of a pod
    Cephfs volumes do not support ownership management or SELinux
    relabeling."""

    __kind__ = 'v1.CephFSVolumeSource'

    __fields__ = {
        'monitors': 'monitors',
        'secret_file': 'secretFile',
        'read_only': 'readOnly',
        'user': 'user',
        'path': 'path',
        'secret_ref': 'secretRef',
    }

    __types__ = {
        'secret_ref': 'v1.LocalObjectReference',
    }

    __required__ = set([
        'monitors',
    ])

    monitors = None # array (required)
    secret_file = None # string
    read_only = None # boolean
    user = None # string
    path = None # string
    secret_ref = None # v1.LocalObjectReference

    def __init__(self, *, monitors, **_kwargs_):

        self.monitors = monitors

        super().__init__(**_kwargs_)

@register_model
class v1_CinderVolumeSource(Resource):

    """Represents a cinder volume resource in Openstack. A Cinder volume must
    exist before mounting to a container. The volume must also be in
    the same region as the kubelet. Cinder volumes support ownership
    management and SELinux relabeling."""

    __kind__ = 'v1.CinderVolumeSource'

    __fields__ = {
        'read_only': 'readOnly',
        'volume_id': 'volumeID',
        'fs_type': 'fsType',
    }

    __types__ = {
    }

    __required__ = set([
        'volume_id',
    ])

    read_only = None # boolean
    volume_id = None # string (required)
    fs_type = None # string

    def __init__(self, *, volume_id, **_kwargs_):

        self.volume_id = volume_id

        super().__init__(**_kwargs_)

@register_model
class v1_ClusterNetwork(Resource):

    """ClusterNetwork describes a cluster network"""

    __kind__ = 'v1.ClusterNetwork'

    __fields__ = {
        'service_network': 'serviceNetwork',
        'api_version': 'apiVersion',
        'hostsubnetlength': 'hostsubnetlength',
        'plugin_name': 'pluginName',
        'network': 'network',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
    }

    __required__ = set([
        'hostsubnetlength',
        'network',
        'service_network',
    ])

    service_network = None # string (required)
    api_version = None # string
    hostsubnetlength = None # integer (required)
    plugin_name = None # string
    network = None # string (required)
    metadata = None # v1.ObjectMeta
    kind = None # string

    def __init__(self, *, hostsubnetlength, network, service_network, **_kwargs_):

        self.kind = 'ObjectMeta'

        self.hostsubnetlength = hostsubnetlength
        self.network = network
        self.service_network = service_network

        super().__init__(**_kwargs_)

@register_model
class v1_ClusterNetworkList(Resource):

    """ClusterNetworkList is a collection of ClusterNetworks"""

    __kind__ = 'v1.ClusterNetworkList'

    __fields__ = {
        'items': 'items',
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'kind': 'kind',
    }

    __types__ = {
        'items': 'v1.ClusterNetwork',
        'metadata': 'unversioned.ListMeta',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    metadata = None # unversioned.ListMeta
    api_version = None # string
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'ListMeta'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_ClusterPolicy(Resource):

    """ClusterPolicy is a object that holds all the ClusterRoles for a
    particular namespace.  There is at most one ClusterPolicy document
    per namespace."""

    __kind__ = 'v1.ClusterPolicy'

    __fields__ = {
        'roles': 'roles',
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'last_modified': 'lastModified',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
        'roles': 'v1.NamedClusterRole',
    }

    __required__ = set([
        'last_modified',
        'roles',
    ])

    roles = None # array (required)
    metadata = None # v1.ObjectMeta
    api_version = None # string
    last_modified = None # string (required)
    kind = None # string

    def __init__(self, *, last_modified, roles, **_kwargs_):

        self.kind = 'NamedClusterRole'

        self.last_modified = last_modified
        self.roles = roles

        super().__init__(**_kwargs_)

@register_model
class v1_ClusterPolicyBinding(Resource):

    """ClusterPolicyBinding is a object that holds all the
    ClusterRoleBindings for a particular namespace.  There is one
    ClusterPolicyBinding document per referenced ClusterPolicy
    namespace"""

    __kind__ = 'v1.ClusterPolicyBinding'

    __fields__ = {
        'api_version': 'apiVersion',
        'last_modified': 'lastModified',
        'metadata': 'metadata',
        'role_bindings': 'roleBindings',
        'policy_ref': 'policyRef',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
        'policy_ref': 'v1.ObjectReference',
        'role_bindings': 'v1.NamedClusterRoleBinding',
    }

    __required__ = set([
        'last_modified',
        'policy_ref',
        'role_bindings',
    ])

    api_version = None # string
    last_modified = None # string (required)
    metadata = None # v1.ObjectMeta
    role_bindings = None # array (required)
    policy_ref = None # v1.ObjectReference (required)
    kind = None # string

    def __init__(self, *, last_modified, policy_ref, role_bindings, **_kwargs_):

        self.kind = 'NamedClusterRoleBinding'

        self.last_modified = last_modified
        self.policy_ref = policy_ref
        self.role_bindings = role_bindings

        super().__init__(**_kwargs_)

@register_model
class v1_ClusterPolicyBindingList(Resource):

    """ClusterPolicyBindingList is a collection of ClusterPolicyBindings"""

    __kind__ = 'v1.ClusterPolicyBindingList'

    __fields__ = {
        'items': 'items',
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'kind': 'kind',
    }

    __types__ = {
        'items': 'v1.ClusterPolicyBinding',
        'metadata': 'unversioned.ListMeta',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    metadata = None # unversioned.ListMeta
    api_version = None # string
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'ListMeta'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_ClusterPolicyList(Resource):

    """ClusterPolicyList is a collection of ClusterPolicies"""

    __kind__ = 'v1.ClusterPolicyList'

    __fields__ = {
        'items': 'items',
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'kind': 'kind',
    }

    __types__ = {
        'items': 'v1.ClusterPolicy',
        'metadata': 'unversioned.ListMeta',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    metadata = None # unversioned.ListMeta
    api_version = None # string
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'ListMeta'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_ClusterResourceQuota(Resource):

    """ClusterResourceQuota mirrors ResourceQuota at a cluster scope.  This
    object is easily convertible to synthetic ResourceQuota object to
    allow quota evaluation re-use."""

    __kind__ = 'v1.ClusterResourceQuota'

    __fields__ = {
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'spec': 'spec',
        'status': 'status',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
        'spec': 'v1.ClusterResourceQuotaSpec',
        'status': 'v1.ClusterResourceQuotaStatus',
    }

    __required__ = set([
        'metadata',
        'spec',
    ])

    metadata = None # v1.ObjectMeta (required)
    api_version = None # string
    spec = None # v1.ClusterResourceQuotaSpec (required)
    status = None # v1.ClusterResourceQuotaStatus
    kind = None # string

    def __init__(self, *, metadata, spec, **_kwargs_):

        self.kind = 'ClusterResourceQuotaStatus'

        self.metadata = metadata
        self.spec = spec

        super().__init__(**_kwargs_)

@register_model
class v1_ClusterResourceQuotaList(Resource):

    """ClusterResourceQuotaList is a collection of ClusterResourceQuotas"""

    __kind__ = 'v1.ClusterResourceQuotaList'

    __fields__ = {
        'items': 'items',
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'kind': 'kind',
    }

    __types__ = {
        'items': 'v1.ClusterResourceQuota',
        'metadata': 'unversioned.ListMeta',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    metadata = None # unversioned.ListMeta
    api_version = None # string
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'ListMeta'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_ClusterResourceQuotaSelector(Resource):

    """ClusterResourceQuotaSelector is used to select projects.  At least one
    of LabelSelector or AnnotationSelector must present.  If only one
    is present, it is the only selection criteria.  If both are
    specified, the project must match both restrictions."""

    __kind__ = 'v1.ClusterResourceQuotaSelector'

    __fields__ = {
        'labels': 'labels',
        'annotations': 'annotations',
    }

    __types__ = {
        'labels': 'unversioned.LabelSelector',
    }

    __required__ = set([
        'annotations',
        'labels',
    ])

    labels = None # unversioned.LabelSelector (required)
    annotations = None # object (required)

    def __init__(self, *, annotations, labels, **_kwargs_):

        self.annotations = annotations
        self.labels = labels

        super().__init__(**_kwargs_)

@register_model
class v1_ClusterResourceQuotaSpec(Resource):

    """ClusterResourceQuotaSpec defines the desired quota restrictions"""

    __kind__ = 'v1.ClusterResourceQuotaSpec'

    __fields__ = {
        'selector': 'selector',
        'quota': 'quota',
    }

    __types__ = {
        'selector': 'v1.ClusterResourceQuotaSelector',
        'quota': 'v1.ResourceQuotaSpec',
    }

    __required__ = set([
        'quota',
        'selector',
    ])

    selector = None # v1.ClusterResourceQuotaSelector (required)
    quota = None # v1.ResourceQuotaSpec (required)

    def __init__(self, *, quota, selector, **_kwargs_):

        self.quota = quota
        self.selector = selector

        super().__init__(**_kwargs_)

@register_model
class v1_ClusterResourceQuotaStatus(Resource):

    """ClusterResourceQuotaStatus defines the actual enforced quota and its
    current usage"""

    __kind__ = 'v1.ClusterResourceQuotaStatus'

    __fields__ = {
        'total': 'total',
        'namespaces': 'namespaces',
    }

    __types__ = {
        'total': 'v1.ResourceQuotaStatus',
        'namespaces': 'v1.ResourceQuotaStatusByNamespace',
    }

    __required__ = set([
        'namespaces',
        'total',
    ])

    total = None # v1.ResourceQuotaStatus (required)
    namespaces = None # array (required)

    def __init__(self, *, namespaces, total, **_kwargs_):

        self.namespaces = namespaces
        self.total = total

        super().__init__(**_kwargs_)

@register_model
class v1_ClusterRole(Resource):

    """ClusterRole is a logical grouping of PolicyRules that can be
    referenced as a unit by ClusterRoleBindings."""

    __kind__ = 'v1.ClusterRole'

    __fields__ = {
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'rules': 'rules',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
        'rules': 'v1.PolicyRule',
    }

    __required__ = set([
        'rules',
    ])

    metadata = None # v1.ObjectMeta
    api_version = None # string
    rules = None # array (required)
    kind = None # string

    def __init__(self, *, rules, **_kwargs_):

        self.kind = 'PolicyRule'

        self.rules = rules

        super().__init__(**_kwargs_)

@register_model
class v1_ClusterRoleBinding(Resource):

    """ClusterRoleBinding references a ClusterRole, but not contain it.  It
    can reference any ClusterRole in the same namespace or in the
    global namespace. It adds who information via Users and Groups and
    namespace information by which namespace it exists in.
    ClusterRoleBindings in a given namespace only have effect in that
    namespace (excepting the master namespace which has power in all
    namespaces)."""

    __kind__ = 'v1.ClusterRoleBinding'

    __fields__ = {
        'role_ref': 'roleRef',
        'subjects': 'subjects',
        'api_version': 'apiVersion',
        'group_names': 'groupNames',
        'metadata': 'metadata',
        'user_names': 'userNames',
        'kind': 'kind',
    }

    __types__ = {
        'role_ref': 'v1.ObjectReference',
        'subjects': 'v1.ObjectReference',
        'metadata': 'v1.ObjectMeta',
    }

    __required__ = set([
        'group_names',
        'role_ref',
        'subjects',
        'user_names',
    ])

    role_ref = None # v1.ObjectReference (required)
    subjects = None # array (required)
    api_version = None # string
    group_names = None # array (required)
    metadata = None # v1.ObjectMeta
    user_names = None # array (required)
    kind = None # string

    def __init__(self, *, group_names, role_ref, subjects, user_names, **_kwargs_):

        self.kind = 'ObjectMeta'

        self.group_names = group_names
        self.role_ref = role_ref
        self.subjects = subjects
        self.user_names = user_names

        super().__init__(**_kwargs_)

@register_model
class v1_ClusterRoleBindingList(Resource):

    """ClusterRoleBindingList is a collection of ClusterRoleBindings"""

    __kind__ = 'v1.ClusterRoleBindingList'

    __fields__ = {
        'items': 'items',
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'kind': 'kind',
    }

    __types__ = {
        'items': 'v1.ClusterRoleBinding',
        'metadata': 'unversioned.ListMeta',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    metadata = None # unversioned.ListMeta
    api_version = None # string
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'ListMeta'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_ClusterRoleList(Resource):

    """ClusterRoleList is a collection of ClusterRoles"""

    __kind__ = 'v1.ClusterRoleList'

    __fields__ = {
        'items': 'items',
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'kind': 'kind',
    }

    __types__ = {
        'items': 'v1.ClusterRole',
        'metadata': 'unversioned.ListMeta',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    metadata = None # unversioned.ListMeta
    api_version = None # string
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'ListMeta'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_ClusterRoleScopeRestriction(Resource):

    """ClusterRoleScopeRestriction describes restrictions on cluster role
    scopes"""

    __kind__ = 'v1.ClusterRoleScopeRestriction'

    __fields__ = {
        'role_names': 'roleNames',
        'allow_escalation': 'allowEscalation',
        'namespaces': 'namespaces',
    }

    __types__ = {
    }

    __required__ = set([
        'allow_escalation',
        'namespaces',
        'role_names',
    ])

    role_names = None # array (required)
    allow_escalation = None # boolean (required)
    namespaces = None # array (required)

    def __init__(self, *, allow_escalation, namespaces, role_names, **_kwargs_):

        self.allow_escalation = allow_escalation
        self.namespaces = namespaces
        self.role_names = role_names

        super().__init__(**_kwargs_)

@register_model
class v1_ConfigMapKeySelector(Resource):

    """Selects a key from a ConfigMap."""

    __kind__ = 'v1.ConfigMapKeySelector'

    __fields__ = {
        'name': 'name',
        'key': 'key',
    }

    __types__ = {
    }

    __required__ = set([
        'key',
    ])

    name = None # string
    key = None # string (required)

    def __init__(self, *, key, **_kwargs_):

        self.key = key

        super().__init__(**_kwargs_)

@register_model
class v1_ConfigMapVolumeSource(Resource):

    """Adapts a ConfigMap into a volume.  The contents of the target
    ConfigMap's Data field will be presented in a volume as files
    using the keys in the Data field as the file names, unless the
    items element is populated with specific mappings of keys to
    paths. ConfigMap volumes support ownership management and SELinux
    relabeling."""

    __kind__ = 'v1.ConfigMapVolumeSource'

    __fields__ = {
        'name': 'name',
        'items': 'items',
    }

    __types__ = {
        'items': 'v1.KeyToPath',
    }

    __required__ = set()

    name = None # string
    items = None # array

    def __init__(self, **_kwargs_):
        self.items = []

        super().__init__(**_kwargs_)

@register_model
class v1_Container(Resource):

    """A single application container that you want to run within a pod."""

    __kind__ = 'v1.Container'

    __fields__ = {
        'name': 'name',
        'ports': 'ports',
        'stdin_once': 'stdinOnce',
        'command': 'command',
        'stdin': 'stdin',
        'liveness_probe': 'livenessProbe',
        'readiness_probe': 'readinessProbe',
        'args': 'args',
        'env': 'env',
        'lifecycle': 'lifecycle',
        'termination_message_path': 'terminationMessagePath',
        'image_pull_policy': 'imagePullPolicy',
        'resources': 'resources',
        'volume_mounts': 'volumeMounts',
        'security_context': 'securityContext',
        'tty': 'tty',
        'working_dir': 'workingDir',
        'image': 'image',
    }

    __types__ = {
        'readiness_probe': 'v1.Probe',
        'env': 'v1.EnvVar',
        'lifecycle': 'v1.Lifecycle',
        'security_context': 'v1.SecurityContext',
        'liveness_probe': 'v1.Probe',
        'volume_mounts': 'v1.VolumeMount',
        'ports': 'v1.ContainerPort',
        'resources': 'v1.ResourceRequirements',
    }

    __required__ = set([
        'name',
    ])

    name = None # string (required)
    ports = None # array
    stdin_once = None # boolean
    command = None # array
    stdin = None # boolean
    liveness_probe = None # v1.Probe
    readiness_probe = None # v1.Probe
    args = None # array
    env = None # array
    lifecycle = None # v1.Lifecycle
    termination_message_path = None # string
    image_pull_policy = None # string
    resources = None # v1.ResourceRequirements
    volume_mounts = None # array
    security_context = None # v1.SecurityContext
    tty = None # boolean
    working_dir = None # string
    image = None # string

    def __init__(self, *, name, **_kwargs_):
        self.ports = []
        self.command = []
        self.args = []
        self.env = []
        self.volume_mounts = []

        self.name = name

        super().__init__(**_kwargs_)

@register_model
class v1_ContainerPort(Resource):

    """ContainerPort represents a network port in a single container."""

    __kind__ = 'v1.ContainerPort'

    __fields__ = {
        'name': 'name',
        'protocol': 'protocol',
        'host_port': 'hostPort',
        'container_port': 'containerPort',
        'host_ip': 'hostIP',
    }

    __types__ = {
    }

    __required__ = set([
        'container_port',
    ])

    name = None # string
    protocol = None # string
    host_port = None # integer
    container_port = None # integer (required)
    host_ip = None # string

    def __init__(self, *, container_port, **_kwargs_):

        self.container_port = container_port

        super().__init__(**_kwargs_)

@register_model
class v1_CustomBuildStrategy(Resource):

    """CustomBuildStrategy defines input parameters specific to Custom build."""

    __kind__ = 'v1.CustomBuildStrategy'

    __fields__ = {
        'from_': 'from',
        'pull_secret': 'pullSecret',
        'env': 'env',
        'force_pull': 'forcePull',
        'secrets': 'secrets',
        'expose_docker_socket': 'exposeDockerSocket',
        'build_api_version': 'buildAPIVersion',
    }

    __types__ = {
        'from_': 'v1.ObjectReference',
        'pull_secret': 'v1.LocalObjectReference',
        'env': 'v1.EnvVar',
        'secrets': 'v1.SecretSpec',
    }

    __required__ = set([
        'from_',
    ])

    from_ = None # v1.ObjectReference (required)
    pull_secret = None # v1.LocalObjectReference
    env = None # array
    force_pull = None # boolean
    secrets = None # array
    expose_docker_socket = None # boolean
    build_api_version = None # string

    def __init__(self, *, from_, **_kwargs_):
        self.env = []
        self.secrets = []

        self.from_ = from_

        super().__init__(**_kwargs_)

@register_model
class v1_CustomDeploymentStrategyParams(Resource):

    """CustomDeploymentStrategyParams are the input to the Custom deployment
    strategy."""

    __kind__ = 'v1.CustomDeploymentStrategyParams'

    __fields__ = {
        'environment': 'environment',
        'command': 'command',
        'image': 'image',
    }

    __types__ = {
        'environment': 'v1.EnvVar',
    }

    __required__ = set()

    environment = None # array
    command = None # array
    image = None # string

    def __init__(self, **_kwargs_):
        self.environment = []
        self.command = []

        super().__init__(**_kwargs_)

@register_model
class v1_DeleteOptions(Resource):

    """DeleteOptions may be provided when deleting an API object"""

    __kind__ = 'v1.DeleteOptions'

    __fields__ = {
        'preconditions': 'preconditions',
        'api_version': 'apiVersion',
        'grace_period_seconds': 'gracePeriodSeconds',
        'orphan_dependents': 'orphanDependents',
        'kind': 'kind',
    }

    __types__ = {
        'preconditions': 'v1.Preconditions',
    }

    __required__ = set()

    preconditions = None # v1.Preconditions
    api_version = None # string
    grace_period_seconds = None # integer
    orphan_dependents = None # boolean
    kind = None # string

    def __init__(self, **_kwargs_):

        self.kind = 'Preconditions'

        super().__init__(**_kwargs_)

@register_model
class v1_DeploymentCause(Resource):

    """DeploymentCause captures information about a particular cause of a
    deployment."""

    __kind__ = 'v1.DeploymentCause'

    __fields__ = {
        'image_trigger': 'imageTrigger',
        'type': 'type',
    }

    __types__ = {
        'image_trigger': 'v1.DeploymentCauseImageTrigger',
    }

    __required__ = set([
        'type',
    ])

    image_trigger = None # v1.DeploymentCauseImageTrigger
    type = None # string (required)

    def __init__(self, *, type, **_kwargs_):

        self.type = type

        super().__init__(**_kwargs_)

@register_model
class v1_DeploymentCauseImageTrigger(Resource):

    """DeploymentCauseImageTrigger represents details about the cause of a
    deployment originating from an image change trigger"""

    __kind__ = 'v1.DeploymentCauseImageTrigger'

    __fields__ = {
        'from_': 'from',
    }

    __types__ = {
        'from_': 'v1.ObjectReference',
    }

    __required__ = set([
        'from_',
    ])

    from_ = None # v1.ObjectReference (required)

    def __init__(self, *, from_, **_kwargs_):

        self.from_ = from_

        super().__init__(**_kwargs_)

@register_model
class v1_DeploymentConfig(Resource):

    """DeploymentConfig represents a configuration for a single deployment
    (represented as a ReplicationController). It also contains details
    about changes which resulted in the current state of the
    DeploymentConfig. Each change to the DeploymentConfig which should
    result in a new deployment results in an increment of
    LatestVersion."""

    __kind__ = 'v1.DeploymentConfig'

    __fields__ = {
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'spec': 'spec',
        'status': 'status',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
        'spec': 'v1.DeploymentConfigSpec',
        'status': 'v1.DeploymentConfigStatus',
    }

    __required__ = set([
        'spec',
        'status',
    ])

    metadata = None # v1.ObjectMeta
    api_version = None # string
    spec = None # v1.DeploymentConfigSpec (required)
    status = None # v1.DeploymentConfigStatus (required)
    kind = None # string

    def __init__(self, *, spec, status, **_kwargs_):

        self.kind = 'DeploymentConfigStatus'

        self.spec = spec
        self.status = status

        super().__init__(**_kwargs_)

@register_model
class v1_DeploymentConfigList(Resource):

    """DeploymentConfigList is a collection of deployment configs."""

    __kind__ = 'v1.DeploymentConfigList'

    __fields__ = {
        'items': 'items',
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'kind': 'kind',
    }

    __types__ = {
        'items': 'v1.DeploymentConfig',
        'metadata': 'unversioned.ListMeta',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    metadata = None # unversioned.ListMeta
    api_version = None # string
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'ListMeta'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_DeploymentConfigRollback(Resource):

    """DeploymentConfigRollback provides the input to rollback generation."""

    __kind__ = 'v1.DeploymentConfigRollback'

    __fields__ = {
        'name': 'name',
        'api_version': 'apiVersion',
        'spec': 'spec',
        'updated_annotations': 'updatedAnnotations',
        'kind': 'kind',
    }

    __types__ = {
        'spec': 'v1.DeploymentConfigRollbackSpec',
    }

    __required__ = set([
        'name',
        'spec',
    ])

    name = None # string (required)
    api_version = None # string
    spec = None # v1.DeploymentConfigRollbackSpec (required)
    updated_annotations = None # object
    kind = None # string

    def __init__(self, *, name, spec, **_kwargs_):

        self.kind = 'DeploymentConfigRollbackSpec'

        self.name = name
        self.spec = spec

        super().__init__(**_kwargs_)

@register_model
class v1_DeploymentConfigRollbackSpec(Resource):

    """DeploymentConfigRollbackSpec represents the options for rollback
    generation."""

    __kind__ = 'v1.DeploymentConfigRollbackSpec'

    __fields__ = {
        'from_': 'from',
        'include_replication_meta': 'includeReplicationMeta',
        'include_template': 'includeTemplate',
        'include_triggers': 'includeTriggers',
        'include_strategy': 'includeStrategy',
        'revision': 'revision',
    }

    __types__ = {
        'from_': 'v1.ObjectReference',
    }

    __required__ = set([
        'from_',
        'include_replication_meta',
        'include_strategy',
        'include_template',
        'include_triggers',
    ])

    from_ = None # v1.ObjectReference (required)
    include_replication_meta = None # boolean (required)
    include_template = None # boolean (required)
    include_triggers = None # boolean (required)
    include_strategy = None # boolean (required)
    revision = None # integer

    def __init__(self, *, from_, include_replication_meta, include_strategy, include_template, include_triggers, **_kwargs_):

        self.from_ = from_
        self.include_replication_meta = include_replication_meta
        self.include_strategy = include_strategy
        self.include_template = include_template
        self.include_triggers = include_triggers

        super().__init__(**_kwargs_)

@register_model
class v1_DeploymentConfigSpec(Resource):

    """DeploymentConfigSpec represents the desired state of the deployment."""

    __kind__ = 'v1.DeploymentConfigSpec'

    __fields__ = {
        'paused': 'paused',
        'template': 'template',
        'strategy': 'strategy',
        'triggers': 'triggers',
        'revision_history_limit': 'revisionHistoryLimit',
        'selector': 'selector',
        'test': 'test',
        'min_ready_seconds': 'minReadySeconds',
        'replicas': 'replicas',
    }

    __types__ = {
        'template': 'v1.PodTemplateSpec',
        'triggers': 'v1.DeploymentTriggerPolicy',
        'strategy': 'v1.DeploymentStrategy',
    }

    __required__ = set([
        'replicas',
        'strategy',
        'test',
        'triggers',
    ])

    paused = None # boolean
    template = None # v1.PodTemplateSpec
    strategy = None # v1.DeploymentStrategy (required)
    triggers = None # array (required)
    revision_history_limit = None # integer
    selector = None # object
    test = None # boolean (required)
    min_ready_seconds = None # integer
    replicas = None # integer (required)

    def __init__(self, *, replicas, strategy, test, triggers, **_kwargs_):

        self.replicas = replicas
        self.strategy = strategy
        self.test = test
        self.triggers = triggers

        super().__init__(**_kwargs_)

@register_model
class v1_DeploymentConfigStatus(Resource):

    """DeploymentConfigStatus represents the current deployment state."""

    __kind__ = 'v1.DeploymentConfigStatus'

    __fields__ = {
        'details': 'details',
        'updated_replicas': 'updatedReplicas',
        'replicas': 'replicas',
        'unavailable_replicas': 'unavailableReplicas',
        'latest_version': 'latestVersion',
        'observed_generation': 'observedGeneration',
        'available_replicas': 'availableReplicas',
    }

    __types__ = {
        'details': 'v1.DeploymentDetails',
    }

    __required__ = set()

    details = None # v1.DeploymentDetails
    updated_replicas = None # integer
    replicas = None # integer
    unavailable_replicas = None # integer
    latest_version = None # integer
    observed_generation = None # integer
    available_replicas = None # integer

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_DeploymentDetails(Resource):

    """DeploymentDetails captures information about the causes of a
    deployment."""

    __kind__ = 'v1.DeploymentDetails'

    __fields__ = {
        'message': 'message',
        'causes': 'causes',
    }

    __types__ = {
        'causes': 'v1.DeploymentCause',
    }

    __required__ = set([
        'causes',
    ])

    message = None # string
    causes = None # array (required)

    def __init__(self, *, causes, **_kwargs_):

        self.causes = causes

        super().__init__(**_kwargs_)

@register_model
class v1_DeploymentLog(Resource):

    """DeploymentLog represents the logs for a deployment"""

    __kind__ = 'v1.DeploymentLog'

    __fields__ = {
        'api_version': 'apiVersion',
        'kind': 'kind',
    }

    __types__ = {
    }

    __required__ = set()

    api_version = None # string
    kind = None # string

    def __init__(self, **_kwargs_):

        self.kind = 'DeploymentLog'

        super().__init__(**_kwargs_)

@register_model
class v1_DeploymentStrategy(Resource):

    """DeploymentStrategy describes how to perform a deployment."""

    __kind__ = 'v1.DeploymentStrategy'

    __fields__ = {
        'type': 'type',
        'recreate_params': 'recreateParams',
        'resources': 'resources',
        'rolling_params': 'rollingParams',
        'labels': 'labels',
        'annotations': 'annotations',
        'custom_params': 'customParams',
    }

    __types__ = {
        'rolling_params': 'v1.RollingDeploymentStrategyParams',
        'custom_params': 'v1.CustomDeploymentStrategyParams',
        'recreate_params': 'v1.RecreateDeploymentStrategyParams',
        'resources': 'v1.ResourceRequirements',
    }

    __required__ = set()

    type = None # string
    recreate_params = None # v1.RecreateDeploymentStrategyParams
    resources = None # v1.ResourceRequirements
    rolling_params = None # v1.RollingDeploymentStrategyParams
    labels = None # object
    annotations = None # object
    custom_params = None # v1.CustomDeploymentStrategyParams

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_DeploymentTriggerImageChangeParams(Resource):

    """DeploymentTriggerImageChangeParams represents the parameters to the
    ImageChange trigger."""

    __kind__ = 'v1.DeploymentTriggerImageChangeParams'

    __fields__ = {
        'container_names': 'containerNames',
        'automatic': 'automatic',
        'last_triggered_image': 'lastTriggeredImage',
        'from_': 'from',
    }

    __types__ = {
        'from_': 'v1.ObjectReference',
    }

    __required__ = set([
        'from_',
    ])

    container_names = None # array
    automatic = None # boolean
    last_triggered_image = None # string
    from_ = None # v1.ObjectReference (required)

    def __init__(self, *, from_, **_kwargs_):
        self.container_names = []

        self.from_ = from_

        super().__init__(**_kwargs_)

@register_model
class v1_DeploymentTriggerPolicy(Resource):

    """DeploymentTriggerPolicy describes a policy for a single trigger that
    results in a new deployment."""

    __kind__ = 'v1.DeploymentTriggerPolicy'

    __fields__ = {
        'type': 'type',
        'image_change_params': 'imageChangeParams',
    }

    __types__ = {
        'image_change_params': 'v1.DeploymentTriggerImageChangeParams',
    }

    __required__ = set()

    type = None # string
    image_change_params = None # v1.DeploymentTriggerImageChangeParams

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_DeprecatedDownwardAPIVolumeFile(Resource):

    """DeprecatedDownwardAPIVolumeFile represents information to create the
    file containing the pod field This type is deprecated and should
    be replaced by use of the downwardAPI volume source."""

    __kind__ = 'v1.DeprecatedDownwardAPIVolumeFile'

    __fields__ = {
        'name': 'name',
        'field_ref': 'fieldRef',
        'resource_field_ref': 'resourceFieldRef',
    }

    __types__ = {
        'field_ref': 'v1.ObjectFieldSelector',
        'resource_field_ref': 'v1.ResourceFieldSelector',
    }

    __required__ = set([
        'name',
    ])

    name = None # string (required)
    field_ref = None # v1.ObjectFieldSelector
    resource_field_ref = None # v1.ResourceFieldSelector

    def __init__(self, *, name, **_kwargs_):

        self.name = name

        super().__init__(**_kwargs_)

@register_model
class v1_DeprecatedDownwardAPIVolumeSource(Resource):

    """DeprecatedDownwardAPIVolumeSource represents a volume containing
    downward API info. This type is deprecated and should be replaced
    by use of the downwardAPI volume source."""

    __kind__ = 'v1.DeprecatedDownwardAPIVolumeSource'

    __fields__ = {
        'items': 'items',
    }

    __types__ = {
        'items': 'v1.DeprecatedDownwardAPIVolumeFile',
    }

    __required__ = set()

    items = None # array

    def __init__(self, **_kwargs_):
        self.items = []

        super().__init__(**_kwargs_)

@register_model
class v1_DockerBuildStrategy(Resource):

    """DockerBuildStrategy defines input parameters specific to Docker build."""

    __kind__ = 'v1.DockerBuildStrategy'

    __fields__ = {
        'from_': 'from',
        'pull_secret': 'pullSecret',
        'no_cache': 'noCache',
        'force_pull': 'forcePull',
        'env': 'env',
        'dockerfile_path': 'dockerfilePath',
    }

    __types__ = {
        'from_': 'v1.ObjectReference',
        'pull_secret': 'v1.LocalObjectReference',
        'env': 'v1.EnvVar',
    }

    __required__ = set()

    from_ = None # v1.ObjectReference
    pull_secret = None # v1.LocalObjectReference
    no_cache = None # boolean
    force_pull = None # boolean
    env = None # array
    dockerfile_path = None # string

    def __init__(self, **_kwargs_):
        self.env = []

        super().__init__(**_kwargs_)

@register_model
class v1_DownwardAPIVolumeFile(Resource):

    """DownwardAPIVolumeFile represents information to create the file
    containing the pod field"""

    __kind__ = 'v1.DownwardAPIVolumeFile'

    __fields__ = {
        'path': 'path',
        'field_ref': 'fieldRef',
        'resource_field_ref': 'resourceFieldRef',
    }

    __types__ = {
        'field_ref': 'v1.ObjectFieldSelector',
        'resource_field_ref': 'v1.ResourceFieldSelector',
    }

    __required__ = set([
        'path',
    ])

    path = None # string (required)
    field_ref = None # v1.ObjectFieldSelector
    resource_field_ref = None # v1.ResourceFieldSelector

    def __init__(self, *, path, **_kwargs_):

        self.path = path

        super().__init__(**_kwargs_)

@register_model
class v1_DownwardAPIVolumeSource(Resource):

    """DownwardAPIVolumeSource represents a volume containing downward API
    info. Downward API volumes support ownership management and
    SELinux relabeling."""

    __kind__ = 'v1.DownwardAPIVolumeSource'

    __fields__ = {
        'items': 'items',
    }

    __types__ = {
        'items': 'v1.DownwardAPIVolumeFile',
    }

    __required__ = set()

    items = None # array

    def __init__(self, **_kwargs_):
        self.items = []

        super().__init__(**_kwargs_)

@register_model
class v1_EgressNetworkPolicy(Resource):

    """EgressNetworkPolicy describes the current egress network policy for a
    Namespace. When using the 'redhat/openshift-ovs-multitenant'
    network plugin, traffic from a pod to an IP address outside the
    cluster will be checked against each EgressNetworkPolicyRule in
    the pod's namespace's EgressNetworkPolicy, in order. If no rule
    matches (or no EgressNetworkPolicy is present) then the traffic
    will be allowed by default."""

    __kind__ = 'v1.EgressNetworkPolicy'

    __fields__ = {
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'spec': 'spec',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
        'spec': 'v1.EgressNetworkPolicySpec',
    }

    __required__ = set([
        'spec',
    ])

    metadata = None # v1.ObjectMeta
    api_version = None # string
    spec = None # v1.EgressNetworkPolicySpec (required)
    kind = None # string

    def __init__(self, *, spec, **_kwargs_):

        self.kind = 'EgressNetworkPolicySpec'

        self.spec = spec

        super().__init__(**_kwargs_)

@register_model
class v1_EgressNetworkPolicyList(Resource):

    """EgressNetworkPolicyList is a collection of EgressNetworkPolicy"""

    __kind__ = 'v1.EgressNetworkPolicyList'

    __fields__ = {
        'items': 'items',
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'kind': 'kind',
    }

    __types__ = {
        'items': 'v1.EgressNetworkPolicy',
        'metadata': 'unversioned.ListMeta',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    metadata = None # unversioned.ListMeta
    api_version = None # string
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'ListMeta'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_EgressNetworkPolicyPeer(Resource):

    """EgressNetworkPolicyPeer specifies a target to apply egress network
    policy to"""

    __kind__ = 'v1.EgressNetworkPolicyPeer'

    __fields__ = {
        'cidr_selector': 'cidrSelector',
    }

    __types__ = {
    }

    __required__ = set([
        'cidr_selector',
    ])

    cidr_selector = None # string (required)

    def __init__(self, *, cidr_selector, **_kwargs_):

        self.cidr_selector = cidr_selector

        super().__init__(**_kwargs_)

@register_model
class v1_EgressNetworkPolicyRule(Resource):

    """EgressNetworkPolicyRule contains a single egress network policy rule"""

    __kind__ = 'v1.EgressNetworkPolicyRule'

    __fields__ = {
        'to': 'to',
        'type': 'type',
    }

    __types__ = {
        'to': 'v1.EgressNetworkPolicyPeer',
    }

    __required__ = set([
        'to',
        'type',
    ])

    to = None # v1.EgressNetworkPolicyPeer (required)
    type = None # string (required)

    def __init__(self, *, to, type, **_kwargs_):

        self.to = to
        self.type = type

        super().__init__(**_kwargs_)

@register_model
class v1_EgressNetworkPolicySpec(Resource):

    """EgressNetworkPolicySpec provides a list of policies on outgoing
    network traffic"""

    __kind__ = 'v1.EgressNetworkPolicySpec'

    __fields__ = {
        'egress': 'egress',
    }

    __types__ = {
        'egress': 'v1.EgressNetworkPolicyRule',
    }

    __required__ = set([
        'egress',
    ])

    egress = None # array (required)

    def __init__(self, *, egress, **_kwargs_):

        self.egress = egress

        super().__init__(**_kwargs_)

@register_model
class v1_EmptyDirVolumeSource(Resource):

    """Represents an empty directory for a pod. Empty directory volumes
    support ownership management and SELinux relabeling."""

    __kind__ = 'v1.EmptyDirVolumeSource'

    __fields__ = {
        'medium': 'medium',
    }

    __types__ = {
    }

    __required__ = set()

    medium = None # string

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_EnvVar(Resource):

    """EnvVar represents an environment variable present in a Container."""

    __kind__ = 'v1.EnvVar'

    __fields__ = {
        'name': 'name',
        'value': 'value',
        'value_from': 'valueFrom',
    }

    __types__ = {
        'value_from': 'v1.EnvVarSource',
    }

    __required__ = set([
        'name',
    ])

    name = None # string (required)
    value = None # string
    value_from = None # v1.EnvVarSource

    def __init__(self, *, name, **_kwargs_):

        self.name = name

        super().__init__(**_kwargs_)

@register_model
class v1_EnvVarSource(Resource):

    """EnvVarSource represents a source for the value of an EnvVar."""

    __kind__ = 'v1.EnvVarSource'

    __fields__ = {
        'secret_key_ref': 'secretKeyRef',
        'field_ref': 'fieldRef',
        'config_map_key_ref': 'configMapKeyRef',
        'resource_field_ref': 'resourceFieldRef',
    }

    __types__ = {
        'secret_key_ref': 'v1.SecretKeySelector',
        'field_ref': 'v1.ObjectFieldSelector',
        'resource_field_ref': 'v1.ResourceFieldSelector',
        'config_map_key_ref': 'v1.ConfigMapKeySelector',
    }

    __required__ = set()

    secret_key_ref = None # v1.SecretKeySelector
    field_ref = None # v1.ObjectFieldSelector
    config_map_key_ref = None # v1.ConfigMapKeySelector
    resource_field_ref = None # v1.ResourceFieldSelector

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_ExecAction(Resource):

    """ExecAction describes a "run in container" action."""

    __kind__ = 'v1.ExecAction'

    __fields__ = {
        'command': 'command',
    }

    __types__ = {
    }

    __required__ = set()

    command = None # array

    def __init__(self, **_kwargs_):
        self.command = []

        super().__init__(**_kwargs_)

@register_model
class v1_ExecNewPodHook(Resource):

    """ExecNewPodHook is a hook implementation which runs a command in a new
    pod based on the specified container which is assumed to be part
    of the deployment template."""

    __kind__ = 'v1.ExecNewPodHook'

    __fields__ = {
        'command': 'command',
        'env': 'env',
        'container_name': 'containerName',
        'volumes': 'volumes',
    }

    __types__ = {
        'env': 'v1.EnvVar',
    }

    __required__ = set([
        'command',
        'container_name',
    ])

    command = None # array (required)
    env = None # array
    container_name = None # string (required)
    volumes = None # array

    def __init__(self, *, command, container_name, **_kwargs_):
        self.env = []
        self.volumes = []

        self.command = command
        self.container_name = container_name

        super().__init__(**_kwargs_)

@register_model
class v1_FCVolumeSource(Resource):

    """Represents a Fibre Channel volume. Fibre Channel volumes can only be
    mounted as read/write once. Fibre Channel volumes support
    ownership management and SELinux relabeling."""

    __kind__ = 'v1.FCVolumeSource'

    __fields__ = {
        'target_ww_ns': 'targetWWNs',
        'read_only': 'readOnly',
        'fs_type': 'fsType',
        'lun': 'lun',
    }

    __types__ = {
    }

    __required__ = set([
        'lun',
        'target_ww_ns',
    ])

    target_ww_ns = None # array (required)
    read_only = None # boolean
    fs_type = None # string
    lun = None # integer (required)

    def __init__(self, *, lun, target_ww_ns, **_kwargs_):

        self.lun = lun
        self.target_ww_ns = target_ww_ns

        super().__init__(**_kwargs_)

@register_model
class v1_FinalizerName(Resource):

    __kind__ = 'v1.FinalizerName'

    __fields__ = {
    }

    __types__ = {
    }

    __required__ = set()


    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_FlexVolumeSource(Resource):

    """FlexVolume represents a generic volume resource that is
    provisioned/attached using a exec based plugin. This is an alpha
    feature and may change in future."""

    __kind__ = 'v1.FlexVolumeSource'

    __fields__ = {
        'read_only': 'readOnly',
        'options': 'options',
        'driver': 'driver',
        'fs_type': 'fsType',
        'secret_ref': 'secretRef',
    }

    __types__ = {
        'secret_ref': 'v1.LocalObjectReference',
    }

    __required__ = set([
        'driver',
    ])

    read_only = None # boolean
    options = None # object
    driver = None # string (required)
    fs_type = None # string
    secret_ref = None # v1.LocalObjectReference

    def __init__(self, *, driver, **_kwargs_):

        self.driver = driver

        super().__init__(**_kwargs_)

@register_model
class v1_FlockerVolumeSource(Resource):

    """Represents a Flocker volume mounted by the Flocker agent. Flocker
    volumes do not support ownership management or SELinux relabeling."""

    __kind__ = 'v1.FlockerVolumeSource'

    __fields__ = {
        'dataset_name': 'datasetName',
    }

    __types__ = {
    }

    __required__ = set([
        'dataset_name',
    ])

    dataset_name = None # string (required)

    def __init__(self, *, dataset_name, **_kwargs_):

        self.dataset_name = dataset_name

        super().__init__(**_kwargs_)

@register_model
class v1_GCEPersistentDiskVolumeSource(Resource):

    """Represents a Persistent Disk resource in Google Compute Engine.  A GCE
    PD must exist before mounting to a container. The disk must also
    be in the same GCE project and zone as the kubelet. A GCE PD can
    only be mounted as read/write once or read-only many times. GCE
    PDs support ownership management and SELinux relabeling."""

    __kind__ = 'v1.GCEPersistentDiskVolumeSource'

    __fields__ = {
        'read_only': 'readOnly',
        'partition': 'partition',
        'fs_type': 'fsType',
        'pd_name': 'pdName',
    }

    __types__ = {
    }

    __required__ = set([
        'pd_name',
    ])

    read_only = None # boolean
    partition = None # integer
    fs_type = None # string
    pd_name = None # string (required)

    def __init__(self, *, pd_name, **_kwargs_):

        self.pd_name = pd_name

        super().__init__(**_kwargs_)

@register_model
class v1_GenericWebHookCause(Resource):

    """GenericWebHookCause holds information about a generic WebHook that
    triggered a build."""

    __kind__ = 'v1.GenericWebHookCause'

    __fields__ = {
        'revision': 'revision',
        'secret': 'secret',
    }

    __types__ = {
        'revision': 'v1.SourceRevision',
    }

    __required__ = set()

    revision = None # v1.SourceRevision
    secret = None # string

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_GitBuildSource(Resource):

    """GitBuildSource defines the parameters of a Git SCM"""

    __kind__ = 'v1.GitBuildSource'

    __fields__ = {
        'uri': 'uri',
        'https_proxy': 'httpsProxy',
        'http_proxy': 'httpProxy',
        'ref': 'ref',
    }

    __types__ = {
    }

    __required__ = set([
        'uri',
    ])

    uri = None # string (required)
    https_proxy = None # string
    http_proxy = None # string
    ref = None # string

    def __init__(self, *, uri, **_kwargs_):

        self.uri = uri

        super().__init__(**_kwargs_)

@register_model
class v1_GitHubWebHookCause(Resource):

    """GitHubWebHookCause has information about a GitHub webhook that
    triggered a build."""

    __kind__ = 'v1.GitHubWebHookCause'

    __fields__ = {
        'revision': 'revision',
        'secret': 'secret',
    }

    __types__ = {
        'revision': 'v1.SourceRevision',
    }

    __required__ = set()

    revision = None # v1.SourceRevision
    secret = None # string

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_GitRepoVolumeSource(Resource):

    """Represents a volume that is populated with the contents of a git
    repository. Git repo volumes do not support ownership management.
    Git repo volumes support SELinux relabeling."""

    __kind__ = 'v1.GitRepoVolumeSource'

    __fields__ = {
        'repository': 'repository',
        'directory': 'directory',
        'revision': 'revision',
    }

    __types__ = {
    }

    __required__ = set([
        'repository',
    ])

    repository = None # string (required)
    directory = None # string
    revision = None # string

    def __init__(self, *, repository, **_kwargs_):

        self.repository = repository

        super().__init__(**_kwargs_)

@register_model
class v1_GitSourceRevision(Resource):

    """GitSourceRevision is the commit information from a git source for a
    build"""

    __kind__ = 'v1.GitSourceRevision'

    __fields__ = {
        'committer': 'committer',
        'message': 'message',
        'commit': 'commit',
        'author': 'author',
    }

    __types__ = {
        'committer': 'v1.SourceControlUser',
        'author': 'v1.SourceControlUser',
    }

    __required__ = set()

    committer = None # v1.SourceControlUser
    message = None # string
    commit = None # string
    author = None # v1.SourceControlUser

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_GlusterfsVolumeSource(Resource):

    """Represents a Glusterfs mount that lasts the lifetime of a pod.
    Glusterfs volumes do not support ownership management or SELinux
    relabeling."""

    __kind__ = 'v1.GlusterfsVolumeSource'

    __fields__ = {
        'path': 'path',
        'endpoints': 'endpoints',
        'read_only': 'readOnly',
    }

    __types__ = {
    }

    __required__ = set([
        'endpoints',
        'path',
    ])

    path = None # string (required)
    endpoints = None # string (required)
    read_only = None # boolean

    def __init__(self, *, endpoints, path, **_kwargs_):

        self.endpoints = endpoints
        self.path = path

        super().__init__(**_kwargs_)

@register_model
class v1_Group(Resource):

    """Group represents a referenceable set of Users"""

    __kind__ = 'v1.Group'

    __fields__ = {
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'users': 'users',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
    }

    __required__ = set([
        'users',
    ])

    metadata = None # v1.ObjectMeta
    api_version = None # string
    users = None # array (required)
    kind = None # string

    def __init__(self, *, users, **_kwargs_):

        self.kind = 'ObjectMeta'

        self.users = users

        super().__init__(**_kwargs_)

@register_model
class v1_GroupList(Resource):

    """GroupList is a collection of Groups"""

    __kind__ = 'v1.GroupList'

    __fields__ = {
        'items': 'items',
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'kind': 'kind',
    }

    __types__ = {
        'items': 'v1.Group',
        'metadata': 'unversioned.ListMeta',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    metadata = None # unversioned.ListMeta
    api_version = None # string
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'ListMeta'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_HTTPGetAction(Resource):

    """HTTPGetAction describes an action based on HTTP Get requests."""

    __kind__ = 'v1.HTTPGetAction'

    __fields__ = {
        'path': 'path',
        'http_headers': 'httpHeaders',
        'scheme': 'scheme',
        'port': 'port',
        'host': 'host',
    }

    __types__ = {
        'http_headers': 'v1.HTTPHeader',
    }

    __required__ = set([
        'port',
    ])

    path = None # string
    http_headers = None # array
    scheme = None # string
    port = None # string (required)
    host = None # string

    def __init__(self, *, port, **_kwargs_):
        self.http_headers = []

        self.port = port

        super().__init__(**_kwargs_)

@register_model
class v1_HTTPHeader(Resource):

    """HTTPHeader describes a custom header to be used in HTTP probes"""

    __kind__ = 'v1.HTTPHeader'

    __fields__ = {
        'name': 'name',
        'value': 'value',
    }

    __types__ = {
    }

    __required__ = set([
        'name',
        'value',
    ])

    name = None # string (required)
    value = None # string (required)

    def __init__(self, *, name, value, **_kwargs_):

        self.name = name
        self.value = value

        super().__init__(**_kwargs_)

@register_model
class v1_Handler(Resource):

    """Handler defines a specific action that should be taken"""

    __kind__ = 'v1.Handler'

    __fields__ = {
        'http_get': 'httpGet',
        'tcp_socket': 'tcpSocket',
        'exec': 'exec',
    }

    __types__ = {
        'http_get': 'v1.HTTPGetAction',
        'exec': 'v1.ExecAction',
        'tcp_socket': 'v1.TCPSocketAction',
    }

    __required__ = set()

    http_get = None # v1.HTTPGetAction
    tcp_socket = None # v1.TCPSocketAction
    exec = None # v1.ExecAction

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_HostPathVolumeSource(Resource):

    """Represents a host path mapped into a pod. Host path volumes do not
    support ownership management or SELinux relabeling."""

    __kind__ = 'v1.HostPathVolumeSource'

    __fields__ = {
        'path': 'path',
    }

    __types__ = {
    }

    __required__ = set([
        'path',
    ])

    path = None # string (required)

    def __init__(self, *, path, **_kwargs_):

        self.path = path

        super().__init__(**_kwargs_)

@register_model
class v1_HostSubnet(Resource):

    """HostSubnet encapsulates the inputs needed to define the container
    subnet network on a node"""

    __kind__ = 'v1.HostSubnet'

    __fields__ = {
        'subnet': 'subnet',
        'api_version': 'apiVersion',
        'host': 'host',
        'metadata': 'metadata',
        'host_ip': 'hostIP',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
    }

    __required__ = set([
        'host',
        'host_ip',
        'subnet',
    ])

    subnet = None # string (required)
    api_version = None # string
    host = None # string (required)
    metadata = None # v1.ObjectMeta
    host_ip = None # string (required)
    kind = None # string

    def __init__(self, *, host, host_ip, subnet, **_kwargs_):

        self.kind = 'ObjectMeta'

        self.host = host
        self.host_ip = host_ip
        self.subnet = subnet

        super().__init__(**_kwargs_)

@register_model
class v1_HostSubnetList(Resource):

    """HostSubnetList is a collection of HostSubnets"""

    __kind__ = 'v1.HostSubnetList'

    __fields__ = {
        'items': 'items',
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'kind': 'kind',
    }

    __types__ = {
        'items': 'v1.HostSubnet',
        'metadata': 'unversioned.ListMeta',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    metadata = None # unversioned.ListMeta
    api_version = None # string
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'ListMeta'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_ISCSIVolumeSource(Resource):

    """Represents an ISCSI disk. ISCSI volumes can only be mounted as
    read/write once. ISCSI volumes support ownership management and
    SELinux relabeling."""

    __kind__ = 'v1.ISCSIVolumeSource'

    __fields__ = {
        'target_portal': 'targetPortal',
        'read_only': 'readOnly',
        'iqn': 'iqn',
        'iscsi_interface': 'iscsiInterface',
        'fs_type': 'fsType',
        'lun': 'lun',
    }

    __types__ = {
    }

    __required__ = set([
        'iqn',
        'lun',
        'target_portal',
    ])

    target_portal = None # string (required)
    read_only = None # boolean
    iqn = None # string (required)
    iscsi_interface = None # string
    fs_type = None # string
    lun = None # integer (required)

    def __init__(self, *, iqn, lun, target_portal, **_kwargs_):

        self.iqn = iqn
        self.lun = lun
        self.target_portal = target_portal

        super().__init__(**_kwargs_)

@register_model
class v1_Identity(Resource):

    """Identity records a successful authentication of a user with an
    identity provider"""

    __kind__ = 'v1.Identity'

    __fields__ = {
        'provider_user_name': 'providerUserName',
        'api_version': 'apiVersion',
        'user': 'user',
        'provider_name': 'providerName',
        'metadata': 'metadata',
        'extra': 'extra',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
        'user': 'v1.ObjectReference',
    }

    __required__ = set([
        'provider_name',
        'provider_user_name',
        'user',
    ])

    provider_user_name = None # string (required)
    api_version = None # string
    user = None # v1.ObjectReference (required)
    provider_name = None # string (required)
    metadata = None # v1.ObjectMeta
    extra = None # object
    kind = None # string

    def __init__(self, *, provider_name, provider_user_name, user, **_kwargs_):

        self.kind = 'ObjectReference'

        self.provider_name = provider_name
        self.provider_user_name = provider_user_name
        self.user = user

        super().__init__(**_kwargs_)

@register_model
class v1_IdentityList(Resource):

    """IdentityList is a collection of Identities"""

    __kind__ = 'v1.IdentityList'

    __fields__ = {
        'items': 'items',
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'kind': 'kind',
    }

    __types__ = {
        'items': 'v1.Identity',
        'metadata': 'unversioned.ListMeta',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    metadata = None # unversioned.ListMeta
    api_version = None # string
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'ListMeta'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_Image(Resource):

    """Image is an immutable representation of a Docker image and metadata at
    a point in time."""

    __kind__ = 'v1.Image'

    __fields__ = {
        'docker_image_reference': 'dockerImageReference',
        'docker_image_config': 'dockerImageConfig',
        'signatures': 'signatures',
        'docker_image_manifest_media_type': 'dockerImageManifestMediaType',
        'metadata': 'metadata',
        'docker_image_metadata_version': 'dockerImageMetadataVersion',
        'api_version': 'apiVersion',
        'docker_image_metadata': 'dockerImageMetadata',
        'docker_image_manifest': 'dockerImageManifest',
        'docker_image_layers': 'dockerImageLayers',
        'docker_image_signatures': 'dockerImageSignatures',
        'kind': 'kind',
    }

    __types__ = {
        'docker_image_layers': 'v1.ImageLayer',
        'metadata': 'v1.ObjectMeta',
        'docker_image_signatures': 'v1.Image.dockerImageSignatures',
        'signatures': 'v1.ImageSignature',
    }

    __required__ = set([
        'docker_image_layers',
    ])

    docker_image_reference = None # string
    docker_image_config = None # string
    signatures = None # array
    docker_image_manifest_media_type = None # string
    metadata = None # v1.ObjectMeta
    docker_image_metadata_version = None # string
    api_version = None # string
    docker_image_metadata = None # string
    docker_image_manifest = None # string
    docker_image_layers = None # array (required)
    docker_image_signatures = None # array
    kind = None # string

    def __init__(self, *, docker_image_layers, **_kwargs_):
        self.signatures = []
        self.docker_image_signatures = []

        self.kind = 'ImageSignature'

        self.docker_image_layers = docker_image_layers

        super().__init__(**_kwargs_)

@register_model
class v1_Image_dockerImageSignatures(Resource):

    __kind__ = 'v1.Image.dockerImageSignatures'

    __fields__ = {
    }

    __types__ = {
    }

    __required__ = set()


    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_ImageChangeCause(Resource):

    """ImageChangeCause contains information about the image that triggered a
    build"""

    __kind__ = 'v1.ImageChangeCause'

    __fields__ = {
        'from_ref': 'fromRef',
        'image_id': 'imageID',
    }

    __types__ = {
        'from_ref': 'v1.ObjectReference',
    }

    __required__ = set()

    from_ref = None # v1.ObjectReference
    image_id = None # string

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_ImageChangeTrigger(Resource):

    """ImageChangeTrigger allows builds to be triggered when an ImageStream
    changes"""

    __kind__ = 'v1.ImageChangeTrigger'

    __fields__ = {
        'last_triggered_image_id': 'lastTriggeredImageID',
        'from_': 'from',
    }

    __types__ = {
        'from_': 'v1.ObjectReference',
    }

    __required__ = set()

    last_triggered_image_id = None # string
    from_ = None # v1.ObjectReference

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_ImageImportSpec(Resource):

    """ImageImportSpec describes a request to import a specific image."""

    __kind__ = 'v1.ImageImportSpec'

    __fields__ = {
        'to': 'to',
        'from_': 'from',
        'import_policy': 'importPolicy',
        'include_manifest': 'includeManifest',
    }

    __types__ = {
        'to': 'v1.LocalObjectReference',
        'from_': 'v1.ObjectReference',
        'import_policy': 'v1.TagImportPolicy',
    }

    __required__ = set([
        'from_',
    ])

    to = None # v1.LocalObjectReference
    from_ = None # v1.ObjectReference (required)
    import_policy = None # v1.TagImportPolicy
    include_manifest = None # boolean

    def __init__(self, *, from_, **_kwargs_):

        self.from_ = from_

        super().__init__(**_kwargs_)

@register_model
class v1_ImageImportStatus(Resource):

    """ImageImportStatus describes the result of an image import."""

    __kind__ = 'v1.ImageImportStatus'

    __fields__ = {
        'tag': 'tag',
        'status': 'status',
        'image': 'image',
    }

    __types__ = {
        'status': 'unversioned.Status',
        'image': 'v1.Image',
    }

    __required__ = set([
        'status',
    ])

    tag = None # string
    status = None # unversioned.Status (required)
    image = None # v1.Image

    def __init__(self, *, status, **_kwargs_):

        self.status = status

        super().__init__(**_kwargs_)

@register_model
class v1_ImageLayer(Resource):

    """ImageLayer represents a single layer of the image. Some images may
    have multiple layers. Some may have none."""

    __kind__ = 'v1.ImageLayer'

    __fields__ = {
        'name': 'name',
        'media_type': 'mediaType',
        'size': 'size',
    }

    __types__ = {
    }

    __required__ = set([
        'media_type',
        'name',
        'size',
    ])

    name = None # string (required)
    media_type = None # string (required)
    size = None # integer (required)

    def __init__(self, *, media_type, name, size, **_kwargs_):

        self.media_type = media_type
        self.name = name
        self.size = size

        super().__init__(**_kwargs_)

@register_model
class v1_ImageList(Resource):

    """ImageList is a list of Image objects."""

    __kind__ = 'v1.ImageList'

    __fields__ = {
        'items': 'items',
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'kind': 'kind',
    }

    __types__ = {
        'items': 'v1.Image',
        'metadata': 'unversioned.ListMeta',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    metadata = None # unversioned.ListMeta
    api_version = None # string
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'ListMeta'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_ImageSignature(Resource):

    """ImageSignature holds a signature of an image. It allows to verify
    image identity and possibly other claims as long as the signature
    is trusted. Based on this information it is possible to restrict
    runnable images to those matching cluster-wide policy. Mandatory
    fields should be parsed by clients doing image verification. The
    others are parsed from signature's content by the server. They
    serve just an informative purpose."""

    __kind__ = 'v1.ImageSignature'

    __fields__ = {
        'image_identity': 'imageIdentity',
        'signed_claims': 'signedClaims',
        'api_version': 'apiVersion',
        'type': 'type',
        'conditions': 'conditions',
        'issued_by': 'issuedBy',
        'content': 'content',
        'metadata': 'metadata',
        'created': 'created',
        'issued_to': 'issuedTo',
        'kind': 'kind',
    }

    __types__ = {
        'conditions': 'v1.SignatureCondition',
        'metadata': 'v1.ObjectMeta',
        'issued_to': 'v1.SignatureSubject',
        'issued_by': 'v1.SignatureIssuer',
    }

    __required__ = set([
        'content',
        'type',
    ])

    image_identity = None # string
    signed_claims = None # object
    api_version = None # string
    type = None # string (required)
    conditions = None # array
    issued_by = None # v1.SignatureIssuer
    content = None # array (required)
    metadata = None # v1.ObjectMeta
    created = None # string
    issued_to = None # v1.SignatureSubject
    kind = None # string

    def __init__(self, *, content, type, **_kwargs_):
        self.conditions = []

        self.kind = 'SignatureIssuer'

        self.content = content
        self.type = type

        super().__init__(**_kwargs_)

@register_model
class v1_ImageSource(Resource):

    """ImageSource describes an image that is used as source for the build"""

    __kind__ = 'v1.ImageSource'

    __fields__ = {
        'paths': 'paths',
        'from_': 'from',
        'pull_secret': 'pullSecret',
    }

    __types__ = {
        'paths': 'v1.ImageSourcePath',
        'from_': 'v1.ObjectReference',
        'pull_secret': 'v1.LocalObjectReference',
    }

    __required__ = set([
        'from_',
        'paths',
    ])

    paths = None # array (required)
    from_ = None # v1.ObjectReference (required)
    pull_secret = None # v1.LocalObjectReference

    def __init__(self, *, from_, paths, **_kwargs_):

        self.from_ = from_
        self.paths = paths

        super().__init__(**_kwargs_)

@register_model
class v1_ImageSourcePath(Resource):

    """ImageSourcePath describes a path to be copied from a source image and
    its destination within the build directory."""

    __kind__ = 'v1.ImageSourcePath'

    __fields__ = {
        'source_path': 'sourcePath',
        'destination_dir': 'destinationDir',
    }

    __types__ = {
    }

    __required__ = set([
        'destination_dir',
        'source_path',
    ])

    source_path = None # string (required)
    destination_dir = None # string (required)

    def __init__(self, *, destination_dir, source_path, **_kwargs_):

        self.destination_dir = destination_dir
        self.source_path = source_path

        super().__init__(**_kwargs_)

@register_model
class v1_ImageStream(Resource):

    """ImageStream stores a mapping of tags to images, metadata overrides
    that are applied when images are tagged in a stream, and an
    optional reference to a Docker image repository on a registry."""

    __kind__ = 'v1.ImageStream'

    __fields__ = {
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'spec': 'spec',
        'status': 'status',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
        'spec': 'v1.ImageStreamSpec',
        'status': 'v1.ImageStreamStatus',
    }

    __required__ = set([
        'spec',
    ])

    metadata = None # v1.ObjectMeta
    api_version = None # string
    spec = None # v1.ImageStreamSpec (required)
    status = None # v1.ImageStreamStatus
    kind = None # string

    def __init__(self, *, spec, **_kwargs_):

        self.kind = 'ImageStreamStatus'

        self.spec = spec

        super().__init__(**_kwargs_)

@register_model
class v1_ImageStreamImage(Resource):

    """ImageStreamImage represents an Image that is retrieved by image name
    from an ImageStream."""

    __kind__ = 'v1.ImageStreamImage'

    __fields__ = {
        'image': 'image',
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
        'image': 'v1.Image',
    }

    __required__ = set([
        'image',
    ])

    image = None # v1.Image (required)
    metadata = None # v1.ObjectMeta
    api_version = None # string
    kind = None # string

    def __init__(self, *, image, **_kwargs_):

        self.kind = 'Image'

        self.image = image

        super().__init__(**_kwargs_)

@register_model
class v1_ImageStreamImport(Resource):

    """ImageStreamImport imports an image from remote repositories into
    OpenShift."""

    __kind__ = 'v1.ImageStreamImport'

    __fields__ = {
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'spec': 'spec',
        'status': 'status',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
        'spec': 'v1.ImageStreamImportSpec',
        'status': 'v1.ImageStreamImportStatus',
    }

    __required__ = set([
        'spec',
        'status',
    ])

    metadata = None # v1.ObjectMeta
    api_version = None # string
    spec = None # v1.ImageStreamImportSpec (required)
    status = None # v1.ImageStreamImportStatus (required)
    kind = None # string

    def __init__(self, *, spec, status, **_kwargs_):

        self.kind = 'ImageStreamImportStatus'

        self.spec = spec
        self.status = status

        super().__init__(**_kwargs_)

@register_model
class v1_ImageStreamImportSpec(Resource):

    """ImageStreamImportSpec defines what images should be imported."""

    __kind__ = 'v1.ImageStreamImportSpec'

    __fields__ = {
        'repository': 'repository',
        'import_': 'import',
        'images': 'images',
    }

    __types__ = {
        'repository': 'v1.RepositoryImportSpec',
        'images': 'v1.ImageImportSpec',
    }

    __required__ = set([
        'import_',
    ])

    repository = None # v1.RepositoryImportSpec
    import_ = None # boolean (required)
    images = None # array

    def __init__(self, *, import_, **_kwargs_):
        self.images = []

        self.import_ = import_

        super().__init__(**_kwargs_)

@register_model
class v1_ImageStreamImportStatus(Resource):

    """ImageStreamImportStatus contains information about the status of an
    image stream import."""

    __kind__ = 'v1.ImageStreamImportStatus'

    __fields__ = {
        'repository': 'repository',
        'import_': 'import',
        'images': 'images',
    }

    __types__ = {
        'repository': 'v1.RepositoryImportStatus',
        'import_': 'v1.ImageStream',
        'images': 'v1.ImageImportStatus',
    }

    __required__ = set()

    repository = None # v1.RepositoryImportStatus
    import_ = None # v1.ImageStream
    images = None # array

    def __init__(self, **_kwargs_):
        self.images = []

        super().__init__(**_kwargs_)

@register_model
class v1_ImageStreamList(Resource):

    """ImageStreamList is a list of ImageStream objects."""

    __kind__ = 'v1.ImageStreamList'

    __fields__ = {
        'items': 'items',
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'kind': 'kind',
    }

    __types__ = {
        'items': 'v1.ImageStream',
        'metadata': 'unversioned.ListMeta',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    metadata = None # unversioned.ListMeta
    api_version = None # string
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'ListMeta'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_ImageStreamMapping(Resource):

    """ImageStreamMapping represents a mapping from a single tag to a Docker
    image as well as the reference to the Docker image stream the
    image came from."""

    __kind__ = 'v1.ImageStreamMapping'

    __fields__ = {
        'image': 'image',
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'tag': 'tag',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
        'image': 'v1.Image',
    }

    __required__ = set([
        'image',
        'tag',
    ])

    image = None # v1.Image (required)
    metadata = None # v1.ObjectMeta
    api_version = None # string
    tag = None # string (required)
    kind = None # string

    def __init__(self, *, image, tag, **_kwargs_):

        self.kind = 'Image'

        self.image = image
        self.tag = tag

        super().__init__(**_kwargs_)

@register_model
class v1_ImageStreamSpec(Resource):

    """ImageStreamSpec represents options for ImageStreams."""

    __kind__ = 'v1.ImageStreamSpec'

    __fields__ = {
        'tags': 'tags',
        'docker_image_repository': 'dockerImageRepository',
    }

    __types__ = {
        'tags': 'v1.TagReference',
    }

    __required__ = set()

    tags = None # array
    docker_image_repository = None # string

    def __init__(self, **_kwargs_):
        self.tags = []

        super().__init__(**_kwargs_)

@register_model
class v1_ImageStreamStatus(Resource):

    """ImageStreamStatus contains information about the state of this image
    stream."""

    __kind__ = 'v1.ImageStreamStatus'

    __fields__ = {
        'tags': 'tags',
        'docker_image_repository': 'dockerImageRepository',
    }

    __types__ = {
        'tags': 'v1.NamedTagEventList',
    }

    __required__ = set([
        'docker_image_repository',
    ])

    tags = None # array
    docker_image_repository = None # string (required)

    def __init__(self, *, docker_image_repository, **_kwargs_):
        self.tags = []

        self.docker_image_repository = docker_image_repository

        super().__init__(**_kwargs_)

@register_model
class v1_ImageStreamTag(Resource):

    """ImageStreamTag represents an Image that is retrieved by tag name from
    an ImageStream."""

    __kind__ = 'v1.ImageStreamTag'

    __fields__ = {
        'generation': 'generation',
        'tag': 'tag',
        'api_version': 'apiVersion',
        'conditions': 'conditions',
        'metadata': 'metadata',
        'image': 'image',
        'kind': 'kind',
    }

    __types__ = {
        'conditions': 'v1.TagEventCondition',
        'tag': 'v1.TagReference',
        'metadata': 'v1.ObjectMeta',
        'image': 'v1.Image',
    }

    __required__ = set([
        'generation',
        'image',
        'tag',
    ])

    generation = None # integer (required)
    tag = None # v1.TagReference (required)
    api_version = None # string
    conditions = None # array
    metadata = None # v1.ObjectMeta
    image = None # v1.Image (required)
    kind = None # string

    def __init__(self, *, generation, image, tag, **_kwargs_):
        self.conditions = []

        self.kind = 'Image'

        self.generation = generation
        self.image = image
        self.tag = tag

        super().__init__(**_kwargs_)

@register_model
class v1_ImageStreamTagList(Resource):

    """ImageStreamTagList is a list of ImageStreamTag objects."""

    __kind__ = 'v1.ImageStreamTagList'

    __fields__ = {
        'items': 'items',
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'kind': 'kind',
    }

    __types__ = {
        'items': 'v1.ImageStreamTag',
        'metadata': 'unversioned.ListMeta',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    metadata = None # unversioned.ListMeta
    api_version = None # string
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'ListMeta'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_JenkinsPipelineBuildStrategy(Resource):

    """JenkinsPipelineBuildStrategy holds parameters specific to a Jenkins
    Pipeline build. This strategy is experimental."""

    __kind__ = 'v1.JenkinsPipelineBuildStrategy'

    __fields__ = {
        'jenkinsfile': 'jenkinsfile',
        'jenkinsfile_path': 'jenkinsfilePath',
    }

    __types__ = {
    }

    __required__ = set()

    jenkinsfile = None # string
    jenkinsfile_path = None # string

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_KeyToPath(Resource):

    """Maps a string key to a path within a volume."""

    __kind__ = 'v1.KeyToPath'

    __fields__ = {
        'path': 'path',
        'key': 'key',
    }

    __types__ = {
    }

    __required__ = set([
        'key',
        'path',
    ])

    path = None # string (required)
    key = None # string (required)

    def __init__(self, *, key, path, **_kwargs_):

        self.key = key
        self.path = path

        super().__init__(**_kwargs_)

@register_model
class v1_Lifecycle(Resource):

    """Lifecycle describes actions that the management system should take in
    response to container lifecycle events. For the PostStart and
    PreStop lifecycle handlers, management of the container blocks
    until the action is complete, unless the container process fails,
    in which case the handler is aborted."""

    __kind__ = 'v1.Lifecycle'

    __fields__ = {
        'pre_stop': 'preStop',
        'post_start': 'postStart',
    }

    __types__ = {
        'pre_stop': 'v1.Handler',
        'post_start': 'v1.Handler',
    }

    __required__ = set()

    pre_stop = None # v1.Handler
    post_start = None # v1.Handler

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_LifecycleHook(Resource):

    """LifecycleHook defines a specific deployment lifecycle action. Only one
    type of action may be specified at any time."""

    __kind__ = 'v1.LifecycleHook'

    __fields__ = {
        'tag_images': 'tagImages',
        'failure_policy': 'failurePolicy',
        'exec_new_pod': 'execNewPod',
    }

    __types__ = {
        'tag_images': 'v1.TagImageHook',
        'exec_new_pod': 'v1.ExecNewPodHook',
    }

    __required__ = set([
        'failure_policy',
    ])

    tag_images = None # array
    failure_policy = None # string (required)
    exec_new_pod = None # v1.ExecNewPodHook

    def __init__(self, *, failure_policy, **_kwargs_):
        self.tag_images = []

        self.failure_policy = failure_policy

        super().__init__(**_kwargs_)

@register_model
class v1_LocalObjectReference(Resource):

    """LocalObjectReference contains enough information to let you locate the
    referenced object inside the same namespace."""

    __kind__ = 'v1.LocalObjectReference'

    __fields__ = {
        'name': 'name',
    }

    __types__ = {
    }

    __required__ = set()

    name = None # string

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_LocalResourceAccessReview(Resource):

    """LocalResourceAccessReview is a means to request a list of which users
    and groups are authorized to perform the action specified by spec
    in a particular namespace"""

    __kind__ = 'v1.LocalResourceAccessReview'

    __fields__ = {
        'resource_name': 'resourceName',
        'resource': 'resource',
        'verb': 'verb',
        'api_version': 'apiVersion',
        'resource_api_version': 'resourceAPIVersion',
        'content': 'content',
        'resource_api_group': 'resourceAPIGroup',
        'namespace': 'namespace',
        'kind': 'kind',
    }

    __types__ = {
    }

    __required__ = set([
        'namespace',
        'resource',
        'resource_api_group',
        'resource_api_version',
        'resource_name',
        'verb',
    ])

    resource_name = None # string (required)
    resource = None # string (required)
    verb = None # string (required)
    api_version = None # string
    resource_api_version = None # string (required)
    content = None # string
    resource_api_group = None # string (required)
    namespace = None # string (required)
    kind = None # string

    def __init__(self, *, namespace, resource, resource_api_group, resource_api_version, resource_name, verb, **_kwargs_):

        self.kind = 'LocalResourceAccessReview'

        self.namespace = namespace
        self.resource = resource
        self.resource_api_group = resource_api_group
        self.resource_api_version = resource_api_version
        self.resource_name = resource_name
        self.verb = verb

        super().__init__(**_kwargs_)

@register_model
class v1_LocalSubjectAccessReview(Resource):

    """LocalSubjectAccessReview is an object for requesting information about
    whether a user or group can perform an action in a particular
    namespace"""

    __kind__ = 'v1.LocalSubjectAccessReview'

    __fields__ = {
        'resource': 'resource',
        'resource_api_version': 'resourceAPIVersion',
        'scopes': 'scopes',
        'content': 'content',
        'resource_api_group': 'resourceAPIGroup',
        'resource_name': 'resourceName',
        'verb': 'verb',
        'api_version': 'apiVersion',
        'user': 'user',
        'kind': 'kind',
        'namespace': 'namespace',
        'groups': 'groups',
    }

    __types__ = {
    }

    __required__ = set([
        'groups',
        'namespace',
        'resource',
        'resource_api_group',
        'resource_api_version',
        'resource_name',
        'scopes',
        'user',
        'verb',
    ])

    resource = None # string (required)
    resource_api_version = None # string (required)
    scopes = None # array (required)
    content = None # string
    resource_api_group = None # string (required)
    resource_name = None # string (required)
    verb = None # string (required)
    api_version = None # string
    user = None # string (required)
    kind = None # string
    namespace = None # string (required)
    groups = None # array (required)

    def __init__(self, *, groups, namespace, resource, resource_api_group, resource_api_version, resource_name, scopes, user, verb, **_kwargs_):

        self.kind = 'LocalSubjectAccessReview'

        self.groups = groups
        self.namespace = namespace
        self.resource = resource
        self.resource_api_group = resource_api_group
        self.resource_api_version = resource_api_version
        self.resource_name = resource_name
        self.scopes = scopes
        self.user = user
        self.verb = verb

        super().__init__(**_kwargs_)

@register_model
class v1_NFSVolumeSource(Resource):

    """Represents an NFS mount that lasts the lifetime of a pod. NFS volumes
    do not support ownership management or SELinux relabeling."""

    __kind__ = 'v1.NFSVolumeSource'

    __fields__ = {
        'path': 'path',
        'read_only': 'readOnly',
        'server': 'server',
    }

    __types__ = {
    }

    __required__ = set([
        'path',
        'server',
    ])

    path = None # string (required)
    read_only = None # boolean
    server = None # string (required)

    def __init__(self, *, path, server, **_kwargs_):

        self.path = path
        self.server = server

        super().__init__(**_kwargs_)

@register_model
class v1_NamedClusterRole(Resource):

    """NamedClusterRole relates a name with a cluster role"""

    __kind__ = 'v1.NamedClusterRole'

    __fields__ = {
        'name': 'name',
        'role': 'role',
    }

    __types__ = {
        'role': 'v1.ClusterRole',
    }

    __required__ = set([
        'name',
        'role',
    ])

    name = None # string (required)
    role = None # v1.ClusterRole (required)

    def __init__(self, *, name, role, **_kwargs_):

        self.name = name
        self.role = role

        super().__init__(**_kwargs_)

@register_model
class v1_NamedClusterRoleBinding(Resource):

    """NamedClusterRoleBinding relates a name with a cluster role binding"""

    __kind__ = 'v1.NamedClusterRoleBinding'

    __fields__ = {
        'name': 'name',
        'role_binding': 'roleBinding',
    }

    __types__ = {
        'role_binding': 'v1.ClusterRoleBinding',
    }

    __required__ = set([
        'name',
        'role_binding',
    ])

    name = None # string (required)
    role_binding = None # v1.ClusterRoleBinding (required)

    def __init__(self, *, name, role_binding, **_kwargs_):

        self.name = name
        self.role_binding = role_binding

        super().__init__(**_kwargs_)

@register_model
class v1_NamedRole(Resource):

    """NamedRole relates a Role with a name"""

    __kind__ = 'v1.NamedRole'

    __fields__ = {
        'name': 'name',
        'role': 'role',
    }

    __types__ = {
        'role': 'v1.Role',
    }

    __required__ = set([
        'name',
        'role',
    ])

    name = None # string (required)
    role = None # v1.Role (required)

    def __init__(self, *, name, role, **_kwargs_):

        self.name = name
        self.role = role

        super().__init__(**_kwargs_)

@register_model
class v1_NamedRoleBinding(Resource):

    """NamedRoleBinding relates a role binding with a name"""

    __kind__ = 'v1.NamedRoleBinding'

    __fields__ = {
        'name': 'name',
        'role_binding': 'roleBinding',
    }

    __types__ = {
        'role_binding': 'v1.RoleBinding',
    }

    __required__ = set([
        'name',
        'role_binding',
    ])

    name = None # string (required)
    role_binding = None # v1.RoleBinding (required)

    def __init__(self, *, name, role_binding, **_kwargs_):

        self.name = name
        self.role_binding = role_binding

        super().__init__(**_kwargs_)

@register_model
class v1_NamedTagEventList(Resource):

    """NamedTagEventList relates a tag to its image history."""

    __kind__ = 'v1.NamedTagEventList'

    __fields__ = {
        'items': 'items',
        'conditions': 'conditions',
        'tag': 'tag',
    }

    __types__ = {
        'items': 'v1.TagEvent',
        'conditions': 'v1.TagEventCondition',
    }

    __required__ = set([
        'items',
        'tag',
    ])

    items = None # array (required)
    conditions = None # array
    tag = None # string (required)

    def __init__(self, *, items, tag, **_kwargs_):
        self.conditions = []

        self.items = items
        self.tag = tag

        super().__init__(**_kwargs_)

@register_model
class v1_NetNamespace(Resource):

    """NetNamespace encapsulates the inputs needed to define a unique network
    namespace on the cluster"""

    __kind__ = 'v1.NetNamespace'

    __fields__ = {
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'netname': 'netname',
        'netid': 'netid',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
    }

    __required__ = set([
        'netid',
        'netname',
    ])

    metadata = None # v1.ObjectMeta
    api_version = None # string
    netname = None # string (required)
    netid = None # integer (required)
    kind = None # string

    def __init__(self, *, netid, netname, **_kwargs_):

        self.kind = 'ObjectMeta'

        self.netid = netid
        self.netname = netname

        super().__init__(**_kwargs_)

@register_model
class v1_NetNamespaceList(Resource):

    """NetNamespaceList is a collection of NetNamespaces"""

    __kind__ = 'v1.NetNamespaceList'

    __fields__ = {
        'items': 'items',
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'kind': 'kind',
    }

    __types__ = {
        'items': 'v1.NetNamespace',
        'metadata': 'unversioned.ListMeta',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    metadata = None # unversioned.ListMeta
    api_version = None # string
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'ListMeta'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_OAuthAccessToken(Resource):

    """OAuthAccessToken describes an OAuth access token"""

    __kind__ = 'v1.OAuthAccessToken'

    __fields__ = {
        'expires_in': 'expiresIn',
        'api_version': 'apiVersion',
        'scopes': 'scopes',
        'user_uid': 'userUID',
        'refresh_token': 'refreshToken',
        'metadata': 'metadata',
        'client_name': 'clientName',
        'redirect_uri': 'redirectURI',
        'user_name': 'userName',
        'authorize_token': 'authorizeToken',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
    }

    __required__ = set()

    expires_in = None # integer
    api_version = None # string
    scopes = None # array
    user_uid = None # string
    refresh_token = None # string
    metadata = None # v1.ObjectMeta
    client_name = None # string
    redirect_uri = None # string
    user_name = None # string
    authorize_token = None # string
    kind = None # string

    def __init__(self, **_kwargs_):
        self.scopes = []

        self.kind = 'ObjectMeta'

        super().__init__(**_kwargs_)

@register_model
class v1_OAuthAccessTokenList(Resource):

    """OAuthAccessTokenList is a collection of OAuth access tokens"""

    __kind__ = 'v1.OAuthAccessTokenList'

    __fields__ = {
        'items': 'items',
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'kind': 'kind',
    }

    __types__ = {
        'items': 'v1.OAuthAccessToken',
        'metadata': 'unversioned.ListMeta',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    metadata = None # unversioned.ListMeta
    api_version = None # string
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'ListMeta'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_OAuthAuthorizeToken(Resource):

    """OAuthAuthorizeToken describes an OAuth authorization token"""

    __kind__ = 'v1.OAuthAuthorizeToken'

    __fields__ = {
        'state': 'state',
        'expires_in': 'expiresIn',
        'api_version': 'apiVersion',
        'scopes': 'scopes',
        'user_uid': 'userUID',
        'metadata': 'metadata',
        'client_name': 'clientName',
        'redirect_uri': 'redirectURI',
        'user_name': 'userName',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
    }

    __required__ = set()

    state = None # string
    expires_in = None # integer
    api_version = None # string
    scopes = None # array
    user_uid = None # string
    metadata = None # v1.ObjectMeta
    client_name = None # string
    redirect_uri = None # string
    user_name = None # string
    kind = None # string

    def __init__(self, **_kwargs_):
        self.scopes = []

        self.kind = 'ObjectMeta'

        super().__init__(**_kwargs_)

@register_model
class v1_OAuthAuthorizeTokenList(Resource):

    """OAuthAuthorizeTokenList is a collection of OAuth authorization tokens"""

    __kind__ = 'v1.OAuthAuthorizeTokenList'

    __fields__ = {
        'items': 'items',
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'kind': 'kind',
    }

    __types__ = {
        'items': 'v1.OAuthAuthorizeToken',
        'metadata': 'unversioned.ListMeta',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    metadata = None # unversioned.ListMeta
    api_version = None # string
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'ListMeta'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_OAuthClient(Resource):

    """OAuthClient describes an OAuth client"""

    __kind__ = 'v1.OAuthClient'

    __fields__ = {
        'redirect_ur_is': 'redirectURIs',
        'api_version': 'apiVersion',
        'scope_restrictions': 'scopeRestrictions',
        'grant_method': 'grantMethod',
        'additional_secrets': 'additionalSecrets',
        'kind': 'kind',
        'respond_with_challenges': 'respondWithChallenges',
        'metadata': 'metadata',
        'secret': 'secret',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
        'scope_restrictions': 'v1.ScopeRestriction',
    }

    __required__ = set()

    redirect_ur_is = None # array
    api_version = None # string
    scope_restrictions = None # array
    grant_method = None # string
    additional_secrets = None # array
    kind = None # string
    respond_with_challenges = None # boolean
    metadata = None # v1.ObjectMeta
    secret = None # string

    def __init__(self, **_kwargs_):
        self.redirect_ur_is = []
        self.scope_restrictions = []
        self.additional_secrets = []

        self.kind = 'ScopeRestriction'

        super().__init__(**_kwargs_)

@register_model
class v1_OAuthClientAuthorization(Resource):

    """OAuthClientAuthorization describes an authorization created by an
    OAuth client"""

    __kind__ = 'v1.OAuthClientAuthorization'

    __fields__ = {
        'api_version': 'apiVersion',
        'scopes': 'scopes',
        'user_uid': 'userUID',
        'metadata': 'metadata',
        'client_name': 'clientName',
        'user_name': 'userName',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
    }

    __required__ = set()

    api_version = None # string
    scopes = None # array
    user_uid = None # string
    metadata = None # v1.ObjectMeta
    client_name = None # string
    user_name = None # string
    kind = None # string

    def __init__(self, **_kwargs_):
        self.scopes = []

        self.kind = 'ObjectMeta'

        super().__init__(**_kwargs_)

@register_model
class v1_OAuthClientAuthorizationList(Resource):

    """OAuthClientAuthorizationList is a collection of OAuth client
    authorizations"""

    __kind__ = 'v1.OAuthClientAuthorizationList'

    __fields__ = {
        'items': 'items',
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'kind': 'kind',
    }

    __types__ = {
        'items': 'v1.OAuthClientAuthorization',
        'metadata': 'unversioned.ListMeta',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    metadata = None # unversioned.ListMeta
    api_version = None # string
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'ListMeta'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_OAuthClientList(Resource):

    """OAuthClientList is a collection of OAuth clients"""

    __kind__ = 'v1.OAuthClientList'

    __fields__ = {
        'items': 'items',
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'kind': 'kind',
    }

    __types__ = {
        'items': 'v1.OAuthClient',
        'metadata': 'unversioned.ListMeta',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    metadata = None # unversioned.ListMeta
    api_version = None # string
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'ListMeta'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_ObjectFieldSelector(Resource):

    """ObjectFieldSelector selects an APIVersioned field of an object."""

    __kind__ = 'v1.ObjectFieldSelector'

    __fields__ = {
        'field_path': 'fieldPath',
        'api_version': 'apiVersion',
    }

    __types__ = {
    }

    __required__ = set([
        'field_path',
    ])

    field_path = None # string (required)
    api_version = None # string

    def __init__(self, *, field_path, **_kwargs_):

        self.field_path = field_path

        super().__init__(**_kwargs_)

@register_model
class v1_ObjectMeta(Resource):

    """ObjectMeta is metadata that all persisted resources must have, which
    includes all objects users must create."""

    __kind__ = 'v1.ObjectMeta'

    __fields__ = {
        'name': 'name',
        'finalizers': 'finalizers',
        'self_link': 'selfLink',
        'uid': 'uid',
        'generate_name': 'generateName',
        'annotations': 'annotations',
        'namespace': 'namespace',
        'generation': 'generation',
        'deletion_timestamp': 'deletionTimestamp',
        'creation_timestamp': 'creationTimestamp',
        'owner_references': 'ownerReferences',
        'labels': 'labels',
        'deletion_grace_period_seconds': 'deletionGracePeriodSeconds',
        'resource_version': 'resourceVersion',
    }

    __types__ = {
        'owner_references': 'v1.OwnerReference',
    }

    __required__ = set()

    name = None # string
    finalizers = None # array
    self_link = None # string
    uid = None # string
    generate_name = None # string
    annotations = None # object
    namespace = None # string
    generation = None # integer
    deletion_timestamp = None # string
    creation_timestamp = None # string
    owner_references = None # array
    labels = None # object
    deletion_grace_period_seconds = None # integer
    resource_version = None # string

    def __init__(self, **_kwargs_):
        self.finalizers = []
        self.owner_references = []

        super().__init__(**_kwargs_)

@register_model
class v1_ObjectReference(Resource):

    """ObjectReference contains enough information to let you inspect or
    modify the referred object."""

    __kind__ = 'v1.ObjectReference'

    __fields__ = {
        'name': 'name',
        'field_path': 'fieldPath',
        'api_version': 'apiVersion',
        'uid': 'uid',
        'resource_version': 'resourceVersion',
        'namespace': 'namespace',
        'kind': 'kind',
    }

    __types__ = {
    }

    __required__ = set()

    name = None # string
    field_path = None # string
    api_version = None # string
    uid = None # string
    resource_version = None # string
    namespace = None # string
    kind = None # string

    def __init__(self, **_kwargs_):

        self.kind = 'ObjectReference'

        super().__init__(**_kwargs_)

@register_model
class v1_OwnerReference(Resource):

    """OwnerReference contains enough information to let you identify an
    owning object. Currently, an owning object must be in the same
    namespace, so there is no namespace field."""

    __kind__ = 'v1.OwnerReference'

    __fields__ = {
        'name': 'name',
        'api_version': 'apiVersion',
        'uid': 'uid',
        'controller': 'controller',
        'kind': 'kind',
    }

    __types__ = {
    }

    __required__ = set([
        'api_version',
        'kind',
        'name',
        'uid',
    ])

    name = None # string (required)
    api_version = None # string (required)
    uid = None # string (required)
    controller = None # boolean
    kind = None # string (required)

    def __init__(self, *, api_version, kind, name, uid, **_kwargs_):

        self.kind = 'OwnerReference'

        self.api_version = api_version
        self.kind = kind
        self.name = name
        self.uid = uid

        super().__init__(**_kwargs_)

@register_model
class v1_Parameter(Resource):

    """Parameter defines a name/value variable that is to be processed during
    the Template to Config transformation."""

    __kind__ = 'v1.Parameter'

    __fields__ = {
        'name': 'name',
        'description': 'description',
        'from_': 'from',
        'generate': 'generate',
        'value': 'value',
        'display_name': 'displayName',
        'required': 'required',
    }

    __types__ = {
    }

    __required__ = set([
        'name',
    ])

    name = None # string (required)
    description = None # string
    from_ = None # string
    generate = None # string
    value = None # string
    display_name = None # string
    required = None # boolean

    def __init__(self, *, name, **_kwargs_):

        self.name = name

        super().__init__(**_kwargs_)

@register_model
class v1_PersistentVolumeClaimVolumeSource(Resource):

    """PersistentVolumeClaimVolumeSource references the user's PVC in the
    same namespace. This volume finds the bound PV and mounts that
    volume for the pod. A PersistentVolumeClaimVolumeSource is,
    essentially, a wrapper around another type of volume that is owned
    by someone else (the system)."""

    __kind__ = 'v1.PersistentVolumeClaimVolumeSource'

    __fields__ = {
        'claim_name': 'claimName',
        'read_only': 'readOnly',
    }

    __types__ = {
    }

    __required__ = set([
        'claim_name',
    ])

    claim_name = None # string (required)
    read_only = None # boolean

    def __init__(self, *, claim_name, **_kwargs_):

        self.claim_name = claim_name

        super().__init__(**_kwargs_)

@register_model
class v1_PodSecurityContext(Resource):

    """PodSecurityContext holds pod-level security attributes and common
    container settings. Some fields are also present in
    container.securityContext.  Field values of
    container.securityContext take precedence over field values of
    PodSecurityContext."""

    __kind__ = 'v1.PodSecurityContext'

    __fields__ = {
        'run_as_user': 'runAsUser',
        'se_linux_options': 'seLinuxOptions',
        'fs_group': 'fsGroup',
        'run_as_non_root': 'runAsNonRoot',
        'supplemental_groups': 'supplementalGroups',
    }

    __types__ = {
        'se_linux_options': 'v1.SELinuxOptions',
    }

    __required__ = set()

    run_as_user = None # integer
    se_linux_options = None # v1.SELinuxOptions
    fs_group = None # integer
    run_as_non_root = None # boolean
    supplemental_groups = None # array

    def __init__(self, **_kwargs_):
        self.supplemental_groups = []

        super().__init__(**_kwargs_)

@register_model
class v1_PodSpec(Resource):

    """PodSpec is a description of a pod."""

    __kind__ = 'v1.PodSpec'

    __fields__ = {
        'service_account': 'serviceAccount',
        'active_deadline_seconds': 'activeDeadlineSeconds',
        'node_name': 'nodeName',
        'subdomain': 'subdomain',
        'host_pid': 'hostPID',
        'containers': 'containers',
        'image_pull_secrets': 'imagePullSecrets',
        'node_selector': 'nodeSelector',
        'dns_policy': 'dnsPolicy',
        'service_account_name': 'serviceAccountName',
        'security_context': 'securityContext',
        'host_ipc': 'hostIPC',
        'host': 'host',
        'host_network': 'hostNetwork',
        'restart_policy': 'restartPolicy',
        'termination_grace_period_seconds': 'terminationGracePeriodSeconds',
        'hostname': 'hostname',
        'volumes': 'volumes',
    }

    __types__ = {
        'image_pull_secrets': 'v1.LocalObjectReference',
        'volumes': 'v1.Volume',
        'security_context': 'v1.PodSecurityContext',
        'containers': 'v1.Container',
    }

    __required__ = set([
        'containers',
    ])

    service_account = None # string
    active_deadline_seconds = None # integer
    node_name = None # string
    subdomain = None # string
    host_pid = None # boolean
    containers = None # array (required)
    image_pull_secrets = None # array
    node_selector = None # object
    dns_policy = None # string
    service_account_name = None # string
    security_context = None # v1.PodSecurityContext
    host_ipc = None # boolean
    host = None # string
    host_network = None # boolean
    restart_policy = None # string
    termination_grace_period_seconds = None # integer
    hostname = None # string
    volumes = None # array

    def __init__(self, *, containers, **_kwargs_):
        self.image_pull_secrets = []
        self.volumes = []

        self.containers = containers

        super().__init__(**_kwargs_)

@register_model
class v1_PodTemplateSpec(Resource):

    """PodTemplateSpec describes the data a pod should have when created from
    a template"""

    __kind__ = 'v1.PodTemplateSpec'

    __fields__ = {
        'metadata': 'metadata',
        'spec': 'spec',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
        'spec': 'v1.PodSpec',
    }

    __required__ = set()

    metadata = None # v1.ObjectMeta
    spec = None # v1.PodSpec

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_Policy(Resource):

    """Policy is a object that holds all the Roles for a particular
    namespace.  There is at most one Policy document per namespace."""

    __kind__ = 'v1.Policy'

    __fields__ = {
        'roles': 'roles',
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'last_modified': 'lastModified',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
        'roles': 'v1.NamedRole',
    }

    __required__ = set([
        'last_modified',
        'roles',
    ])

    roles = None # array (required)
    metadata = None # v1.ObjectMeta
    api_version = None # string
    last_modified = None # string (required)
    kind = None # string

    def __init__(self, *, last_modified, roles, **_kwargs_):

        self.kind = 'NamedRole'

        self.last_modified = last_modified
        self.roles = roles

        super().__init__(**_kwargs_)

@register_model
class v1_PolicyBinding(Resource):

    """PolicyBinding is a object that holds all the RoleBindings for a
    particular namespace.  There is one PolicyBinding document per
    referenced Policy namespace"""

    __kind__ = 'v1.PolicyBinding'

    __fields__ = {
        'api_version': 'apiVersion',
        'last_modified': 'lastModified',
        'metadata': 'metadata',
        'role_bindings': 'roleBindings',
        'policy_ref': 'policyRef',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
        'policy_ref': 'v1.ObjectReference',
        'role_bindings': 'v1.NamedRoleBinding',
    }

    __required__ = set([
        'last_modified',
        'policy_ref',
        'role_bindings',
    ])

    api_version = None # string
    last_modified = None # string (required)
    metadata = None # v1.ObjectMeta
    role_bindings = None # array (required)
    policy_ref = None # v1.ObjectReference (required)
    kind = None # string

    def __init__(self, *, last_modified, policy_ref, role_bindings, **_kwargs_):

        self.kind = 'NamedRoleBinding'

        self.last_modified = last_modified
        self.policy_ref = policy_ref
        self.role_bindings = role_bindings

        super().__init__(**_kwargs_)

@register_model
class v1_PolicyBindingList(Resource):

    """PolicyBindingList is a collection of PolicyBindings"""

    __kind__ = 'v1.PolicyBindingList'

    __fields__ = {
        'items': 'items',
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'kind': 'kind',
    }

    __types__ = {
        'items': 'v1.PolicyBinding',
        'metadata': 'unversioned.ListMeta',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    metadata = None # unversioned.ListMeta
    api_version = None # string
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'ListMeta'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_PolicyList(Resource):

    """PolicyList is a collection of Policies"""

    __kind__ = 'v1.PolicyList'

    __fields__ = {
        'items': 'items',
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'kind': 'kind',
    }

    __types__ = {
        'items': 'v1.Policy',
        'metadata': 'unversioned.ListMeta',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    metadata = None # unversioned.ListMeta
    api_version = None # string
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'ListMeta'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_PolicyRule(Resource):

    """PolicyRule holds information that describes a policy rule, but does
    not contain information about who the rule applies to or which
    namespace the rule applies to."""

    __kind__ = 'v1.PolicyRule'

    __fields__ = {
        'resource_names': 'resourceNames',
        'attribute_restrictions': 'attributeRestrictions',
        'resources': 'resources',
        'verbs': 'verbs',
        'api_groups': 'apiGroups',
        'non_resource_ur_ls': 'nonResourceURLs',
    }

    __types__ = {
    }

    __required__ = set([
        'api_groups',
        'resources',
        'verbs',
    ])

    resource_names = None # array
    attribute_restrictions = None # string
    resources = None # array (required)
    verbs = None # array (required)
    api_groups = None # array (required)
    non_resource_ur_ls = None # array

    def __init__(self, *, api_groups, resources, verbs, **_kwargs_):
        self.resource_names = []
        self.non_resource_ur_ls = []

        self.api_groups = api_groups
        self.resources = resources
        self.verbs = verbs

        super().__init__(**_kwargs_)

@register_model
class v1_Preconditions(Resource):

    """Preconditions must be fulfilled before an operation (update, delete,
    etc.) is carried out."""

    __kind__ = 'v1.Preconditions'

    __fields__ = {
        'uid': 'uid',
    }

    __types__ = {
        'uid': 'types.UID',
    }

    __required__ = set()

    uid = None # types.UID

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_Probe(Resource):

    """Probe describes a health check to be performed against a container to
    determine whether it is alive or ready to receive traffic."""

    __kind__ = 'v1.Probe'

    __fields__ = {
        'failure_threshold': 'failureThreshold',
        'exec': 'exec',
        'tcp_socket': 'tcpSocket',
        'timeout_seconds': 'timeoutSeconds',
        'http_get': 'httpGet',
        'period_seconds': 'periodSeconds',
        'initial_delay_seconds': 'initialDelaySeconds',
        'success_threshold': 'successThreshold',
    }

    __types__ = {
        'http_get': 'v1.HTTPGetAction',
        'tcp_socket': 'v1.TCPSocketAction',
        'exec': 'v1.ExecAction',
    }

    __required__ = set()

    failure_threshold = None # integer
    exec = None # v1.ExecAction
    tcp_socket = None # v1.TCPSocketAction
    timeout_seconds = None # integer
    http_get = None # v1.HTTPGetAction
    period_seconds = None # integer
    initial_delay_seconds = None # integer
    success_threshold = None # integer

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_Project(Resource):

    """Project is a logical top-level container for a set of origin resources"""

    __kind__ = 'v1.Project'

    __fields__ = {
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'spec': 'spec',
        'status': 'status',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
        'spec': 'v1.ProjectSpec',
        'status': 'v1.ProjectStatus',
    }

    __required__ = set()

    metadata = None # v1.ObjectMeta
    api_version = None # string
    spec = None # v1.ProjectSpec
    status = None # v1.ProjectStatus
    kind = None # string

    def __init__(self, **_kwargs_):

        self.kind = 'ProjectStatus'

        super().__init__(**_kwargs_)

@register_model
class v1_ProjectList(Resource):

    """ProjectList is a list of Project objects."""

    __kind__ = 'v1.ProjectList'

    __fields__ = {
        'items': 'items',
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'kind': 'kind',
    }

    __types__ = {
        'items': 'v1.Project',
        'metadata': 'unversioned.ListMeta',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    metadata = None # unversioned.ListMeta
    api_version = None # string
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'ListMeta'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_ProjectRequest(Resource):

    """ProjecRequest is the set of options necessary to fully qualify a
    project request"""

    __kind__ = 'v1.ProjectRequest'

    __fields__ = {
        'description': 'description',
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'display_name': 'displayName',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
    }

    __required__ = set()

    description = None # string
    metadata = None # v1.ObjectMeta
    api_version = None # string
    display_name = None # string
    kind = None # string

    def __init__(self, **_kwargs_):

        self.kind = 'ObjectMeta'

        super().__init__(**_kwargs_)

@register_model
class v1_ProjectSpec(Resource):

    """ProjectSpec describes the attributes on a Project"""

    __kind__ = 'v1.ProjectSpec'

    __fields__ = {
        'finalizers': 'finalizers',
    }

    __types__ = {
        'finalizers': 'v1.FinalizerName',
    }

    __required__ = set()

    finalizers = None # array

    def __init__(self, **_kwargs_):
        self.finalizers = []

        super().__init__(**_kwargs_)

@register_model
class v1_ProjectStatus(Resource):

    """ProjectStatus is information about the current status of a Project"""

    __kind__ = 'v1.ProjectStatus'

    __fields__ = {
        'phase': 'phase',
    }

    __types__ = {
    }

    __required__ = set()

    phase = None # string

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_RBDVolumeSource(Resource):

    """Represents a Rados Block Device mount that lasts the lifetime of a
    pod. RBD volumes support ownership management and SELinux
    relabeling."""

    __kind__ = 'v1.RBDVolumeSource'

    __fields__ = {
        'monitors': 'monitors',
        'pool': 'pool',
        'user': 'user',
        'keyring': 'keyring',
        'secret_ref': 'secretRef',
        'read_only': 'readOnly',
        'fs_type': 'fsType',
        'image': 'image',
    }

    __types__ = {
        'secret_ref': 'v1.LocalObjectReference',
    }

    __required__ = set([
        'image',
        'monitors',
    ])

    monitors = None # array (required)
    pool = None # string
    user = None # string
    keyring = None # string
    secret_ref = None # v1.LocalObjectReference
    read_only = None # boolean
    fs_type = None # string
    image = None # string (required)

    def __init__(self, *, image, monitors, **_kwargs_):

        self.image = image
        self.monitors = monitors

        super().__init__(**_kwargs_)

@register_model
class v1_RecreateDeploymentStrategyParams(Resource):

    """RecreateDeploymentStrategyParams are the input to the Recreate
    deployment strategy."""

    __kind__ = 'v1.RecreateDeploymentStrategyParams'

    __fields__ = {
        'post': 'post',
        'mid': 'mid',
        'pre': 'pre',
        'timeout_seconds': 'timeoutSeconds',
    }

    __types__ = {
        'mid': 'v1.LifecycleHook',
        'pre': 'v1.LifecycleHook',
        'post': 'v1.LifecycleHook',
    }

    __required__ = set()

    post = None # v1.LifecycleHook
    mid = None # v1.LifecycleHook
    pre = None # v1.LifecycleHook
    timeout_seconds = None # integer

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_RepositoryImportSpec(Resource):

    """RepositoryImportSpec describes a request to import images from a
    Docker image repository."""

    __kind__ = 'v1.RepositoryImportSpec'

    __fields__ = {
        'import_policy': 'importPolicy',
        'from_': 'from',
        'include_manifest': 'includeManifest',
    }

    __types__ = {
        'import_policy': 'v1.TagImportPolicy',
        'from_': 'v1.ObjectReference',
    }

    __required__ = set([
        'from_',
    ])

    import_policy = None # v1.TagImportPolicy
    from_ = None # v1.ObjectReference (required)
    include_manifest = None # boolean

    def __init__(self, *, from_, **_kwargs_):

        self.from_ = from_

        super().__init__(**_kwargs_)

@register_model
class v1_RepositoryImportStatus(Resource):

    """RepositoryImportStatus describes the result of an image repository
    import"""

    __kind__ = 'v1.RepositoryImportStatus'

    __fields__ = {
        'additional_tags': 'additionalTags',
        'status': 'status',
        'images': 'images',
    }

    __types__ = {
        'status': 'unversioned.Status',
        'images': 'v1.ImageImportStatus',
    }

    __required__ = set()

    additional_tags = None # array
    status = None # unversioned.Status
    images = None # array

    def __init__(self, **_kwargs_):
        self.additional_tags = []
        self.images = []

        super().__init__(**_kwargs_)

@register_model
class v1_ResourceAccessReview(Resource):

    """ResourceAccessReview is a means to request a list of which users and
    groups are authorized to perform the action specified by spec"""

    __kind__ = 'v1.ResourceAccessReview'

    __fields__ = {
        'resource_name': 'resourceName',
        'resource': 'resource',
        'verb': 'verb',
        'api_version': 'apiVersion',
        'resource_api_version': 'resourceAPIVersion',
        'content': 'content',
        'resource_api_group': 'resourceAPIGroup',
        'namespace': 'namespace',
        'kind': 'kind',
    }

    __types__ = {
    }

    __required__ = set([
        'namespace',
        'resource',
        'resource_api_group',
        'resource_api_version',
        'resource_name',
        'verb',
    ])

    resource_name = None # string (required)
    resource = None # string (required)
    verb = None # string (required)
    api_version = None # string
    resource_api_version = None # string (required)
    content = None # string
    resource_api_group = None # string (required)
    namespace = None # string (required)
    kind = None # string

    def __init__(self, *, namespace, resource, resource_api_group, resource_api_version, resource_name, verb, **_kwargs_):

        self.kind = 'ResourceAccessReview'

        self.namespace = namespace
        self.resource = resource
        self.resource_api_group = resource_api_group
        self.resource_api_version = resource_api_version
        self.resource_name = resource_name
        self.verb = verb

        super().__init__(**_kwargs_)

@register_model
class v1_ResourceFieldSelector(Resource):

    """ResourceFieldSelector represents container resources (cpu, memory) and
    their output format"""

    __kind__ = 'v1.ResourceFieldSelector'

    __fields__ = {
        'resource': 'resource',
        'container_name': 'containerName',
        'divisor': 'divisor',
    }

    __types__ = {
    }

    __required__ = set([
        'resource',
    ])

    resource = None # string (required)
    container_name = None # string
    divisor = None # string

    def __init__(self, *, resource, **_kwargs_):

        self.resource = resource

        super().__init__(**_kwargs_)

@register_model
class v1_ResourceQuotaScope(Resource):

    __kind__ = 'v1.ResourceQuotaScope'

    __fields__ = {
    }

    __types__ = {
    }

    __required__ = set()


    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_ResourceQuotaSpec(Resource):

    """ResourceQuotaSpec defines the desired hard limits to enforce for
    Quota."""

    __kind__ = 'v1.ResourceQuotaSpec'

    __fields__ = {
        'hard': 'hard',
        'scopes': 'scopes',
    }

    __types__ = {
        'scopes': 'v1.ResourceQuotaScope',
    }

    __required__ = set()

    hard = None # object
    scopes = None # array

    def __init__(self, **_kwargs_):
        self.scopes = []

        super().__init__(**_kwargs_)

@register_model
class v1_ResourceQuotaStatus(Resource):

    """ResourceQuotaStatus defines the enforced hard limits and observed use."""

    __kind__ = 'v1.ResourceQuotaStatus'

    __fields__ = {
        'hard': 'hard',
        'used': 'used',
    }

    __types__ = {
    }

    __required__ = set()

    hard = None # object
    used = None # object

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_ResourceQuotaStatusByNamespace(Resource):

    """ResourceQuotaStatusByNamespace gives status for a particular project"""

    __kind__ = 'v1.ResourceQuotaStatusByNamespace'

    __fields__ = {
        'namespace': 'namespace',
        'status': 'status',
    }

    __types__ = {
        'status': 'v1.ResourceQuotaStatus',
    }

    __required__ = set([
        'namespace',
        'status',
    ])

    namespace = None # string (required)
    status = None # v1.ResourceQuotaStatus (required)

    def __init__(self, *, namespace, status, **_kwargs_):

        self.namespace = namespace
        self.status = status

        super().__init__(**_kwargs_)

@register_model
class v1_ResourceRequirements(Resource):

    """ResourceRequirements describes the compute resource requirements."""

    __kind__ = 'v1.ResourceRequirements'

    __fields__ = {
        'limits': 'limits',
        'requests': 'requests',
    }

    __types__ = {
    }

    __required__ = set()

    limits = None # object
    requests = None # object

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_Role(Resource):

    """Role is a logical grouping of PolicyRules that can be referenced as a
    unit by RoleBindings."""

    __kind__ = 'v1.Role'

    __fields__ = {
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'rules': 'rules',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
        'rules': 'v1.PolicyRule',
    }

    __required__ = set([
        'rules',
    ])

    metadata = None # v1.ObjectMeta
    api_version = None # string
    rules = None # array (required)
    kind = None # string

    def __init__(self, *, rules, **_kwargs_):

        self.kind = 'PolicyRule'

        self.rules = rules

        super().__init__(**_kwargs_)

@register_model
class v1_RoleBinding(Resource):

    """RoleBinding references a Role, but not contain it.  It can reference
    any Role in the same namespace or in the global namespace. It adds
    who information via Users and Groups and namespace information by
    which namespace it exists in.  RoleBindings in a given namespace
    only have effect in that namespace (excepting the master namespace
    which has power in all namespaces)."""

    __kind__ = 'v1.RoleBinding'

    __fields__ = {
        'role_ref': 'roleRef',
        'subjects': 'subjects',
        'api_version': 'apiVersion',
        'group_names': 'groupNames',
        'metadata': 'metadata',
        'user_names': 'userNames',
        'kind': 'kind',
    }

    __types__ = {
        'role_ref': 'v1.ObjectReference',
        'subjects': 'v1.ObjectReference',
        'metadata': 'v1.ObjectMeta',
    }

    __required__ = set([
        'group_names',
        'role_ref',
        'subjects',
        'user_names',
    ])

    role_ref = None # v1.ObjectReference (required)
    subjects = None # array (required)
    api_version = None # string
    group_names = None # array (required)
    metadata = None # v1.ObjectMeta
    user_names = None # array (required)
    kind = None # string

    def __init__(self, *, group_names, role_ref, subjects, user_names, **_kwargs_):

        self.kind = 'ObjectMeta'

        self.group_names = group_names
        self.role_ref = role_ref
        self.subjects = subjects
        self.user_names = user_names

        super().__init__(**_kwargs_)

@register_model
class v1_RoleBindingList(Resource):

    """RoleBindingList is a collection of RoleBindings"""

    __kind__ = 'v1.RoleBindingList'

    __fields__ = {
        'items': 'items',
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'kind': 'kind',
    }

    __types__ = {
        'items': 'v1.RoleBinding',
        'metadata': 'unversioned.ListMeta',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    metadata = None # unversioned.ListMeta
    api_version = None # string
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'ListMeta'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_RoleList(Resource):

    """RoleList is a collection of Roles"""

    __kind__ = 'v1.RoleList'

    __fields__ = {
        'items': 'items',
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'kind': 'kind',
    }

    __types__ = {
        'items': 'v1.Role',
        'metadata': 'unversioned.ListMeta',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    metadata = None # unversioned.ListMeta
    api_version = None # string
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'ListMeta'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_RollingDeploymentStrategyParams(Resource):

    """RollingDeploymentStrategyParams are the input to the Rolling
    deployment strategy."""

    __kind__ = 'v1.RollingDeploymentStrategyParams'

    __fields__ = {
        'timeout_seconds': 'timeoutSeconds',
        'interval_seconds': 'intervalSeconds',
        'pre': 'pre',
        'max_surge': 'maxSurge',
        'update_period_seconds': 'updatePeriodSeconds',
        'max_unavailable': 'maxUnavailable',
        'update_percent': 'updatePercent',
        'post': 'post',
    }

    __types__ = {
        'pre': 'v1.LifecycleHook',
        'post': 'v1.LifecycleHook',
    }

    __required__ = set()

    timeout_seconds = None # integer
    interval_seconds = None # integer
    pre = None # v1.LifecycleHook
    max_surge = None # string
    update_period_seconds = None # integer
    max_unavailable = None # string
    update_percent = None # integer
    post = None # v1.LifecycleHook

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_Route(Resource):

    """Route encapsulates the inputs needed to connect an alias to endpoints."""

    __kind__ = 'v1.Route'

    __fields__ = {
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'spec': 'spec',
        'status': 'status',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
        'spec': 'v1.RouteSpec',
        'status': 'v1.RouteStatus',
    }

    __required__ = set([
        'spec',
        'status',
    ])

    metadata = None # v1.ObjectMeta
    api_version = None # string
    spec = None # v1.RouteSpec (required)
    status = None # v1.RouteStatus (required)
    kind = None # string

    def __init__(self, *, spec, status, **_kwargs_):

        self.kind = 'RouteStatus'

        self.spec = spec
        self.status = status

        super().__init__(**_kwargs_)

@register_model
class v1_RouteIngress(Resource):

    """RouteIngress holds information about the places where a route is
    exposed"""

    __kind__ = 'v1.RouteIngress'

    __fields__ = {
        'conditions': 'conditions',
        'router_name': 'routerName',
        'host': 'host',
    }

    __types__ = {
        'conditions': 'v1.RouteIngressCondition',
    }

    __required__ = set()

    conditions = None # array
    router_name = None # string
    host = None # string

    def __init__(self, **_kwargs_):
        self.conditions = []

        super().__init__(**_kwargs_)

@register_model
class v1_RouteIngressCondition(Resource):

    """RouteIngressCondition contains details for the current condition of
    this pod."""

    __kind__ = 'v1.RouteIngressCondition'

    __fields__ = {
        'last_transition_time': 'lastTransitionTime',
        'reason': 'reason',
        'message': 'message',
        'type': 'type',
        'status': 'status',
    }

    __types__ = {
    }

    __required__ = set([
        'status',
        'type',
    ])

    last_transition_time = None # string
    reason = None # string
    message = None # string
    type = None # string (required)
    status = None # string (required)

    def __init__(self, *, status, type, **_kwargs_):

        self.status = status
        self.type = type

        super().__init__(**_kwargs_)

@register_model
class v1_RouteList(Resource):

    """RouteList is a collection of Routes."""

    __kind__ = 'v1.RouteList'

    __fields__ = {
        'items': 'items',
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'kind': 'kind',
    }

    __types__ = {
        'items': 'v1.Route',
        'metadata': 'unversioned.ListMeta',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    metadata = None # unversioned.ListMeta
    api_version = None # string
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'ListMeta'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_RoutePort(Resource):

    """RoutePort defines a port mapping from a router to an endpoint in the
    service endpoints."""

    __kind__ = 'v1.RoutePort'

    __fields__ = {
        'target_port': 'targetPort',
    }

    __types__ = {
    }

    __required__ = set([
        'target_port',
    ])

    target_port = None # string (required)

    def __init__(self, *, target_port, **_kwargs_):

        self.target_port = target_port

        super().__init__(**_kwargs_)

@register_model
class v1_RouteSpec(Resource):

    """RouteSpec describes the route the user wishes to exist."""

    __kind__ = 'v1.RouteSpec'

    __fields__ = {
        'to': 'to',
        'host': 'host',
        'path': 'path',
        'alternate_backends': 'alternateBackends',
        'port': 'port',
        'tls': 'tls',
    }

    __types__ = {
        'to': 'v1.RouteTargetReference',
        'alternate_backends': 'v1.RouteTargetReference',
        'port': 'v1.RoutePort',
        'tls': 'v1.TLSConfig',
    }

    __required__ = set([
        'host',
        'to',
    ])

    to = None # v1.RouteTargetReference (required)
    host = None # string (required)
    path = None # string
    alternate_backends = None # array
    port = None # v1.RoutePort
    tls = None # v1.TLSConfig

    def __init__(self, *, host, to, **_kwargs_):
        self.alternate_backends = []

        self.host = host
        self.to = to

        super().__init__(**_kwargs_)

@register_model
class v1_RouteStatus(Resource):

    """RouteStatus provides relevant info about the status of a route,
    including which routers acknowledge it."""

    __kind__ = 'v1.RouteStatus'

    __fields__ = {
        'ingress': 'ingress',
    }

    __types__ = {
        'ingress': 'v1.RouteIngress',
    }

    __required__ = set([
        'ingress',
    ])

    ingress = None # array (required)

    def __init__(self, *, ingress, **_kwargs_):

        self.ingress = ingress

        super().__init__(**_kwargs_)

@register_model
class v1_RouteTargetReference(Resource):

    """RouteTargetReference specifies the target that resolve into endpoints.
    Only the 'Service' kind is allowed. Use 'weight' field to
    emphasize one over others."""

    __kind__ = 'v1.RouteTargetReference'

    __fields__ = {
        'name': 'name',
        'weight': 'weight',
        'kind': 'kind',
    }

    __types__ = {
    }

    __required__ = set([
        'kind',
        'name',
    ])

    name = None # string (required)
    weight = None # integer
    kind = None # string (required)

    def __init__(self, *, kind, name, **_kwargs_):

        self.kind = 'RouteTargetReference'

        self.kind = kind
        self.name = name

        super().__init__(**_kwargs_)

@register_model
class v1_SELinuxOptions(Resource):

    """SELinuxOptions are the labels to be applied to the container"""

    __kind__ = 'v1.SELinuxOptions'

    __fields__ = {
        'level': 'level',
        'user': 'user',
        'role': 'role',
        'type': 'type',
    }

    __types__ = {
    }

    __required__ = set()

    level = None # string
    user = None # string
    role = None # string
    type = None # string

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_ScopeRestriction(Resource):

    """ScopeRestriction describe one restriction on scopes.  Exactly one
    option must be non-nil."""

    __kind__ = 'v1.ScopeRestriction'

    __fields__ = {
        'cluster_role': 'clusterRole',
        'literals': 'literals',
    }

    __types__ = {
        'cluster_role': 'v1.ClusterRoleScopeRestriction',
    }

    __required__ = set()

    cluster_role = None # v1.ClusterRoleScopeRestriction
    literals = None # array

    def __init__(self, **_kwargs_):
        self.literals = []

        super().__init__(**_kwargs_)

@register_model
class v1_Secret(Resource):

    """Secret holds secret data of a certain type. The total bytes of the
    values in the Data field must be less than MaxSecretSize bytes."""

    __kind__ = 'v1.Secret'

    __fields__ = {
        'api_version': 'apiVersion',
        'data': 'data',
        'metadata': 'metadata',
        'string_data': 'stringData',
        'type': 'type',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
    }

    __required__ = set()

    api_version = None # string
    data = None # object
    metadata = None # v1.ObjectMeta
    string_data = None # object
    type = None # string
    kind = None # string

    def __init__(self, **_kwargs_):

        self.kind = 'ObjectMeta'

        super().__init__(**_kwargs_)

@register_model
class v1_SecretBuildSource(Resource):

    """SecretBuildSource describes a secret and its destination directory
    that will be used only at the build time. The content of the
    secret referenced here will be copied into the destination
    directory instead of mounting."""

    __kind__ = 'v1.SecretBuildSource'

    __fields__ = {
        'destination_dir': 'destinationDir',
        'secret': 'secret',
    }

    __types__ = {
        'secret': 'v1.LocalObjectReference',
    }

    __required__ = set([
        'secret',
    ])

    destination_dir = None # string
    secret = None # v1.LocalObjectReference (required)

    def __init__(self, *, secret, **_kwargs_):

        self.secret = secret

        super().__init__(**_kwargs_)

@register_model
class v1_SecretKeySelector(Resource):

    """SecretKeySelector selects a key of a Secret."""

    __kind__ = 'v1.SecretKeySelector'

    __fields__ = {
        'name': 'name',
        'key': 'key',
    }

    __types__ = {
    }

    __required__ = set([
        'key',
    ])

    name = None # string
    key = None # string (required)

    def __init__(self, *, key, **_kwargs_):

        self.key = key

        super().__init__(**_kwargs_)

@register_model
class v1_SecretList(Resource):

    """SecretList is a list of Secret."""

    __kind__ = 'v1.SecretList'

    __fields__ = {
        'items': 'items',
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'kind': 'kind',
    }

    __types__ = {
        'items': 'v1.Secret',
        'metadata': 'unversioned.ListMeta',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    metadata = None # unversioned.ListMeta
    api_version = None # string
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'ListMeta'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_SecretSpec(Resource):

    """SecretSpec specifies a secret to be included in a build pod and its
    corresponding mount point"""

    __kind__ = 'v1.SecretSpec'

    __fields__ = {
        'mount_path': 'mountPath',
        'secret_source': 'secretSource',
    }

    __types__ = {
        'secret_source': 'v1.LocalObjectReference',
    }

    __required__ = set([
        'mount_path',
        'secret_source',
    ])

    mount_path = None # string (required)
    secret_source = None # v1.LocalObjectReference (required)

    def __init__(self, *, mount_path, secret_source, **_kwargs_):

        self.mount_path = mount_path
        self.secret_source = secret_source

        super().__init__(**_kwargs_)

@register_model
class v1_SecretVolumeSource(Resource):

    """Adapts a Secret into a volume.  The contents of the target Secret's
    Data field will be presented in a volume as files using the keys
    in the Data field as the file names. Secret volumes support
    ownership management and SELinux relabeling."""

    __kind__ = 'v1.SecretVolumeSource'

    __fields__ = {
        'items': 'items',
        'secret_name': 'secretName',
    }

    __types__ = {
        'items': 'v1.KeyToPath',
    }

    __required__ = set()

    items = None # array
    secret_name = None # string

    def __init__(self, **_kwargs_):
        self.items = []

        super().__init__(**_kwargs_)

@register_model
class v1_SecurityContext(Resource):

    """SecurityContext holds security configuration that will be applied to a
    container. Some fields are present in both SecurityContext and
    PodSecurityContext.  When both are set, the values in
    SecurityContext take precedence."""

    __kind__ = 'v1.SecurityContext'

    __fields__ = {
        'run_as_user': 'runAsUser',
        'se_linux_options': 'seLinuxOptions',
        'privileged': 'privileged',
        'run_as_non_root': 'runAsNonRoot',
        'capabilities': 'capabilities',
        'read_only_root_filesystem': 'readOnlyRootFilesystem',
    }

    __types__ = {
        'se_linux_options': 'v1.SELinuxOptions',
        'capabilities': 'v1.Capabilities',
    }

    __required__ = set()

    run_as_user = None # integer
    se_linux_options = None # v1.SELinuxOptions
    privileged = None # boolean
    run_as_non_root = None # boolean
    capabilities = None # v1.Capabilities
    read_only_root_filesystem = None # boolean

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_SelfSubjectRulesReview(Resource):

    """SelfSubjectRulesReview is a resource you can create to determine which
    actions you can perform in a namespace"""

    __kind__ = 'v1.SelfSubjectRulesReview'

    __fields__ = {
        'api_version': 'apiVersion',
        'spec': 'spec',
        'status': 'status',
        'kind': 'kind',
    }

    __types__ = {
        'spec': 'v1.SelfSubjectRulesReviewSpec',
        'status': 'v1.SubjectRulesReviewStatus',
    }

    __required__ = set([
        'spec',
    ])

    api_version = None # string
    spec = None # v1.SelfSubjectRulesReviewSpec (required)
    status = None # v1.SubjectRulesReviewStatus
    kind = None # string

    def __init__(self, *, spec, **_kwargs_):

        self.kind = 'SubjectRulesReviewStatus'

        self.spec = spec

        super().__init__(**_kwargs_)

@register_model
class v1_SelfSubjectRulesReviewSpec(Resource):

    """SelfSubjectRulesReviewSpec adds information about how to conduct the
    check"""

    __kind__ = 'v1.SelfSubjectRulesReviewSpec'

    __fields__ = {
        'scopes': 'scopes',
    }

    __types__ = {
    }

    __required__ = set([
        'scopes',
    ])

    scopes = None # array (required)

    def __init__(self, *, scopes, **_kwargs_):

        self.scopes = scopes

        super().__init__(**_kwargs_)

@register_model
class v1_SignatureCondition(Resource):

    """SignatureCondition describes an image signature condition of
    particular kind at particular probe time."""

    __kind__ = 'v1.SignatureCondition'

    __fields__ = {
        'last_transition_time': 'lastTransitionTime',
        'reason': 'reason',
        'type': 'type',
        'last_probe_time': 'lastProbeTime',
        'message': 'message',
        'status': 'status',
    }

    __types__ = {
    }

    __required__ = set([
        'status',
        'type',
    ])

    last_transition_time = None # string
    reason = None # string
    type = None # string (required)
    last_probe_time = None # string
    message = None # string
    status = None # string (required)

    def __init__(self, *, status, type, **_kwargs_):

        self.status = status
        self.type = type

        super().__init__(**_kwargs_)

@register_model
class v1_SignatureIssuer(Resource):

    """SignatureIssuer holds information about an issuer of signing
    certificate or key."""

    __kind__ = 'v1.SignatureIssuer'

    __fields__ = {
        'organization': 'organization',
        'common_name': 'commonName',
    }

    __types__ = {
    }

    __required__ = set()

    organization = None # string
    common_name = None # string

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_SignatureSubject(Resource):

    """SignatureSubject holds information about a person or entity who
    created the signature."""

    __kind__ = 'v1.SignatureSubject'

    __fields__ = {
        'public_key_id': 'publicKeyID',
        'organization': 'organization',
        'common_name': 'commonName',
    }

    __types__ = {
    }

    __required__ = set([
        'public_key_id',
    ])

    public_key_id = None # string (required)
    organization = None # string
    common_name = None # string

    def __init__(self, *, public_key_id, **_kwargs_):

        self.public_key_id = public_key_id

        super().__init__(**_kwargs_)

@register_model
class v1_SourceBuildStrategy(Resource):

    """SourceBuildStrategy defines input parameters specific to an Source
    build."""

    __kind__ = 'v1.SourceBuildStrategy'

    __fields__ = {
        'from_': 'from',
        'pull_secret': 'pullSecret',
        'env': 'env',
        'incremental': 'incremental',
        'force_pull': 'forcePull',
        'runtime_artifacts': 'runtimeArtifacts',
        'scripts': 'scripts',
        'runtime_image': 'runtimeImage',
    }

    __types__ = {
        'from_': 'v1.ObjectReference',
        'pull_secret': 'v1.LocalObjectReference',
        'env': 'v1.EnvVar',
        'runtime_artifacts': 'v1.ImageSourcePath',
        'runtime_image': 'v1.ObjectReference',
    }

    __required__ = set([
        'from_',
    ])

    from_ = None # v1.ObjectReference (required)
    pull_secret = None # v1.LocalObjectReference
    env = None # array
    incremental = None # boolean
    force_pull = None # boolean
    runtime_artifacts = None # array
    scripts = None # string
    runtime_image = None # v1.ObjectReference

    def __init__(self, *, from_, **_kwargs_):
        self.env = []
        self.runtime_artifacts = []

        self.from_ = from_

        super().__init__(**_kwargs_)

@register_model
class v1_SourceControlUser(Resource):

    """SourceControlUser defines the identity of a user of source control"""

    __kind__ = 'v1.SourceControlUser'

    __fields__ = {
        'name': 'name',
        'email': 'email',
    }

    __types__ = {
    }

    __required__ = set()

    name = None # string
    email = None # string

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_SourceRevision(Resource):

    """SourceRevision is the revision or commit information from the source
    for the build"""

    __kind__ = 'v1.SourceRevision'

    __fields__ = {
        'git': 'git',
        'type': 'type',
    }

    __types__ = {
        'git': 'v1.GitSourceRevision',
    }

    __required__ = set([
        'type',
    ])

    git = None # v1.GitSourceRevision
    type = None # string (required)

    def __init__(self, *, type, **_kwargs_):

        self.type = type

        super().__init__(**_kwargs_)

@register_model
class v1_SubjectAccessReview(Resource):

    """SubjectAccessReview is an object for requesting information about
    whether a user or group can perform an action"""

    __kind__ = 'v1.SubjectAccessReview'

    __fields__ = {
        'resource': 'resource',
        'resource_api_version': 'resourceAPIVersion',
        'scopes': 'scopes',
        'content': 'content',
        'resource_api_group': 'resourceAPIGroup',
        'resource_name': 'resourceName',
        'verb': 'verb',
        'api_version': 'apiVersion',
        'user': 'user',
        'kind': 'kind',
        'namespace': 'namespace',
        'groups': 'groups',
    }

    __types__ = {
    }

    __required__ = set([
        'groups',
        'namespace',
        'resource',
        'resource_api_group',
        'resource_api_version',
        'resource_name',
        'scopes',
        'user',
        'verb',
    ])

    resource = None # string (required)
    resource_api_version = None # string (required)
    scopes = None # array (required)
    content = None # string
    resource_api_group = None # string (required)
    resource_name = None # string (required)
    verb = None # string (required)
    api_version = None # string
    user = None # string (required)
    kind = None # string
    namespace = None # string (required)
    groups = None # array (required)

    def __init__(self, *, groups, namespace, resource, resource_api_group, resource_api_version, resource_name, scopes, user, verb, **_kwargs_):

        self.kind = 'SubjectAccessReview'

        self.groups = groups
        self.namespace = namespace
        self.resource = resource
        self.resource_api_group = resource_api_group
        self.resource_api_version = resource_api_version
        self.resource_name = resource_name
        self.scopes = scopes
        self.user = user
        self.verb = verb

        super().__init__(**_kwargs_)

@register_model
class v1_SubjectRulesReviewStatus(Resource):

    """SubjectRulesReviewStatus is contains the result of a rules check"""

    __kind__ = 'v1.SubjectRulesReviewStatus'

    __fields__ = {
        'evaluation_error': 'evaluationError',
        'rules': 'rules',
    }

    __types__ = {
        'rules': 'v1.PolicyRule',
    }

    __required__ = set([
        'rules',
    ])

    evaluation_error = None # string
    rules = None # array (required)

    def __init__(self, *, rules, **_kwargs_):

        self.rules = rules

        super().__init__(**_kwargs_)

@register_model
class v1_TCPSocketAction(Resource):

    """TCPSocketAction describes an action based on opening a socket"""

    __kind__ = 'v1.TCPSocketAction'

    __fields__ = {
        'port': 'port',
    }

    __types__ = {
    }

    __required__ = set([
        'port',
    ])

    port = None # string (required)

    def __init__(self, *, port, **_kwargs_):

        self.port = port

        super().__init__(**_kwargs_)

@register_model
class v1_TLSConfig(Resource):

    """TLSConfig defines config used to secure a route and provide
    termination"""

    __kind__ = 'v1.TLSConfig'

    __fields__ = {
        'destination_ca_certificate': 'destinationCACertificate',
        'certificate': 'certificate',
        'termination': 'termination',
        'ca_certificate': 'caCertificate',
        'insecure_edge_termination_policy': 'insecureEdgeTerminationPolicy',
        'key': 'key',
    }

    __types__ = {
    }

    __required__ = set([
        'termination',
    ])

    destination_ca_certificate = None # string
    certificate = None # string
    termination = None # string (required)
    ca_certificate = None # string
    insecure_edge_termination_policy = None # string
    key = None # string

    def __init__(self, *, termination, **_kwargs_):

        self.termination = termination

        super().__init__(**_kwargs_)

@register_model
class v1_TagEvent(Resource):

    """TagEvent is used by ImageStreamStatus to keep a historical record of
    images associated with a tag."""

    __kind__ = 'v1.TagEvent'

    __fields__ = {
        'generation': 'generation',
        'created': 'created',
        'docker_image_reference': 'dockerImageReference',
        'image': 'image',
    }

    __types__ = {
    }

    __required__ = set([
        'created',
        'docker_image_reference',
        'generation',
        'image',
    ])

    generation = None # integer (required)
    created = None # string (required)
    docker_image_reference = None # string (required)
    image = None # string (required)

    def __init__(self, *, created, docker_image_reference, generation, image, **_kwargs_):

        self.created = created
        self.docker_image_reference = docker_image_reference
        self.generation = generation
        self.image = image

        super().__init__(**_kwargs_)

@register_model
class v1_TagEventCondition(Resource):

    """TagEventCondition contains condition information for a tag event."""

    __kind__ = 'v1.TagEventCondition'

    __fields__ = {
        'last_transition_time': 'lastTransitionTime',
        'reason': 'reason',
        'type': 'type',
        'generation': 'generation',
        'message': 'message',
        'status': 'status',
    }

    __types__ = {
    }

    __required__ = set([
        'generation',
        'status',
        'type',
    ])

    last_transition_time = None # string
    reason = None # string
    type = None # string (required)
    generation = None # integer (required)
    message = None # string
    status = None # string (required)

    def __init__(self, *, generation, status, type, **_kwargs_):

        self.generation = generation
        self.status = status
        self.type = type

        super().__init__(**_kwargs_)

@register_model
class v1_TagImageHook(Resource):

    """TagImageHook is a request to tag the image in a particular container
    onto an ImageStreamTag."""

    __kind__ = 'v1.TagImageHook'

    __fields__ = {
        'to': 'to',
        'container_name': 'containerName',
    }

    __types__ = {
        'to': 'v1.ObjectReference',
    }

    __required__ = set([
        'container_name',
        'to',
    ])

    to = None # v1.ObjectReference (required)
    container_name = None # string (required)

    def __init__(self, *, container_name, to, **_kwargs_):

        self.container_name = container_name
        self.to = to

        super().__init__(**_kwargs_)

@register_model
class v1_TagImportPolicy(Resource):

    """TagImportPolicy describes the tag import policy"""

    __kind__ = 'v1.TagImportPolicy'

    __fields__ = {
        'scheduled': 'scheduled',
        'insecure': 'insecure',
    }

    __types__ = {
    }

    __required__ = set()

    scheduled = None # boolean
    insecure = None # boolean

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_TagReference(Resource):

    """TagReference specifies optional annotations for images using this tag
    and an optional reference to an ImageStreamTag, ImageStreamImage,
    or DockerImage this tag should track."""

    __kind__ = 'v1.TagReference'

    __fields__ = {
        'name': 'name',
        'from_': 'from',
        'generation': 'generation',
        'import_policy': 'importPolicy',
        'reference': 'reference',
        'annotations': 'annotations',
    }

    __types__ = {
        'import_policy': 'v1.TagImportPolicy',
        'from_': 'v1.ObjectReference',
    }

    __required__ = set([
        'annotations',
        'generation',
        'name',
    ])

    name = None # string (required)
    from_ = None # v1.ObjectReference
    generation = None # integer (required)
    import_policy = None # v1.TagImportPolicy
    reference = None # boolean
    annotations = None # object (required)

    def __init__(self, *, annotations, generation, name, **_kwargs_):

        self.annotations = annotations
        self.generation = generation
        self.name = name

        super().__init__(**_kwargs_)

@register_model
class v1_Template(Resource):

    """Template contains the inputs needed to produce a Config."""

    __kind__ = 'v1.Template'

    __fields__ = {
        'objects': 'objects',
        'api_version': 'apiVersion',
        'parameters': 'parameters',
        'metadata': 'metadata',
        'message': 'message',
        'labels': 'labels',
        'kind': 'kind',
    }

    __types__ = {
        'objects': 'runtime.RawExtension',
        'parameters': 'v1.Parameter',
        'metadata': 'v1.ObjectMeta',
    }

    __required__ = set([
        'objects',
    ])

    objects = None # array (required)
    api_version = None # string
    parameters = None # array
    metadata = None # v1.ObjectMeta
    message = None # string
    labels = None # object
    kind = None # string

    def __init__(self, *, objects, **_kwargs_):
        self.parameters = []

        self.kind = 'ObjectMeta'

        self.objects = objects

        super().__init__(**_kwargs_)

@register_model
class v1_TemplateList(Resource):

    """TemplateList is a list of Template objects."""

    __kind__ = 'v1.TemplateList'

    __fields__ = {
        'items': 'items',
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'kind': 'kind',
    }

    __types__ = {
        'items': 'v1.Template',
        'metadata': 'unversioned.ListMeta',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    metadata = None # unversioned.ListMeta
    api_version = None # string
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'ListMeta'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_User(Resource):

    """User describes someone that makes requests to the API"""

    __kind__ = 'v1.User'

    __fields__ = {
        'groups': 'groups',
        'api_version': 'apiVersion',
        'identities': 'identities',
        'metadata': 'metadata',
        'kind': 'kind',
        'full_name': 'fullName',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
    }

    __required__ = set([
        'groups',
        'identities',
    ])

    groups = None # array (required)
    api_version = None # string
    identities = None # array (required)
    metadata = None # v1.ObjectMeta
    kind = None # string
    full_name = None # string

    def __init__(self, *, groups, identities, **_kwargs_):

        self.kind = 'ObjectMeta'

        self.groups = groups
        self.identities = identities

        super().__init__(**_kwargs_)

@register_model
class v1_UserIdentityMapping(Resource):

    """UserIdentityMapping maps a user to an identity"""

    __kind__ = 'v1.UserIdentityMapping'

    __fields__ = {
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'user': 'user',
        'identity': 'identity',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
        'user': 'v1.ObjectReference',
        'identity': 'v1.ObjectReference',
    }

    __required__ = set()

    metadata = None # v1.ObjectMeta
    api_version = None # string
    user = None # v1.ObjectReference
    identity = None # v1.ObjectReference
    kind = None # string

    def __init__(self, **_kwargs_):

        self.kind = 'ObjectReference'

        super().__init__(**_kwargs_)

@register_model
class v1_UserList(Resource):

    """UserList is a collection of Users"""

    __kind__ = 'v1.UserList'

    __fields__ = {
        'items': 'items',
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'kind': 'kind',
    }

    __types__ = {
        'items': 'v1.User',
        'metadata': 'unversioned.ListMeta',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    metadata = None # unversioned.ListMeta
    api_version = None # string
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'ListMeta'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_Volume(Resource):

    """Volume represents a named volume in a pod that may be accessed by any
    container in the pod."""

    __kind__ = 'v1.Volume'

    __fields__ = {
        'flex_volume': 'flexVolume',
        'flocker': 'flocker',
        'aws_elastic_block_store': 'awsElasticBlockStore',
        'empty_dir': 'emptyDir',
        'host_path': 'hostPath',
        'iscsi': 'iscsi',
        'cinder': 'cinder',
        'fc': 'fc',
        'gce_persistent_disk': 'gcePersistentDisk',
        'name': 'name',
        'azure_file': 'azureFile',
        'nfs': 'nfs',
        'metadata': 'metadata',
        'persistent_volume_claim': 'persistentVolumeClaim',
        'git_repo': 'gitRepo',
        'rbd': 'rbd',
        'glusterfs': 'glusterfs',
        'config_map': 'configMap',
        'cephfs': 'cephfs',
        'downward_api': 'downwardAPI',
        'vsphere_volume': 'vsphereVolume',
        'secret': 'secret',
    }

    __types__ = {
        'flex_volume': 'v1.FlexVolumeSource',
        'flocker': 'v1.FlockerVolumeSource',
        'aws_elastic_block_store': 'v1.AWSElasticBlockStoreVolumeSource',
        'empty_dir': 'v1.EmptyDirVolumeSource',
        'host_path': 'v1.HostPathVolumeSource',
        'iscsi': 'v1.ISCSIVolumeSource',
        'cinder': 'v1.CinderVolumeSource',
        'nfs': 'v1.NFSVolumeSource',
        'metadata': 'v1.DeprecatedDownwardAPIVolumeSource',
        'azure_file': 'v1.AzureFileVolumeSource',
        'persistent_volume_claim': 'v1.PersistentVolumeClaimVolumeSource',
        'rbd': 'v1.RBDVolumeSource',
        'gce_persistent_disk': 'v1.GCEPersistentDiskVolumeSource',
        'config_map': 'v1.ConfigMapVolumeSource',
        'fc': 'v1.FCVolumeSource',
        'cephfs': 'v1.CephFSVolumeSource',
        'git_repo': 'v1.GitRepoVolumeSource',
        'glusterfs': 'v1.GlusterfsVolumeSource',
        'vsphere_volume': 'v1.VsphereVirtualDiskVolumeSource',
        'downward_api': 'v1.DownwardAPIVolumeSource',
        'secret': 'v1.SecretVolumeSource',
    }

    __required__ = set([
        'name',
    ])

    flex_volume = None # v1.FlexVolumeSource
    flocker = None # v1.FlockerVolumeSource
    aws_elastic_block_store = None # v1.AWSElasticBlockStoreVolumeSource
    empty_dir = None # v1.EmptyDirVolumeSource
    host_path = None # v1.HostPathVolumeSource
    iscsi = None # v1.ISCSIVolumeSource
    cinder = None # v1.CinderVolumeSource
    fc = None # v1.FCVolumeSource
    gce_persistent_disk = None # v1.GCEPersistentDiskVolumeSource
    name = None # string (required)
    azure_file = None # v1.AzureFileVolumeSource
    nfs = None # v1.NFSVolumeSource
    metadata = None # v1.DeprecatedDownwardAPIVolumeSource
    persistent_volume_claim = None # v1.PersistentVolumeClaimVolumeSource
    git_repo = None # v1.GitRepoVolumeSource
    rbd = None # v1.RBDVolumeSource
    glusterfs = None # v1.GlusterfsVolumeSource
    config_map = None # v1.ConfigMapVolumeSource
    cephfs = None # v1.CephFSVolumeSource
    downward_api = None # v1.DownwardAPIVolumeSource
    vsphere_volume = None # v1.VsphereVirtualDiskVolumeSource
    secret = None # v1.SecretVolumeSource

    def __init__(self, *, name, **_kwargs_):

        self.name = name

        super().__init__(**_kwargs_)

@register_model
class v1_VolumeMount(Resource):

    """VolumeMount describes a mounting of a Volume within a container."""

    __kind__ = 'v1.VolumeMount'

    __fields__ = {
        'name': 'name',
        'mount_path': 'mountPath',
        'read_only': 'readOnly',
        'sub_path': 'subPath',
    }

    __types__ = {
    }

    __required__ = set([
        'mount_path',
        'name',
    ])

    name = None # string (required)
    mount_path = None # string (required)
    read_only = None # boolean
    sub_path = None # string

    def __init__(self, *, mount_path, name, **_kwargs_):

        self.mount_path = mount_path
        self.name = name

        super().__init__(**_kwargs_)

@register_model
class v1_VsphereVirtualDiskVolumeSource(Resource):

    """Represents a vSphere volume resource."""

    __kind__ = 'v1.VsphereVirtualDiskVolumeSource'

    __fields__ = {
        'volume_path': 'volumePath',
        'fs_type': 'fsType',
    }

    __types__ = {
    }

    __required__ = set([
        'volume_path',
    ])

    volume_path = None # string (required)
    fs_type = None # string

    def __init__(self, *, volume_path, **_kwargs_):

        self.volume_path = volume_path

        super().__init__(**_kwargs_)

@register_model
class v1_WebHookTrigger(Resource):

    """WebHookTrigger is a trigger that gets invoked using a webhook type of
    post"""

    __kind__ = 'v1.WebHookTrigger'

    __fields__ = {
        'allow_env': 'allowEnv',
        'secret': 'secret',
    }

    __types__ = {
    }

    __required__ = set()

    allow_env = None # boolean
    secret = None # string

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1beta1_Scale(Resource):

    """represents a scaling request for a resource."""

    __kind__ = 'v1beta1.Scale'

    __fields__ = {
        'metadata': 'metadata',
        'api_version': 'apiVersion',
        'spec': 'spec',
        'status': 'status',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
        'spec': 'v1beta1.ScaleSpec',
        'status': 'v1beta1.ScaleStatus',
    }

    __required__ = set()

    metadata = None # v1.ObjectMeta
    api_version = None # string
    spec = None # v1beta1.ScaleSpec
    status = None # v1beta1.ScaleStatus
    kind = None # string

    def __init__(self, **_kwargs_):

        self.kind = 'ScaleStatus'

        super().__init__(**_kwargs_)

@register_model
class v1beta1_ScaleSpec(Resource):

    """describes the attributes of a scale subresource"""

    __kind__ = 'v1beta1.ScaleSpec'

    __fields__ = {
        'replicas': 'replicas',
    }

    __types__ = {
    }

    __required__ = set()

    replicas = None # integer

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1beta1_ScaleStatus(Resource):

    """represents the current status of a scale subresource."""

    __kind__ = 'v1beta1.ScaleStatus'

    __fields__ = {
        'selector': 'selector',
        'replicas': 'replicas',
        'target_selector': 'targetSelector',
    }

    __types__ = {
    }

    __required__ = set([
        'replicas',
    ])

    selector = None # object
    replicas = None # integer (required)
    target_selector = None # string

    def __init__(self, *, replicas, **_kwargs_):

        self.replicas = replicas

        super().__init__(**_kwargs_)
__all__ = ['versioned_Event', 'patch_Object', 'runtime_RawExtension', 'types_UID', 'unversioned_APIResource', 'unversioned_APIResourceList', 'unversioned_LabelSelector', 'unversioned_LabelSelectorRequirement', 'unversioned_ListMeta', 'unversioned_Patch', 'unversioned_Status', 'unversioned_StatusCause', 'unversioned_StatusDetails', 'v1_AWSElasticBlockStoreVolumeSource', 'v1_AppliedClusterResourceQuota', 'v1_AppliedClusterResourceQuotaList', 'v1_AzureFileVolumeSource', 'v1_BinaryBuildSource', 'v1_Build', 'v1_BuildConfig', 'v1_BuildConfigList', 'v1_BuildConfigSpec', 'v1_BuildConfigStatus', 'v1_BuildList', 'v1_BuildLog', 'v1_BuildOutput', 'v1_BuildPostCommitSpec', 'v1_BuildRequest', 'v1_BuildSource', 'v1_BuildSpec', 'v1_BuildStatus', 'v1_BuildStrategy', 'v1_BuildTriggerCause', 'v1_BuildTriggerPolicy', 'v1_Capabilities', 'v1_Capability', 'v1_CephFSVolumeSource', 'v1_CinderVolumeSource', 'v1_ClusterNetwork', 'v1_ClusterNetworkList', 'v1_ClusterPolicy', 'v1_ClusterPolicyBinding', 'v1_ClusterPolicyBindingList', 'v1_ClusterPolicyList', 'v1_ClusterResourceQuota', 'v1_ClusterResourceQuotaList', 'v1_ClusterResourceQuotaSelector', 'v1_ClusterResourceQuotaSpec', 'v1_ClusterResourceQuotaStatus', 'v1_ClusterRole', 'v1_ClusterRoleBinding', 'v1_ClusterRoleBindingList', 'v1_ClusterRoleList', 'v1_ClusterRoleScopeRestriction', 'v1_ConfigMapKeySelector', 'v1_ConfigMapVolumeSource', 'v1_Container', 'v1_ContainerPort', 'v1_CustomBuildStrategy', 'v1_CustomDeploymentStrategyParams', 'v1_DeleteOptions', 'v1_DeploymentCause', 'v1_DeploymentCauseImageTrigger', 'v1_DeploymentConfig', 'v1_DeploymentConfigList', 'v1_DeploymentConfigRollback', 'v1_DeploymentConfigRollbackSpec', 'v1_DeploymentConfigSpec', 'v1_DeploymentConfigStatus', 'v1_DeploymentDetails', 'v1_DeploymentLog', 'v1_DeploymentStrategy', 'v1_DeploymentTriggerImageChangeParams', 'v1_DeploymentTriggerPolicy', 'v1_DeprecatedDownwardAPIVolumeFile', 'v1_DeprecatedDownwardAPIVolumeSource', 'v1_DockerBuildStrategy', 'v1_DownwardAPIVolumeFile', 'v1_DownwardAPIVolumeSource', 'v1_EgressNetworkPolicy', 'v1_EgressNetworkPolicyList', 'v1_EgressNetworkPolicyPeer', 'v1_EgressNetworkPolicyRule', 'v1_EgressNetworkPolicySpec', 'v1_EmptyDirVolumeSource', 'v1_EnvVar', 'v1_EnvVarSource', 'v1_ExecAction', 'v1_ExecNewPodHook', 'v1_FCVolumeSource', 'v1_FinalizerName', 'v1_FlexVolumeSource', 'v1_FlockerVolumeSource', 'v1_GCEPersistentDiskVolumeSource', 'v1_GenericWebHookCause', 'v1_GitBuildSource', 'v1_GitHubWebHookCause', 'v1_GitRepoVolumeSource', 'v1_GitSourceRevision', 'v1_GlusterfsVolumeSource', 'v1_Group', 'v1_GroupList', 'v1_HTTPGetAction', 'v1_HTTPHeader', 'v1_Handler', 'v1_HostPathVolumeSource', 'v1_HostSubnet', 'v1_HostSubnetList', 'v1_ISCSIVolumeSource', 'v1_Identity', 'v1_IdentityList', 'v1_Image', 'v1_Image_dockerImageSignatures', 'v1_ImageChangeCause', 'v1_ImageChangeTrigger', 'v1_ImageImportSpec', 'v1_ImageImportStatus', 'v1_ImageLayer', 'v1_ImageList', 'v1_ImageSignature', 'v1_ImageSource', 'v1_ImageSourcePath', 'v1_ImageStream', 'v1_ImageStreamImage', 'v1_ImageStreamImport', 'v1_ImageStreamImportSpec', 'v1_ImageStreamImportStatus', 'v1_ImageStreamList', 'v1_ImageStreamMapping', 'v1_ImageStreamSpec', 'v1_ImageStreamStatus', 'v1_ImageStreamTag', 'v1_ImageStreamTagList', 'v1_JenkinsPipelineBuildStrategy', 'v1_KeyToPath', 'v1_Lifecycle', 'v1_LifecycleHook', 'v1_LocalObjectReference', 'v1_LocalResourceAccessReview', 'v1_LocalSubjectAccessReview', 'v1_NFSVolumeSource', 'v1_NamedClusterRole', 'v1_NamedClusterRoleBinding', 'v1_NamedRole', 'v1_NamedRoleBinding', 'v1_NamedTagEventList', 'v1_NetNamespace', 'v1_NetNamespaceList', 'v1_OAuthAccessToken', 'v1_OAuthAccessTokenList', 'v1_OAuthAuthorizeToken', 'v1_OAuthAuthorizeTokenList', 'v1_OAuthClient', 'v1_OAuthClientAuthorization', 'v1_OAuthClientAuthorizationList', 'v1_OAuthClientList', 'v1_ObjectFieldSelector', 'v1_ObjectMeta', 'v1_ObjectReference', 'v1_OwnerReference', 'v1_Parameter', 'v1_PersistentVolumeClaimVolumeSource', 'v1_PodSecurityContext', 'v1_PodSpec', 'v1_PodTemplateSpec', 'v1_Policy', 'v1_PolicyBinding', 'v1_PolicyBindingList', 'v1_PolicyList', 'v1_PolicyRule', 'v1_Preconditions', 'v1_Probe', 'v1_Project', 'v1_ProjectList', 'v1_ProjectRequest', 'v1_ProjectSpec', 'v1_ProjectStatus', 'v1_RBDVolumeSource', 'v1_RecreateDeploymentStrategyParams', 'v1_RepositoryImportSpec', 'v1_RepositoryImportStatus', 'v1_ResourceAccessReview', 'v1_ResourceFieldSelector', 'v1_ResourceQuotaScope', 'v1_ResourceQuotaSpec', 'v1_ResourceQuotaStatus', 'v1_ResourceQuotaStatusByNamespace', 'v1_ResourceRequirements', 'v1_Role', 'v1_RoleBinding', 'v1_RoleBindingList', 'v1_RoleList', 'v1_RollingDeploymentStrategyParams', 'v1_Route', 'v1_RouteIngress', 'v1_RouteIngressCondition', 'v1_RouteList', 'v1_RoutePort', 'v1_RouteSpec', 'v1_RouteStatus', 'v1_RouteTargetReference', 'v1_SELinuxOptions', 'v1_ScopeRestriction', 'v1_Secret', 'v1_SecretBuildSource', 'v1_SecretKeySelector', 'v1_SecretList', 'v1_SecretSpec', 'v1_SecretVolumeSource', 'v1_SecurityContext', 'v1_SelfSubjectRulesReview', 'v1_SelfSubjectRulesReviewSpec', 'v1_SignatureCondition', 'v1_SignatureIssuer', 'v1_SignatureSubject', 'v1_SourceBuildStrategy', 'v1_SourceControlUser', 'v1_SourceRevision', 'v1_SubjectAccessReview', 'v1_SubjectRulesReviewStatus', 'v1_TCPSocketAction', 'v1_TLSConfig', 'v1_TagEvent', 'v1_TagEventCondition', 'v1_TagImageHook', 'v1_TagImportPolicy', 'v1_TagReference', 'v1_Template', 'v1_TemplateList', 'v1_User', 'v1_UserIdentityMapping', 'v1_UserList', 'v1_Volume', 'v1_VolumeMount', 'v1_VsphereVirtualDiskVolumeSource', 'v1_WebHookTrigger', 'v1beta1_Scale', 'v1beta1_ScaleSpec', 'v1beta1_ScaleStatus']
