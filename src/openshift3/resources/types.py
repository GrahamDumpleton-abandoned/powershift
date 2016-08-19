
# XXX This code file has been automatically generated. Do not edit it.

from .base import Resource, register_model


@register_model
class unversioned_ListMeta(Resource):

    """ListMeta describes metadata that synthetic resources must have,
    including lists and various status objects. A resource may have
    only one of {ObjectMeta, ListMeta}."""

    __kind__ = 'unversioned.ListMeta'

    __fields__ = {
        'self_link': 'selfLink',
        'resource_version': 'resourceVersion',
    }

    __types__ = {
    }

    __required__ = set()

    self_link = None # string
    resource_version = None # string

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_Capabilities(Resource):

    """Adds and removes POSIX capabilities from running containers."""

    __kind__ = 'v1.Capabilities'

    __fields__ = {
        'add': 'add',
        'drop': 'drop',
    }

    __types__ = {
        'add': 'v1.Capability',
    }

    __required__ = set()

    add = None # array
    drop = None # array

    def __init__(self, **_kwargs_):
        self.add = []
        self.drop = []

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
        'subsets': 'subsets',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'subsets': 'v1.EndpointSubset',
        'metadata': 'v1.ObjectMeta',
    }

    __required__ = set([
        'subsets',
    ])

    subsets = None # array (required)
    api_version = None # string
    metadata = None # v1.ObjectMeta
    kind = None # string

    def __init__(self, *, subsets, **_kwargs_):

        self.kind = 'ObjectMeta'

        self.subsets = subsets

        super().__init__(**_kwargs_)

@register_model
class v1_SecurityContext(Resource):

    """SecurityContext holds security configuration that will be applied to a
    container. Some fields are present in both SecurityContext and
    PodSecurityContext.  When both are set, the values in
    SecurityContext take precedence."""

    __kind__ = 'v1.SecurityContext'

    __fields__ = {
        'privileged': 'privileged',
        'capabilities': 'capabilities',
        'run_as_non_root': 'runAsNonRoot',
        'run_as_user': 'runAsUser',
        'se_linux_options': 'seLinuxOptions',
        'read_only_root_filesystem': 'readOnlyRootFilesystem',
    }

    __types__ = {
        'se_linux_options': 'v1.SELinuxOptions',
        'capabilities': 'v1.Capabilities',
    }

    __required__ = set()

    privileged = None # boolean
    capabilities = None # v1.Capabilities
    run_as_non_root = None # boolean
    run_as_user = None # integer
    se_linux_options = None # v1.SELinuxOptions
    read_only_root_filesystem = None # boolean

    def __init__(self, **_kwargs_):

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
        'items': 'items',
        'name': 'name',
    }

    __types__ = {
        'items': 'v1.KeyToPath',
    }

    __required__ = set()

    items = None # array
    name = None # string

    def __init__(self, **_kwargs_):
        self.items = []

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
class v1_ContainerPort(Resource):

    """ContainerPort represents a network port in a single container."""

    __kind__ = 'v1.ContainerPort'

    __fields__ = {
        'host_ip': 'hostIP',
        'host_port': 'hostPort',
        'protocol': 'protocol',
        'name': 'name',
        'container_port': 'containerPort',
    }

    __types__ = {
    }

    __required__ = set([
        'container_port',
    ])

    host_ip = None # string
    host_port = None # integer
    protocol = None # string
    name = None # string
    container_port = None # integer (required)

    def __init__(self, *, container_port, **_kwargs_):

        self.container_port = container_port

        super().__init__(**_kwargs_)

@register_model
class v1_ObjectMeta(Resource):

    """ObjectMeta is metadata that all persisted resources must have, which
    includes all objects users must create."""

    __kind__ = 'v1.ObjectMeta'

    __fields__ = {
        'generation': 'generation',
        'namespace': 'namespace',
        'annotations': 'annotations',
        'generate_name': 'generateName',
        'creation_timestamp': 'creationTimestamp',
        'deletion_grace_period_seconds': 'deletionGracePeriodSeconds',
        'name': 'name',
        'resource_version': 'resourceVersion',
        'finalizers': 'finalizers',
        'owner_references': 'ownerReferences',
        'deletion_timestamp': 'deletionTimestamp',
        'uid': 'uid',
        'self_link': 'selfLink',
        'labels': 'labels',
    }

    __types__ = {
        'owner_references': 'v1.OwnerReference',
    }

    __required__ = set()

    generation = None # integer
    namespace = None # string
    annotations = None # object
    generate_name = None # string
    creation_timestamp = None # string
    deletion_grace_period_seconds = None # integer
    name = None # string
    resource_version = None # string
    finalizers = None # array
    owner_references = None # array
    deletion_timestamp = None # string
    uid = None # string
    self_link = None # string
    labels = None # object

    def __init__(self, **_kwargs_):
        self.finalizers = []
        self.owner_references = []

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
class v1_PodTemplateSpec(Resource):

    """PodTemplateSpec describes the data a pod should have when created from
    a template"""

    __kind__ = 'v1.PodTemplateSpec'

    __fields__ = {
        'spec': 'spec',
        'metadata': 'metadata',
    }

    __types__ = {
        'spec': 'v1.PodSpec',
        'metadata': 'v1.ObjectMeta',
    }

    __required__ = set()

    spec = None # v1.PodSpec
    metadata = None # v1.ObjectMeta

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_PersistentVolumeClaimStatus(Resource):

    """PersistentVolumeClaimStatus is the current status of a persistent
    volume claim."""

    __kind__ = 'v1.PersistentVolumeClaimStatus'

    __fields__ = {
        'capacity': 'capacity',
        'phase': 'phase',
        'access_modes': 'accessModes',
    }

    __types__ = {
        'access_modes': 'v1.PersistentVolumeAccessMode',
    }

    __required__ = set()

    capacity = None # object
    phase = None # string
    access_modes = None # array

    def __init__(self, **_kwargs_):
        self.access_modes = []

        super().__init__(**_kwargs_)

@register_model
class v1_SELinuxContextStrategyOptions(Resource):

    """SELinuxContextStrategyOptions defines the strategy type and any
    options used to create the strategy."""

    __kind__ = 'v1.SELinuxContextStrategyOptions'

    __fields__ = {
        'type': 'type',
        'se_linux_options': 'seLinuxOptions',
    }

    __types__ = {
        'se_linux_options': 'v1.SELinuxOptions',
    }

    __required__ = set()

    type = None # string
    se_linux_options = None # v1.SELinuxOptions

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_EndpointPort(Resource):

    """EndpointPort is a tuple that describes a single port."""

    __kind__ = 'v1.EndpointPort'

    __fields__ = {
        'port': 'port',
        'protocol': 'protocol',
        'name': 'name',
    }

    __types__ = {
    }

    __required__ = set([
        'port',
    ])

    port = None # integer (required)
    protocol = None # string
    name = None # string

    def __init__(self, *, port, **_kwargs_):

        self.port = port

        super().__init__(**_kwargs_)

@register_model
class v1_Node(Resource):

    """Node is a worker node in Kubernetes, formerly known as minion. Each
    node will have a unique identifier in the cache (i.e. in etcd)."""

    __kind__ = 'v1.Node'

    __fields__ = {
        'status': 'status',
        'spec': 'spec',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'status': 'v1.NodeStatus',
        'spec': 'v1.NodeSpec',
        'metadata': 'v1.ObjectMeta',
    }

    __required__ = set()

    status = None # v1.NodeStatus
    spec = None # v1.NodeSpec
    api_version = None # string
    metadata = None # v1.ObjectMeta
    kind = None # string

    def __init__(self, **_kwargs_):

        self.kind = 'ObjectMeta'

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
class v1_LimitRange(Resource):

    """LimitRange sets resource usage limits for each kind of resource in a
    Namespace."""

    __kind__ = 'v1.LimitRange'

    __fields__ = {
        'spec': 'spec',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'spec': 'v1.LimitRangeSpec',
        'metadata': 'v1.ObjectMeta',
    }

    __required__ = set()

    spec = None # v1.LimitRangeSpec
    api_version = None # string
    metadata = None # v1.ObjectMeta
    kind = None # string

    def __init__(self, **_kwargs_):

        self.kind = 'ObjectMeta'

        super().__init__(**_kwargs_)

@register_model
class v1_SecurityContextConstraintsList(Resource):

    """SecurityContextConstraintsList is a list of SecurityContextConstraints
    objects"""

    __kind__ = 'v1.SecurityContextConstraintsList'

    __fields__ = {
        'items': 'items',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'unversioned.ListMeta',
        'items': 'v1.SecurityContextConstraints',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    api_version = None # string
    metadata = None # unversioned.ListMeta
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'SecurityContextConstraints'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_NodeList(Resource):

    """NodeList is the whole list of all Nodes which have been registered
    with master."""

    __kind__ = 'v1.NodeList'

    __fields__ = {
        'items': 'items',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'unversioned.ListMeta',
        'items': 'v1.Node',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    api_version = None # string
    metadata = None # unversioned.ListMeta
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'Node'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_PersistentVolumeClaim(Resource):

    """PersistentVolumeClaim is a user's request for and claim to a
    persistent volume"""

    __kind__ = 'v1.PersistentVolumeClaim'

    __fields__ = {
        'status': 'status',
        'spec': 'spec',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'status': 'v1.PersistentVolumeClaimStatus',
        'spec': 'v1.PersistentVolumeClaimSpec',
        'metadata': 'v1.ObjectMeta',
    }

    __required__ = set()

    status = None # v1.PersistentVolumeClaimStatus
    spec = None # v1.PersistentVolumeClaimSpec
    api_version = None # string
    metadata = None # v1.ObjectMeta
    kind = None # string

    def __init__(self, **_kwargs_):

        self.kind = 'ObjectMeta'

        super().__init__(**_kwargs_)

@register_model
class v1_EventList(Resource):

    """EventList is a list of events."""

    __kind__ = 'v1.EventList'

    __fields__ = {
        'items': 'items',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'unversioned.ListMeta',
        'items': 'v1.Event',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    api_version = None # string
    metadata = None # unversioned.ListMeta
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'Event'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_PersistentVolumeSpec(Resource):

    """PersistentVolumeSpec is the specification of a persistent volume."""

    __kind__ = 'v1.PersistentVolumeSpec'

    __fields__ = {
        'cinder': 'cinder',
        'nfs': 'nfs',
        'host_path': 'hostPath',
        'fc': 'fc',
        'iscsi': 'iscsi',
        'gce_persistent_disk': 'gcePersistentDisk',
        'cephfs': 'cephfs',
        'access_modes': 'accessModes',
        'vsphere_volume': 'vsphereVolume',
        'aws_elastic_block_store': 'awsElasticBlockStore',
        'azure_file': 'azureFile',
        'rbd': 'rbd',
        'glusterfs': 'glusterfs',
        'flex_volume': 'flexVolume',
        'persistent_volume_reclaim_policy': 'persistentVolumeReclaimPolicy',
        'capacity': 'capacity',
        'claim_ref': 'claimRef',
        'flocker': 'flocker',
    }

    __types__ = {
        'cinder': 'v1.CinderVolumeSource',
        'nfs': 'v1.NFSVolumeSource',
        'host_path': 'v1.HostPathVolumeSource',
        'fc': 'v1.FCVolumeSource',
        'iscsi': 'v1.ISCSIVolumeSource',
        'claim_ref': 'v1.ObjectReference',
        'cephfs': 'v1.CephFSVolumeSource',
        'access_modes': 'v1.PersistentVolumeAccessMode',
        'vsphere_volume': 'v1.VsphereVirtualDiskVolumeSource',
        'aws_elastic_block_store': 'v1.AWSElasticBlockStoreVolumeSource',
        'azure_file': 'v1.AzureFileVolumeSource',
        'rbd': 'v1.RBDVolumeSource',
        'glusterfs': 'v1.GlusterfsVolumeSource',
        'flex_volume': 'v1.FlexVolumeSource',
        'gce_persistent_disk': 'v1.GCEPersistentDiskVolumeSource',
        'flocker': 'v1.FlockerVolumeSource',
    }

    __required__ = set()

    cinder = None # v1.CinderVolumeSource
    nfs = None # v1.NFSVolumeSource
    host_path = None # v1.HostPathVolumeSource
    fc = None # v1.FCVolumeSource
    iscsi = None # v1.ISCSIVolumeSource
    gce_persistent_disk = None # v1.GCEPersistentDiskVolumeSource
    cephfs = None # v1.CephFSVolumeSource
    access_modes = None # array
    vsphere_volume = None # v1.VsphereVirtualDiskVolumeSource
    aws_elastic_block_store = None # v1.AWSElasticBlockStoreVolumeSource
    azure_file = None # v1.AzureFileVolumeSource
    rbd = None # v1.RBDVolumeSource
    glusterfs = None # v1.GlusterfsVolumeSource
    flex_volume = None # v1.FlexVolumeSource
    persistent_volume_reclaim_policy = None # string
    capacity = None # object
    claim_ref = None # v1.ObjectReference
    flocker = None # v1.FlockerVolumeSource

    def __init__(self, **_kwargs_):
        self.access_modes = []

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
class v1_PersistentVolumeClaimSpec(Resource):

    """PersistentVolumeClaimSpec describes the common attributes of storage
    devices and allows a Source for provider-specific attributes"""

    __kind__ = 'v1.PersistentVolumeClaimSpec'

    __fields__ = {
        'volume_name': 'volumeName',
        'selector': 'selector',
        'resources': 'resources',
        'access_modes': 'accessModes',
    }

    __types__ = {
        'resources': 'v1.ResourceRequirements',
        'selector': 'unversioned.LabelSelector',
    }

    __required__ = set()

    volume_name = None # string
    selector = None # unversioned.LabelSelector
    resources = None # v1.ResourceRequirements
    access_modes = None # array

    def __init__(self, **_kwargs_):
        self.access_modes = []

        super().__init__(**_kwargs_)

@register_model
class v1_ContainerImage(Resource):

    """Describe a container image"""

    __kind__ = 'v1.ContainerImage'

    __fields__ = {
        'size_bytes': 'sizeBytes',
        'names': 'names',
    }

    __types__ = {
    }

    __required__ = set([
        'names',
    ])

    size_bytes = None # integer
    names = None # array (required)

    def __init__(self, *, names, **_kwargs_):

        self.names = names

        super().__init__(**_kwargs_)

@register_model
class v1_GitRepoVolumeSource(Resource):

    """Represents a volume that is populated with the contents of a git
    repository. Git repo volumes do not support ownership management.
    Git repo volumes support SELinux relabeling."""

    __kind__ = 'v1.GitRepoVolumeSource'

    __fields__ = {
        'directory': 'directory',
        'repository': 'repository',
        'revision': 'revision',
    }

    __types__ = {
    }

    __required__ = set([
        'repository',
    ])

    directory = None # string
    repository = None # string (required)
    revision = None # string

    def __init__(self, *, repository, **_kwargs_):

        self.repository = repository

        super().__init__(**_kwargs_)

@register_model
class v1_NodeSystemInfo(Resource):

    """NodeSystemInfo is a set of ids/uuids to uniquely identify the node."""

    __kind__ = 'v1.NodeSystemInfo'

    __fields__ = {
        'os_image': 'osImage',
        'boot_id': 'bootID',
        'kube_proxy_version': 'kubeProxyVersion',
        'container_runtime_version': 'containerRuntimeVersion',
        'operating_system': 'operatingSystem',
        'kubelet_version': 'kubeletVersion',
        'system_uuid': 'systemUUID',
        'architecture': 'architecture',
        'kernel_version': 'kernelVersion',
        'machine_id': 'machineID',
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

    os_image = None # string (required)
    boot_id = None # string (required)
    kube_proxy_version = None # string (required)
    container_runtime_version = None # string (required)
    operating_system = None # string (required)
    kubelet_version = None # string (required)
    system_uuid = None # string (required)
    architecture = None # string (required)
    kernel_version = None # string (required)
    machine_id = None # string (required)

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
class v1_SecurityContextConstraints(Resource):

    """SecurityContextConstraints governs the ability to make requests that
    affect the SecurityContext that will be applied to a container."""

    __kind__ = 'v1.SecurityContextConstraints'

    __fields__ = {
        'allow_host_pid': 'allowHostPID',
        'seccomp_profiles': 'seccompProfiles',
        'allow_host_network': 'allowHostNetwork',
        'se_linux_context': 'seLinuxContext',
        'groups': 'groups',
        'volumes': 'volumes',
        'allow_host_ports': 'allowHostPorts',
        'users': 'users',
        'default_add_capabilities': 'defaultAddCapabilities',
        'fs_group': 'fsGroup',
        'required_drop_capabilities': 'requiredDropCapabilities',
        'allow_host_ipc': 'allowHostIPC',
        'supplemental_groups': 'supplementalGroups',
        'read_only_root_filesystem': 'readOnlyRootFilesystem',
        'metadata': 'metadata',
        'allow_privileged_container': 'allowPrivilegedContainer',
        'allowed_capabilities': 'allowedCapabilities',
        'priority': 'priority',
        'api_version': 'apiVersion',
        'run_as_user': 'runAsUser',
        'kind': 'kind',
        'allow_host_dir_volume_plugin': 'allowHostDirVolumePlugin',
    }

    __types__ = {
        'volumes': 'v1.FSType',
        'metadata': 'v1.ObjectMeta',
        'required_drop_capabilities': 'v1.Capability',
        'fs_group': 'v1.FSGroupStrategyOptions',
        'allowed_capabilities': 'v1.Capability',
        'default_add_capabilities': 'v1.Capability',
        'supplemental_groups': 'v1.SupplementalGroupsStrategyOptions',
        'se_linux_context': 'v1.SELinuxContextStrategyOptions',
        'run_as_user': 'v1.RunAsUserStrategyOptions',
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

    allow_host_pid = None # boolean (required)
    seccomp_profiles = None # array
    allow_host_network = None # boolean (required)
    se_linux_context = None # v1.SELinuxContextStrategyOptions
    groups = None # array
    volumes = None # array (required)
    allow_host_ports = None # boolean (required)
    users = None # array
    default_add_capabilities = None # array (required)
    fs_group = None # v1.FSGroupStrategyOptions
    required_drop_capabilities = None # array (required)
    allow_host_ipc = None # boolean (required)
    supplemental_groups = None # v1.SupplementalGroupsStrategyOptions
    read_only_root_filesystem = None # boolean (required)
    metadata = None # v1.ObjectMeta
    allow_privileged_container = None # boolean (required)
    allowed_capabilities = None # array (required)
    priority = None # integer (required)
    api_version = None # string
    run_as_user = None # v1.RunAsUserStrategyOptions
    kind = None # string
    allow_host_dir_volume_plugin = None # boolean (required)

    def __init__(self, *, allow_host_dir_volume_plugin, allow_host_ipc, allow_host_network, allow_host_pid, allow_host_ports, allow_privileged_container, allowed_capabilities, default_add_capabilities, priority, read_only_root_filesystem, required_drop_capabilities, volumes, **_kwargs_):
        self.seccomp_profiles = []
        self.groups = []
        self.users = []

        self.kind = 'RunAsUserStrategyOptions'

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
class v1_ReplicationController(Resource):

    """ReplicationController represents the configuration of a replication
    controller."""

    __kind__ = 'v1.ReplicationController'

    __fields__ = {
        'status': 'status',
        'spec': 'spec',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'status': 'v1.ReplicationControllerStatus',
        'spec': 'v1.ReplicationControllerSpec',
        'metadata': 'v1.ObjectMeta',
    }

    __required__ = set()

    status = None # v1.ReplicationControllerStatus
    spec = None # v1.ReplicationControllerSpec
    api_version = None # string
    metadata = None # v1.ObjectMeta
    kind = None # string

    def __init__(self, **_kwargs_):

        self.kind = 'ObjectMeta'

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
        'tcp_socket': 'v1.TCPSocketAction',
        'exec': 'v1.ExecAction',
    }

    __required__ = set()

    http_get = None # v1.HTTPGetAction
    tcp_socket = None # v1.TCPSocketAction
    exec = None # v1.ExecAction

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_Namespace(Resource):

    """Namespace provides a scope for Names. Use of multiple namespaces is
    optional."""

    __kind__ = 'v1.Namespace'

    __fields__ = {
        'status': 'status',
        'spec': 'spec',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'status': 'v1.NamespaceStatus',
        'spec': 'v1.NamespaceSpec',
        'metadata': 'v1.ObjectMeta',
    }

    __required__ = set()

    status = None # v1.NamespaceStatus
    spec = None # v1.NamespaceSpec
    api_version = None # string
    metadata = None # v1.ObjectMeta
    kind = None # string

    def __init__(self, **_kwargs_):

        self.kind = 'ObjectMeta'

        super().__init__(**_kwargs_)

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
class v1_Probe(Resource):

    """Probe describes a health check to be performed against a container to
    determine whether it is alive or ready to receive traffic."""

    __kind__ = 'v1.Probe'

    __fields__ = {
        'initial_delay_seconds': 'initialDelaySeconds',
        'success_threshold': 'successThreshold',
        'period_seconds': 'periodSeconds',
        'http_get': 'httpGet',
        'failure_threshold': 'failureThreshold',
        'tcp_socket': 'tcpSocket',
        'timeout_seconds': 'timeoutSeconds',
        'exec': 'exec',
    }

    __types__ = {
        'http_get': 'v1.HTTPGetAction',
        'tcp_socket': 'v1.TCPSocketAction',
        'exec': 'v1.ExecAction',
    }

    __required__ = set()

    initial_delay_seconds = None # integer
    success_threshold = None # integer
    period_seconds = None # integer
    http_get = None # v1.HTTPGetAction
    failure_threshold = None # integer
    tcp_socket = None # v1.TCPSocketAction
    timeout_seconds = None # integer
    exec = None # v1.ExecAction

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_ServicePort(Resource):

    """ServicePort contains information on service's port."""

    __kind__ = 'v1.ServicePort'

    __fields__ = {
        'target_port': 'targetPort',
        'port': 'port',
        'protocol': 'protocol',
        'name': 'name',
        'node_port': 'nodePort',
    }

    __types__ = {
    }

    __required__ = set([
        'port',
    ])

    target_port = None # string
    port = None # integer (required)
    protocol = None # string
    name = None # string
    node_port = None # integer

    def __init__(self, *, port, **_kwargs_):

        self.port = port

        super().__init__(**_kwargs_)

@register_model
class v1_ServiceAccountList(Resource):

    """ServiceAccountList is a list of ServiceAccount objects"""

    __kind__ = 'v1.ServiceAccountList'

    __fields__ = {
        'items': 'items',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'unversioned.ListMeta',
        'items': 'v1.ServiceAccount',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    api_version = None # string
    metadata = None # unversioned.ListMeta
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'ServiceAccount'

        self.items = items

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
class v1_NodeStatus(Resource):

    """NodeStatus is information about the current status of a node."""

    __kind__ = 'v1.NodeStatus'

    __fields__ = {
        'images': 'images',
        'volumes_attached': 'volumesAttached',
        'daemon_endpoints': 'daemonEndpoints',
        'node_info': 'nodeInfo',
        'phase': 'phase',
        'volumes_in_use': 'volumesInUse',
        'capacity': 'capacity',
        'conditions': 'conditions',
        'allocatable': 'allocatable',
        'addresses': 'addresses',
    }

    __types__ = {
        'volumes_attached': 'v1.AttachedVolume',
        'daemon_endpoints': 'v1.NodeDaemonEndpoints',
        'conditions': 'v1.NodeCondition',
        'volumes_in_use': 'v1.UniqueVolumeName',
        'images': 'v1.ContainerImage',
        'node_info': 'v1.NodeSystemInfo',
        'addresses': 'v1.NodeAddress',
    }

    __required__ = set()

    images = None # array
    volumes_attached = None # array
    daemon_endpoints = None # v1.NodeDaemonEndpoints
    node_info = None # v1.NodeSystemInfo
    phase = None # string
    volumes_in_use = None # array
    capacity = None # object
    conditions = None # array
    allocatable = None # object
    addresses = None # array

    def __init__(self, **_kwargs_):
        self.images = []
        self.volumes_attached = []
        self.volumes_in_use = []
        self.conditions = []
        self.addresses = []

        super().__init__(**_kwargs_)

@register_model
class v1_NodeSpec(Resource):

    """NodeSpec describes the attributes that a node is created with."""

    __kind__ = 'v1.NodeSpec'

    __fields__ = {
        'pod_cidr': 'podCIDR',
        'external_id': 'externalID',
        'unschedulable': 'unschedulable',
        'provider_id': 'providerID',
    }

    __types__ = {
    }

    __required__ = set()

    pod_cidr = None # string
    external_id = None # string
    unschedulable = None # boolean
    provider_id = None # string

    def __init__(self, **_kwargs_):

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
class v1_SupplementalGroupsStrategyOptions(Resource):

    """SupplementalGroupsStrategyOptions defines the strategy type and
    options used to create the strategy."""

    __kind__ = 'v1.SupplementalGroupsStrategyOptions'

    __fields__ = {
        'ranges': 'ranges',
        'type': 'type',
    }

    __types__ = {
        'ranges': 'v1.IDRange',
    }

    __required__ = set()

    ranges = None # array
    type = None # string

    def __init__(self, **_kwargs_):
        self.ranges = []

        super().__init__(**_kwargs_)

@register_model
class v1_EnvVarSource(Resource):

    """EnvVarSource represents a source for the value of an EnvVar."""

    __kind__ = 'v1.EnvVarSource'

    __fields__ = {
        'resource_field_ref': 'resourceFieldRef',
        'secret_key_ref': 'secretKeyRef',
        'config_map_key_ref': 'configMapKeyRef',
        'field_ref': 'fieldRef',
    }

    __types__ = {
        'resource_field_ref': 'v1.ResourceFieldSelector',
        'secret_key_ref': 'v1.SecretKeySelector',
        'config_map_key_ref': 'v1.ConfigMapKeySelector',
        'field_ref': 'v1.ObjectFieldSelector',
    }

    __required__ = set()

    resource_field_ref = None # v1.ResourceFieldSelector
    secret_key_ref = None # v1.SecretKeySelector
    config_map_key_ref = None # v1.ConfigMapKeySelector
    field_ref = None # v1.ObjectFieldSelector

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_AzureFileVolumeSource(Resource):

    """AzureFile represents an Azure File Service mount on the host and bind
    mount to the pod."""

    __kind__ = 'v1.AzureFileVolumeSource'

    __fields__ = {
        'read_only': 'readOnly',
        'secret_name': 'secretName',
        'share_name': 'shareName',
    }

    __types__ = {
    }

    __required__ = set([
        'secret_name',
        'share_name',
    ])

    read_only = None # boolean
    secret_name = None # string (required)
    share_name = None # string (required)

    def __init__(self, *, secret_name, share_name, **_kwargs_):

        self.secret_name = secret_name
        self.share_name = share_name

        super().__init__(**_kwargs_)

@register_model
class v1_CephFSVolumeSource(Resource):

    """Represents a Ceph Filesystem mount that lasts the lifetime of a pod
    Cephfs volumes do not support ownership management or SELinux
    relabeling."""

    __kind__ = 'v1.CephFSVolumeSource'

    __fields__ = {
        'path': 'path',
        'secret_file': 'secretFile',
        'monitors': 'monitors',
        'read_only': 'readOnly',
        'secret_ref': 'secretRef',
        'user': 'user',
    }

    __types__ = {
        'secret_ref': 'v1.LocalObjectReference',
    }

    __required__ = set([
        'monitors',
    ])

    path = None # string
    secret_file = None # string
    monitors = None # array (required)
    read_only = None # boolean
    secret_ref = None # v1.LocalObjectReference
    user = None # string

    def __init__(self, *, monitors, **_kwargs_):

        self.monitors = monitors

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
class v1_ComponentCondition(Resource):

    """Information about the condition of a component."""

    __kind__ = 'v1.ComponentCondition'

    __fields__ = {
        'status': 'status',
        'message': 'message',
        'type': 'type',
        'error': 'error',
    }

    __types__ = {
    }

    __required__ = set([
        'status',
        'type',
    ])

    status = None # string (required)
    message = None # string
    type = None # string (required)
    error = None # string

    def __init__(self, *, status, type, **_kwargs_):

        self.status = status
        self.type = type

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
class unversioned_LabelSelector(Resource):

    """A label selector is a label query over a set of resources. The result
    of matchLabels and matchExpressions are ANDed. An empty label
    selector matches all objects. A null label selector matches no
    objects."""

    __kind__ = 'unversioned.LabelSelector'

    __fields__ = {
        'match_labels': 'matchLabels',
        'match_expressions': 'matchExpressions',
    }

    __types__ = {
        'match_expressions': 'unversioned.LabelSelectorRequirement',
    }

    __required__ = set()

    match_labels = None # object
    match_expressions = None # array

    def __init__(self, **_kwargs_):
        self.match_expressions = []

        super().__init__(**_kwargs_)

@register_model
class v1_NodeCondition(Resource):

    """NodeCondition contains condition infromation for a node."""

    __kind__ = 'v1.NodeCondition'

    __fields__ = {
        'last_heartbeat_time': 'lastHeartbeatTime',
        'message': 'message',
        'reason': 'reason',
        'type': 'type',
        'status': 'status',
        'last_transition_time': 'lastTransitionTime',
    }

    __types__ = {
    }

    __required__ = set([
        'status',
        'type',
    ])

    last_heartbeat_time = None # string
    message = None # string
    reason = None # string
    type = None # string (required)
    status = None # string (required)
    last_transition_time = None # string

    def __init__(self, *, status, type, **_kwargs_):

        self.status = status
        self.type = type

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
class v1_PersistentVolumeList(Resource):

    """PersistentVolumeList is a list of PersistentVolume items."""

    __kind__ = 'v1.PersistentVolumeList'

    __fields__ = {
        'items': 'items',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'unversioned.ListMeta',
        'items': 'v1.PersistentVolume',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    api_version = None # string
    metadata = None # unversioned.ListMeta
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'PersistentVolume'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_ResourceFieldSelector(Resource):

    """ResourceFieldSelector represents container resources (cpu, memory) and
    their output format"""

    __kind__ = 'v1.ResourceFieldSelector'

    __fields__ = {
        'container_name': 'containerName',
        'resource': 'resource',
        'divisor': 'divisor',
    }

    __types__ = {
    }

    __required__ = set([
        'resource',
    ])

    container_name = None # string
    resource = None # string (required)
    divisor = None # string

    def __init__(self, *, resource, **_kwargs_):

        self.resource = resource

        super().__init__(**_kwargs_)

@register_model
class v1_FSGroupStrategyOptions(Resource):

    """FSGroupStrategyOptions defines the strategy type and options used to
    create the strategy."""

    __kind__ = 'v1.FSGroupStrategyOptions'

    __fields__ = {
        'ranges': 'ranges',
        'type': 'type',
    }

    __types__ = {
        'ranges': 'v1.IDRange',
    }

    __required__ = set()

    ranges = None # array
    type = None # string

    def __init__(self, **_kwargs_):
        self.ranges = []

        super().__init__(**_kwargs_)

@register_model
class v1_PodStatus(Resource):

    """PodStatus represents information about the status of a pod. Status may
    trail the actual state of a system."""

    __kind__ = 'v1.PodStatus'

    __fields__ = {
        'message': 'message',
        'reason': 'reason',
        'pod_ip': 'podIP',
        'phase': 'phase',
        'start_time': 'startTime',
        'container_statuses': 'containerStatuses',
        'host_ip': 'hostIP',
        'conditions': 'conditions',
    }

    __types__ = {
        'conditions': 'v1.PodCondition',
        'container_statuses': 'v1.ContainerStatus',
    }

    __required__ = set()

    message = None # string
    reason = None # string
    pod_ip = None # string
    phase = None # string
    start_time = None # string
    container_statuses = None # array
    host_ip = None # string
    conditions = None # array

    def __init__(self, **_kwargs_):
        self.container_statuses = []
        self.conditions = []

        super().__init__(**_kwargs_)

@register_model
class v1_NamespaceList(Resource):

    """NamespaceList is a list of Namespaces."""

    __kind__ = 'v1.NamespaceList'

    __fields__ = {
        'items': 'items',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'unversioned.ListMeta',
        'items': 'v1.Namespace',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    api_version = None # string
    metadata = None # unversioned.ListMeta
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'Namespace'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_ObjectFieldSelector(Resource):

    """ObjectFieldSelector selects an APIVersioned field of an object."""

    __kind__ = 'v1.ObjectFieldSelector'

    __fields__ = {
        'api_version': 'apiVersion',
        'field_path': 'fieldPath',
    }

    __types__ = {
    }

    __required__ = set([
        'field_path',
    ])

    api_version = None # string
    field_path = None # string (required)

    def __init__(self, *, field_path, **_kwargs_):

        self.field_path = field_path

        super().__init__(**_kwargs_)

@register_model
class v1_PodList(Resource):

    """PodList is a list of Pods."""

    __kind__ = 'v1.PodList'

    __fields__ = {
        'items': 'items',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'unversioned.ListMeta',
        'items': 'v1.Pod',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    api_version = None # string
    metadata = None # unversioned.ListMeta
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'Pod'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_PodTemplateList(Resource):

    """PodTemplateList is a list of PodTemplates."""

    __kind__ = 'v1.PodTemplateList'

    __fields__ = {
        'items': 'items',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'unversioned.ListMeta',
        'items': 'v1.PodTemplate',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    api_version = None # string
    metadata = None # unversioned.ListMeta
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'PodTemplate'

        self.items = items

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
        'kind': 'kind',
        'group_version': 'groupVersion',
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
    kind = None # string
    group_version = None # string (required)

    def __init__(self, *, group_version, resources, **_kwargs_):

        self.kind = 'APIResource'

        self.group_version = group_version
        self.resources = resources

        super().__init__(**_kwargs_)

@register_model
class v1_PersistentVolume(Resource):

    """PersistentVolume (PV) is a storage resource provisioned by an
    administrator. It is analogous to a node. More info:
    http://releases.k8s.io/release-1.3/docs/user-guide/persistent-
    volumes.md"""

    __kind__ = 'v1.PersistentVolume'

    __fields__ = {
        'status': 'status',
        'spec': 'spec',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'status': 'v1.PersistentVolumeStatus',
        'spec': 'v1.PersistentVolumeSpec',
        'metadata': 'v1.ObjectMeta',
    }

    __required__ = set()

    status = None # v1.PersistentVolumeStatus
    spec = None # v1.PersistentVolumeSpec
    api_version = None # string
    metadata = None # v1.ObjectMeta
    kind = None # string

    def __init__(self, **_kwargs_):

        self.kind = 'ObjectMeta'

        super().__init__(**_kwargs_)

@register_model
class v1_Binding(Resource):

    """Binding ties one object to another. For example, a pod is bound to a
    node by a scheduler."""

    __kind__ = 'v1.Binding'

    __fields__ = {
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'target': 'target',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
        'target': 'v1.ObjectReference',
    }

    __required__ = set([
        'target',
    ])

    api_version = None # string
    metadata = None # v1.ObjectMeta
    target = None # v1.ObjectReference (required)
    kind = None # string

    def __init__(self, *, target, **_kwargs_):

        self.kind = 'ObjectReference'

        self.target = target

        super().__init__(**_kwargs_)

@register_model
class v1_Event(Resource):

    """Event is a report of an event somewhere in the cluster."""

    __kind__ = 'v1.Event'

    __fields__ = {
        'message': 'message',
        'first_timestamp': 'firstTimestamp',
        'reason': 'reason',
        'metadata': 'metadata',
        'type': 'type',
        'kind': 'kind',
        'api_version': 'apiVersion',
        'last_timestamp': 'lastTimestamp',
        'count': 'count',
        'involved_object': 'involvedObject',
        'source': 'source',
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

    message = None # string
    first_timestamp = None # string
    reason = None # string
    metadata = None # v1.ObjectMeta (required)
    type = None # string
    kind = None # string
    api_version = None # string
    last_timestamp = None # string
    count = None # integer
    involved_object = None # v1.ObjectReference (required)
    source = None # v1.EventSource

    def __init__(self, *, involved_object, metadata, **_kwargs_):

        self.kind = 'ObjectReference'

        self.involved_object = involved_object
        self.metadata = metadata

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
        'volume_id': 'volumeID',
        'read_only': 'readOnly',
        'fs_type': 'fsType',
        'partition': 'partition',
    }

    __types__ = {
    }

    __required__ = set([
        'volume_id',
    ])

    volume_id = None # string (required)
    read_only = None # boolean
    fs_type = None # string
    partition = None # integer

    def __init__(self, *, volume_id, **_kwargs_):

        self.volume_id = volume_id

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
class v1_ServiceAccount(Resource):

    """ServiceAccount binds together: * a name, understood by users, and
    perhaps by peripheral systems, for an identity * a principal that
    can be authenticated and authorized * a set of secrets"""

    __kind__ = 'v1.ServiceAccount'

    __fields__ = {
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'secrets': 'secrets',
        'kind': 'kind',
        'image_pull_secrets': 'imagePullSecrets',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
        'image_pull_secrets': 'v1.LocalObjectReference',
        'secrets': 'v1.ObjectReference',
    }

    __required__ = set()

    api_version = None # string
    metadata = None # v1.ObjectMeta
    secrets = None # array
    kind = None # string
    image_pull_secrets = None # array

    def __init__(self, **_kwargs_):
        self.secrets = []
        self.image_pull_secrets = []

        self.kind = 'ObjectReference'

        super().__init__(**_kwargs_)

@register_model
class v1_HTTPGetAction(Resource):

    """HTTPGetAction describes an action based on HTTP Get requests."""

    __kind__ = 'v1.HTTPGetAction'

    __fields__ = {
        'path': 'path',
        'host': 'host',
        'scheme': 'scheme',
        'http_headers': 'httpHeaders',
        'port': 'port',
    }

    __types__ = {
        'http_headers': 'v1.HTTPHeader',
    }

    __required__ = set([
        'port',
    ])

    path = None # string
    host = None # string
    scheme = None # string
    http_headers = None # array
    port = None # string (required)

    def __init__(self, *, port, **_kwargs_):
        self.http_headers = []

        self.port = port

        super().__init__(**_kwargs_)

@register_model
class v1_ContainerState(Resource):

    """ContainerState holds a possible state of container. Only one of its
    members may be specified. If none of them is specified, the
    default one is ContainerStateWaiting."""

    __kind__ = 'v1.ContainerState'

    __fields__ = {
        'running': 'running',
        'terminated': 'terminated',
        'waiting': 'waiting',
    }

    __types__ = {
        'running': 'v1.ContainerStateRunning',
        'terminated': 'v1.ContainerStateTerminated',
        'waiting': 'v1.ContainerStateWaiting',
    }

    __required__ = set()

    running = None # v1.ContainerStateRunning
    terminated = None # v1.ContainerStateTerminated
    waiting = None # v1.ContainerStateWaiting

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_ReplicationControllerList(Resource):

    """ReplicationControllerList is a collection of replication controllers."""

    __kind__ = 'v1.ReplicationControllerList'

    __fields__ = {
        'items': 'items',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'unversioned.ListMeta',
        'items': 'v1.ReplicationController',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    api_version = None # string
    metadata = None # unversioned.ListMeta
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'ReplicationController'

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
class unversioned_StatusDetails(Resource):

    """StatusDetails is a set of additional properties that MAY be set by the
    server to provide additional information about a response. The
    Reason field of a Status object defines what attributes will be
    set. Clients must ignore fields that do not match the defined type
    of each attribute, and should assume that any attribute may be
    empty, invalid, or under defined."""

    __kind__ = 'unversioned.StatusDetails'

    __fields__ = {
        'retry_after_seconds': 'retryAfterSeconds',
        'causes': 'causes',
        'group': 'group',
        'name': 'name',
        'kind': 'kind',
    }

    __types__ = {
        'causes': 'unversioned.StatusCause',
    }

    __required__ = set()

    retry_after_seconds = None # integer
    causes = None # array
    group = None # string
    name = None # string
    kind = None # string

    def __init__(self, **_kwargs_):
        self.causes = []

        self.kind = 'StatusCause'

        super().__init__(**_kwargs_)

@register_model
class v1_ServiceSpec(Resource):

    """ServiceSpec describes the attributes that a user creates on a service."""

    __kind__ = 'v1.ServiceSpec'

    __fields__ = {
        'external_i_ps': 'externalIPs',
        'portal_ip': 'portalIP',
        'ports': 'ports',
        'type': 'type',
        'load_balancer_ip': 'loadBalancerIP',
        'cluster_ip': 'clusterIP',
        'selector': 'selector',
        'load_balancer_source_ranges': 'loadBalancerSourceRanges',
        'deprecated_public_i_ps': 'deprecatedPublicIPs',
        'session_affinity': 'sessionAffinity',
    }

    __types__ = {
        'ports': 'v1.ServicePort',
    }

    __required__ = set([
        'ports',
    ])

    external_i_ps = None # array
    portal_ip = None # string
    ports = None # array (required)
    type = None # string
    load_balancer_ip = None # string
    cluster_ip = None # string
    selector = None # object
    load_balancer_source_ranges = None # array
    deprecated_public_i_ps = None # array
    session_affinity = None # string

    def __init__(self, *, ports, **_kwargs_):
        self.external_i_ps = []
        self.load_balancer_source_ranges = []
        self.deprecated_public_i_ps = []

        self.ports = ports

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
        'ports': 'ports',
        'not_ready_addresses': 'notReadyAddresses',
        'addresses': 'addresses',
    }

    __types__ = {
        'ports': 'v1.EndpointPort',
        'addresses': 'v1.EndpointAddress',
        'not_ready_addresses': 'v1.EndpointAddress',
    }

    __required__ = set()

    ports = None # array
    not_ready_addresses = None # array
    addresses = None # array

    def __init__(self, **_kwargs_):
        self.ports = []
        self.not_ready_addresses = []
        self.addresses = []

        super().__init__(**_kwargs_)

@register_model
class v1_VolumeMount(Resource):

    """VolumeMount describes a mounting of a Volume within a container."""

    __kind__ = 'v1.VolumeMount'

    __fields__ = {
        'mount_path': 'mountPath',
        'read_only': 'readOnly',
        'name': 'name',
        'sub_path': 'subPath',
    }

    __types__ = {
    }

    __required__ = set([
        'mount_path',
        'name',
    ])

    mount_path = None # string (required)
    read_only = None # boolean
    name = None # string (required)
    sub_path = None # string

    def __init__(self, *, mount_path, name, **_kwargs_):

        self.mount_path = mount_path
        self.name = name

        super().__init__(**_kwargs_)

@register_model
class v1_Scale(Resource):

    """Scale represents a scaling request for a resource."""

    __kind__ = 'v1.Scale'

    __fields__ = {
        'status': 'status',
        'spec': 'spec',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'status': 'v1.ScaleStatus',
        'spec': 'v1.ScaleSpec',
        'metadata': 'v1.ObjectMeta',
    }

    __required__ = set()

    status = None # v1.ScaleStatus
    spec = None # v1.ScaleSpec
    api_version = None # string
    metadata = None # v1.ObjectMeta
    kind = None # string

    def __init__(self, **_kwargs_):

        self.kind = 'ObjectMeta'

        super().__init__(**_kwargs_)

@register_model
class v1_SecretKeySelector(Resource):

    """SecretKeySelector selects a key of a Secret."""

    __kind__ = 'v1.SecretKeySelector'

    __fields__ = {
        'key': 'key',
        'name': 'name',
    }

    __types__ = {
    }

    __required__ = set([
        'key',
    ])

    key = None # string (required)
    name = None # string

    def __init__(self, *, key, **_kwargs_):

        self.key = key

        super().__init__(**_kwargs_)

@register_model
class v1_ComponentStatusList(Resource):

    """Status of all the conditions for the component as a list of
    ComponentStatus objects."""

    __kind__ = 'v1.ComponentStatusList'

    __fields__ = {
        'items': 'items',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'unversioned.ListMeta',
        'items': 'v1.ComponentStatus',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    api_version = None # string
    metadata = None # unversioned.ListMeta
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'ComponentStatus'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_LimitRangeList(Resource):

    """LimitRangeList is a list of LimitRange items."""

    __kind__ = 'v1.LimitRangeList'

    __fields__ = {
        'items': 'items',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'unversioned.ListMeta',
        'items': 'v1.LimitRange',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    api_version = None # string
    metadata = None # unversioned.ListMeta
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'LimitRange'

        self.items = items

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
class v1_LimitRangeItem(Resource):

    """LimitRangeItem defines a min/max usage limit for any resource that
    matches on kind."""

    __kind__ = 'v1.LimitRangeItem'

    __fields__ = {
        'default_request': 'defaultRequest',
        'default': 'default',
        'max': 'max',
        'type': 'type',
        'max_limit_request_ratio': 'maxLimitRequestRatio',
        'min': 'min',
    }

    __types__ = {
    }

    __required__ = set()

    default_request = None # object
    default = None # object
    max = None # object
    type = None # string
    max_limit_request_ratio = None # object
    min = None # object

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_RBDVolumeSource(Resource):

    """Represents a Rados Block Device mount that lasts the lifetime of a
    pod. RBD volumes support ownership management and SELinux
    relabeling."""

    __kind__ = 'v1.RBDVolumeSource'

    __fields__ = {
        'image': 'image',
        'keyring': 'keyring',
        'monitors': 'monitors',
        'read_only': 'readOnly',
        'fs_type': 'fsType',
        'secret_ref': 'secretRef',
        'user': 'user',
        'pool': 'pool',
    }

    __types__ = {
        'secret_ref': 'v1.LocalObjectReference',
    }

    __required__ = set([
        'image',
        'monitors',
    ])

    image = None # string (required)
    keyring = None # string
    monitors = None # array (required)
    read_only = None # boolean
    fs_type = None # string
    secret_ref = None # v1.LocalObjectReference
    user = None # string
    pool = None # string

    def __init__(self, *, image, monitors, **_kwargs_):

        self.image = image
        self.monitors = monitors

        super().__init__(**_kwargs_)

@register_model
class v1_DownwardAPIVolumeFile(Resource):

    """DownwardAPIVolumeFile represents information to create the file
    containing the pod field"""

    __kind__ = 'v1.DownwardAPIVolumeFile'

    __fields__ = {
        'path': 'path',
        'resource_field_ref': 'resourceFieldRef',
        'field_ref': 'fieldRef',
    }

    __types__ = {
        'resource_field_ref': 'v1.ResourceFieldSelector',
        'field_ref': 'v1.ObjectFieldSelector',
    }

    __required__ = set([
        'path',
    ])

    path = None # string (required)
    resource_field_ref = None # v1.ResourceFieldSelector
    field_ref = None # v1.ObjectFieldSelector

    def __init__(self, *, path, **_kwargs_):

        self.path = path

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
class unversioned_Status(Resource):

    """Status is a return value for calls that don't return other objects."""

    __kind__ = 'unversioned.Status'

    __fields__ = {
        'message': 'message',
        'reason': 'reason',
        'metadata': 'metadata',
        'details': 'details',
        'status': 'status',
        'api_version': 'apiVersion',
        'code': 'code',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'unversioned.ListMeta',
        'details': 'unversioned.StatusDetails',
    }

    __required__ = set()

    message = None # string
    reason = None # string
    metadata = None # unversioned.ListMeta
    details = None # unversioned.StatusDetails
    status = None # string
    api_version = None # string
    code = None # integer
    kind = None # string

    def __init__(self, **_kwargs_):

        self.kind = 'StatusDetails'

        super().__init__(**_kwargs_)

@register_model
class v1_HTTPHeader(Resource):

    """HTTPHeader describes a custom header to be used in HTTP probes"""

    __kind__ = 'v1.HTTPHeader'

    __fields__ = {
        'value': 'value',
        'name': 'name',
    }

    __types__ = {
    }

    __required__ = set([
        'name',
        'value',
    ])

    value = None # string (required)
    name = None # string (required)

    def __init__(self, *, name, value, **_kwargs_):

        self.name = name
        self.value = value

        super().__init__(**_kwargs_)

@register_model
class v1_ResourceQuotaStatus(Resource):

    """ResourceQuotaStatus defines the enforced hard limits and observed use."""

    __kind__ = 'v1.ResourceQuotaStatus'

    __fields__ = {
        'used': 'used',
        'hard': 'hard',
    }

    __types__ = {
    }

    __required__ = set()

    used = None # object
    hard = None # object

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_SecretList(Resource):

    """SecretList is a list of Secret."""

    __kind__ = 'v1.SecretList'

    __fields__ = {
        'items': 'items',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'unversioned.ListMeta',
        'items': 'v1.Secret',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    api_version = None # string
    metadata = None # unversioned.ListMeta
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'Secret'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_ResourceQuotaSpec(Resource):

    """ResourceQuotaSpec defines the desired hard limits to enforce for
    Quota."""

    __kind__ = 'v1.ResourceQuotaSpec'

    __fields__ = {
        'scopes': 'scopes',
        'hard': 'hard',
    }

    __types__ = {
        'scopes': 'v1.ResourceQuotaScope',
    }

    __required__ = set()

    scopes = None # array
    hard = None # object

    def __init__(self, **_kwargs_):
        self.scopes = []

        super().__init__(**_kwargs_)

@register_model
class v1_RunAsUserStrategyOptions(Resource):

    """RunAsUserStrategyOptions defines the strategy type and any options
    used to create the strategy."""

    __kind__ = 'v1.RunAsUserStrategyOptions'

    __fields__ = {
        'uid_range_max': 'uidRangeMax',
        'uid_range_min': 'uidRangeMin',
        'type': 'type',
        'uid': 'uid',
    }

    __types__ = {
    }

    __required__ = set()

    uid_range_max = None # integer
    uid_range_min = None # integer
    type = None # string
    uid = None # integer

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_ResourceQuotaList(Resource):

    """ResourceQuotaList is a list of ResourceQuota items."""

    __kind__ = 'v1.ResourceQuotaList'

    __fields__ = {
        'items': 'items',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'unversioned.ListMeta',
        'items': 'v1.ResourceQuota',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    api_version = None # string
    metadata = None # unversioned.ListMeta
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'ResourceQuota'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_PodTemplate(Resource):

    """PodTemplate describes a template for creating copies of a predefined
    pod."""

    __kind__ = 'v1.PodTemplate'

    __fields__ = {
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'template': 'template',
        'kind': 'kind',
    }

    __types__ = {
        'template': 'v1.PodTemplateSpec',
        'metadata': 'v1.ObjectMeta',
    }

    __required__ = set()

    api_version = None # string
    metadata = None # v1.ObjectMeta
    template = None # v1.PodTemplateSpec
    kind = None # string

    def __init__(self, **_kwargs_):

        self.kind = 'ObjectMeta'

        super().__init__(**_kwargs_)

@register_model
class v1_OwnerReference(Resource):

    """OwnerReference contains enough information to let you identify an
    owning object. Currently, an owning object must be in the same
    namespace, so there is no namespace field."""

    __kind__ = 'v1.OwnerReference'

    __fields__ = {
        'controller': 'controller',
        'api_version': 'apiVersion',
        'name': 'name',
        'kind': 'kind',
        'uid': 'uid',
    }

    __types__ = {
    }

    __required__ = set([
        'api_version',
        'kind',
        'name',
        'uid',
    ])

    controller = None # boolean
    api_version = None # string (required)
    name = None # string (required)
    kind = None # string (required)
    uid = None # string (required)

    def __init__(self, *, api_version, kind, name, uid, **_kwargs_):

        self.kind = 'OwnerReference'

        self.api_version = api_version
        self.kind = kind
        self.name = name
        self.uid = uid

        super().__init__(**_kwargs_)

@register_model
class v1_Pod(Resource):

    """Pod is a collection of containers that can run on a host. This
    resource is created by clients and scheduled onto hosts."""

    __kind__ = 'v1.Pod'

    __fields__ = {
        'status': 'status',
        'spec': 'spec',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'status': 'v1.PodStatus',
        'spec': 'v1.PodSpec',
        'metadata': 'v1.ObjectMeta',
    }

    __required__ = set()

    status = None # v1.PodStatus
    spec = None # v1.PodSpec
    api_version = None # string
    metadata = None # v1.ObjectMeta
    kind = None # string

    def __init__(self, **_kwargs_):

        self.kind = 'ObjectMeta'

        super().__init__(**_kwargs_)

@register_model
class unversioned_StatusCause(Resource):

    """StatusCause provides more information about an api.Status failure,
    including cases when multiple errors are encountered."""

    __kind__ = 'unversioned.StatusCause'

    __fields__ = {
        'message': 'message',
        'reason': 'reason',
        'field': 'field',
    }

    __types__ = {
    }

    __required__ = set()

    message = None # string
    reason = None # string
    field = None # string

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_Service(Resource):

    """Service is a named abstraction of software service (for example,
    mysql) consisting of local port (for example 3306) that the proxy
    listens on, and the selector that determines which pods will
    answer requests sent through the proxy."""

    __kind__ = 'v1.Service'

    __fields__ = {
        'status': 'status',
        'spec': 'spec',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'status': 'v1.ServiceStatus',
        'spec': 'v1.ServiceSpec',
        'metadata': 'v1.ObjectMeta',
    }

    __required__ = set()

    status = None # v1.ServiceStatus
    spec = None # v1.ServiceSpec
    api_version = None # string
    metadata = None # v1.ObjectMeta
    kind = None # string

    def __init__(self, **_kwargs_):

        self.kind = 'ObjectMeta'

        super().__init__(**_kwargs_)

@register_model
class v1_PodCondition(Resource):

    """PodCondition contains details for the current condition of this pod."""

    __kind__ = 'v1.PodCondition'

    __fields__ = {
        'message': 'message',
        'reason': 'reason',
        'type': 'type',
        'last_probe_time': 'lastProbeTime',
        'status': 'status',
        'last_transition_time': 'lastTransitionTime',
    }

    __types__ = {
    }

    __required__ = set([
        'status',
        'type',
    ])

    message = None # string
    reason = None # string
    type = None # string (required)
    last_probe_time = None # string
    status = None # string (required)
    last_transition_time = None # string

    def __init__(self, *, status, type, **_kwargs_):

        self.status = status
        self.type = type

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
class v1_EndpointsList(Resource):

    """EndpointsList is a list of endpoints."""

    __kind__ = 'v1.EndpointsList'

    __fields__ = {
        'items': 'items',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'unversioned.ListMeta',
        'items': 'v1.Endpoints',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    api_version = None # string
    metadata = None # unversioned.ListMeta
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'Endpoints'

        self.items = items

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
class v1_PersistentVolumeClaimList(Resource):

    """PersistentVolumeClaimList is a list of PersistentVolumeClaim items."""

    __kind__ = 'v1.PersistentVolumeClaimList'

    __fields__ = {
        'items': 'items',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'unversioned.ListMeta',
        'items': 'v1.PersistentVolumeClaim',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    api_version = None # string
    metadata = None # unversioned.ListMeta
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'PersistentVolumeClaim'

        self.items = items

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
class v1_ServiceList(Resource):

    """ServiceList holds a list of services."""

    __kind__ = 'v1.ServiceList'

    __fields__ = {
        'items': 'items',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'unversioned.ListMeta',
        'items': 'v1.Service',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    api_version = None # string
    metadata = None # unversioned.ListMeta
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'Service'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_ReplicationControllerSpec(Resource):

    """ReplicationControllerSpec is the specification of a replication
    controller."""

    __kind__ = 'v1.ReplicationControllerSpec'

    __fields__ = {
        'template': 'template',
        'replicas': 'replicas',
        'selector': 'selector',
    }

    __types__ = {
        'template': 'v1.PodTemplateSpec',
    }

    __required__ = set()

    template = None # v1.PodTemplateSpec
    replicas = None # integer
    selector = None # object

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_ObjectReference(Resource):

    """ObjectReference contains enough information to let you inspect or
    modify the referred object."""

    __kind__ = 'v1.ObjectReference'

    __fields__ = {
        'namespace': 'namespace',
        'field_path': 'fieldPath',
        'resource_version': 'resourceVersion',
        'api_version': 'apiVersion',
        'name': 'name',
        'kind': 'kind',
        'uid': 'uid',
    }

    __types__ = {
    }

    __required__ = set()

    namespace = None # string
    field_path = None # string
    resource_version = None # string
    api_version = None # string
    name = None # string
    kind = None # string
    uid = None # string

    def __init__(self, **_kwargs_):

        self.kind = 'ObjectReference'

        super().__init__(**_kwargs_)

@register_model
class v1_ScaleStatus(Resource):

    """ScaleStatus represents the current status of a scale subresource."""

    __kind__ = 'v1.ScaleStatus'

    __fields__ = {
        'replicas': 'replicas',
        'selector': 'selector',
    }

    __types__ = {
    }

    __required__ = set([
        'replicas',
    ])

    replicas = None # integer (required)
    selector = None # string

    def __init__(self, *, replicas, **_kwargs_):

        self.replicas = replicas

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
class v1_DeleteOptions(Resource):

    """DeleteOptions may be provided when deleting an API object"""

    __kind__ = 'v1.DeleteOptions'

    __fields__ = {
        'api_version': 'apiVersion',
        'orphan_dependents': 'orphanDependents',
        'grace_period_seconds': 'gracePeriodSeconds',
        'preconditions': 'preconditions',
        'kind': 'kind',
    }

    __types__ = {
        'preconditions': 'v1.Preconditions',
    }

    __required__ = set()

    api_version = None # string
    orphan_dependents = None # boolean
    grace_period_seconds = None # integer
    preconditions = None # v1.Preconditions
    kind = None # string

    def __init__(self, **_kwargs_):

        self.kind = 'Preconditions'

        super().__init__(**_kwargs_)

@register_model
class unversioned_APIResource(Resource):

    """APIResource specifies the name of a resource and whether it is
    namespaced."""

    __kind__ = 'unversioned.APIResource'

    __fields__ = {
        'namespaced': 'namespaced',
        'name': 'name',
        'kind': 'kind',
    }

    __types__ = {
    }

    __required__ = set([
        'kind',
        'name',
        'namespaced',
    ])

    namespaced = None # boolean (required)
    name = None # string (required)
    kind = None # string (required)

    def __init__(self, *, kind, name, namespaced, **_kwargs_):

        self.kind = 'APIResource'

        self.kind = kind
        self.name = name
        self.namespaced = namespaced

        super().__init__(**_kwargs_)

@register_model
class v1_ComponentStatus(Resource):

    """ComponentStatus (and ComponentStatusList) holds the cluster validation
    info."""

    __kind__ = 'v1.ComponentStatus'

    __fields__ = {
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'conditions': 'conditions',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
        'conditions': 'v1.ComponentCondition',
    }

    __required__ = set()

    api_version = None # string
    metadata = None # v1.ObjectMeta
    conditions = None # array
    kind = None # string

    def __init__(self, **_kwargs_):
        self.conditions = []

        self.kind = 'ComponentCondition'

        super().__init__(**_kwargs_)

@register_model
class v1_ConfigMapList(Resource):

    """ConfigMapList is a resource containing a list of ConfigMap objects."""

    __kind__ = 'v1.ConfigMapList'

    __fields__ = {
        'items': 'items',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'unversioned.ListMeta',
        'items': 'v1.ConfigMap',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    api_version = None # string
    metadata = None # unversioned.ListMeta
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'ConfigMap'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_ConfigMapKeySelector(Resource):

    """Selects a key from a ConfigMap."""

    __kind__ = 'v1.ConfigMapKeySelector'

    __fields__ = {
        'key': 'key',
        'name': 'name',
    }

    __types__ = {
    }

    __required__ = set([
        'key',
    ])

    key = None # string (required)
    name = None # string

    def __init__(self, *, key, **_kwargs_):

        self.key = key

        super().__init__(**_kwargs_)

@register_model
class v1_FlexVolumeSource(Resource):

    """FlexVolume represents a generic volume resource that is
    provisioned/attached using a exec based plugin. This is an alpha
    feature and may change in future."""

    __kind__ = 'v1.FlexVolumeSource'

    __fields__ = {
        'secret_ref': 'secretRef',
        'read_only': 'readOnly',
        'fs_type': 'fsType',
        'driver': 'driver',
        'options': 'options',
    }

    __types__ = {
        'secret_ref': 'v1.LocalObjectReference',
    }

    __required__ = set([
        'driver',
    ])

    secret_ref = None # v1.LocalObjectReference
    read_only = None # boolean
    fs_type = None # string
    driver = None # string (required)
    options = None # object

    def __init__(self, *, driver, **_kwargs_):

        self.driver = driver

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
class v1_ContainerStateWaiting(Resource):

    """ContainerStateWaiting is a waiting state of a container."""

    __kind__ = 'v1.ContainerStateWaiting'

    __fields__ = {
        'message': 'message',
        'reason': 'reason',
    }

    __types__ = {
    }

    __required__ = set()

    message = None # string
    reason = None # string

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_Container(Resource):

    """A single application container that you want to run within a pod."""

    __kind__ = 'v1.Container'

    __fields__ = {
        'tty': 'tty',
        'ports': 'ports',
        'stdin_once': 'stdinOnce',
        'args': 'args',
        'readiness_probe': 'readinessProbe',
        'resources': 'resources',
        'liveness_probe': 'livenessProbe',
        'name': 'name',
        'env': 'env',
        'termination_message_path': 'terminationMessagePath',
        'image': 'image',
        'working_dir': 'workingDir',
        'stdin': 'stdin',
        'security_context': 'securityContext',
        'volume_mounts': 'volumeMounts',
        'image_pull_policy': 'imagePullPolicy',
        'command': 'command',
        'lifecycle': 'lifecycle',
    }

    __types__ = {
        'volume_mounts': 'v1.VolumeMount',
        'env': 'v1.EnvVar',
        'security_context': 'v1.SecurityContext',
        'ports': 'v1.ContainerPort',
        'readiness_probe': 'v1.Probe',
        'resources': 'v1.ResourceRequirements',
        'liveness_probe': 'v1.Probe',
        'lifecycle': 'v1.Lifecycle',
    }

    __required__ = set([
        'name',
    ])

    tty = None # boolean
    ports = None # array
    stdin_once = None # boolean
    args = None # array
    readiness_probe = None # v1.Probe
    resources = None # v1.ResourceRequirements
    liveness_probe = None # v1.Probe
    name = None # string (required)
    env = None # array
    termination_message_path = None # string
    image = None # string
    working_dir = None # string
    stdin = None # boolean
    security_context = None # v1.SecurityContext
    volume_mounts = None # array
    image_pull_policy = None # string
    command = None # array
    lifecycle = None # v1.Lifecycle

    def __init__(self, *, name, **_kwargs_):
        self.ports = []
        self.args = []
        self.env = []
        self.volume_mounts = []
        self.command = []

        self.name = name

        super().__init__(**_kwargs_)

@register_model
class v1_SELinuxOptions(Resource):

    """SELinuxOptions are the labels to be applied to the container"""

    __kind__ = 'v1.SELinuxOptions'

    __fields__ = {
        'role': 'role',
        'type': 'type',
        'user': 'user',
        'level': 'level',
    }

    __types__ = {
    }

    __required__ = set()

    role = None # string
    type = None # string
    user = None # string
    level = None # string

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
class v1_ContainerStatus(Resource):

    """ContainerStatus contains details for the current status of this
    container."""

    __kind__ = 'v1.ContainerStatus'

    __fields__ = {
        'ready': 'ready',
        'last_state': 'lastState',
        'restart_count': 'restartCount',
        'image_id': 'imageID',
        'state': 'state',
        'image': 'image',
        'container_id': 'containerID',
        'name': 'name',
    }

    __types__ = {
        'state': 'v1.ContainerState',
        'last_state': 'v1.ContainerState',
    }

    __required__ = set([
        'image',
        'image_id',
        'name',
        'ready',
        'restart_count',
    ])

    ready = None # boolean (required)
    last_state = None # v1.ContainerState
    restart_count = None # integer (required)
    image_id = None # string (required)
    state = None # v1.ContainerState
    image = None # string (required)
    container_id = None # string
    name = None # string (required)

    def __init__(self, *, image, image_id, name, ready, restart_count, **_kwargs_):

        self.image = image
        self.image_id = image_id
        self.name = name
        self.ready = ready
        self.restart_count = restart_count

        super().__init__(**_kwargs_)

@register_model
class v1_ContainerStateTerminated(Resource):

    """ContainerStateTerminated is a terminated state of a container."""

    __kind__ = 'v1.ContainerStateTerminated'

    __fields__ = {
        'message': 'message',
        'reason': 'reason',
        'container_id': 'containerID',
        'signal': 'signal',
        'started_at': 'startedAt',
        'finished_at': 'finishedAt',
        'exit_code': 'exitCode',
    }

    __types__ = {
    }

    __required__ = set([
        'exit_code',
    ])

    message = None # string
    reason = None # string
    container_id = None # string
    signal = None # integer
    started_at = None # string
    finished_at = None # string
    exit_code = None # integer (required)

    def __init__(self, *, exit_code, **_kwargs_):

        self.exit_code = exit_code

        super().__init__(**_kwargs_)

@register_model
class v1_Secret(Resource):

    """Secret holds secret data of a certain type. The total bytes of the
    values in the Data field must be less than MaxSecretSize bytes."""

    __kind__ = 'v1.Secret'

    __fields__ = {
        'type': 'type',
        'metadata': 'metadata',
        'data': 'data',
        'string_data': 'stringData',
        'api_version': 'apiVersion',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
    }

    __required__ = set()

    type = None # string
    metadata = None # v1.ObjectMeta
    data = None # object
    string_data = None # object
    api_version = None # string
    kind = None # string

    def __init__(self, **_kwargs_):

        self.kind = 'ObjectMeta'

        super().__init__(**_kwargs_)

@register_model
class v1_ResourceQuota(Resource):

    """ResourceQuota sets aggregate quota restrictions enforced per namespace"""

    __kind__ = 'v1.ResourceQuota'

    __fields__ = {
        'status': 'status',
        'spec': 'spec',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'status': 'v1.ResourceQuotaStatus',
        'spec': 'v1.ResourceQuotaSpec',
        'metadata': 'v1.ObjectMeta',
    }

    __required__ = set()

    status = None # v1.ResourceQuotaStatus
    spec = None # v1.ResourceQuotaSpec
    api_version = None # string
    metadata = None # v1.ObjectMeta
    kind = None # string

    def __init__(self, **_kwargs_):

        self.kind = 'ObjectMeta'

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
class v1_FCVolumeSource(Resource):

    """Represents a Fibre Channel volume. Fibre Channel volumes can only be
    mounted as read/write once. Fibre Channel volumes support
    ownership management and SELinux relabeling."""

    __kind__ = 'v1.FCVolumeSource'

    __fields__ = {
        'read_only': 'readOnly',
        'fs_type': 'fsType',
        'lun': 'lun',
        'target_ww_ns': 'targetWWNs',
    }

    __types__ = {
    }

    __required__ = set([
        'lun',
        'target_ww_ns',
    ])

    read_only = None # boolean
    fs_type = None # string
    lun = None # integer (required)
    target_ww_ns = None # array (required)

    def __init__(self, *, lun, target_ww_ns, **_kwargs_):

        self.lun = lun
        self.target_ww_ns = target_ww_ns

        super().__init__(**_kwargs_)

@register_model
class v1_GlusterfsVolumeSource(Resource):

    """Represents a Glusterfs mount that lasts the lifetime of a pod.
    Glusterfs volumes do not support ownership management or SELinux
    relabeling."""

    __kind__ = 'v1.GlusterfsVolumeSource'

    __fields__ = {
        'path': 'path',
        'read_only': 'readOnly',
        'endpoints': 'endpoints',
    }

    __types__ = {
    }

    __required__ = set([
        'endpoints',
        'path',
    ])

    path = None # string (required)
    read_only = None # boolean
    endpoints = None # string (required)

    def __init__(self, *, endpoints, path, **_kwargs_):

        self.endpoints = endpoints
        self.path = path

        super().__init__(**_kwargs_)

@register_model
class v1_Volume(Resource):

    """Volume represents a named volume in a pod that may be accessed by any
    container in the pod."""

    __kind__ = 'v1.Volume'

    __fields__ = {
        'cinder': 'cinder',
        'nfs': 'nfs',
        'git_repo': 'gitRepo',
        'secret': 'secret',
        'cephfs': 'cephfs',
        'iscsi': 'iscsi',
        'aws_elastic_block_store': 'awsElasticBlockStore',
        'azure_file': 'azureFile',
        'downward_api': 'downwardAPI',
        'glusterfs': 'glusterfs',
        'persistent_volume_claim': 'persistentVolumeClaim',
        'host_path': 'hostPath',
        'empty_dir': 'emptyDir',
        'fc': 'fc',
        'vsphere_volume': 'vsphereVolume',
        'flocker': 'flocker',
        'name': 'name',
        'metadata': 'metadata',
        'rbd': 'rbd',
        'config_map': 'configMap',
        'flex_volume': 'flexVolume',
        'gce_persistent_disk': 'gcePersistentDisk',
    }

    __types__ = {
        'persistent_volume_claim': 'v1.PersistentVolumeClaimVolumeSource',
        'cinder': 'v1.CinderVolumeSource',
        'nfs': 'v1.NFSVolumeSource',
        'host_path': 'v1.HostPathVolumeSource',
        'empty_dir': 'v1.EmptyDirVolumeSource',
        'git_repo': 'v1.GitRepoVolumeSource',
        'secret': 'v1.SecretVolumeSource',
        'cephfs': 'v1.CephFSVolumeSource',
        'iscsi': 'v1.ISCSIVolumeSource',
        'fc': 'v1.FCVolumeSource',
        'vsphere_volume': 'v1.VsphereVirtualDiskVolumeSource',
        'aws_elastic_block_store': 'v1.AWSElasticBlockStoreVolumeSource',
        'metadata': 'v1.DeprecatedDownwardAPIVolumeSource',
        'azure_file': 'v1.AzureFileVolumeSource',
        'rbd': 'v1.RBDVolumeSource',
        'downward_api': 'v1.DownwardAPIVolumeSource',
        'glusterfs': 'v1.GlusterfsVolumeSource',
        'flex_volume': 'v1.FlexVolumeSource',
        'gce_persistent_disk': 'v1.GCEPersistentDiskVolumeSource',
        'config_map': 'v1.ConfigMapVolumeSource',
        'flocker': 'v1.FlockerVolumeSource',
    }

    __required__ = set([
        'name',
    ])

    cinder = None # v1.CinderVolumeSource
    nfs = None # v1.NFSVolumeSource
    git_repo = None # v1.GitRepoVolumeSource
    secret = None # v1.SecretVolumeSource
    cephfs = None # v1.CephFSVolumeSource
    iscsi = None # v1.ISCSIVolumeSource
    aws_elastic_block_store = None # v1.AWSElasticBlockStoreVolumeSource
    azure_file = None # v1.AzureFileVolumeSource
    downward_api = None # v1.DownwardAPIVolumeSource
    glusterfs = None # v1.GlusterfsVolumeSource
    persistent_volume_claim = None # v1.PersistentVolumeClaimVolumeSource
    host_path = None # v1.HostPathVolumeSource
    empty_dir = None # v1.EmptyDirVolumeSource
    fc = None # v1.FCVolumeSource
    vsphere_volume = None # v1.VsphereVirtualDiskVolumeSource
    flocker = None # v1.FlockerVolumeSource
    name = None # string (required)
    metadata = None # v1.DeprecatedDownwardAPIVolumeSource
    rbd = None # v1.RBDVolumeSource
    config_map = None # v1.ConfigMapVolumeSource
    flex_volume = None # v1.FlexVolumeSource
    gce_persistent_disk = None # v1.GCEPersistentDiskVolumeSource

    def __init__(self, *, name, **_kwargs_):

        self.name = name

        super().__init__(**_kwargs_)

@register_model
class v1_PodSpec(Resource):

    """PodSpec is a description of a pod."""

    __kind__ = 'v1.PodSpec'

    __fields__ = {
        'dns_policy': 'dnsPolicy',
        'node_name': 'nodeName',
        'active_deadline_seconds': 'activeDeadlineSeconds',
        'node_selector': 'nodeSelector',
        'service_account_name': 'serviceAccountName',
        'host_pid': 'hostPID',
        'host': 'host',
        'service_account': 'serviceAccount',
        'volumes': 'volumes',
        'security_context': 'securityContext',
        'hostname': 'hostname',
        'host_network': 'hostNetwork',
        'subdomain': 'subdomain',
        'restart_policy': 'restartPolicy',
        'host_ipc': 'hostIPC',
        'termination_grace_period_seconds': 'terminationGracePeriodSeconds',
        'containers': 'containers',
        'image_pull_secrets': 'imagePullSecrets',
    }

    __types__ = {
        'volumes': 'v1.Volume',
        'security_context': 'v1.PodSecurityContext',
        'image_pull_secrets': 'v1.LocalObjectReference',
        'containers': 'v1.Container',
    }

    __required__ = set([
        'containers',
    ])

    dns_policy = None # string
    node_name = None # string
    active_deadline_seconds = None # integer
    node_selector = None # object
    service_account_name = None # string
    host_pid = None # boolean
    host = None # string
    service_account = None # string
    volumes = None # array
    security_context = None # v1.PodSecurityContext
    hostname = None # string
    host_network = None # boolean
    subdomain = None # string
    restart_policy = None # string
    host_ipc = None # boolean
    termination_grace_period_seconds = None # integer
    containers = None # array (required)
    image_pull_secrets = None # array

    def __init__(self, *, containers, **_kwargs_):
        self.volumes = []
        self.image_pull_secrets = []

        self.containers = containers

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
class v1_PersistentVolumeStatus(Resource):

    """PersistentVolumeStatus is the current status of a persistent volume."""

    __kind__ = 'v1.PersistentVolumeStatus'

    __fields__ = {
        'message': 'message',
        'reason': 'reason',
        'phase': 'phase',
    }

    __types__ = {
    }

    __required__ = set()

    message = None # string
    reason = None # string
    phase = None # string

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_ConfigMap(Resource):

    """ConfigMap holds configuration data for pods to consume."""

    __kind__ = 'v1.ConfigMap'

    __fields__ = {
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'data': 'data',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
    }

    __required__ = set()

    api_version = None # string
    metadata = None # v1.ObjectMeta
    data = None # object
    kind = None # string

    def __init__(self, **_kwargs_):

        self.kind = 'ObjectMeta'

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
class v1_GCEPersistentDiskVolumeSource(Resource):

    """Represents a Persistent Disk resource in Google Compute Engine.  A GCE
    PD must exist before mounting to a container. The disk must also
    be in the same GCE project and zone as the kubelet. A GCE PD can
    only be mounted as read/write once or read-only many times. GCE
    PDs support ownership management and SELinux relabeling."""

    __kind__ = 'v1.GCEPersistentDiskVolumeSource'

    __fields__ = {
        'read_only': 'readOnly',
        'pd_name': 'pdName',
        'fs_type': 'fsType',
        'partition': 'partition',
    }

    __types__ = {
    }

    __required__ = set([
        'pd_name',
    ])

    read_only = None # boolean
    pd_name = None # string (required)
    fs_type = None # string
    partition = None # integer

    def __init__(self, *, pd_name, **_kwargs_):

        self.pd_name = pd_name

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
class v1_DeprecatedDownwardAPIVolumeFile(Resource):

    """DeprecatedDownwardAPIVolumeFile represents information to create the
    file containing the pod field This type is deprecated and should
    be replaced by use of the downwardAPI volume source."""

    __kind__ = 'v1.DeprecatedDownwardAPIVolumeFile'

    __fields__ = {
        'resource_field_ref': 'resourceFieldRef',
        'name': 'name',
        'field_ref': 'fieldRef',
    }

    __types__ = {
        'resource_field_ref': 'v1.ResourceFieldSelector',
        'field_ref': 'v1.ObjectFieldSelector',
    }

    __required__ = set([
        'name',
    ])

    resource_field_ref = None # v1.ResourceFieldSelector
    name = None # string (required)
    field_ref = None # v1.ObjectFieldSelector

    def __init__(self, *, name, **_kwargs_):

        self.name = name

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
class v1_EnvVar(Resource):

    """EnvVar represents an environment variable present in a Container."""

    __kind__ = 'v1.EnvVar'

    __fields__ = {
        'value_from': 'valueFrom',
        'value': 'value',
        'name': 'name',
    }

    __types__ = {
        'value_from': 'v1.EnvVarSource',
    }

    __required__ = set([
        'name',
    ])

    value_from = None # v1.EnvVarSource
    value = None # string
    name = None # string (required)

    def __init__(self, *, name, **_kwargs_):

        self.name = name

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
        'supplemental_groups': 'supplementalGroups',
        'fs_group': 'fsGroup',
        'run_as_non_root': 'runAsNonRoot',
        'run_as_user': 'runAsUser',
        'se_linux_options': 'seLinuxOptions',
    }

    __types__ = {
        'se_linux_options': 'v1.SELinuxOptions',
    }

    __required__ = set()

    supplemental_groups = None # array
    fs_group = None # integer
    run_as_non_root = None # boolean
    run_as_user = None # integer
    se_linux_options = None # v1.SELinuxOptions

    def __init__(self, **_kwargs_):
        self.supplemental_groups = []

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
class v1_CinderVolumeSource(Resource):

    """Represents a cinder volume resource in Openstack. A Cinder volume must
    exist before mounting to a container. The volume must also be in
    the same region as the kubelet. Cinder volumes support ownership
    management and SELinux relabeling."""

    __kind__ = 'v1.CinderVolumeSource'

    __fields__ = {
        'volume_id': 'volumeID',
        'read_only': 'readOnly',
        'fs_type': 'fsType',
    }

    __types__ = {
    }

    __required__ = set([
        'volume_id',
    ])

    volume_id = None # string (required)
    read_only = None # boolean
    fs_type = None # string

    def __init__(self, *, volume_id, **_kwargs_):

        self.volume_id = volume_id

        super().__init__(**_kwargs_)

@register_model
class v1_ISCSIVolumeSource(Resource):

    """Represents an ISCSI disk. ISCSI volumes can only be mounted as
    read/write once. ISCSI volumes support ownership management and
    SELinux relabeling."""

    __kind__ = 'v1.ISCSIVolumeSource'

    __fields__ = {
        'iscsi_interface': 'iscsiInterface',
        'lun': 'lun',
        'iqn': 'iqn',
        'target_portal': 'targetPortal',
        'read_only': 'readOnly',
        'fs_type': 'fsType',
    }

    __types__ = {
    }

    __required__ = set([
        'iqn',
        'lun',
        'target_portal',
    ])

    iscsi_interface = None # string
    lun = None # integer (required)
    iqn = None # string (required)
    target_portal = None # string (required)
    read_only = None # boolean
    fs_type = None # string

    def __init__(self, *, iqn, lun, target_portal, **_kwargs_):

        self.iqn = iqn
        self.lun = lun
        self.target_portal = target_portal

        super().__init__(**_kwargs_)
__all__ = ['unversioned_ListMeta', 'v1_Capabilities', 'v1_Endpoints', 'v1_SecurityContext', 'v1_ConfigMapVolumeSource', 'v1_IDRange', 'v1_Capability', 'v1_NodeAddress', 'v1_FlockerVolumeSource', 'v1_ContainerPort', 'v1_ObjectMeta', 'types_UID', 'v1_PodTemplateSpec', 'v1_PersistentVolumeClaimStatus', 'v1_SELinuxContextStrategyOptions', 'v1_EndpointPort', 'v1_Node', 'v1_ServiceStatus', 'v1_LimitRange', 'v1_SecurityContextConstraintsList', 'v1_NodeList', 'v1_PersistentVolumeClaim', 'v1_EventList', 'v1_PersistentVolumeSpec', 'unversioned_Patch', 'v1_PersistentVolumeClaimSpec', 'v1_ContainerImage', 'v1_GitRepoVolumeSource', 'v1_NodeSystemInfo', 'v1_SecurityContextConstraints', 'v1_ReplicationController', 'v1_Handler', 'v1_Namespace', 'versioned_Event', 'v1_Probe', 'v1_ServicePort', 'v1_ServiceAccountList', 'v1_DeprecatedDownwardAPIVolumeSource', 'v1_HostPathVolumeSource', 'v1_NodeStatus', 'v1_NodeSpec', 'v1_ResourceQuotaScope', 'v1_Lifecycle', 'v1_AttachedVolume', 'v1_SupplementalGroupsStrategyOptions', 'v1_EnvVarSource', 'v1_AzureFileVolumeSource', 'v1_CephFSVolumeSource', 'v1_PersistentVolumeAccessMode', 'unversioned_LabelSelectorRequirement', 'v1_ComponentCondition', 'v1_TCPSocketAction', 'unversioned_LabelSelector', 'v1_NodeCondition', 'v1_LoadBalancerIngress', 'v1_PersistentVolumeList', 'v1_ResourceFieldSelector', 'v1_FSGroupStrategyOptions', 'v1_PodStatus', 'v1_NamespaceList', 'v1_ObjectFieldSelector', 'v1_PodList', 'v1_PodTemplateList', 'unversioned_APIResourceList', 'v1_PersistentVolume', 'v1_Binding', 'v1_Event', 'v1_AWSElasticBlockStoreVolumeSource', 'v1_LimitRangeSpec', 'v1_ServiceAccount', 'v1_HTTPGetAction', 'v1_ContainerState', 'v1_ReplicationControllerList', 'v1_EventSource', 'unversioned_StatusDetails', 'v1_ServiceSpec', 'v1_EndpointSubset', 'v1_VolumeMount', 'v1_Scale', 'v1_SecretKeySelector', 'v1_ComponentStatusList', 'v1_LimitRangeList', 'v1_VsphereVirtualDiskVolumeSource', 'v1_LimitRangeItem', 'v1_RBDVolumeSource', 'v1_DownwardAPIVolumeFile', 'v1_FinalizerName', 'unversioned_Status', 'v1_HTTPHeader', 'v1_ResourceQuotaStatus', 'v1_SecretList', 'v1_ResourceQuotaSpec', 'v1_RunAsUserStrategyOptions', 'v1_ResourceQuotaList', 'v1_PodTemplate', 'v1_OwnerReference', 'v1_Pod', 'unversioned_StatusCause', 'v1_Service', 'v1_PodCondition', 'v1_NFSVolumeSource', 'v1_ContainerStateRunning', 'v1_NodeDaemonEndpoints', 'v1_EndpointsList', 'v1_NamespaceStatus', 'v1_PersistentVolumeClaimList', 'v1_EmptyDirVolumeSource', 'v1_ServiceList', 'v1_ReplicationControllerSpec', 'v1_ObjectReference', 'v1_ScaleStatus', 'v1_ExecAction', 'v1_DeleteOptions', 'unversioned_APIResource', 'v1_ComponentStatus', 'v1_ConfigMapList', 'v1_ConfigMapKeySelector', 'v1_FlexVolumeSource', 'v1_ResourceRequirements', 'v1_ContainerStateWaiting', 'v1_Container', 'v1_SELinuxOptions', 'v1_KeyToPath', 'v1_PersistentVolumeClaimVolumeSource', 'v1_ContainerStatus', 'v1_ContainerStateTerminated', 'v1_Secret', 'v1_ResourceQuota', 'v1_SecretVolumeSource', 'v1_EndpointAddress', 'v1_FCVolumeSource', 'v1_GlusterfsVolumeSource', 'v1_Volume', 'v1_PodSpec', 'v1_Preconditions', 'v1_NamespaceSpec', 'v1_PersistentVolumeStatus', 'v1_ConfigMap', 'v1_ReplicationControllerStatus', 'v1_GCEPersistentDiskVolumeSource', 'v1_FSType', 'v1_UniqueVolumeName', 'v1_DeprecatedDownwardAPIVolumeFile', 'v1_LoadBalancerStatus', 'v1_DaemonEndpoint', 'v1_LocalObjectReference', 'v1_ScaleSpec', 'v1_EnvVar', 'v1_PodSecurityContext', 'v1_DownwardAPIVolumeSource', 'v1_CinderVolumeSource', 'v1_ISCSIVolumeSource']

@register_model
class v1_TemplateList(Resource):

    """TemplateList is a list of Template objects."""

    __kind__ = 'v1.TemplateList'

    __fields__ = {
        'items': 'items',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'unversioned.ListMeta',
        'items': 'v1.Template',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    api_version = None # string
    metadata = None # unversioned.ListMeta
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'Template'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_SelfSubjectRulesReview(Resource):

    """SelfSubjectRulesReview is a resource you can create to determine which
    actions you can perform in a namespace"""

    __kind__ = 'v1.SelfSubjectRulesReview'

    __fields__ = {
        'status': 'status',
        'spec': 'spec',
        'api_version': 'apiVersion',
        'kind': 'kind',
    }

    __types__ = {
        'status': 'v1.SubjectRulesReviewStatus',
        'spec': 'v1.SelfSubjectRulesReviewSpec',
    }

    __required__ = set([
        'spec',
    ])

    status = None # v1.SubjectRulesReviewStatus
    spec = None # v1.SelfSubjectRulesReviewSpec (required)
    api_version = None # string
    kind = None # string

    def __init__(self, *, spec, **_kwargs_):

        self.kind = 'SelfSubjectRulesReviewSpec'

        self.spec = spec

        super().__init__(**_kwargs_)

@register_model
class v1_SecurityContext(Resource):

    """SecurityContext holds security configuration that will be applied to a
    container. Some fields are present in both SecurityContext and
    PodSecurityContext.  When both are set, the values in
    SecurityContext take precedence."""

    __kind__ = 'v1.SecurityContext'

    __fields__ = {
        'privileged': 'privileged',
        'capabilities': 'capabilities',
        'run_as_non_root': 'runAsNonRoot',
        'run_as_user': 'runAsUser',
        'se_linux_options': 'seLinuxOptions',
        'read_only_root_filesystem': 'readOnlyRootFilesystem',
    }

    __types__ = {
        'se_linux_options': 'v1.SELinuxOptions',
        'capabilities': 'v1.Capabilities',
    }

    __required__ = set()

    privileged = None # boolean
    capabilities = None # v1.Capabilities
    run_as_non_root = None # boolean
    run_as_user = None # integer
    se_linux_options = None # v1.SELinuxOptions
    read_only_root_filesystem = None # boolean

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_ClusterNetwork(Resource):

    """ClusterNetwork describes a cluster network"""

    __kind__ = 'v1.ClusterNetwork'

    __fields__ = {
        'plugin_name': 'pluginName',
        'metadata': 'metadata',
        'network': 'network',
        'api_version': 'apiVersion',
        'service_network': 'serviceNetwork',
        'hostsubnetlength': 'hostsubnetlength',
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

    plugin_name = None # string
    metadata = None # v1.ObjectMeta
    network = None # string (required)
    api_version = None # string
    service_network = None # string (required)
    hostsubnetlength = None # integer (required)
    kind = None # string

    def __init__(self, *, hostsubnetlength, network, service_network, **_kwargs_):

        self.kind = 'ObjectMeta'

        self.hostsubnetlength = hostsubnetlength
        self.network = network
        self.service_network = service_network

        super().__init__(**_kwargs_)

@register_model
class v1_BuildSpec(Resource):

    """BuildSpec has the information to represent a build and also additional
    information about a build"""

    __kind__ = 'v1.BuildSpec'

    __fields__ = {
        'triggered_by': 'triggeredBy',
        'strategy': 'strategy',
        'source': 'source',
        'resources': 'resources',
        'post_commit': 'postCommit',
        'service_account': 'serviceAccount',
        'output': 'output',
        'completion_deadline_seconds': 'completionDeadlineSeconds',
        'revision': 'revision',
    }

    __types__ = {
        'triggered_by': 'v1.BuildTriggerCause',
        'strategy': 'v1.BuildStrategy',
        'source': 'v1.BuildSource',
        'revision': 'v1.SourceRevision',
        'resources': 'v1.ResourceRequirements',
        'output': 'v1.BuildOutput',
        'post_commit': 'v1.BuildPostCommitSpec',
    }

    __required__ = set([
        'strategy',
        'triggered_by',
    ])

    triggered_by = None # array (required)
    strategy = None # v1.BuildStrategy (required)
    source = None # v1.BuildSource
    resources = None # v1.ResourceRequirements
    post_commit = None # v1.BuildPostCommitSpec
    service_account = None # string
    output = None # v1.BuildOutput
    completion_deadline_seconds = None # integer
    revision = None # v1.SourceRevision

    def __init__(self, *, strategy, triggered_by, **_kwargs_):

        self.strategy = strategy
        self.triggered_by = triggered_by

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
        'kind': 'kind',
        'group_version': 'groupVersion',
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
    kind = None # string
    group_version = None # string (required)

    def __init__(self, *, group_version, resources, **_kwargs_):

        self.kind = 'APIResource'

        self.group_version = group_version
        self.resources = resources

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
class v1_ContainerPort(Resource):

    """ContainerPort represents a network port in a single container."""

    __kind__ = 'v1.ContainerPort'

    __fields__ = {
        'host_ip': 'hostIP',
        'host_port': 'hostPort',
        'protocol': 'protocol',
        'name': 'name',
        'container_port': 'containerPort',
    }

    __types__ = {
    }

    __required__ = set([
        'container_port',
    ])

    host_ip = None # string
    host_port = None # integer
    protocol = None # string
    name = None # string
    container_port = None # integer (required)

    def __init__(self, *, container_port, **_kwargs_):

        self.container_port = container_port

        super().__init__(**_kwargs_)

@register_model
class v1_ObjectMeta(Resource):

    """ObjectMeta is metadata that all persisted resources must have, which
    includes all objects users must create."""

    __kind__ = 'v1.ObjectMeta'

    __fields__ = {
        'generation': 'generation',
        'namespace': 'namespace',
        'annotations': 'annotations',
        'generate_name': 'generateName',
        'creation_timestamp': 'creationTimestamp',
        'deletion_grace_period_seconds': 'deletionGracePeriodSeconds',
        'name': 'name',
        'resource_version': 'resourceVersion',
        'finalizers': 'finalizers',
        'owner_references': 'ownerReferences',
        'deletion_timestamp': 'deletionTimestamp',
        'uid': 'uid',
        'self_link': 'selfLink',
        'labels': 'labels',
    }

    __types__ = {
        'owner_references': 'v1.OwnerReference',
    }

    __required__ = set()

    generation = None # integer
    namespace = None # string
    annotations = None # object
    generate_name = None # string
    creation_timestamp = None # string
    deletion_grace_period_seconds = None # integer
    name = None # string
    resource_version = None # string
    finalizers = None # array
    owner_references = None # array
    deletion_timestamp = None # string
    uid = None # string
    self_link = None # string
    labels = None # object

    def __init__(self, **_kwargs_):
        self.finalizers = []
        self.owner_references = []

        super().__init__(**_kwargs_)

@register_model
class v1_ImageStreamImportSpec(Resource):

    """ImageStreamImportSpec defines what images should be imported."""

    __kind__ = 'v1.ImageStreamImportSpec'

    __fields__ = {
        'import_': 'import',
        'images': 'images',
        'repository': 'repository',
    }

    __types__ = {
        'images': 'v1.ImageImportSpec',
        'repository': 'v1.RepositoryImportSpec',
    }

    __required__ = set([
        'import_',
    ])

    import_ = None # boolean (required)
    images = None # array
    repository = None # v1.RepositoryImportSpec

    def __init__(self, *, import_, **_kwargs_):
        self.images = []

        self.import_ = import_

        super().__init__(**_kwargs_)

@register_model
class v1_PodTemplateSpec(Resource):

    """PodTemplateSpec describes the data a pod should have when created from
    a template"""

    __kind__ = 'v1.PodTemplateSpec'

    __fields__ = {
        'spec': 'spec',
        'metadata': 'metadata',
    }

    __types__ = {
        'spec': 'v1.PodSpec',
        'metadata': 'v1.ObjectMeta',
    }

    __required__ = set()

    spec = None # v1.PodSpec
    metadata = None # v1.ObjectMeta

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_AppliedClusterResourceQuota(Resource):

    """AppliedClusterResourceQuota mirrors ClusterResourceQuota at a project
    scope, for projection into a project.  It allows a project-admin
    to know which ClusterResourceQuotas are applied to his project and
    their associated usage."""

    __kind__ = 'v1.AppliedClusterResourceQuota'

    __fields__ = {
        'status': 'status',
        'spec': 'spec',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'status': 'v1.ClusterResourceQuotaStatus',
        'spec': 'v1.ClusterResourceQuotaSpec',
        'metadata': 'v1.ObjectMeta',
    }

    __required__ = set([
        'metadata',
        'spec',
    ])

    status = None # v1.ClusterResourceQuotaStatus
    spec = None # v1.ClusterResourceQuotaSpec (required)
    api_version = None # string
    metadata = None # v1.ObjectMeta (required)
    kind = None # string

    def __init__(self, *, metadata, spec, **_kwargs_):

        self.kind = 'ObjectMeta'

        self.metadata = metadata
        self.spec = spec

        super().__init__(**_kwargs_)

@register_model
class v1_DeploymentConfigRollback(Resource):

    """DeploymentConfigRollback provides the input to rollback generation."""

    __kind__ = 'v1.DeploymentConfigRollback'

    __fields__ = {
        'spec': 'spec',
        'api_version': 'apiVersion',
        'updated_annotations': 'updatedAnnotations',
        'name': 'name',
        'kind': 'kind',
    }

    __types__ = {
        'spec': 'v1.DeploymentConfigRollbackSpec',
    }

    __required__ = set([
        'name',
        'spec',
    ])

    spec = None # v1.DeploymentConfigRollbackSpec (required)
    api_version = None # string
    updated_annotations = None # object
    name = None # string (required)
    kind = None # string

    def __init__(self, *, name, spec, **_kwargs_):

        self.kind = 'DeploymentConfigRollbackSpec'

        self.name = name
        self.spec = spec

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
class v1_ResourceFieldSelector(Resource):

    """ResourceFieldSelector represents container resources (cpu, memory) and
    their output format"""

    __kind__ = 'v1.ResourceFieldSelector'

    __fields__ = {
        'container_name': 'containerName',
        'resource': 'resource',
        'divisor': 'divisor',
    }

    __types__ = {
    }

    __required__ = set([
        'resource',
    ])

    container_name = None # string
    resource = None # string (required)
    divisor = None # string

    def __init__(self, *, resource, **_kwargs_):

        self.resource = resource

        super().__init__(**_kwargs_)

@register_model
class v1_OAuthClientAuthorizationList(Resource):

    """OAuthClientAuthorizationList is a collection of OAuth client
    authorizations"""

    __kind__ = 'v1.OAuthClientAuthorizationList'

    __fields__ = {
        'items': 'items',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'unversioned.ListMeta',
        'items': 'v1.OAuthClientAuthorization',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    api_version = None # string
    metadata = None # unversioned.ListMeta
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'OAuthClientAuthorization'

        self.items = items

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
class v1_TagEventCondition(Resource):

    """TagEventCondition contains condition information for a tag event."""

    __kind__ = 'v1.TagEventCondition'

    __fields__ = {
        'message': 'message',
        'generation': 'generation',
        'reason': 'reason',
        'type': 'type',
        'status': 'status',
        'last_transition_time': 'lastTransitionTime',
    }

    __types__ = {
    }

    __required__ = set([
        'generation',
        'status',
        'type',
    ])

    message = None # string
    generation = None # integer (required)
    reason = None # string
    type = None # string (required)
    status = None # string (required)
    last_transition_time = None # string

    def __init__(self, *, generation, status, type, **_kwargs_):

        self.generation = generation
        self.status = status
        self.type = type

        super().__init__(**_kwargs_)

@register_model
class v1_GitRepoVolumeSource(Resource):

    """Represents a volume that is populated with the contents of a git
    repository. Git repo volumes do not support ownership management.
    Git repo volumes support SELinux relabeling."""

    __kind__ = 'v1.GitRepoVolumeSource'

    __fields__ = {
        'directory': 'directory',
        'repository': 'repository',
        'revision': 'revision',
    }

    __types__ = {
    }

    __required__ = set([
        'repository',
    ])

    directory = None # string
    repository = None # string (required)
    revision = None # string

    def __init__(self, *, repository, **_kwargs_):

        self.repository = repository

        super().__init__(**_kwargs_)

@register_model
class v1_GenericWebHookCause(Resource):

    """GenericWebHookCause holds information about a generic WebHook that
    triggered a build."""

    __kind__ = 'v1.GenericWebHookCause'

    __fields__ = {
        'secret': 'secret',
        'revision': 'revision',
    }

    __types__ = {
        'revision': 'v1.SourceRevision',
    }

    __required__ = set()

    secret = None # string
    revision = None # v1.SourceRevision

    def __init__(self, **_kwargs_):

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
        'user_names': 'userNames',
        'group_names': 'groupNames',
        'metadata': 'metadata',
        'role_ref': 'roleRef',
        'api_version': 'apiVersion',
        'subjects': 'subjects',
        'kind': 'kind',
    }

    __types__ = {
        'subjects': 'v1.ObjectReference',
        'metadata': 'v1.ObjectMeta',
        'role_ref': 'v1.ObjectReference',
    }

    __required__ = set([
        'group_names',
        'role_ref',
        'subjects',
        'user_names',
    ])

    user_names = None # array (required)
    group_names = None # array (required)
    metadata = None # v1.ObjectMeta
    role_ref = None # v1.ObjectReference (required)
    api_version = None # string
    subjects = None # array (required)
    kind = None # string

    def __init__(self, *, group_names, role_ref, subjects, user_names, **_kwargs_):

        self.kind = 'ObjectReference'

        self.group_names = group_names
        self.role_ref = role_ref
        self.subjects = subjects
        self.user_names = user_names

        super().__init__(**_kwargs_)

@register_model
class v1_DeploymentConfigStatus(Resource):

    """DeploymentConfigStatus represents the current deployment state."""

    __kind__ = 'v1.DeploymentConfigStatus'

    __fields__ = {
        'latest_version': 'latestVersion',
        'observed_generation': 'observedGeneration',
        'updated_replicas': 'updatedReplicas',
        'available_replicas': 'availableReplicas',
        'replicas': 'replicas',
        'unavailable_replicas': 'unavailableReplicas',
        'details': 'details',
    }

    __types__ = {
        'details': 'v1.DeploymentDetails',
    }

    __required__ = set()

    latest_version = None # integer
    observed_generation = None # integer
    updated_replicas = None # integer
    available_replicas = None # integer
    replicas = None # integer
    unavailable_replicas = None # integer
    details = None # v1.DeploymentDetails

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_NamedRole(Resource):

    """NamedRole relates a Role with a name"""

    __kind__ = 'v1.NamedRole'

    __fields__ = {
        'role': 'role',
        'name': 'name',
    }

    __types__ = {
        'role': 'v1.Role',
    }

    __required__ = set([
        'name',
        'role',
    ])

    role = None # v1.Role (required)
    name = None # string (required)

    def __init__(self, *, name, role, **_kwargs_):

        self.name = name
        self.role = role

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
        'tcp_socket': 'v1.TCPSocketAction',
        'exec': 'v1.ExecAction',
    }

    __required__ = set()

    http_get = None # v1.HTTPGetAction
    tcp_socket = None # v1.TCPSocketAction
    exec = None # v1.ExecAction

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_UserIdentityMapping(Resource):

    """UserIdentityMapping maps a user to an identity"""

    __kind__ = 'v1.UserIdentityMapping'

    __fields__ = {
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'identity': 'identity',
        'kind': 'kind',
        'user': 'user',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
        'user': 'v1.ObjectReference',
        'identity': 'v1.ObjectReference',
    }

    __required__ = set()

    api_version = None # string
    metadata = None # v1.ObjectMeta
    identity = None # v1.ObjectReference
    kind = None # string
    user = None # v1.ObjectReference

    def __init__(self, **_kwargs_):

        self.kind = 'ObjectReference'

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
class v1_DeploymentStrategy(Resource):

    """DeploymentStrategy describes how to perform a deployment."""

    __kind__ = 'v1.DeploymentStrategy'

    __fields__ = {
        'recreate_params': 'recreateParams',
        'type': 'type',
        'rolling_params': 'rollingParams',
        'labels': 'labels',
        'resources': 'resources',
        'annotations': 'annotations',
        'custom_params': 'customParams',
    }

    __types__ = {
        'rolling_params': 'v1.RollingDeploymentStrategyParams',
        'recreate_params': 'v1.RecreateDeploymentStrategyParams',
        'resources': 'v1.ResourceRequirements',
        'custom_params': 'v1.CustomDeploymentStrategyParams',
    }

    __required__ = set()

    recreate_params = None # v1.RecreateDeploymentStrategyParams
    type = None # string
    rolling_params = None # v1.RollingDeploymentStrategyParams
    labels = None # object
    resources = None # v1.ResourceRequirements
    annotations = None # object
    custom_params = None # v1.CustomDeploymentStrategyParams

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

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
class v1_OAuthClientList(Resource):

    """OAuthClientList is a collection of OAuth clients"""

    __kind__ = 'v1.OAuthClientList'

    __fields__ = {
        'items': 'items',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'unversioned.ListMeta',
        'items': 'v1.OAuthClient',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    api_version = None # string
    metadata = None # unversioned.ListMeta
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'OAuthClient'

        self.items = items

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
class v1_Capabilities(Resource):

    """Adds and removes POSIX capabilities from running containers."""

    __kind__ = 'v1.Capabilities'

    __fields__ = {
        'add': 'add',
        'drop': 'drop',
    }

    __types__ = {
        'add': 'v1.Capability',
    }

    __required__ = set()

    add = None # array
    drop = None # array

    def __init__(self, **_kwargs_):
        self.add = []
        self.drop = []

        super().__init__(**_kwargs_)

@register_model
class v1_OAuthAccessTokenList(Resource):

    """OAuthAccessTokenList is a collection of OAuth access tokens"""

    __kind__ = 'v1.OAuthAccessTokenList'

    __fields__ = {
        'items': 'items',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'unversioned.ListMeta',
        'items': 'v1.OAuthAccessToken',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    api_version = None # string
    metadata = None # unversioned.ListMeta
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'OAuthAccessToken'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_PolicyList(Resource):

    """PolicyList is a collection of Policies"""

    __kind__ = 'v1.PolicyList'

    __fields__ = {
        'items': 'items',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'unversioned.ListMeta',
        'items': 'v1.Policy',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    api_version = None # string
    metadata = None # unversioned.ListMeta
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'Policy'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_EnvVarSource(Resource):

    """EnvVarSource represents a source for the value of an EnvVar."""

    __kind__ = 'v1.EnvVarSource'

    __fields__ = {
        'resource_field_ref': 'resourceFieldRef',
        'secret_key_ref': 'secretKeyRef',
        'config_map_key_ref': 'configMapKeyRef',
        'field_ref': 'fieldRef',
    }

    __types__ = {
        'resource_field_ref': 'v1.ResourceFieldSelector',
        'secret_key_ref': 'v1.SecretKeySelector',
        'config_map_key_ref': 'v1.ConfigMapKeySelector',
        'field_ref': 'v1.ObjectFieldSelector',
    }

    __required__ = set()

    resource_field_ref = None # v1.ResourceFieldSelector
    secret_key_ref = None # v1.SecretKeySelector
    config_map_key_ref = None # v1.ConfigMapKeySelector
    field_ref = None # v1.ObjectFieldSelector

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_Policy(Resource):

    """Policy is a object that holds all the Roles for a particular
    namespace.  There is at most one Policy document per namespace."""

    __kind__ = 'v1.Policy'

    __fields__ = {
        'roles': 'roles',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'last_modified': 'lastModified',
        'kind': 'kind',
    }

    __types__ = {
        'roles': 'v1.NamedRole',
        'metadata': 'v1.ObjectMeta',
    }

    __required__ = set([
        'last_modified',
        'roles',
    ])

    roles = None # array (required)
    api_version = None # string
    metadata = None # v1.ObjectMeta
    last_modified = None # string (required)
    kind = None # string

    def __init__(self, *, last_modified, roles, **_kwargs_):

        self.kind = 'ObjectMeta'

        self.last_modified = last_modified
        self.roles = roles

        super().__init__(**_kwargs_)

@register_model
class v1_OAuthClient(Resource):

    """OAuthClient describes an OAuth client"""

    __kind__ = 'v1.OAuthClient'

    __fields__ = {
        'metadata': 'metadata',
        'respond_with_challenges': 'respondWithChallenges',
        'secret': 'secret',
        'additional_secrets': 'additionalSecrets',
        'api_version': 'apiVersion',
        'grant_method': 'grantMethod',
        'scope_restrictions': 'scopeRestrictions',
        'kind': 'kind',
        'redirect_ur_is': 'redirectURIs',
    }

    __types__ = {
        'scope_restrictions': 'v1.ScopeRestriction',
        'metadata': 'v1.ObjectMeta',
    }

    __required__ = set()

    metadata = None # v1.ObjectMeta
    respond_with_challenges = None # boolean
    secret = None # string
    additional_secrets = None # array
    api_version = None # string
    grant_method = None # string
    scope_restrictions = None # array
    kind = None # string
    redirect_ur_is = None # array

    def __init__(self, **_kwargs_):
        self.additional_secrets = []
        self.scope_restrictions = []
        self.redirect_ur_is = []

        self.kind = 'ObjectMeta'

        super().__init__(**_kwargs_)

@register_model
class v1_SecretList(Resource):

    """SecretList is a list of Secret."""

    __kind__ = 'v1.SecretList'

    __fields__ = {
        'items': 'items',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'unversioned.ListMeta',
        'items': 'v1.Secret',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    api_version = None # string
    metadata = None # unversioned.ListMeta
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'Secret'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_Identity(Resource):

    """Identity records a successful authentication of a user with an
    identity provider"""

    __kind__ = 'v1.Identity'

    __fields__ = {
        'metadata': 'metadata',
        'kind': 'kind',
        'extra': 'extra',
        'api_version': 'apiVersion',
        'user': 'user',
        'provider_name': 'providerName',
        'provider_user_name': 'providerUserName',
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

    metadata = None # v1.ObjectMeta
    kind = None # string
    extra = None # object
    api_version = None # string
    user = None # v1.ObjectReference (required)
    provider_name = None # string (required)
    provider_user_name = None # string (required)

    def __init__(self, *, provider_name, provider_user_name, user, **_kwargs_):

        self.kind = 'ObjectReference'

        self.provider_name = provider_name
        self.provider_user_name = provider_user_name
        self.user = user

        super().__init__(**_kwargs_)

@register_model
class v1_DeleteOptions(Resource):

    """DeleteOptions may be provided when deleting an API object"""

    __kind__ = 'v1.DeleteOptions'

    __fields__ = {
        'api_version': 'apiVersion',
        'orphan_dependents': 'orphanDependents',
        'grace_period_seconds': 'gracePeriodSeconds',
        'preconditions': 'preconditions',
        'kind': 'kind',
    }

    __types__ = {
        'preconditions': 'v1.Preconditions',
    }

    __required__ = set()

    api_version = None # string
    orphan_dependents = None # boolean
    grace_period_seconds = None # integer
    preconditions = None # v1.Preconditions
    kind = None # string

    def __init__(self, **_kwargs_):

        self.kind = 'Preconditions'

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
class v1_RoleList(Resource):

    """RoleList is a collection of Roles"""

    __kind__ = 'v1.RoleList'

    __fields__ = {
        'items': 'items',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'unversioned.ListMeta',
        'items': 'v1.Role',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    api_version = None # string
    metadata = None # unversioned.ListMeta
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'Role'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_BuildConfig(Resource):

    """BuildConfig is a template which can be used to create new builds."""

    __kind__ = 'v1.BuildConfig'

    __fields__ = {
        'status': 'status',
        'spec': 'spec',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'status': 'v1.BuildConfigStatus',
        'spec': 'v1.BuildConfigSpec',
        'metadata': 'v1.ObjectMeta',
    }

    __required__ = set([
        'spec',
        'status',
    ])

    status = None # v1.BuildConfigStatus (required)
    spec = None # v1.BuildConfigSpec (required)
    api_version = None # string
    metadata = None # v1.ObjectMeta
    kind = None # string

    def __init__(self, *, spec, status, **_kwargs_):

        self.kind = 'ObjectMeta'

        self.spec = spec
        self.status = status

        super().__init__(**_kwargs_)

@register_model
class v1_ProjectList(Resource):

    """ProjectList is a list of Project objects."""

    __kind__ = 'v1.ProjectList'

    __fields__ = {
        'items': 'items',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'unversioned.ListMeta',
        'items': 'v1.Project',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    api_version = None # string
    metadata = None # unversioned.ListMeta
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'Project'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_ProjectRequest(Resource):

    """ProjecRequest is the set of options necessary to fully qualify a
    project request"""

    __kind__ = 'v1.ProjectRequest'

    __fields__ = {
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'display_name': 'displayName',
        'kind': 'kind',
        'description': 'description',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
    }

    __required__ = set()

    api_version = None # string
    metadata = None # v1.ObjectMeta
    display_name = None # string
    kind = None # string
    description = None # string

    def __init__(self, **_kwargs_):

        self.kind = 'ObjectMeta'

        super().__init__(**_kwargs_)

@register_model
class v1_ImageImportSpec(Resource):

    """ImageImportSpec describes a request to import a specific image."""

    __kind__ = 'v1.ImageImportSpec'

    __fields__ = {
        'from_': 'from',
        'to': 'to',
        'include_manifest': 'includeManifest',
        'import_policy': 'importPolicy',
    }

    __types__ = {
        'from_': 'v1.ObjectReference',
        'to': 'v1.LocalObjectReference',
        'import_policy': 'v1.TagImportPolicy',
    }

    __required__ = set([
        'from_',
    ])

    from_ = None # v1.ObjectReference (required)
    to = None # v1.LocalObjectReference
    include_manifest = None # boolean
    import_policy = None # v1.TagImportPolicy

    def __init__(self, *, from_, **_kwargs_):

        self.from_ = from_

        super().__init__(**_kwargs_)

@register_model
class v1_Build(Resource):

    """Build encapsulates the inputs needed to produce a new deployable
    image, as well as the status of the execution and a reference to
    the Pod which executed the build."""

    __kind__ = 'v1.Build'

    __fields__ = {
        'status': 'status',
        'spec': 'spec',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'status': 'v1.BuildStatus',
        'spec': 'v1.BuildSpec',
        'metadata': 'v1.ObjectMeta',
    }

    __required__ = set()

    status = None # v1.BuildStatus
    spec = None # v1.BuildSpec
    api_version = None # string
    metadata = None # v1.ObjectMeta
    kind = None # string

    def __init__(self, **_kwargs_):

        self.kind = 'ObjectMeta'

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
        'user_names': 'userNames',
        'group_names': 'groupNames',
        'metadata': 'metadata',
        'role_ref': 'roleRef',
        'api_version': 'apiVersion',
        'subjects': 'subjects',
        'kind': 'kind',
    }

    __types__ = {
        'subjects': 'v1.ObjectReference',
        'metadata': 'v1.ObjectMeta',
        'role_ref': 'v1.ObjectReference',
    }

    __required__ = set([
        'group_names',
        'role_ref',
        'subjects',
        'user_names',
    ])

    user_names = None # array (required)
    group_names = None # array (required)
    metadata = None # v1.ObjectMeta
    role_ref = None # v1.ObjectReference (required)
    api_version = None # string
    subjects = None # array (required)
    kind = None # string

    def __init__(self, *, group_names, role_ref, subjects, user_names, **_kwargs_):

        self.kind = 'ObjectReference'

        self.group_names = group_names
        self.role_ref = role_ref
        self.subjects = subjects
        self.user_names = user_names

        super().__init__(**_kwargs_)

@register_model
class v1_FlexVolumeSource(Resource):

    """FlexVolume represents a generic volume resource that is
    provisioned/attached using a exec based plugin. This is an alpha
    feature and may change in future."""

    __kind__ = 'v1.FlexVolumeSource'

    __fields__ = {
        'secret_ref': 'secretRef',
        'read_only': 'readOnly',
        'fs_type': 'fsType',
        'driver': 'driver',
        'options': 'options',
    }

    __types__ = {
        'secret_ref': 'v1.LocalObjectReference',
    }

    __required__ = set([
        'driver',
    ])

    secret_ref = None # v1.LocalObjectReference
    read_only = None # boolean
    fs_type = None # string
    driver = None # string (required)
    options = None # object

    def __init__(self, *, driver, **_kwargs_):

        self.driver = driver

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
class v1_BuildStatus(Resource):

    """BuildStatus contains the status of a build"""

    __kind__ = 'v1.BuildStatus'

    __fields__ = {
        'message': 'message',
        'reason': 'reason',
        'config': 'config',
        'phase': 'phase',
        'output_docker_image_reference': 'outputDockerImageReference',
        'completion_timestamp': 'completionTimestamp',
        'duration': 'duration',
        'start_timestamp': 'startTimestamp',
        'cancelled': 'cancelled',
    }

    __types__ = {
        'duration': 'time.Duration',
        'config': 'v1.ObjectReference',
    }

    __required__ = set([
        'phase',
    ])

    message = None # string
    reason = None # string
    config = None # v1.ObjectReference
    phase = None # string (required)
    output_docker_image_reference = None # string
    completion_timestamp = None # string
    duration = None # time.Duration
    start_timestamp = None # string
    cancelled = None # boolean

    def __init__(self, *, phase, **_kwargs_):

        self.phase = phase

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
class v1_TLSConfig(Resource):

    """TLSConfig defines config used to secure a route and provide
    termination"""

    __kind__ = 'v1.TLSConfig'

    __fields__ = {
        'insecure_edge_termination_policy': 'insecureEdgeTerminationPolicy',
        'termination': 'termination',
        'destination_ca_certificate': 'destinationCACertificate',
        'certificate': 'certificate',
        'ca_certificate': 'caCertificate',
        'key': 'key',
    }

    __types__ = {
    }

    __required__ = set([
        'termination',
    ])

    insecure_edge_termination_policy = None # string
    termination = None # string (required)
    destination_ca_certificate = None # string
    certificate = None # string
    ca_certificate = None # string
    key = None # string

    def __init__(self, *, termination, **_kwargs_):

        self.termination = termination

        super().__init__(**_kwargs_)

@register_model
class v1_ImageChangeTrigger(Resource):

    """ImageChangeTrigger allows builds to be triggered when an ImageStream
    changes"""

    __kind__ = 'v1.ImageChangeTrigger'

    __fields__ = {
        'from_': 'from',
        'last_triggered_image_id': 'lastTriggeredImageID',
    }

    __types__ = {
        'from_': 'v1.ObjectReference',
    }

    __required__ = set()

    from_ = None # v1.ObjectReference
    last_triggered_image_id = None # string

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_ImageLayer(Resource):

    """ImageLayer represents a single layer of the image. Some images may
    have multiple layers. Some may have none."""

    __kind__ = 'v1.ImageLayer'

    __fields__ = {
        'size': 'size',
        'name': 'name',
        'media_type': 'mediaType',
    }

    __types__ = {
    }

    __required__ = set([
        'media_type',
        'name',
        'size',
    ])

    size = None # integer (required)
    name = None # string (required)
    media_type = None # string (required)

    def __init__(self, *, media_type, name, size, **_kwargs_):

        self.media_type = media_type
        self.name = name
        self.size = size

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
class v1_PolicyRule(Resource):

    """PolicyRule holds information that describes a policy rule, but does
    not contain information about who the rule applies to or which
    namespace the rule applies to."""

    __kind__ = 'v1.PolicyRule'

    __fields__ = {
        'non_resource_ur_ls': 'nonResourceURLs',
        'resource_names': 'resourceNames',
        'verbs': 'verbs',
        'attribute_restrictions': 'attributeRestrictions',
        'api_groups': 'apiGroups',
        'resources': 'resources',
    }

    __types__ = {
    }

    __required__ = set([
        'api_groups',
        'resources',
        'verbs',
    ])

    non_resource_ur_ls = None # array
    resource_names = None # array
    verbs = None # array (required)
    attribute_restrictions = None # string
    api_groups = None # array (required)
    resources = None # array (required)

    def __init__(self, *, api_groups, resources, verbs, **_kwargs_):
        self.non_resource_ur_ls = []
        self.resource_names = []

        self.api_groups = api_groups
        self.resources = resources
        self.verbs = verbs

        super().__init__(**_kwargs_)

@register_model
class v1_HTTPGetAction(Resource):

    """HTTPGetAction describes an action based on HTTP Get requests."""

    __kind__ = 'v1.HTTPGetAction'

    __fields__ = {
        'path': 'path',
        'host': 'host',
        'scheme': 'scheme',
        'http_headers': 'httpHeaders',
        'port': 'port',
    }

    __types__ = {
        'http_headers': 'v1.HTTPHeader',
    }

    __required__ = set([
        'port',
    ])

    path = None # string
    host = None # string
    scheme = None # string
    http_headers = None # array
    port = None # string (required)

    def __init__(self, *, port, **_kwargs_):
        self.http_headers = []

        self.port = port

        super().__init__(**_kwargs_)

@register_model
class v1_OAuthAccessToken(Resource):

    """OAuthAccessToken describes an OAuth access token"""

    __kind__ = 'v1.OAuthAccessToken'

    __fields__ = {
        'user_uid': 'userUID',
        'expires_in': 'expiresIn',
        'metadata': 'metadata',
        'scopes': 'scopes',
        'client_name': 'clientName',
        'authorize_token': 'authorizeToken',
        'user_name': 'userName',
        'api_version': 'apiVersion',
        'redirect_uri': 'redirectURI',
        'refresh_token': 'refreshToken',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
    }

    __required__ = set()

    user_uid = None # string
    expires_in = None # integer
    metadata = None # v1.ObjectMeta
    scopes = None # array
    client_name = None # string
    authorize_token = None # string
    user_name = None # string
    api_version = None # string
    redirect_uri = None # string
    refresh_token = None # string
    kind = None # string

    def __init__(self, **_kwargs_):
        self.scopes = []

        self.kind = 'ObjectMeta'

        super().__init__(**_kwargs_)

@register_model
class v1_GitBuildSource(Resource):

    """GitBuildSource defines the parameters of a Git SCM"""

    __kind__ = 'v1.GitBuildSource'

    __fields__ = {
        'https_proxy': 'httpsProxy',
        'uri': 'uri',
        'ref': 'ref',
        'http_proxy': 'httpProxy',
    }

    __types__ = {
    }

    __required__ = set([
        'uri',
    ])

    https_proxy = None # string
    uri = None # string (required)
    ref = None # string
    http_proxy = None # string

    def __init__(self, *, uri, **_kwargs_):

        self.uri = uri

        super().__init__(**_kwargs_)

@register_model
class v1_DeprecatedDownwardAPIVolumeFile(Resource):

    """DeprecatedDownwardAPIVolumeFile represents information to create the
    file containing the pod field This type is deprecated and should
    be replaced by use of the downwardAPI volume source."""

    __kind__ = 'v1.DeprecatedDownwardAPIVolumeFile'

    __fields__ = {
        'resource_field_ref': 'resourceFieldRef',
        'name': 'name',
        'field_ref': 'fieldRef',
    }

    __types__ = {
        'resource_field_ref': 'v1.ResourceFieldSelector',
        'field_ref': 'v1.ObjectFieldSelector',
    }

    __required__ = set([
        'name',
    ])

    resource_field_ref = None # v1.ResourceFieldSelector
    name = None # string (required)
    field_ref = None # v1.ObjectFieldSelector

    def __init__(self, *, name, **_kwargs_):

        self.name = name

        super().__init__(**_kwargs_)

@register_model
class v1_ResourceQuotaStatusByNamespace(Resource):

    """ResourceQuotaStatusByNamespace gives status for a particular project"""

    __kind__ = 'v1.ResourceQuotaStatusByNamespace'

    __fields__ = {
        'status': 'status',
        'namespace': 'namespace',
    }

    __types__ = {
        'status': 'v1.ResourceQuotaStatus',
    }

    __required__ = set([
        'namespace',
        'status',
    ])

    status = None # v1.ResourceQuotaStatus (required)
    namespace = None # string (required)

    def __init__(self, *, namespace, status, **_kwargs_):

        self.namespace = namespace
        self.status = status

        super().__init__(**_kwargs_)

@register_model
class v1_ImageStream(Resource):

    """ImageStream stores a mapping of tags to images, metadata overrides
    that are applied when images are tagged in a stream, and an
    optional reference to a Docker image repository on a registry."""

    __kind__ = 'v1.ImageStream'

    __fields__ = {
        'status': 'status',
        'spec': 'spec',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'status': 'v1.ImageStreamStatus',
        'spec': 'v1.ImageStreamSpec',
        'metadata': 'v1.ObjectMeta',
    }

    __required__ = set([
        'spec',
    ])

    status = None # v1.ImageStreamStatus
    spec = None # v1.ImageStreamSpec (required)
    api_version = None # string
    metadata = None # v1.ObjectMeta
    kind = None # string

    def __init__(self, *, spec, **_kwargs_):

        self.kind = 'ObjectMeta'

        self.spec = spec

        super().__init__(**_kwargs_)

@register_model
class v1_ImageStreamImportStatus(Resource):

    """ImageStreamImportStatus contains information about the status of an
    image stream import."""

    __kind__ = 'v1.ImageStreamImportStatus'

    __fields__ = {
        'import_': 'import',
        'images': 'images',
        'repository': 'repository',
    }

    __types__ = {
        'import_': 'v1.ImageStream',
        'images': 'v1.ImageImportStatus',
        'repository': 'v1.RepositoryImportStatus',
    }

    __required__ = set()

    import_ = None # v1.ImageStream
    images = None # array
    repository = None # v1.RepositoryImportStatus

    def __init__(self, **_kwargs_):
        self.images = []

        super().__init__(**_kwargs_)

@register_model
class v1_VolumeMount(Resource):

    """VolumeMount describes a mounting of a Volume within a container."""

    __kind__ = 'v1.VolumeMount'

    __fields__ = {
        'mount_path': 'mountPath',
        'read_only': 'readOnly',
        'name': 'name',
        'sub_path': 'subPath',
    }

    __types__ = {
    }

    __required__ = set([
        'mount_path',
        'name',
    ])

    mount_path = None # string (required)
    read_only = None # boolean
    name = None # string (required)
    sub_path = None # string

    def __init__(self, *, mount_path, name, **_kwargs_):

        self.mount_path = mount_path
        self.name = name

        super().__init__(**_kwargs_)

@register_model
class v1_ClusterRoleBindingList(Resource):

    """ClusterRoleBindingList is a collection of ClusterRoleBindings"""

    __kind__ = 'v1.ClusterRoleBindingList'

    __fields__ = {
        'items': 'items',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'unversioned.ListMeta',
        'items': 'v1.ClusterRoleBinding',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    api_version = None # string
    metadata = None # unversioned.ListMeta
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'ClusterRoleBinding'

        self.items = items

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
class v1_SignatureCondition(Resource):

    """SignatureCondition describes an image signature condition of
    particular kind at particular probe time."""

    __kind__ = 'v1.SignatureCondition'

    __fields__ = {
        'message': 'message',
        'reason': 'reason',
        'type': 'type',
        'last_probe_time': 'lastProbeTime',
        'status': 'status',
        'last_transition_time': 'lastTransitionTime',
    }

    __types__ = {
    }

    __required__ = set([
        'status',
        'type',
    ])

    message = None # string
    reason = None # string
    type = None # string (required)
    last_probe_time = None # string
    status = None # string (required)
    last_transition_time = None # string

    def __init__(self, *, status, type, **_kwargs_):

        self.status = status
        self.type = type

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
class v1_LocalSubjectAccessReview(Resource):

    """LocalSubjectAccessReview is an object for requesting information about
    whether a user or group can perform an action in a particular
    namespace"""

    __kind__ = 'v1.LocalSubjectAccessReview'

    __fields__ = {
        'content': 'content',
        'user': 'user',
        'resource': 'resource',
        'namespace': 'namespace',
        'resource_api_version': 'resourceAPIVersion',
        'resource_api_group': 'resourceAPIGroup',
        'resource_name': 'resourceName',
        'verb': 'verb',
        'groups': 'groups',
        'api_version': 'apiVersion',
        'kind': 'kind',
        'scopes': 'scopes',
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

    content = None # string
    user = None # string (required)
    resource = None # string (required)
    namespace = None # string (required)
    resource_api_version = None # string (required)
    resource_api_group = None # string (required)
    resource_name = None # string (required)
    verb = None # string (required)
    groups = None # array (required)
    api_version = None # string
    kind = None # string
    scopes = None # array (required)

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
class v1_ClusterPolicyBindingList(Resource):

    """ClusterPolicyBindingList is a collection of ClusterPolicyBindings"""

    __kind__ = 'v1.ClusterPolicyBindingList'

    __fields__ = {
        'items': 'items',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'unversioned.ListMeta',
        'items': 'v1.ClusterPolicyBinding',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    api_version = None # string
    metadata = None # unversioned.ListMeta
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'ClusterPolicyBinding'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_HTTPHeader(Resource):

    """HTTPHeader describes a custom header to be used in HTTP probes"""

    __kind__ = 'v1.HTTPHeader'

    __fields__ = {
        'value': 'value',
        'name': 'name',
    }

    __types__ = {
    }

    __required__ = set([
        'name',
        'value',
    ])

    value = None # string (required)
    name = None # string (required)

    def __init__(self, *, name, value, **_kwargs_):

        self.name = name
        self.value = value

        super().__init__(**_kwargs_)

@register_model
class v1_OAuthAuthorizeTokenList(Resource):

    """OAuthAuthorizeTokenList is a collection of OAuth authorization tokens"""

    __kind__ = 'v1.OAuthAuthorizeTokenList'

    __fields__ = {
        'items': 'items',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'unversioned.ListMeta',
        'items': 'v1.OAuthAuthorizeToken',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    api_version = None # string
    metadata = None # unversioned.ListMeta
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'OAuthAuthorizeToken'

        self.items = items

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
class v1_ClusterNetworkList(Resource):

    """ClusterNetworkList is a collection of ClusterNetworks"""

    __kind__ = 'v1.ClusterNetworkList'

    __fields__ = {
        'items': 'items',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'unversioned.ListMeta',
        'items': 'v1.ClusterNetwork',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    api_version = None # string
    metadata = None # unversioned.ListMeta
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'ClusterNetwork'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_NetNamespace(Resource):

    """NetNamespace encapsulates the inputs needed to define a unique network
    namespace on the cluster"""

    __kind__ = 'v1.NetNamespace'

    __fields__ = {
        'netname': 'netname',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
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

    netname = None # string (required)
    api_version = None # string
    metadata = None # v1.ObjectMeta
    netid = None # integer (required)
    kind = None # string

    def __init__(self, *, netid, netname, **_kwargs_):

        self.kind = 'ObjectMeta'

        self.netid = netid
        self.netname = netname

        super().__init__(**_kwargs_)

@register_model
class v1_RepositoryImportSpec(Resource):

    """RepositoryImportSpec describes a request to import images from a
    Docker image repository."""

    __kind__ = 'v1.RepositoryImportSpec'

    __fields__ = {
        'from_': 'from',
        'import_policy': 'importPolicy',
        'include_manifest': 'includeManifest',
    }

    __types__ = {
        'from_': 'v1.ObjectReference',
        'import_policy': 'v1.TagImportPolicy',
    }

    __required__ = set([
        'from_',
    ])

    from_ = None # v1.ObjectReference (required)
    import_policy = None # v1.TagImportPolicy
    include_manifest = None # boolean

    def __init__(self, *, from_, **_kwargs_):

        self.from_ = from_

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
class v1_ImageStreamList(Resource):

    """ImageStreamList is a list of ImageStream objects."""

    __kind__ = 'v1.ImageStreamList'

    __fields__ = {
        'items': 'items',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'unversioned.ListMeta',
        'items': 'v1.ImageStream',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    api_version = None # string
    metadata = None # unversioned.ListMeta
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'ImageStream'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_BuildStrategy(Resource):

    """BuildStrategy contains the details of how to perform a build."""

    __kind__ = 'v1.BuildStrategy'

    __fields__ = {
        'custom_strategy': 'customStrategy',
        'source_strategy': 'sourceStrategy',
        'type': 'type',
        'docker_strategy': 'dockerStrategy',
        'jenkins_pipeline_strategy': 'jenkinsPipelineStrategy',
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
    source_strategy = None # v1.SourceBuildStrategy
    type = None # string (required)
    docker_strategy = None # v1.DockerBuildStrategy
    jenkins_pipeline_strategy = None # v1.JenkinsPipelineBuildStrategy

    def __init__(self, *, type, **_kwargs_):

        self.type = type

        super().__init__(**_kwargs_)

@register_model
class v1_ClusterResourceQuotaSelector(Resource):

    """ClusterResourceQuotaSelector is used to select projects.  At least one
    of LabelSelector or AnnotationSelector must present.  If only one
    is present, it is the only selection criteria.  If both are
    specified, the project must match both restrictions."""

    __kind__ = 'v1.ClusterResourceQuotaSelector'

    __fields__ = {
        'annotations': 'annotations',
        'labels': 'labels',
    }

    __types__ = {
        'labels': 'unversioned.LabelSelector',
    }

    __required__ = set([
        'annotations',
        'labels',
    ])

    annotations = None # object (required)
    labels = None # unversioned.LabelSelector (required)

    def __init__(self, *, annotations, labels, **_kwargs_):

        self.annotations = annotations
        self.labels = labels

        super().__init__(**_kwargs_)

@register_model
class v1_BuildConfigList(Resource):

    """BuildConfigList is a collection of BuildConfigs."""

    __kind__ = 'v1.BuildConfigList'

    __fields__ = {
        'items': 'items',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'unversioned.ListMeta',
        'items': 'v1.BuildConfig',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    api_version = None # string
    metadata = None # unversioned.ListMeta
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'BuildConfig'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_TagImportPolicy(Resource):

    """TagImportPolicy describes the tag import policy"""

    __kind__ = 'v1.TagImportPolicy'

    __fields__ = {
        'insecure': 'insecure',
        'scheduled': 'scheduled',
    }

    __types__ = {
    }

    __required__ = set()

    insecure = None # boolean
    scheduled = None # boolean

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_ObjectReference(Resource):

    """ObjectReference contains enough information to let you inspect or
    modify the referred object."""

    __kind__ = 'v1.ObjectReference'

    __fields__ = {
        'namespace': 'namespace',
        'field_path': 'fieldPath',
        'resource_version': 'resourceVersion',
        'api_version': 'apiVersion',
        'name': 'name',
        'kind': 'kind',
        'uid': 'uid',
    }

    __types__ = {
    }

    __required__ = set()

    namespace = None # string
    field_path = None # string
    resource_version = None # string
    api_version = None # string
    name = None # string
    kind = None # string
    uid = None # string

    def __init__(self, **_kwargs_):

        self.kind = 'ObjectReference'

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
class v1_ClusterPolicyList(Resource):

    """ClusterPolicyList is a collection of ClusterPolicies"""

    __kind__ = 'v1.ClusterPolicyList'

    __fields__ = {
        'items': 'items',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'unversioned.ListMeta',
        'items': 'v1.ClusterPolicy',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    api_version = None # string
    metadata = None # unversioned.ListMeta
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'ClusterPolicy'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_ConfigMapKeySelector(Resource):

    """Selects a key from a ConfigMap."""

    __kind__ = 'v1.ConfigMapKeySelector'

    __fields__ = {
        'key': 'key',
        'name': 'name',
    }

    __types__ = {
    }

    __required__ = set([
        'key',
    ])

    key = None # string (required)
    name = None # string

    def __init__(self, *, key, **_kwargs_):

        self.key = key

        super().__init__(**_kwargs_)

@register_model
class v1_BuildSource(Resource):

    """BuildSource is the SCM used for the build."""

    __kind__ = 'v1.BuildSource'

    __fields__ = {
        'dockerfile': 'dockerfile',
        'git': 'git',
        'context_dir': 'contextDir',
        'type': 'type',
        'images': 'images',
        'binary': 'binary',
        'secrets': 'secrets',
        'source_secret': 'sourceSecret',
    }

    __types__ = {
        'git': 'v1.GitBuildSource',
        'images': 'v1.ImageSource',
        'binary': 'v1.BinaryBuildSource',
        'secrets': 'v1.SecretBuildSource',
        'source_secret': 'v1.LocalObjectReference',
    }

    __required__ = set([
        'type',
    ])

    dockerfile = None # string
    git = None # v1.GitBuildSource
    context_dir = None # string
    type = None # string (required)
    images = None # array
    binary = None # v1.BinaryBuildSource
    secrets = None # array
    source_secret = None # v1.LocalObjectReference

    def __init__(self, *, type, **_kwargs_):
        self.images = []
        self.secrets = []

        self.type = type

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
class v1_HostSubnet(Resource):

    """HostSubnet encapsulates the inputs needed to define the container
    subnet network on a node"""

    __kind__ = 'v1.HostSubnet'

    __fields__ = {
        'metadata': 'metadata',
        'subnet': 'subnet',
        'api_version': 'apiVersion',
        'host_ip': 'hostIP',
        'host': 'host',
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

    metadata = None # v1.ObjectMeta
    subnet = None # string (required)
    api_version = None # string
    host_ip = None # string (required)
    host = None # string (required)
    kind = None # string

    def __init__(self, *, host, host_ip, subnet, **_kwargs_):

        self.kind = 'ObjectMeta'

        self.host = host
        self.host_ip = host_ip
        self.subnet = subnet

        super().__init__(**_kwargs_)

@register_model
class v1_SubjectAccessReview(Resource):

    """SubjectAccessReview is an object for requesting information about
    whether a user or group can perform an action"""

    __kind__ = 'v1.SubjectAccessReview'

    __fields__ = {
        'content': 'content',
        'user': 'user',
        'resource': 'resource',
        'namespace': 'namespace',
        'resource_api_version': 'resourceAPIVersion',
        'resource_api_group': 'resourceAPIGroup',
        'resource_name': 'resourceName',
        'verb': 'verb',
        'groups': 'groups',
        'api_version': 'apiVersion',
        'kind': 'kind',
        'scopes': 'scopes',
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

    content = None # string
    user = None # string (required)
    resource = None # string (required)
    namespace = None # string (required)
    resource_api_version = None # string (required)
    resource_api_group = None # string (required)
    resource_name = None # string (required)
    verb = None # string (required)
    groups = None # array (required)
    api_version = None # string
    kind = None # string
    scopes = None # array (required)

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
class v1_SELinuxOptions(Resource):

    """SELinuxOptions are the labels to be applied to the container"""

    __kind__ = 'v1.SELinuxOptions'

    __fields__ = {
        'role': 'role',
        'type': 'type',
        'user': 'user',
        'level': 'level',
    }

    __types__ = {
    }

    __required__ = set()

    role = None # string
    type = None # string
    user = None # string
    level = None # string

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_ImageImportStatus(Resource):

    """ImageImportStatus describes the result of an image import."""

    __kind__ = 'v1.ImageImportStatus'

    __fields__ = {
        'status': 'status',
        'tag': 'tag',
        'image': 'image',
    }

    __types__ = {
        'status': 'unversioned.Status',
        'image': 'v1.Image',
    }

    __required__ = set([
        'status',
    ])

    status = None # unversioned.Status (required)
    tag = None # string
    image = None # v1.Image

    def __init__(self, *, status, **_kwargs_):

        self.status = status

        super().__init__(**_kwargs_)

@register_model
class v1_Parameter(Resource):

    """Parameter defines a name/value variable that is to be processed during
    the Template to Config transformation."""

    __kind__ = 'v1.Parameter'

    __fields__ = {
        'value': 'value',
        'description': 'description',
        'from_': 'from',
        'display_name': 'displayName',
        'required': 'required',
        'generate': 'generate',
        'name': 'name',
    }

    __types__ = {
    }

    __required__ = set([
        'name',
    ])

    value = None # string
    description = None # string
    from_ = None # string
    display_name = None # string
    required = None # boolean
    generate = None # string
    name = None # string (required)

    def __init__(self, *, name, **_kwargs_):

        self.name = name

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
class v1_HostSubnetList(Resource):

    """HostSubnetList is a collection of HostSubnets"""

    __kind__ = 'v1.HostSubnetList'

    __fields__ = {
        'items': 'items',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'unversioned.ListMeta',
        'items': 'v1.HostSubnet',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    api_version = None # string
    metadata = None # unversioned.ListMeta
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'HostSubnet'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_Project(Resource):

    """Project is a logical top-level container for a set of origin resources"""

    __kind__ = 'v1.Project'

    __fields__ = {
        'status': 'status',
        'spec': 'spec',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'status': 'v1.ProjectStatus',
        'spec': 'v1.ProjectSpec',
        'metadata': 'v1.ObjectMeta',
    }

    __required__ = set()

    status = None # v1.ProjectStatus
    spec = None # v1.ProjectSpec
    api_version = None # string
    metadata = None # v1.ObjectMeta
    kind = None # string

    def __init__(self, **_kwargs_):

        self.kind = 'ObjectMeta'

        super().__init__(**_kwargs_)

@register_model
class v1_DeploymentConfigList(Resource):

    """DeploymentConfigList is a collection of deployment configs."""

    __kind__ = 'v1.DeploymentConfigList'

    __fields__ = {
        'items': 'items',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'unversioned.ListMeta',
        'items': 'v1.DeploymentConfig',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    api_version = None # string
    metadata = None # unversioned.ListMeta
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'DeploymentConfig'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_Volume(Resource):

    """Volume represents a named volume in a pod that may be accessed by any
    container in the pod."""

    __kind__ = 'v1.Volume'

    __fields__ = {
        'cinder': 'cinder',
        'nfs': 'nfs',
        'git_repo': 'gitRepo',
        'secret': 'secret',
        'cephfs': 'cephfs',
        'iscsi': 'iscsi',
        'aws_elastic_block_store': 'awsElasticBlockStore',
        'azure_file': 'azureFile',
        'downward_api': 'downwardAPI',
        'glusterfs': 'glusterfs',
        'persistent_volume_claim': 'persistentVolumeClaim',
        'host_path': 'hostPath',
        'empty_dir': 'emptyDir',
        'fc': 'fc',
        'vsphere_volume': 'vsphereVolume',
        'flocker': 'flocker',
        'name': 'name',
        'metadata': 'metadata',
        'rbd': 'rbd',
        'config_map': 'configMap',
        'flex_volume': 'flexVolume',
        'gce_persistent_disk': 'gcePersistentDisk',
    }

    __types__ = {
        'persistent_volume_claim': 'v1.PersistentVolumeClaimVolumeSource',
        'cinder': 'v1.CinderVolumeSource',
        'nfs': 'v1.NFSVolumeSource',
        'host_path': 'v1.HostPathVolumeSource',
        'empty_dir': 'v1.EmptyDirVolumeSource',
        'git_repo': 'v1.GitRepoVolumeSource',
        'secret': 'v1.SecretVolumeSource',
        'cephfs': 'v1.CephFSVolumeSource',
        'iscsi': 'v1.ISCSIVolumeSource',
        'fc': 'v1.FCVolumeSource',
        'vsphere_volume': 'v1.VsphereVirtualDiskVolumeSource',
        'aws_elastic_block_store': 'v1.AWSElasticBlockStoreVolumeSource',
        'metadata': 'v1.DeprecatedDownwardAPIVolumeSource',
        'azure_file': 'v1.AzureFileVolumeSource',
        'rbd': 'v1.RBDVolumeSource',
        'downward_api': 'v1.DownwardAPIVolumeSource',
        'glusterfs': 'v1.GlusterfsVolumeSource',
        'flex_volume': 'v1.FlexVolumeSource',
        'gce_persistent_disk': 'v1.GCEPersistentDiskVolumeSource',
        'config_map': 'v1.ConfigMapVolumeSource',
        'flocker': 'v1.FlockerVolumeSource',
    }

    __required__ = set([
        'name',
    ])

    cinder = None # v1.CinderVolumeSource
    nfs = None # v1.NFSVolumeSource
    git_repo = None # v1.GitRepoVolumeSource
    secret = None # v1.SecretVolumeSource
    cephfs = None # v1.CephFSVolumeSource
    iscsi = None # v1.ISCSIVolumeSource
    aws_elastic_block_store = None # v1.AWSElasticBlockStoreVolumeSource
    azure_file = None # v1.AzureFileVolumeSource
    downward_api = None # v1.DownwardAPIVolumeSource
    glusterfs = None # v1.GlusterfsVolumeSource
    persistent_volume_claim = None # v1.PersistentVolumeClaimVolumeSource
    host_path = None # v1.HostPathVolumeSource
    empty_dir = None # v1.EmptyDirVolumeSource
    fc = None # v1.FCVolumeSource
    vsphere_volume = None # v1.VsphereVirtualDiskVolumeSource
    flocker = None # v1.FlockerVolumeSource
    name = None # string (required)
    metadata = None # v1.DeprecatedDownwardAPIVolumeSource
    rbd = None # v1.RBDVolumeSource
    config_map = None # v1.ConfigMapVolumeSource
    flex_volume = None # v1.FlexVolumeSource
    gce_persistent_disk = None # v1.GCEPersistentDiskVolumeSource

    def __init__(self, *, name, **_kwargs_):

        self.name = name

        super().__init__(**_kwargs_)

@register_model
class v1_PodSpec(Resource):

    """PodSpec is a description of a pod."""

    __kind__ = 'v1.PodSpec'

    __fields__ = {
        'dns_policy': 'dnsPolicy',
        'node_name': 'nodeName',
        'active_deadline_seconds': 'activeDeadlineSeconds',
        'node_selector': 'nodeSelector',
        'service_account_name': 'serviceAccountName',
        'host_pid': 'hostPID',
        'host': 'host',
        'service_account': 'serviceAccount',
        'volumes': 'volumes',
        'security_context': 'securityContext',
        'hostname': 'hostname',
        'host_network': 'hostNetwork',
        'subdomain': 'subdomain',
        'restart_policy': 'restartPolicy',
        'host_ipc': 'hostIPC',
        'termination_grace_period_seconds': 'terminationGracePeriodSeconds',
        'containers': 'containers',
        'image_pull_secrets': 'imagePullSecrets',
    }

    __types__ = {
        'volumes': 'v1.Volume',
        'security_context': 'v1.PodSecurityContext',
        'image_pull_secrets': 'v1.LocalObjectReference',
        'containers': 'v1.Container',
    }

    __required__ = set([
        'containers',
    ])

    dns_policy = None # string
    node_name = None # string
    active_deadline_seconds = None # integer
    node_selector = None # object
    service_account_name = None # string
    host_pid = None # boolean
    host = None # string
    service_account = None # string
    volumes = None # array
    security_context = None # v1.PodSecurityContext
    hostname = None # string
    host_network = None # boolean
    subdomain = None # string
    restart_policy = None # string
    host_ipc = None # boolean
    termination_grace_period_seconds = None # integer
    containers = None # array (required)
    image_pull_secrets = None # array

    def __init__(self, *, containers, **_kwargs_):
        self.volumes = []
        self.image_pull_secrets = []

        self.containers = containers

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
class v1_ConfigMapVolumeSource(Resource):

    """Adapts a ConfigMap into a volume.  The contents of the target
    ConfigMap's Data field will be presented in a volume as files
    using the keys in the Data field as the file names, unless the
    items element is populated with specific mappings of keys to
    paths. ConfigMap volumes support ownership management and SELinux
    relabeling."""

    __kind__ = 'v1.ConfigMapVolumeSource'

    __fields__ = {
        'items': 'items',
        'name': 'name',
    }

    __types__ = {
        'items': 'v1.KeyToPath',
    }

    __required__ = set()

    items = None # array
    name = None # string

    def __init__(self, **_kwargs_):
        self.items = []

        super().__init__(**_kwargs_)

@register_model
class v1_NetNamespaceList(Resource):

    """NetNamespaceList is a collection of NetNamespaces"""

    __kind__ = 'v1.NetNamespaceList'

    __fields__ = {
        'items': 'items',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'unversioned.ListMeta',
        'items': 'v1.NetNamespace',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    api_version = None # string
    metadata = None # unversioned.ListMeta
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'NetNamespace'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_RouteIngress(Resource):

    """RouteIngress holds information about the places where a route is
    exposed"""

    __kind__ = 'v1.RouteIngress'

    __fields__ = {
        'conditions': 'conditions',
        'host': 'host',
        'router_name': 'routerName',
    }

    __types__ = {
        'conditions': 'v1.RouteIngressCondition',
    }

    __required__ = set()

    conditions = None # array
    host = None # string
    router_name = None # string

    def __init__(self, **_kwargs_):
        self.conditions = []

        super().__init__(**_kwargs_)

@register_model
class v1_ImageStreamImport(Resource):

    """ImageStreamImport imports an image from remote repositories into
    OpenShift."""

    __kind__ = 'v1.ImageStreamImport'

    __fields__ = {
        'status': 'status',
        'spec': 'spec',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'status': 'v1.ImageStreamImportStatus',
        'spec': 'v1.ImageStreamImportSpec',
        'metadata': 'v1.ObjectMeta',
    }

    __required__ = set([
        'spec',
        'status',
    ])

    status = None # v1.ImageStreamImportStatus (required)
    spec = None # v1.ImageStreamImportSpec (required)
    api_version = None # string
    metadata = None # v1.ObjectMeta
    kind = None # string

    def __init__(self, *, spec, status, **_kwargs_):

        self.kind = 'ObjectMeta'

        self.spec = spec
        self.status = status

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
class v1beta1_Scale(Resource):

    """represents a scaling request for a resource."""

    __kind__ = 'v1beta1.Scale'

    __fields__ = {
        'status': 'status',
        'spec': 'spec',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'status': 'v1beta1.ScaleStatus',
        'spec': 'v1beta1.ScaleSpec',
        'metadata': 'v1.ObjectMeta',
    }

    __required__ = set()

    status = None # v1beta1.ScaleStatus
    spec = None # v1beta1.ScaleSpec
    api_version = None # string
    metadata = None # v1.ObjectMeta
    kind = None # string

    def __init__(self, **_kwargs_):

        self.kind = 'ObjectMeta'

        super().__init__(**_kwargs_)

@register_model
class v1_ClusterRoleList(Resource):

    """ClusterRoleList is a collection of ClusterRoles"""

    __kind__ = 'v1.ClusterRoleList'

    __fields__ = {
        'items': 'items',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'unversioned.ListMeta',
        'items': 'v1.ClusterRole',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    api_version = None # string
    metadata = None # unversioned.ListMeta
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'ClusterRole'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_NamedTagEventList(Resource):

    """NamedTagEventList relates a tag to its image history."""

    __kind__ = 'v1.NamedTagEventList'

    __fields__ = {
        'tag': 'tag',
        'items': 'items',
        'conditions': 'conditions',
    }

    __types__ = {
        'items': 'v1.TagEvent',
        'conditions': 'v1.TagEventCondition',
    }

    __required__ = set([
        'items',
        'tag',
    ])

    tag = None # string (required)
    items = None # array (required)
    conditions = None # array

    def __init__(self, *, items, tag, **_kwargs_):
        self.conditions = []

        self.items = items
        self.tag = tag

        super().__init__(**_kwargs_)

@register_model
class v1_GitHubWebHookCause(Resource):

    """GitHubWebHookCause has information about a GitHub webhook that
    triggered a build."""

    __kind__ = 'v1.GitHubWebHookCause'

    __fields__ = {
        'secret': 'secret',
        'revision': 'revision',
    }

    __types__ = {
        'revision': 'v1.SourceRevision',
    }

    __required__ = set()

    secret = None # string
    revision = None # v1.SourceRevision

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_CustomDeploymentStrategyParams(Resource):

    """CustomDeploymentStrategyParams are the input to the Custom deployment
    strategy."""

    __kind__ = 'v1.CustomDeploymentStrategyParams'

    __fields__ = {
        'image': 'image',
        'command': 'command',
        'environment': 'environment',
    }

    __types__ = {
        'environment': 'v1.EnvVar',
    }

    __required__ = set()

    image = None # string
    command = None # array
    environment = None # array

    def __init__(self, **_kwargs_):
        self.command = []
        self.environment = []

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
        'script': 'script',
        'command': 'command',
        'args': 'args',
    }

    __types__ = {
    }

    __required__ = set()

    script = None # string
    command = None # array
    args = None # array

    def __init__(self, **_kwargs_):
        self.command = []
        self.args = []

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
class v1_RepositoryImportStatus(Resource):

    """RepositoryImportStatus describes the result of an image repository
    import"""

    __kind__ = 'v1.RepositoryImportStatus'

    __fields__ = {
        'status': 'status',
        'images': 'images',
        'additional_tags': 'additionalTags',
    }

    __types__ = {
        'status': 'unversioned.Status',
        'images': 'v1.ImageImportStatus',
    }

    __required__ = set()

    status = None # unversioned.Status
    images = None # array
    additional_tags = None # array

    def __init__(self, **_kwargs_):
        self.images = []
        self.additional_tags = []

        super().__init__(**_kwargs_)

@register_model
class v1_ISCSIVolumeSource(Resource):

    """Represents an ISCSI disk. ISCSI volumes can only be mounted as
    read/write once. ISCSI volumes support ownership management and
    SELinux relabeling."""

    __kind__ = 'v1.ISCSIVolumeSource'

    __fields__ = {
        'iscsi_interface': 'iscsiInterface',
        'lun': 'lun',
        'iqn': 'iqn',
        'target_portal': 'targetPortal',
        'read_only': 'readOnly',
        'fs_type': 'fsType',
    }

    __types__ = {
    }

    __required__ = set([
        'iqn',
        'lun',
        'target_portal',
    ])

    iscsi_interface = None # string
    lun = None # integer (required)
    iqn = None # string (required)
    target_portal = None # string (required)
    read_only = None # boolean
    fs_type = None # string

    def __init__(self, *, iqn, lun, target_portal, **_kwargs_):

        self.iqn = iqn
        self.lun = lun
        self.target_portal = target_portal

        super().__init__(**_kwargs_)

@register_model
class unversioned_ListMeta(Resource):

    """ListMeta describes metadata that synthetic resources must have,
    including lists and various status objects. A resource may have
    only one of {ObjectMeta, ListMeta}."""

    __kind__ = 'unversioned.ListMeta'

    __fields__ = {
        'self_link': 'selfLink',
        'resource_version': 'resourceVersion',
    }

    __types__ = {
    }

    __required__ = set()

    self_link = None # string
    resource_version = None # string

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_GitSourceRevision(Resource):

    """GitSourceRevision is the commit information from a git source for a
    build"""

    __kind__ = 'v1.GitSourceRevision'

    __fields__ = {
        'message': 'message',
        'commit': 'commit',
        'author': 'author',
        'committer': 'committer',
    }

    __types__ = {
        'author': 'v1.SourceControlUser',
        'committer': 'v1.SourceControlUser',
    }

    __required__ = set()

    message = None # string
    commit = None # string
    author = None # v1.SourceControlUser
    committer = None # v1.SourceControlUser

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_DockerBuildStrategy(Resource):

    """DockerBuildStrategy defines input parameters specific to Docker build."""

    __kind__ = 'v1.DockerBuildStrategy'

    __fields__ = {
        'no_cache': 'noCache',
        'env': 'env',
        'pull_secret': 'pullSecret',
        'dockerfile_path': 'dockerfilePath',
        'from_': 'from',
        'force_pull': 'forcePull',
    }

    __types__ = {
        'env': 'v1.EnvVar',
        'from_': 'v1.ObjectReference',
        'pull_secret': 'v1.LocalObjectReference',
    }

    __required__ = set()

    no_cache = None # boolean
    env = None # array
    pull_secret = None # v1.LocalObjectReference
    dockerfile_path = None # string
    from_ = None # v1.ObjectReference
    force_pull = None # boolean

    def __init__(self, **_kwargs_):
        self.env = []

        super().__init__(**_kwargs_)

@register_model
class v1_SecretBuildSource(Resource):

    """SecretBuildSource describes a secret and its destination directory
    that will be used only at the build time. The content of the
    secret referenced here will be copied into the destination
    directory instead of mounting."""

    __kind__ = 'v1.SecretBuildSource'

    __fields__ = {
        'secret': 'secret',
        'destination_dir': 'destinationDir',
    }

    __types__ = {
        'secret': 'v1.LocalObjectReference',
    }

    __required__ = set([
        'secret',
    ])

    secret = None # v1.LocalObjectReference (required)
    destination_dir = None # string

    def __init__(self, *, secret, **_kwargs_):

        self.secret = secret

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
class v1_ClusterRole(Resource):

    """ClusterRole is a logical grouping of PolicyRules that can be
    referenced as a unit by ClusterRoleBindings."""

    __kind__ = 'v1.ClusterRole'

    __fields__ = {
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'rules': 'rules',
        'kind': 'kind',
    }

    __types__ = {
        'rules': 'v1.PolicyRule',
        'metadata': 'v1.ObjectMeta',
    }

    __required__ = set([
        'rules',
    ])

    api_version = None # string
    metadata = None # v1.ObjectMeta
    rules = None # array (required)
    kind = None # string

    def __init__(self, *, rules, **_kwargs_):

        self.kind = 'ObjectMeta'

        self.rules = rules

        super().__init__(**_kwargs_)

@register_model
class v1_DeploymentTriggerPolicy(Resource):

    """DeploymentTriggerPolicy describes a policy for a single trigger that
    results in a new deployment."""

    __kind__ = 'v1.DeploymentTriggerPolicy'

    __fields__ = {
        'image_change_params': 'imageChangeParams',
        'type': 'type',
    }

    __types__ = {
        'image_change_params': 'v1.DeploymentTriggerImageChangeParams',
    }

    __required__ = set()

    image_change_params = None # v1.DeploymentTriggerImageChangeParams
    type = None # string

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_ImageStreamMapping(Resource):

    """ImageStreamMapping represents a mapping from a single tag to a Docker
    image as well as the reference to the Docker image stream the
    image came from."""

    __kind__ = 'v1.ImageStreamMapping'

    __fields__ = {
        'tag': 'tag',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'image': 'image',
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

    tag = None # string (required)
    api_version = None # string
    metadata = None # v1.ObjectMeta
    image = None # v1.Image (required)
    kind = None # string

    def __init__(self, *, image, tag, **_kwargs_):

        self.kind = 'Image'

        self.image = image
        self.tag = tag

        super().__init__(**_kwargs_)

@register_model
class v1_ImageStreamImage(Resource):

    """ImageStreamImage represents an Image that is retrieved by image name
    from an ImageStream."""

    __kind__ = 'v1.ImageStreamImage'

    __fields__ = {
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'image': 'image',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
        'image': 'v1.Image',
    }

    __required__ = set([
        'image',
    ])

    api_version = None # string
    metadata = None # v1.ObjectMeta
    image = None # v1.Image (required)
    kind = None # string

    def __init__(self, *, image, **_kwargs_):

        self.kind = 'Image'

        self.image = image

        super().__init__(**_kwargs_)

@register_model
class v1_BuildTriggerPolicy(Resource):

    """BuildTriggerPolicy describes a policy for a single trigger that
    results in a new Build."""

    __kind__ = 'v1.BuildTriggerPolicy'

    __fields__ = {
        'generic': 'generic',
        'type': 'type',
        'image_change': 'imageChange',
        'github': 'github',
    }

    __types__ = {
        'generic': 'v1.WebHookTrigger',
        'image_change': 'v1.ImageChangeTrigger',
        'github': 'v1.WebHookTrigger',
    }

    __required__ = set([
        'type',
    ])

    generic = None # v1.WebHookTrigger
    type = None # string (required)
    image_change = None # v1.ImageChangeTrigger
    github = None # v1.WebHookTrigger

    def __init__(self, *, type, **_kwargs_):

        self.type = type

        super().__init__(**_kwargs_)

@register_model
class v1_ResourceAccessReview(Resource):

    """ResourceAccessReview is a means to request a list of which users and
    groups are authorized to perform the action specified by spec"""

    __kind__ = 'v1.ResourceAccessReview'

    __fields__ = {
        'content': 'content',
        'resource_name': 'resourceName',
        'namespace': 'namespace',
        'verb': 'verb',
        'resource_api_version': 'resourceAPIVersion',
        'api_version': 'apiVersion',
        'resource': 'resource',
        'resource_api_group': 'resourceAPIGroup',
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

    content = None # string
    resource_name = None # string (required)
    namespace = None # string (required)
    verb = None # string (required)
    resource_api_version = None # string (required)
    api_version = None # string
    resource = None # string (required)
    resource_api_group = None # string (required)
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
class v1_RollingDeploymentStrategyParams(Resource):

    """RollingDeploymentStrategyParams are the input to the Rolling
    deployment strategy."""

    __kind__ = 'v1.RollingDeploymentStrategyParams'

    __fields__ = {
        'update_period_seconds': 'updatePeriodSeconds',
        'max_surge': 'maxSurge',
        'pre': 'pre',
        'interval_seconds': 'intervalSeconds',
        'post': 'post',
        'max_unavailable': 'maxUnavailable',
        'timeout_seconds': 'timeoutSeconds',
        'update_percent': 'updatePercent',
    }

    __types__ = {
        'post': 'v1.LifecycleHook',
        'pre': 'v1.LifecycleHook',
    }

    __required__ = set()

    update_period_seconds = None # integer
    max_surge = None # string
    pre = None # v1.LifecycleHook
    interval_seconds = None # integer
    post = None # v1.LifecycleHook
    max_unavailable = None # string
    timeout_seconds = None # integer
    update_percent = None # integer

    def __init__(self, **_kwargs_):

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
class v1_IdentityList(Resource):

    """IdentityList is a collection of Identities"""

    __kind__ = 'v1.IdentityList'

    __fields__ = {
        'items': 'items',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'unversioned.ListMeta',
        'items': 'v1.Identity',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    api_version = None # string
    metadata = None # unversioned.ListMeta
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'Identity'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_PolicyBindingList(Resource):

    """PolicyBindingList is a collection of PolicyBindings"""

    __kind__ = 'v1.PolicyBindingList'

    __fields__ = {
        'items': 'items',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'unversioned.ListMeta',
        'items': 'v1.PolicyBinding',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    api_version = None # string
    metadata = None # unversioned.ListMeta
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'PolicyBinding'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_DeploymentTriggerImageChangeParams(Resource):

    """DeploymentTriggerImageChangeParams represents the parameters to the
    ImageChange trigger."""

    __kind__ = 'v1.DeploymentTriggerImageChangeParams'

    __fields__ = {
        'from_': 'from',
        'container_names': 'containerNames',
        'automatic': 'automatic',
        'last_triggered_image': 'lastTriggeredImage',
    }

    __types__ = {
        'from_': 'v1.ObjectReference',
    }

    __required__ = set([
        'from_',
    ])

    from_ = None # v1.ObjectReference (required)
    container_names = None # array
    automatic = None # boolean
    last_triggered_image = None # string

    def __init__(self, *, from_, **_kwargs_):
        self.container_names = []

        self.from_ = from_

        super().__init__(**_kwargs_)

@register_model
class v1_AzureFileVolumeSource(Resource):

    """AzureFile represents an Azure File Service mount on the host and bind
    mount to the pod."""

    __kind__ = 'v1.AzureFileVolumeSource'

    __fields__ = {
        'read_only': 'readOnly',
        'secret_name': 'secretName',
        'share_name': 'shareName',
    }

    __types__ = {
    }

    __required__ = set([
        'secret_name',
        'share_name',
    ])

    read_only = None # boolean
    secret_name = None # string (required)
    share_name = None # string (required)

    def __init__(self, *, secret_name, share_name, **_kwargs_):

        self.secret_name = secret_name
        self.share_name = share_name

        super().__init__(**_kwargs_)

@register_model
class v1_ImageStreamStatus(Resource):

    """ImageStreamStatus contains information about the state of this image
    stream."""

    __kind__ = 'v1.ImageStreamStatus'

    __fields__ = {
        'docker_image_repository': 'dockerImageRepository',
        'tags': 'tags',
    }

    __types__ = {
        'tags': 'v1.NamedTagEventList',
    }

    __required__ = set([
        'docker_image_repository',
    ])

    docker_image_repository = None # string (required)
    tags = None # array

    def __init__(self, *, docker_image_repository, **_kwargs_):
        self.tags = []

        self.docker_image_repository = docker_image_repository

        super().__init__(**_kwargs_)

@register_model
class v1beta1_ScaleStatus(Resource):

    """represents the current status of a scale subresource."""

    __kind__ = 'v1beta1.ScaleStatus'

    __fields__ = {
        'replicas': 'replicas',
        'target_selector': 'targetSelector',
        'selector': 'selector',
    }

    __types__ = {
    }

    __required__ = set([
        'replicas',
    ])

    replicas = None # integer (required)
    target_selector = None # string
    selector = None # object

    def __init__(self, *, replicas, **_kwargs_):

        self.replicas = replicas

        super().__init__(**_kwargs_)

@register_model
class v1_Probe(Resource):

    """Probe describes a health check to be performed against a container to
    determine whether it is alive or ready to receive traffic."""

    __kind__ = 'v1.Probe'

    __fields__ = {
        'initial_delay_seconds': 'initialDelaySeconds',
        'success_threshold': 'successThreshold',
        'period_seconds': 'periodSeconds',
        'http_get': 'httpGet',
        'failure_threshold': 'failureThreshold',
        'tcp_socket': 'tcpSocket',
        'timeout_seconds': 'timeoutSeconds',
        'exec': 'exec',
    }

    __types__ = {
        'http_get': 'v1.HTTPGetAction',
        'tcp_socket': 'v1.TCPSocketAction',
        'exec': 'v1.ExecAction',
    }

    __required__ = set()

    initial_delay_seconds = None # integer
    success_threshold = None # integer
    period_seconds = None # integer
    http_get = None # v1.HTTPGetAction
    failure_threshold = None # integer
    tcp_socket = None # v1.TCPSocketAction
    timeout_seconds = None # integer
    exec = None # v1.ExecAction

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_BuildConfigSpec(Resource):

    """BuildConfigSpec describes when and how builds are created"""

    __kind__ = 'v1.BuildConfigSpec'

    __fields__ = {
        'run_policy': 'runPolicy',
        'strategy': 'strategy',
        'source': 'source',
        'triggers': 'triggers',
        'resources': 'resources',
        'post_commit': 'postCommit',
        'service_account': 'serviceAccount',
        'output': 'output',
        'completion_deadline_seconds': 'completionDeadlineSeconds',
        'revision': 'revision',
    }

    __types__ = {
        'strategy': 'v1.BuildStrategy',
        'source': 'v1.BuildSource',
        'triggers': 'v1.BuildTriggerPolicy',
        'revision': 'v1.SourceRevision',
        'resources': 'v1.ResourceRequirements',
        'output': 'v1.BuildOutput',
        'post_commit': 'v1.BuildPostCommitSpec',
    }

    __required__ = set([
        'strategy',
        'triggers',
    ])

    run_policy = None # string
    strategy = None # v1.BuildStrategy (required)
    source = None # v1.BuildSource
    triggers = None # array (required)
    resources = None # v1.ResourceRequirements
    post_commit = None # v1.BuildPostCommitSpec
    service_account = None # string
    output = None # v1.BuildOutput
    completion_deadline_seconds = None # integer
    revision = None # v1.SourceRevision

    def __init__(self, *, strategy, triggers, **_kwargs_):

        self.strategy = strategy
        self.triggers = triggers

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
class v1_EgressNetworkPolicyList(Resource):

    """EgressNetworkPolicyList is a collection of EgressNetworkPolicy"""

    __kind__ = 'v1.EgressNetworkPolicyList'

    __fields__ = {
        'items': 'items',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'unversioned.ListMeta',
        'items': 'v1.EgressNetworkPolicy',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    api_version = None # string
    metadata = None # unversioned.ListMeta
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'EgressNetworkPolicy'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_ImageList(Resource):

    """ImageList is a list of Image objects."""

    __kind__ = 'v1.ImageList'

    __fields__ = {
        'items': 'items',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'unversioned.ListMeta',
        'items': 'v1.Image',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    api_version = None # string
    metadata = None # unversioned.ListMeta
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'Image'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_RecreateDeploymentStrategyParams(Resource):

    """RecreateDeploymentStrategyParams are the input to the Recreate
    deployment strategy."""

    __kind__ = 'v1.RecreateDeploymentStrategyParams'

    __fields__ = {
        'post': 'post',
        'pre': 'pre',
        'timeout_seconds': 'timeoutSeconds',
        'mid': 'mid',
    }

    __types__ = {
        'post': 'v1.LifecycleHook',
        'pre': 'v1.LifecycleHook',
        'mid': 'v1.LifecycleHook',
    }

    __required__ = set()

    post = None # v1.LifecycleHook
    pre = None # v1.LifecycleHook
    timeout_seconds = None # integer
    mid = None # v1.LifecycleHook

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_Image(Resource):

    """Image is an immutable representation of a Docker image and metadata at
    a point in time."""

    __kind__ = 'v1.Image'

    __fields__ = {
        'docker_image_config': 'dockerImageConfig',
        'docker_image_manifest_media_type': 'dockerImageManifestMediaType',
        'docker_image_layers': 'dockerImageLayers',
        'signatures': 'signatures',
        'docker_image_manifest': 'dockerImageManifest',
        'docker_image_signatures': 'dockerImageSignatures',
        'docker_image_metadata': 'dockerImageMetadata',
        'docker_image_reference': 'dockerImageReference',
        'metadata': 'metadata',
        'docker_image_metadata_version': 'dockerImageMetadataVersion',
        'api_version': 'apiVersion',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
        'docker_image_signatures': 'v1.Image.dockerImageSignatures',
        'docker_image_layers': 'v1.ImageLayer',
        'signatures': 'v1.ImageSignature',
    }

    __required__ = set([
        'docker_image_layers',
    ])

    docker_image_config = None # string
    docker_image_manifest_media_type = None # string
    docker_image_layers = None # array (required)
    signatures = None # array
    docker_image_manifest = None # string
    docker_image_signatures = None # array
    docker_image_metadata = None # string
    docker_image_reference = None # string
    metadata = None # v1.ObjectMeta
    docker_image_metadata_version = None # string
    api_version = None # string
    kind = None # string

    def __init__(self, *, docker_image_layers, **_kwargs_):
        self.signatures = []
        self.docker_image_signatures = []

        self.kind = 'ImageSignature'

        self.docker_image_layers = docker_image_layers

        super().__init__(**_kwargs_)

@register_model
class v1_Container(Resource):

    """A single application container that you want to run within a pod."""

    __kind__ = 'v1.Container'

    __fields__ = {
        'tty': 'tty',
        'ports': 'ports',
        'stdin_once': 'stdinOnce',
        'args': 'args',
        'readiness_probe': 'readinessProbe',
        'resources': 'resources',
        'liveness_probe': 'livenessProbe',
        'name': 'name',
        'env': 'env',
        'termination_message_path': 'terminationMessagePath',
        'image': 'image',
        'working_dir': 'workingDir',
        'stdin': 'stdin',
        'security_context': 'securityContext',
        'volume_mounts': 'volumeMounts',
        'image_pull_policy': 'imagePullPolicy',
        'command': 'command',
        'lifecycle': 'lifecycle',
    }

    __types__ = {
        'volume_mounts': 'v1.VolumeMount',
        'env': 'v1.EnvVar',
        'security_context': 'v1.SecurityContext',
        'ports': 'v1.ContainerPort',
        'readiness_probe': 'v1.Probe',
        'resources': 'v1.ResourceRequirements',
        'liveness_probe': 'v1.Probe',
        'lifecycle': 'v1.Lifecycle',
    }

    __required__ = set([
        'name',
    ])

    tty = None # boolean
    ports = None # array
    stdin_once = None # boolean
    args = None # array
    readiness_probe = None # v1.Probe
    resources = None # v1.ResourceRequirements
    liveness_probe = None # v1.Probe
    name = None # string (required)
    env = None # array
    termination_message_path = None # string
    image = None # string
    working_dir = None # string
    stdin = None # boolean
    security_context = None # v1.SecurityContext
    volume_mounts = None # array
    image_pull_policy = None # string
    command = None # array
    lifecycle = None # v1.Lifecycle

    def __init__(self, *, name, **_kwargs_):
        self.ports = []
        self.args = []
        self.env = []
        self.volume_mounts = []
        self.command = []

        self.name = name

        super().__init__(**_kwargs_)

@register_model
class v1_RouteIngressCondition(Resource):

    """RouteIngressCondition contains details for the current condition of
    this pod."""

    __kind__ = 'v1.RouteIngressCondition'

    __fields__ = {
        'status': 'status',
        'message': 'message',
        'reason': 'reason',
        'last_transition_time': 'lastTransitionTime',
        'type': 'type',
    }

    __types__ = {
    }

    __required__ = set([
        'status',
        'type',
    ])

    status = None # string (required)
    message = None # string
    reason = None # string
    last_transition_time = None # string
    type = None # string (required)

    def __init__(self, *, status, type, **_kwargs_):

        self.status = status
        self.type = type

        super().__init__(**_kwargs_)

@register_model
class v1_ImageChangeCause(Resource):

    """ImageChangeCause contains information about the image that triggered a
    build"""

    __kind__ = 'v1.ImageChangeCause'

    __fields__ = {
        'image_id': 'imageID',
        'from_ref': 'fromRef',
    }

    __types__ = {
        'from_ref': 'v1.ObjectReference',
    }

    __required__ = set()

    image_id = None # string
    from_ref = None # v1.ObjectReference

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_OAuthClientAuthorization(Resource):

    """OAuthClientAuthorization describes an authorization created by an
    OAuth client"""

    __kind__ = 'v1.OAuthClientAuthorization'

    __fields__ = {
        'user_uid': 'userUID',
        'metadata': 'metadata',
        'scopes': 'scopes',
        'client_name': 'clientName',
        'user_name': 'userName',
        'api_version': 'apiVersion',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
    }

    __required__ = set()

    user_uid = None # string
    metadata = None # v1.ObjectMeta
    scopes = None # array
    client_name = None # string
    user_name = None # string
    api_version = None # string
    kind = None # string

    def __init__(self, **_kwargs_):
        self.scopes = []

        self.kind = 'ObjectMeta'

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
class unversioned_LabelSelector(Resource):

    """A label selector is a label query over a set of resources. The result
    of matchLabels and matchExpressions are ANDed. An empty label
    selector matches all objects. A null label selector matches no
    objects."""

    __kind__ = 'unversioned.LabelSelector'

    __fields__ = {
        'match_labels': 'matchLabels',
        'match_expressions': 'matchExpressions',
    }

    __types__ = {
        'match_expressions': 'unversioned.LabelSelectorRequirement',
    }

    __required__ = set()

    match_labels = None # object
    match_expressions = None # array

    def __init__(self, **_kwargs_):
        self.match_expressions = []

        super().__init__(**_kwargs_)

@register_model
class v1_NamedClusterRole(Resource):

    """NamedClusterRole relates a name with a cluster role"""

    __kind__ = 'v1.NamedClusterRole'

    __fields__ = {
        'role': 'role',
        'name': 'name',
    }

    __types__ = {
        'role': 'v1.ClusterRole',
    }

    __required__ = set([
        'name',
        'role',
    ])

    role = None # v1.ClusterRole (required)
    name = None # string (required)

    def __init__(self, *, name, role, **_kwargs_):

        self.name = name
        self.role = role

        super().__init__(**_kwargs_)

@register_model
class v1_ScopeRestriction(Resource):

    """ScopeRestriction describe one restriction on scopes.  Exactly one
    option must be non-nil."""

    __kind__ = 'v1.ScopeRestriction'

    __fields__ = {
        'literals': 'literals',
        'cluster_role': 'clusterRole',
    }

    __types__ = {
        'cluster_role': 'v1.ClusterRoleScopeRestriction',
    }

    __required__ = set()

    literals = None # array
    cluster_role = None # v1.ClusterRoleScopeRestriction

    def __init__(self, **_kwargs_):
        self.literals = []

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
        'status': 'status',
        'spec': 'spec',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'status': 'v1.DeploymentConfigStatus',
        'spec': 'v1.DeploymentConfigSpec',
        'metadata': 'v1.ObjectMeta',
    }

    __required__ = set([
        'spec',
        'status',
    ])

    status = None # v1.DeploymentConfigStatus (required)
    spec = None # v1.DeploymentConfigSpec (required)
    api_version = None # string
    metadata = None # v1.ObjectMeta
    kind = None # string

    def __init__(self, *, spec, status, **_kwargs_):

        self.kind = 'ObjectMeta'

        self.spec = spec
        self.status = status

        super().__init__(**_kwargs_)

@register_model
class v1_User(Resource):

    """User describes someone that makes requests to the API"""

    __kind__ = 'v1.User'

    __fields__ = {
        'groups': 'groups',
        'metadata': 'metadata',
        'kind': 'kind',
        'identities': 'identities',
        'api_version': 'apiVersion',
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
    metadata = None # v1.ObjectMeta
    kind = None # string
    identities = None # array (required)
    api_version = None # string
    full_name = None # string

    def __init__(self, *, groups, identities, **_kwargs_):

        self.kind = 'ObjectMeta'

        self.groups = groups
        self.identities = identities

        super().__init__(**_kwargs_)

@register_model
class v1_BuildTriggerCause(Resource):

    """BuildTriggerCause holds information about a triggered build. It is
    used for displaying build trigger data for each build and build
    configuration in oc describe. It is also used to describe which
    triggers led to the most recent update in the build configuration."""

    __kind__ = 'v1.BuildTriggerCause'

    __fields__ = {
        'message': 'message',
        'generic_web_hook': 'genericWebHook',
        'image_change_build': 'imageChangeBuild',
        'github_web_hook': 'githubWebHook',
    }

    __types__ = {
        'generic_web_hook': 'v1.GenericWebHookCause',
        'image_change_build': 'v1.ImageChangeCause',
        'github_web_hook': 'v1.GitHubWebHookCause',
    }

    __required__ = set()

    message = None # string
    generic_web_hook = None # v1.GenericWebHookCause
    image_change_build = None # v1.ImageChangeCause
    github_web_hook = None # v1.GitHubWebHookCause

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_NamedClusterRoleBinding(Resource):

    """NamedClusterRoleBinding relates a name with a cluster role binding"""

    __kind__ = 'v1.NamedClusterRoleBinding'

    __fields__ = {
        'role_binding': 'roleBinding',
        'name': 'name',
    }

    __types__ = {
        'role_binding': 'v1.ClusterRoleBinding',
    }

    __required__ = set([
        'name',
        'role_binding',
    ])

    role_binding = None # v1.ClusterRoleBinding (required)
    name = None # string (required)

    def __init__(self, *, name, role_binding, **_kwargs_):

        self.name = name
        self.role_binding = role_binding

        super().__init__(**_kwargs_)

@register_model
class v1_ClusterRoleScopeRestriction(Resource):

    """ClusterRoleScopeRestriction describes restrictions on cluster role
    scopes"""

    __kind__ = 'v1.ClusterRoleScopeRestriction'

    __fields__ = {
        'allow_escalation': 'allowEscalation',
        'namespaces': 'namespaces',
        'role_names': 'roleNames',
    }

    __types__ = {
    }

    __required__ = set([
        'allow_escalation',
        'namespaces',
        'role_names',
    ])

    allow_escalation = None # boolean (required)
    namespaces = None # array (required)
    role_names = None # array (required)

    def __init__(self, *, allow_escalation, namespaces, role_names, **_kwargs_):

        self.allow_escalation = allow_escalation
        self.namespaces = namespaces
        self.role_names = role_names

        super().__init__(**_kwargs_)

@register_model
class v1_ObjectFieldSelector(Resource):

    """ObjectFieldSelector selects an APIVersioned field of an object."""

    __kind__ = 'v1.ObjectFieldSelector'

    __fields__ = {
        'api_version': 'apiVersion',
        'field_path': 'fieldPath',
    }

    __types__ = {
    }

    __required__ = set([
        'field_path',
    ])

    api_version = None # string
    field_path = None # string (required)

    def __init__(self, *, field_path, **_kwargs_):

        self.field_path = field_path

        super().__init__(**_kwargs_)

@register_model
class v1_SignatureSubject(Resource):

    """SignatureSubject holds information about a person or entity who
    created the signature."""

    __kind__ = 'v1.SignatureSubject'

    __fields__ = {
        'common_name': 'commonName',
        'organization': 'organization',
        'public_key_id': 'publicKeyID',
    }

    __types__ = {
    }

    __required__ = set([
        'public_key_id',
    ])

    common_name = None # string
    organization = None # string
    public_key_id = None # string (required)

    def __init__(self, *, public_key_id, **_kwargs_):

        self.public_key_id = public_key_id

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
        'content': 'content',
        'metadata': 'metadata',
        'type': 'type',
        'signed_claims': 'signedClaims',
        'issued_by': 'issuedBy',
        'created': 'created',
        'api_version': 'apiVersion',
        'issued_to': 'issuedTo',
        'conditions': 'conditions',
        'image_identity': 'imageIdentity',
        'kind': 'kind',
    }

    __types__ = {
        'issued_by': 'v1.SignatureIssuer',
        'conditions': 'v1.SignatureCondition',
        'metadata': 'v1.ObjectMeta',
        'issued_to': 'v1.SignatureSubject',
    }

    __required__ = set([
        'content',
        'type',
    ])

    content = None # array (required)
    metadata = None # v1.ObjectMeta
    type = None # string (required)
    signed_claims = None # object
    issued_by = None # v1.SignatureIssuer
    created = None # string
    api_version = None # string
    issued_to = None # v1.SignatureSubject
    conditions = None # array
    image_identity = None # string
    kind = None # string

    def __init__(self, *, content, type, **_kwargs_):
        self.conditions = []

        self.kind = 'SignatureSubject'

        self.content = content
        self.type = type

        super().__init__(**_kwargs_)

@register_model
class v1_ClusterResourceQuota(Resource):

    """ClusterResourceQuota mirrors ResourceQuota at a cluster scope.  This
    object is easily convertible to synthetic ResourceQuota object to
    allow quota evaluation re-use."""

    __kind__ = 'v1.ClusterResourceQuota'

    __fields__ = {
        'status': 'status',
        'spec': 'spec',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'status': 'v1.ClusterResourceQuotaStatus',
        'spec': 'v1.ClusterResourceQuotaSpec',
        'metadata': 'v1.ObjectMeta',
    }

    __required__ = set([
        'metadata',
        'spec',
    ])

    status = None # v1.ClusterResourceQuotaStatus
    spec = None # v1.ClusterResourceQuotaSpec (required)
    api_version = None # string
    metadata = None # v1.ObjectMeta (required)
    kind = None # string

    def __init__(self, *, metadata, spec, **_kwargs_):

        self.kind = 'ObjectMeta'

        self.metadata = metadata
        self.spec = spec

        super().__init__(**_kwargs_)

@register_model
class v1_UserList(Resource):

    """UserList is a collection of Users"""

    __kind__ = 'v1.UserList'

    __fields__ = {
        'items': 'items',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'unversioned.ListMeta',
        'items': 'v1.User',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    api_version = None # string
    metadata = None # unversioned.ListMeta
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'User'

        self.items = items

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
class v1_RouteSpec(Resource):

    """RouteSpec describes the route the user wishes to exist."""

    __kind__ = 'v1.RouteSpec'

    __fields__ = {
        'port': 'port',
        'to': 'to',
        'alternate_backends': 'alternateBackends',
        'path': 'path',
        'host': 'host',
        'tls': 'tls',
    }

    __types__ = {
        'port': 'v1.RoutePort',
        'tls': 'v1.TLSConfig',
        'alternate_backends': 'v1.RouteTargetReference',
        'to': 'v1.RouteTargetReference',
    }

    __required__ = set([
        'host',
        'to',
    ])

    port = None # v1.RoutePort
    to = None # v1.RouteTargetReference (required)
    alternate_backends = None # array
    path = None # string
    host = None # string (required)
    tls = None # v1.TLSConfig

    def __init__(self, *, host, to, **_kwargs_):
        self.alternate_backends = []

        self.host = host
        self.to = to

        super().__init__(**_kwargs_)

@register_model
class v1_AppliedClusterResourceQuotaList(Resource):

    """AppliedClusterResourceQuotaList is a collection of
    AppliedClusterResourceQuotas"""

    __kind__ = 'v1.AppliedClusterResourceQuotaList'

    __fields__ = {
        'items': 'items',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'unversioned.ListMeta',
        'items': 'v1.AppliedClusterResourceQuota',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    api_version = None # string
    metadata = None # unversioned.ListMeta
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'AppliedClusterResourceQuota'

        self.items = items

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
class unversioned_StatusDetails(Resource):

    """StatusDetails is a set of additional properties that MAY be set by the
    server to provide additional information about a response. The
    Reason field of a Status object defines what attributes will be
    set. Clients must ignore fields that do not match the defined type
    of each attribute, and should assume that any attribute may be
    empty, invalid, or under defined."""

    __kind__ = 'unversioned.StatusDetails'

    __fields__ = {
        'retry_after_seconds': 'retryAfterSeconds',
        'causes': 'causes',
        'group': 'group',
        'name': 'name',
        'kind': 'kind',
    }

    __types__ = {
        'causes': 'unversioned.StatusCause',
    }

    __required__ = set()

    retry_after_seconds = None # integer
    causes = None # array
    group = None # string
    name = None # string
    kind = None # string

    def __init__(self, **_kwargs_):
        self.causes = []

        self.kind = 'StatusCause'

        super().__init__(**_kwargs_)

@register_model
class v1_ClusterPolicyBinding(Resource):

    """ClusterPolicyBinding is a object that holds all the
    ClusterRoleBindings for a particular namespace.  There is one
    ClusterPolicyBinding document per referenced ClusterPolicy
    namespace"""

    __kind__ = 'v1.ClusterPolicyBinding'

    __fields__ = {
        'role_bindings': 'roleBindings',
        'metadata': 'metadata',
        'last_modified': 'lastModified',
        'policy_ref': 'policyRef',
        'api_version': 'apiVersion',
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

    role_bindings = None # array (required)
    metadata = None # v1.ObjectMeta
    last_modified = None # string (required)
    policy_ref = None # v1.ObjectReference (required)
    api_version = None # string
    kind = None # string

    def __init__(self, *, last_modified, policy_ref, role_bindings, **_kwargs_):

        self.kind = 'NamedClusterRoleBinding'

        self.last_modified = last_modified
        self.policy_ref = policy_ref
        self.role_bindings = role_bindings

        super().__init__(**_kwargs_)

@register_model
class v1_DeploymentConfigSpec(Resource):

    """DeploymentConfigSpec represents the desired state of the deployment."""

    __kind__ = 'v1.DeploymentConfigSpec'

    __fields__ = {
        'test': 'test',
        'paused': 'paused',
        'strategy': 'strategy',
        'triggers': 'triggers',
        'template': 'template',
        'replicas': 'replicas',
        'selector': 'selector',
        'min_ready_seconds': 'minReadySeconds',
        'revision_history_limit': 'revisionHistoryLimit',
    }

    __types__ = {
        'template': 'v1.PodTemplateSpec',
        'strategy': 'v1.DeploymentStrategy',
        'triggers': 'v1.DeploymentTriggerPolicy',
    }

    __required__ = set([
        'replicas',
        'strategy',
        'test',
        'triggers',
    ])

    test = None # boolean (required)
    paused = None # boolean
    strategy = None # v1.DeploymentStrategy (required)
    triggers = None # array (required)
    template = None # v1.PodTemplateSpec
    replicas = None # integer (required)
    selector = None # object
    min_ready_seconds = None # integer
    revision_history_limit = None # integer

    def __init__(self, *, replicas, strategy, test, triggers, **_kwargs_):

        self.replicas = replicas
        self.strategy = strategy
        self.test = test
        self.triggers = triggers

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
class v1_SignatureIssuer(Resource):

    """SignatureIssuer holds information about an issuer of signing
    certificate or key."""

    __kind__ = 'v1.SignatureIssuer'

    __fields__ = {
        'common_name': 'commonName',
        'organization': 'organization',
    }

    __types__ = {
    }

    __required__ = set()

    common_name = None # string
    organization = None # string

    def __init__(self, **_kwargs_):

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
class v1_SecretKeySelector(Resource):

    """SecretKeySelector selects a key of a Secret."""

    __kind__ = 'v1.SecretKeySelector'

    __fields__ = {
        'key': 'key',
        'name': 'name',
    }

    __types__ = {
    }

    __required__ = set([
        'key',
    ])

    key = None # string (required)
    name = None # string

    def __init__(self, *, key, **_kwargs_):

        self.key = key

        super().__init__(**_kwargs_)

@register_model
class v1_BuildRequest(Resource):

    """BuildRequest is the resource used to pass parameters to build
    generator"""

    __kind__ = 'v1.BuildRequest'

    __fields__ = {
        'env': 'env',
        'metadata': 'metadata',
        'triggered_by_image': 'triggeredByImage',
        'triggered_by': 'triggeredBy',
        'from_': 'from',
        'last_version': 'lastVersion',
        'api_version': 'apiVersion',
        'binary': 'binary',
        'kind': 'kind',
        'revision': 'revision',
    }

    __types__ = {
        'triggered_by': 'v1.BuildTriggerCause',
        'metadata': 'v1.ObjectMeta',
        'env': 'v1.EnvVar',
        'revision': 'v1.SourceRevision',
        'from_': 'v1.ObjectReference',
        'triggered_by_image': 'v1.ObjectReference',
        'binary': 'v1.BinaryBuildSource',
    }

    __required__ = set([
        'triggered_by',
    ])

    env = None # array
    metadata = None # v1.ObjectMeta
    triggered_by_image = None # v1.ObjectReference
    triggered_by = None # array (required)
    from_ = None # v1.ObjectReference
    last_version = None # integer
    api_version = None # string
    binary = None # v1.BinaryBuildSource
    kind = None # string
    revision = None # v1.SourceRevision

    def __init__(self, *, triggered_by, **_kwargs_):
        self.env = []

        self.kind = 'BinaryBuildSource'

        self.triggered_by = triggered_by

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
class v1_PolicyBinding(Resource):

    """PolicyBinding is a object that holds all the RoleBindings for a
    particular namespace.  There is one PolicyBinding document per
    referenced Policy namespace"""

    __kind__ = 'v1.PolicyBinding'

    __fields__ = {
        'role_bindings': 'roleBindings',
        'metadata': 'metadata',
        'last_modified': 'lastModified',
        'policy_ref': 'policyRef',
        'api_version': 'apiVersion',
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

    role_bindings = None # array (required)
    metadata = None # v1.ObjectMeta
    last_modified = None # string (required)
    policy_ref = None # v1.ObjectReference (required)
    api_version = None # string
    kind = None # string

    def __init__(self, *, last_modified, policy_ref, role_bindings, **_kwargs_):

        self.kind = 'NamedRoleBinding'

        self.last_modified = last_modified
        self.policy_ref = policy_ref
        self.role_bindings = role_bindings

        super().__init__(**_kwargs_)

@register_model
class v1_ClusterPolicy(Resource):

    """ClusterPolicy is a object that holds all the ClusterRoles for a
    particular namespace.  There is at most one ClusterPolicy document
    per namespace."""

    __kind__ = 'v1.ClusterPolicy'

    __fields__ = {
        'roles': 'roles',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'last_modified': 'lastModified',
        'kind': 'kind',
    }

    __types__ = {
        'roles': 'v1.NamedClusterRole',
        'metadata': 'v1.ObjectMeta',
    }

    __required__ = set([
        'last_modified',
        'roles',
    ])

    roles = None # array (required)
    api_version = None # string
    metadata = None # v1.ObjectMeta
    last_modified = None # string (required)
    kind = None # string

    def __init__(self, *, last_modified, roles, **_kwargs_):

        self.kind = 'ObjectMeta'

        self.last_modified = last_modified
        self.roles = roles

        super().__init__(**_kwargs_)

@register_model
class v1_RBDVolumeSource(Resource):

    """Represents a Rados Block Device mount that lasts the lifetime of a
    pod. RBD volumes support ownership management and SELinux
    relabeling."""

    __kind__ = 'v1.RBDVolumeSource'

    __fields__ = {
        'image': 'image',
        'keyring': 'keyring',
        'monitors': 'monitors',
        'read_only': 'readOnly',
        'fs_type': 'fsType',
        'secret_ref': 'secretRef',
        'user': 'user',
        'pool': 'pool',
    }

    __types__ = {
        'secret_ref': 'v1.LocalObjectReference',
    }

    __required__ = set([
        'image',
        'monitors',
    ])

    image = None # string (required)
    keyring = None # string
    monitors = None # array (required)
    read_only = None # boolean
    fs_type = None # string
    secret_ref = None # v1.LocalObjectReference
    user = None # string
    pool = None # string

    def __init__(self, *, image, monitors, **_kwargs_):

        self.image = image
        self.monitors = monitors

        super().__init__(**_kwargs_)

@register_model
class v1_DownwardAPIVolumeFile(Resource):

    """DownwardAPIVolumeFile represents information to create the file
    containing the pod field"""

    __kind__ = 'v1.DownwardAPIVolumeFile'

    __fields__ = {
        'path': 'path',
        'resource_field_ref': 'resourceFieldRef',
        'field_ref': 'fieldRef',
    }

    __types__ = {
        'resource_field_ref': 'v1.ResourceFieldSelector',
        'field_ref': 'v1.ObjectFieldSelector',
    }

    __required__ = set([
        'path',
    ])

    path = None # string (required)
    resource_field_ref = None # v1.ResourceFieldSelector
    field_ref = None # v1.ObjectFieldSelector

    def __init__(self, *, path, **_kwargs_):

        self.path = path

        super().__init__(**_kwargs_)

@register_model
class v1_NamedRoleBinding(Resource):

    """NamedRoleBinding relates a role binding with a name"""

    __kind__ = 'v1.NamedRoleBinding'

    __fields__ = {
        'role_binding': 'roleBinding',
        'name': 'name',
    }

    __types__ = {
        'role_binding': 'v1.RoleBinding',
    }

    __required__ = set([
        'name',
        'role_binding',
    ])

    role_binding = None # v1.RoleBinding (required)
    name = None # string (required)

    def __init__(self, *, name, role_binding, **_kwargs_):

        self.name = name
        self.role_binding = role_binding

        super().__init__(**_kwargs_)

@register_model
class unversioned_Status(Resource):

    """Status is a return value for calls that don't return other objects."""

    __kind__ = 'unversioned.Status'

    __fields__ = {
        'message': 'message',
        'reason': 'reason',
        'metadata': 'metadata',
        'details': 'details',
        'status': 'status',
        'api_version': 'apiVersion',
        'code': 'code',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'unversioned.ListMeta',
        'details': 'unversioned.StatusDetails',
    }

    __required__ = set()

    message = None # string
    reason = None # string
    metadata = None # unversioned.ListMeta
    details = None # unversioned.StatusDetails
    status = None # string
    api_version = None # string
    code = None # integer
    kind = None # string

    def __init__(self, **_kwargs_):

        self.kind = 'StatusDetails'

        super().__init__(**_kwargs_)

@register_model
class v1_Template(Resource):

    """Template contains the inputs needed to produce a Config."""

    __kind__ = 'v1.Template'

    __fields__ = {
        'message': 'message',
        'metadata': 'metadata',
        'objects': 'objects',
        'api_version': 'apiVersion',
        'parameters': 'parameters',
        'kind': 'kind',
        'labels': 'labels',
    }

    __types__ = {
        'parameters': 'v1.Parameter',
        'metadata': 'v1.ObjectMeta',
        'objects': 'runtime.RawExtension',
    }

    __required__ = set([
        'objects',
    ])

    message = None # string
    metadata = None # v1.ObjectMeta
    objects = None # array (required)
    api_version = None # string
    parameters = None # array
    kind = None # string
    labels = None # object

    def __init__(self, *, objects, **_kwargs_):
        self.parameters = []

        self.kind = 'RawExtension'

        self.objects = objects

        super().__init__(**_kwargs_)

@register_model
class v1_ResourceQuotaStatus(Resource):

    """ResourceQuotaStatus defines the enforced hard limits and observed use."""

    __kind__ = 'v1.ResourceQuotaStatus'

    __fields__ = {
        'used': 'used',
        'hard': 'hard',
    }

    __types__ = {
    }

    __required__ = set()

    used = None # object
    hard = None # object

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_ClusterResourceQuotaList(Resource):

    """ClusterResourceQuotaList is a collection of ClusterResourceQuotas"""

    __kind__ = 'v1.ClusterResourceQuotaList'

    __fields__ = {
        'items': 'items',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'unversioned.ListMeta',
        'items': 'v1.ClusterResourceQuota',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    api_version = None # string
    metadata = None # unversioned.ListMeta
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'ClusterResourceQuota'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_TagReference(Resource):

    """TagReference specifies optional annotations for images using this tag
    and an optional reference to an ImageStreamTag, ImageStreamImage,
    or DockerImage this tag should track."""

    __kind__ = 'v1.TagReference'

    __fields__ = {
        'reference': 'reference',
        'generation': 'generation',
        'annotations': 'annotations',
        'import_policy': 'importPolicy',
        'from_': 'from',
        'name': 'name',
    }

    __types__ = {
        'from_': 'v1.ObjectReference',
        'import_policy': 'v1.TagImportPolicy',
    }

    __required__ = set([
        'annotations',
        'generation',
        'name',
    ])

    reference = None # boolean
    generation = None # integer (required)
    annotations = None # object (required)
    import_policy = None # v1.TagImportPolicy
    from_ = None # v1.ObjectReference
    name = None # string (required)

    def __init__(self, *, annotations, generation, name, **_kwargs_):

        self.annotations = annotations
        self.generation = generation
        self.name = name

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
class v1_DeploymentConfigRollbackSpec(Resource):

    """DeploymentConfigRollbackSpec represents the options for rollback
    generation."""

    __kind__ = 'v1.DeploymentConfigRollbackSpec'

    __fields__ = {
        'include_template': 'includeTemplate',
        'include_strategy': 'includeStrategy',
        'from_': 'from',
        'include_triggers': 'includeTriggers',
        'revision': 'revision',
        'include_replication_meta': 'includeReplicationMeta',
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

    include_template = None # boolean (required)
    include_strategy = None # boolean (required)
    from_ = None # v1.ObjectReference (required)
    include_triggers = None # boolean (required)
    revision = None # integer
    include_replication_meta = None # boolean (required)

    def __init__(self, *, from_, include_replication_meta, include_strategy, include_template, include_triggers, **_kwargs_):

        self.from_ = from_
        self.include_replication_meta = include_replication_meta
        self.include_strategy = include_strategy
        self.include_template = include_template
        self.include_triggers = include_triggers

        super().__init__(**_kwargs_)

@register_model
class v1_Group(Resource):

    """Group represents a referenceable set of Users"""

    __kind__ = 'v1.Group'

    __fields__ = {
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
        'users': 'users',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
    }

    __required__ = set([
        'users',
    ])

    api_version = None # string
    metadata = None # v1.ObjectMeta
    kind = None # string
    users = None # array (required)

    def __init__(self, *, users, **_kwargs_):

        self.kind = 'ObjectMeta'

        self.users = users

        super().__init__(**_kwargs_)

@register_model
class v1_ClusterResourceQuotaSpec(Resource):

    """ClusterResourceQuotaSpec defines the desired quota restrictions"""

    __kind__ = 'v1.ClusterResourceQuotaSpec'

    __fields__ = {
        'quota': 'quota',
        'selector': 'selector',
    }

    __types__ = {
        'selector': 'v1.ClusterResourceQuotaSelector',
        'quota': 'v1.ResourceQuotaSpec',
    }

    __required__ = set([
        'quota',
        'selector',
    ])

    quota = None # v1.ResourceQuotaSpec (required)
    selector = None # v1.ClusterResourceQuotaSelector (required)

    def __init__(self, *, quota, selector, **_kwargs_):

        self.quota = quota
        self.selector = selector

        super().__init__(**_kwargs_)

@register_model
class v1_ResourceQuotaSpec(Resource):

    """ResourceQuotaSpec defines the desired hard limits to enforce for
    Quota."""

    __kind__ = 'v1.ResourceQuotaSpec'

    __fields__ = {
        'scopes': 'scopes',
        'hard': 'hard',
    }

    __types__ = {
        'scopes': 'v1.ResourceQuotaScope',
    }

    __required__ = set()

    scopes = None # array
    hard = None # object

    def __init__(self, **_kwargs_):
        self.scopes = []

        super().__init__(**_kwargs_)

@register_model
class v1_RouteTargetReference(Resource):

    """RouteTargetReference specifies the target that resolve into endpoints.
    Only the 'Service' kind is allowed. Use 'weight' field to
    emphasize one over others."""

    __kind__ = 'v1.RouteTargetReference'

    __fields__ = {
        'weight': 'weight',
        'name': 'name',
        'kind': 'kind',
    }

    __types__ = {
    }

    __required__ = set([
        'kind',
        'name',
    ])

    weight = None # integer
    name = None # string (required)
    kind = None # string (required)

    def __init__(self, *, kind, name, **_kwargs_):

        self.kind = 'RouteTargetReference'

        self.kind = kind
        self.name = name

        super().__init__(**_kwargs_)

@register_model
class v1_LocalResourceAccessReview(Resource):

    """LocalResourceAccessReview is a means to request a list of which users
    and groups are authorized to perform the action specified by spec
    in a particular namespace"""

    __kind__ = 'v1.LocalResourceAccessReview'

    __fields__ = {
        'content': 'content',
        'resource_name': 'resourceName',
        'namespace': 'namespace',
        'verb': 'verb',
        'resource_api_version': 'resourceAPIVersion',
        'api_version': 'apiVersion',
        'resource': 'resource',
        'resource_api_group': 'resourceAPIGroup',
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

    content = None # string
    resource_name = None # string (required)
    namespace = None # string (required)
    verb = None # string (required)
    resource_api_version = None # string (required)
    api_version = None # string
    resource = None # string (required)
    resource_api_group = None # string (required)
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
class v1_OAuthAuthorizeToken(Resource):

    """OAuthAuthorizeToken describes an OAuth authorization token"""

    __kind__ = 'v1.OAuthAuthorizeToken'

    __fields__ = {
        'user_uid': 'userUID',
        'user_name': 'userName',
        'expires_in': 'expiresIn',
        'metadata': 'metadata',
        'scopes': 'scopes',
        'client_name': 'clientName',
        'state': 'state',
        'api_version': 'apiVersion',
        'redirect_uri': 'redirectURI',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
    }

    __required__ = set()

    user_uid = None # string
    user_name = None # string
    expires_in = None # integer
    metadata = None # v1.ObjectMeta
    scopes = None # array
    client_name = None # string
    state = None # string
    api_version = None # string
    redirect_uri = None # string
    kind = None # string

    def __init__(self, **_kwargs_):
        self.scopes = []

        self.kind = 'ObjectMeta'

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
class v1_LifecycleHook(Resource):

    """LifecycleHook defines a specific deployment lifecycle action. Only one
    type of action may be specified at any time."""

    __kind__ = 'v1.LifecycleHook'

    __fields__ = {
        'exec_new_pod': 'execNewPod',
        'failure_policy': 'failurePolicy',
        'tag_images': 'tagImages',
    }

    __types__ = {
        'exec_new_pod': 'v1.ExecNewPodHook',
        'tag_images': 'v1.TagImageHook',
    }

    __required__ = set([
        'failure_policy',
    ])

    exec_new_pod = None # v1.ExecNewPodHook
    failure_policy = None # string (required)
    tag_images = None # array

    def __init__(self, *, failure_policy, **_kwargs_):
        self.tag_images = []

        self.failure_policy = failure_policy

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
class v1_GroupList(Resource):

    """GroupList is a collection of Groups"""

    __kind__ = 'v1.GroupList'

    __fields__ = {
        'items': 'items',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'unversioned.ListMeta',
        'items': 'v1.Group',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    api_version = None # string
    metadata = None # unversioned.ListMeta
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'Group'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_BuildList(Resource):

    """BuildList is a collection of Builds."""

    __kind__ = 'v1.BuildList'

    __fields__ = {
        'items': 'items',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'unversioned.ListMeta',
        'items': 'v1.Build',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    api_version = None # string
    metadata = None # unversioned.ListMeta
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'Build'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_Role(Resource):

    """Role is a logical grouping of PolicyRules that can be referenced as a
    unit by RoleBindings."""

    __kind__ = 'v1.Role'

    __fields__ = {
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'rules': 'rules',
        'kind': 'kind',
    }

    __types__ = {
        'rules': 'v1.PolicyRule',
        'metadata': 'v1.ObjectMeta',
    }

    __required__ = set([
        'rules',
    ])

    api_version = None # string
    metadata = None # v1.ObjectMeta
    rules = None # array (required)
    kind = None # string

    def __init__(self, *, rules, **_kwargs_):

        self.kind = 'ObjectMeta'

        self.rules = rules

        super().__init__(**_kwargs_)

@register_model
class unversioned_APIResource(Resource):

    """APIResource specifies the name of a resource and whether it is
    namespaced."""

    __kind__ = 'unversioned.APIResource'

    __fields__ = {
        'namespaced': 'namespaced',
        'name': 'name',
        'kind': 'kind',
    }

    __types__ = {
    }

    __required__ = set([
        'kind',
        'name',
        'namespaced',
    ])

    namespaced = None # boolean (required)
    name = None # string (required)
    kind = None # string (required)

    def __init__(self, *, kind, name, namespaced, **_kwargs_):

        self.kind = 'APIResource'

        self.kind = kind
        self.name = name
        self.namespaced = namespaced

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
        'volume_id': 'volumeID',
        'read_only': 'readOnly',
        'fs_type': 'fsType',
        'partition': 'partition',
    }

    __types__ = {
    }

    __required__ = set([
        'volume_id',
    ])

    volume_id = None # string (required)
    read_only = None # boolean
    fs_type = None # string
    partition = None # integer

    def __init__(self, *, volume_id, **_kwargs_):

        self.volume_id = volume_id

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
class v1_CephFSVolumeSource(Resource):

    """Represents a Ceph Filesystem mount that lasts the lifetime of a pod
    Cephfs volumes do not support ownership management or SELinux
    relabeling."""

    __kind__ = 'v1.CephFSVolumeSource'

    __fields__ = {
        'path': 'path',
        'secret_file': 'secretFile',
        'monitors': 'monitors',
        'read_only': 'readOnly',
        'secret_ref': 'secretRef',
        'user': 'user',
    }

    __types__ = {
        'secret_ref': 'v1.LocalObjectReference',
    }

    __required__ = set([
        'monitors',
    ])

    path = None # string
    secret_file = None # string
    monitors = None # array (required)
    read_only = None # boolean
    secret_ref = None # v1.LocalObjectReference
    user = None # string

    def __init__(self, *, monitors, **_kwargs_):

        self.monitors = monitors

        super().__init__(**_kwargs_)

@register_model
class v1_EnvVar(Resource):

    """EnvVar represents an environment variable present in a Container."""

    __kind__ = 'v1.EnvVar'

    __fields__ = {
        'value_from': 'valueFrom',
        'value': 'value',
        'name': 'name',
    }

    __types__ = {
        'value_from': 'v1.EnvVarSource',
    }

    __required__ = set([
        'name',
    ])

    value_from = None # v1.EnvVarSource
    value = None # string
    name = None # string (required)

    def __init__(self, *, name, **_kwargs_):

        self.name = name

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
class v1_ImageSource(Resource):

    """ImageSource describes an image that is used as source for the build"""

    __kind__ = 'v1.ImageSource'

    __fields__ = {
        'from_': 'from',
        'paths': 'paths',
        'pull_secret': 'pullSecret',
    }

    __types__ = {
        'from_': 'v1.ObjectReference',
        'paths': 'v1.ImageSourcePath',
        'pull_secret': 'v1.LocalObjectReference',
    }

    __required__ = set([
        'from_',
        'paths',
    ])

    from_ = None # v1.ObjectReference (required)
    paths = None # array (required)
    pull_secret = None # v1.LocalObjectReference

    def __init__(self, *, from_, paths, **_kwargs_):

        self.from_ = from_
        self.paths = paths

        super().__init__(**_kwargs_)

@register_model
class v1_ImageStreamTag(Resource):

    """ImageStreamTag represents an Image that is retrieved by tag name from
    an ImageStream."""

    __kind__ = 'v1.ImageStreamTag'

    __fields__ = {
        'generation': 'generation',
        'metadata': 'metadata',
        'image': 'image',
        'tag': 'tag',
        'api_version': 'apiVersion',
        'conditions': 'conditions',
        'kind': 'kind',
    }

    __types__ = {
        'tag': 'v1.TagReference',
        'metadata': 'v1.ObjectMeta',
        'image': 'v1.Image',
        'conditions': 'v1.TagEventCondition',
    }

    __required__ = set([
        'generation',
        'image',
        'tag',
    ])

    generation = None # integer (required)
    metadata = None # v1.ObjectMeta
    image = None # v1.Image (required)
    tag = None # v1.TagReference (required)
    api_version = None # string
    conditions = None # array
    kind = None # string

    def __init__(self, *, generation, image, tag, **_kwargs_):
        self.conditions = []

        self.kind = 'TagEventCondition'

        self.generation = generation
        self.image = image
        self.tag = tag

        super().__init__(**_kwargs_)

@register_model
class v1_Secret(Resource):

    """Secret holds secret data of a certain type. The total bytes of the
    values in the Data field must be less than MaxSecretSize bytes."""

    __kind__ = 'v1.Secret'

    __fields__ = {
        'type': 'type',
        'metadata': 'metadata',
        'data': 'data',
        'string_data': 'stringData',
        'api_version': 'apiVersion',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'v1.ObjectMeta',
    }

    __required__ = set()

    type = None # string
    metadata = None # v1.ObjectMeta
    data = None # object
    string_data = None # object
    api_version = None # string
    kind = None # string

    def __init__(self, **_kwargs_):

        self.kind = 'ObjectMeta'

        super().__init__(**_kwargs_)

@register_model
class v1_SourceBuildStrategy(Resource):

    """SourceBuildStrategy defines input parameters specific to an Source
    build."""

    __kind__ = 'v1.SourceBuildStrategy'

    __fields__ = {
        'env': 'env',
        'pull_secret': 'pullSecret',
        'runtime_image': 'runtimeImage',
        'incremental': 'incremental',
        'scripts': 'scripts',
        'from_': 'from',
        'runtime_artifacts': 'runtimeArtifacts',
        'force_pull': 'forcePull',
    }

    __types__ = {
        'env': 'v1.EnvVar',
        'from_': 'v1.ObjectReference',
        'pull_secret': 'v1.LocalObjectReference',
        'runtime_image': 'v1.ObjectReference',
        'runtime_artifacts': 'v1.ImageSourcePath',
    }

    __required__ = set([
        'from_',
    ])

    env = None # array
    pull_secret = None # v1.LocalObjectReference
    runtime_image = None # v1.ObjectReference
    incremental = None # boolean
    scripts = None # string
    from_ = None # v1.ObjectReference (required)
    runtime_artifacts = None # array
    force_pull = None # boolean

    def __init__(self, *, from_, **_kwargs_):
        self.env = []
        self.runtime_artifacts = []

        self.from_ = from_

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
        'spec': 'spec',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'spec': 'v1.EgressNetworkPolicySpec',
        'metadata': 'v1.ObjectMeta',
    }

    __required__ = set([
        'spec',
    ])

    spec = None # v1.EgressNetworkPolicySpec (required)
    api_version = None # string
    metadata = None # v1.ObjectMeta
    kind = None # string

    def __init__(self, *, spec, **_kwargs_):

        self.kind = 'ObjectMeta'

        self.spec = spec

        super().__init__(**_kwargs_)

@register_model
class unversioned_StatusCause(Resource):

    """StatusCause provides more information about an api.Status failure,
    including cases when multiple errors are encountered."""

    __kind__ = 'unversioned.StatusCause'

    __fields__ = {
        'message': 'message',
        'reason': 'reason',
        'field': 'field',
    }

    __types__ = {
    }

    __required__ = set()

    message = None # string
    reason = None # string
    field = None # string

    def __init__(self, **_kwargs_):

        super().__init__(**_kwargs_)

@register_model
class v1_Route(Resource):

    """Route encapsulates the inputs needed to connect an alias to endpoints."""

    __kind__ = 'v1.Route'

    __fields__ = {
        'status': 'status',
        'spec': 'spec',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'status': 'v1.RouteStatus',
        'spec': 'v1.RouteSpec',
        'metadata': 'v1.ObjectMeta',
    }

    __required__ = set([
        'spec',
        'status',
    ])

    status = None # v1.RouteStatus (required)
    spec = None # v1.RouteSpec (required)
    api_version = None # string
    metadata = None # v1.ObjectMeta
    kind = None # string

    def __init__(self, *, spec, status, **_kwargs_):

        self.kind = 'ObjectMeta'

        self.spec = spec
        self.status = status

        super().__init__(**_kwargs_)

@register_model
class v1_FCVolumeSource(Resource):

    """Represents a Fibre Channel volume. Fibre Channel volumes can only be
    mounted as read/write once. Fibre Channel volumes support
    ownership management and SELinux relabeling."""

    __kind__ = 'v1.FCVolumeSource'

    __fields__ = {
        'read_only': 'readOnly',
        'fs_type': 'fsType',
        'lun': 'lun',
        'target_ww_ns': 'targetWWNs',
    }

    __types__ = {
    }

    __required__ = set([
        'lun',
        'target_ww_ns',
    ])

    read_only = None # boolean
    fs_type = None # string
    lun = None # integer (required)
    target_ww_ns = None # array (required)

    def __init__(self, *, lun, target_ww_ns, **_kwargs_):

        self.lun = lun
        self.target_ww_ns = target_ww_ns

        super().__init__(**_kwargs_)

@register_model
class v1_GlusterfsVolumeSource(Resource):

    """Represents a Glusterfs mount that lasts the lifetime of a pod.
    Glusterfs volumes do not support ownership management or SELinux
    relabeling."""

    __kind__ = 'v1.GlusterfsVolumeSource'

    __fields__ = {
        'path': 'path',
        'read_only': 'readOnly',
        'endpoints': 'endpoints',
    }

    __types__ = {
    }

    __required__ = set([
        'endpoints',
        'path',
    ])

    path = None # string (required)
    read_only = None # boolean
    endpoints = None # string (required)

    def __init__(self, *, endpoints, path, **_kwargs_):

        self.endpoints = endpoints
        self.path = path

        super().__init__(**_kwargs_)

@register_model
class v1_RoleBindingList(Resource):

    """RoleBindingList is a collection of RoleBindings"""

    __kind__ = 'v1.RoleBindingList'

    __fields__ = {
        'items': 'items',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'unversioned.ListMeta',
        'items': 'v1.RoleBinding',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    api_version = None # string
    metadata = None # unversioned.ListMeta
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'RoleBinding'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_ImageStreamTagList(Resource):

    """ImageStreamTagList is a list of ImageStreamTag objects."""

    __kind__ = 'v1.ImageStreamTagList'

    __fields__ = {
        'items': 'items',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'unversioned.ListMeta',
        'items': 'v1.ImageStreamTag',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    api_version = None # string
    metadata = None # unversioned.ListMeta
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'ImageStreamTag'

        self.items = items

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
class v1_ExecNewPodHook(Resource):

    """ExecNewPodHook is a hook implementation which runs a command in a new
    pod based on the specified container which is assumed to be part
    of the deployment template."""

    __kind__ = 'v1.ExecNewPodHook'

    __fields__ = {
        'env': 'env',
        'volumes': 'volumes',
        'container_name': 'containerName',
        'command': 'command',
    }

    __types__ = {
        'env': 'v1.EnvVar',
    }

    __required__ = set([
        'command',
        'container_name',
    ])

    env = None # array
    volumes = None # array
    container_name = None # string (required)
    command = None # array (required)

    def __init__(self, *, command, container_name, **_kwargs_):
        self.env = []
        self.volumes = []

        self.command = command
        self.container_name = container_name

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
class v1_GCEPersistentDiskVolumeSource(Resource):

    """Represents a Persistent Disk resource in Google Compute Engine.  A GCE
    PD must exist before mounting to a container. The disk must also
    be in the same GCE project and zone as the kubelet. A GCE PD can
    only be mounted as read/write once or read-only many times. GCE
    PDs support ownership management and SELinux relabeling."""

    __kind__ = 'v1.GCEPersistentDiskVolumeSource'

    __fields__ = {
        'read_only': 'readOnly',
        'pd_name': 'pdName',
        'fs_type': 'fsType',
        'partition': 'partition',
    }

    __types__ = {
    }

    __required__ = set([
        'pd_name',
    ])

    read_only = None # boolean
    pd_name = None # string (required)
    fs_type = None # string
    partition = None # integer

    def __init__(self, *, pd_name, **_kwargs_):

        self.pd_name = pd_name

        super().__init__(**_kwargs_)

@register_model
class v1_RouteList(Resource):

    """RouteList is a collection of Routes."""

    __kind__ = 'v1.RouteList'

    __fields__ = {
        'items': 'items',
        'api_version': 'apiVersion',
        'metadata': 'metadata',
        'kind': 'kind',
    }

    __types__ = {
        'metadata': 'unversioned.ListMeta',
        'items': 'v1.Route',
    }

    __required__ = set([
        'items',
    ])

    items = None # array (required)
    api_version = None # string
    metadata = None # unversioned.ListMeta
    kind = None # string

    def __init__(self, *, items, **_kwargs_):

        self.kind = 'Route'

        self.items = items

        super().__init__(**_kwargs_)

@register_model
class v1_OwnerReference(Resource):

    """OwnerReference contains enough information to let you identify an
    owning object. Currently, an owning object must be in the same
    namespace, so there is no namespace field."""

    __kind__ = 'v1.OwnerReference'

    __fields__ = {
        'controller': 'controller',
        'api_version': 'apiVersion',
        'name': 'name',
        'kind': 'kind',
        'uid': 'uid',
    }

    __types__ = {
    }

    __required__ = set([
        'api_version',
        'kind',
        'name',
        'uid',
    ])

    controller = None # boolean
    api_version = None # string (required)
    name = None # string (required)
    kind = None # string (required)
    uid = None # string (required)

    def __init__(self, *, api_version, kind, name, uid, **_kwargs_):

        self.kind = 'OwnerReference'

        self.api_version = api_version
        self.kind = kind
        self.name = name
        self.uid = uid

        super().__init__(**_kwargs_)

@register_model
class v1_JenkinsPipelineBuildStrategy(Resource):

    """JenkinsPipelineBuildStrategy holds parameters specific to a Jenkins
    Pipeline build. This strategy is experimental."""

    __kind__ = 'v1.JenkinsPipelineBuildStrategy'

    __fields__ = {
        'jenkinsfile_path': 'jenkinsfilePath',
        'jenkinsfile': 'jenkinsfile',
    }

    __types__ = {
    }

    __required__ = set()

    jenkinsfile_path = None # string
    jenkinsfile = None # string

    def __init__(self, **_kwargs_):

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
class v1_PodSecurityContext(Resource):

    """PodSecurityContext holds pod-level security attributes and common
    container settings. Some fields are also present in
    container.securityContext.  Field values of
    container.securityContext take precedence over field values of
    PodSecurityContext."""

    __kind__ = 'v1.PodSecurityContext'

    __fields__ = {
        'supplemental_groups': 'supplementalGroups',
        'fs_group': 'fsGroup',
        'run_as_non_root': 'runAsNonRoot',
        'run_as_user': 'runAsUser',
        'se_linux_options': 'seLinuxOptions',
    }

    __types__ = {
        'se_linux_options': 'v1.SELinuxOptions',
    }

    __required__ = set()

    supplemental_groups = None # array
    fs_group = None # integer
    run_as_non_root = None # boolean
    run_as_user = None # integer
    se_linux_options = None # v1.SELinuxOptions

    def __init__(self, **_kwargs_):
        self.supplemental_groups = []

        super().__init__(**_kwargs_)

@register_model
class v1_CustomBuildStrategy(Resource):

    """CustomBuildStrategy defines input parameters specific to Custom build."""

    __kind__ = 'v1.CustomBuildStrategy'

    __fields__ = {
        'env': 'env',
        'pull_secret': 'pullSecret',
        'build_api_version': 'buildAPIVersion',
        'from_': 'from',
        'expose_docker_socket': 'exposeDockerSocket',
        'secrets': 'secrets',
        'force_pull': 'forcePull',
    }

    __types__ = {
        'env': 'v1.EnvVar',
        'from_': 'v1.ObjectReference',
        'pull_secret': 'v1.LocalObjectReference',
        'secrets': 'v1.SecretSpec',
    }

    __required__ = set([
        'from_',
    ])

    env = None # array
    pull_secret = None # v1.LocalObjectReference
    build_api_version = None # string
    from_ = None # v1.ObjectReference (required)
    expose_docker_socket = None # boolean
    secrets = None # array
    force_pull = None # boolean

    def __init__(self, *, from_, **_kwargs_):
        self.env = []
        self.secrets = []

        self.from_ = from_

        super().__init__(**_kwargs_)

@register_model
class v1_ImageStreamSpec(Resource):

    """ImageStreamSpec represents options for ImageStreams."""

    __kind__ = 'v1.ImageStreamSpec'

    __fields__ = {
        'docker_image_repository': 'dockerImageRepository',
        'tags': 'tags',
    }

    __types__ = {
        'tags': 'v1.TagReference',
    }

    __required__ = set()

    docker_image_repository = None # string
    tags = None # array

    def __init__(self, **_kwargs_):
        self.tags = []

        super().__init__(**_kwargs_)

@register_model
class v1_CinderVolumeSource(Resource):

    """Represents a cinder volume resource in Openstack. A Cinder volume must
    exist before mounting to a container. The volume must also be in
    the same region as the kubelet. Cinder volumes support ownership
    management and SELinux relabeling."""

    __kind__ = 'v1.CinderVolumeSource'

    __fields__ = {
        'volume_id': 'volumeID',
        'read_only': 'readOnly',
        'fs_type': 'fsType',
    }

    __types__ = {
    }

    __required__ = set([
        'volume_id',
    ])

    volume_id = None # string (required)
    read_only = None # boolean
    fs_type = None # string

    def __init__(self, *, volume_id, **_kwargs_):

        self.volume_id = volume_id

        super().__init__(**_kwargs_)
__all__ = ['v1_TemplateList', 'v1_SelfSubjectRulesReview', 'v1_SecurityContext', 'v1_ClusterNetwork', 'v1_BuildSpec', 'unversioned_APIResourceList', 'v1_FlockerVolumeSource', 'v1_ContainerPort', 'v1_ObjectMeta', 'v1_ImageStreamImportSpec', 'v1_PodTemplateSpec', 'v1_AppliedClusterResourceQuota', 'v1_DeploymentConfigRollback', 'v1_DeploymentDetails', 'v1_ResourceFieldSelector', 'v1_OAuthClientAuthorizationList', 'v1_PersistentVolumeClaimVolumeSource', 'v1_ClusterResourceQuotaStatus', 'v1_TagEventCondition', 'v1_GitRepoVolumeSource', 'v1_GenericWebHookCause', 'v1_RoleBinding', 'v1_DeploymentConfigStatus', 'v1_NamedRole', 'v1_Handler', 'v1_UserIdentityMapping', 'v1_DeploymentCause', 'v1_DeploymentStrategy', 'versioned_Event', 'v1_OAuthClientList', 'v1_Capability', 'v1_RouteStatus', 'v1_Capabilities', 'v1_OAuthAccessTokenList', 'v1_PolicyList', 'v1_EnvVarSource', 'v1_Policy', 'v1_OAuthClient', 'v1_SecretList', 'v1_Identity', 'v1_DeleteOptions', 'v1_ImageSourcePath', 'v1_TagImageHook', 'v1_RoleList', 'v1_BuildConfig', 'v1_ProjectList', 'v1_ProjectRequest', 'v1_ImageImportSpec', 'v1_Build', 'v1_ClusterRoleBinding', 'v1_FlexVolumeSource', 'v1_WebHookTrigger', 'v1_Image_dockerImageSignatures', 'v1_BuildStatus', 'v1_BuildConfigStatus', 'v1_TLSConfig', 'v1_ImageChangeTrigger', 'v1_ImageLayer', 'v1beta1_ScaleSpec', 'v1_PolicyRule', 'v1_HTTPGetAction', 'v1_OAuthAccessToken', 'v1_GitBuildSource', 'v1_DeprecatedDownwardAPIVolumeFile', 'v1_ResourceQuotaStatusByNamespace', 'v1_ImageStream', 'v1_ImageStreamImportStatus', 'v1_VolumeMount', 'v1_ClusterRoleBindingList', 'v1_FinalizerName', 'v1_SignatureCondition', 'v1_VsphereVirtualDiskVolumeSource', 'v1_LocalSubjectAccessReview', 'v1_ClusterPolicyBindingList', 'v1_HTTPHeader', 'v1_OAuthAuthorizeTokenList', 'v1_DeploymentCauseImageTrigger', 'v1_ClusterNetworkList', 'v1_NetNamespace', 'v1_RepositoryImportSpec', 'patch_Object', 'v1_ImageStreamList', 'v1_BuildStrategy', 'v1_ClusterResourceQuotaSelector', 'v1_BuildConfigList', 'v1_TagImportPolicy', 'v1_ObjectReference', 'v1_ExecAction', 'v1_EgressNetworkPolicyPeer', 'runtime_RawExtension', 'v1_RoutePort', 'v1_ClusterPolicyList', 'v1_ConfigMapKeySelector', 'v1_BuildSource', 'types_UID', 'v1_HostSubnet', 'v1_SubjectAccessReview', 'v1_SELinuxOptions', 'v1_ImageImportStatus', 'v1_Parameter', 'v1_ProjectSpec', 'v1_SecretVolumeSource', 'v1_HostSubnetList', 'v1_Project', 'v1_DeploymentConfigList', 'v1_Volume', 'v1_PodSpec', 'v1_Preconditions', 'v1_ConfigMapVolumeSource', 'v1_NetNamespaceList', 'v1_RouteIngress', 'v1_ImageStreamImport', 'v1_BuildLog', 'v1beta1_Scale', 'v1_ClusterRoleList', 'v1_NamedTagEventList', 'v1_GitHubWebHookCause', 'v1_CustomDeploymentStrategyParams', 'v1_BuildPostCommitSpec', 'v1_DownwardAPIVolumeSource', 'v1_RepositoryImportStatus', 'v1_ISCSIVolumeSource', 'unversioned_ListMeta', 'v1_GitSourceRevision', 'v1_DockerBuildStrategy', 'v1_SecretBuildSource', 'unversioned_LabelSelectorRequirement', 'v1_ClusterRole', 'v1_DeploymentTriggerPolicy', 'v1_ImageStreamMapping', 'v1_ImageStreamImage', 'v1_BuildTriggerPolicy', 'v1_ResourceAccessReview', 'v1_RollingDeploymentStrategyParams', 'v1_SourceControlUser', 'unversioned_Patch', 'v1_IdentityList', 'v1_PolicyBindingList', 'v1_DeploymentTriggerImageChangeParams', 'v1_AzureFileVolumeSource', 'v1_ImageStreamStatus', 'v1beta1_ScaleStatus', 'v1_Probe', 'v1_BuildConfigSpec', 'v1_SubjectRulesReviewStatus', 'v1_DeprecatedDownwardAPIVolumeSource', 'v1_EgressNetworkPolicyList', 'v1_ImageList', 'v1_RecreateDeploymentStrategyParams', 'v1_Image', 'v1_Container', 'v1_RouteIngressCondition', 'v1_ImageChangeCause', 'v1_OAuthClientAuthorization', 'v1_TCPSocketAction', 'unversioned_LabelSelector', 'v1_NamedClusterRole', 'v1_ScopeRestriction', 'v1_DeploymentConfig', 'v1_User', 'v1_BuildTriggerCause', 'v1_NamedClusterRoleBinding', 'v1_ClusterRoleScopeRestriction', 'v1_ObjectFieldSelector', 'v1_SignatureSubject', 'v1_ImageSignature', 'v1_ClusterResourceQuota', 'v1_UserList', 'v1_NFSVolumeSource', 'v1_RouteSpec', 'v1_AppliedClusterResourceQuotaList', 'v1_EgressNetworkPolicySpec', 'unversioned_StatusDetails', 'v1_ClusterPolicyBinding', 'v1_DeploymentConfigSpec', 'v1_HostPathVolumeSource', 'v1_ProjectStatus', 'v1_BinaryBuildSource', 'v1_SignatureIssuer', 'v1_DeploymentLog', 'v1_SecretKeySelector', 'v1_BuildRequest', 'v1_TagEvent', 'v1_PolicyBinding', 'v1_ClusterPolicy', 'v1_RBDVolumeSource', 'v1_DownwardAPIVolumeFile', 'v1_NamedRoleBinding', 'unversioned_Status', 'v1_Template', 'v1_ResourceQuotaStatus', 'v1_ClusterResourceQuotaList', 'v1_TagReference', 'v1_Lifecycle', 'v1_DeploymentConfigRollbackSpec', 'v1_Group', 'v1_ClusterResourceQuotaSpec', 'v1_ResourceQuotaSpec', 'v1_RouteTargetReference', 'v1_LocalResourceAccessReview', 'v1_OAuthAuthorizeToken', 'v1_EmptyDirVolumeSource', 'v1_LifecycleHook', 'v1_SecretSpec', 'v1_GroupList', 'v1_BuildList', 'v1_Role', 'unversioned_APIResource', 'v1_AWSElasticBlockStoreVolumeSource', 'v1_ResourceQuotaScope', 'v1_EgressNetworkPolicyRule', 'v1_ResourceRequirements', 'v1_CephFSVolumeSource', 'v1_EnvVar', 'v1_KeyToPath', 'v1_ImageSource', 'v1_ImageStreamTag', 'v1_Secret', 'v1_SourceBuildStrategy', 'v1_EgressNetworkPolicy', 'unversioned_StatusCause', 'v1_Route', 'v1_FCVolumeSource', 'v1_GlusterfsVolumeSource', 'v1_RoleBindingList', 'v1_ImageStreamTagList', 'v1_SourceRevision', 'v1_ExecNewPodHook', 'v1_BuildOutput', 'v1_GCEPersistentDiskVolumeSource', 'v1_RouteList', 'v1_OwnerReference', 'v1_JenkinsPipelineBuildStrategy', 'v1_LocalObjectReference', 'v1_SelfSubjectRulesReviewSpec', 'v1_PodSecurityContext', 'v1_CustomBuildStrategy', 'v1_ImageStreamSpec', 'v1_CinderVolumeSource']
