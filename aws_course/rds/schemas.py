from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class Endpoint(BaseModel):
    address: str = Field(..., alias='Address')
    port: int = Field(..., alias='Port')
    hosted_zone_id: str = Field(..., alias='HostedZoneId')


class VpcSecurityGroup(BaseModel):
    vpc_security_group_id: str = Field(..., alias='VpcSecurityGroupId')
    status: str = Field(..., alias='Status')


class DbParameterGroup(BaseModel):
    db_parameter_group_name: str = Field(..., alias='DBParameterGroupName')
    parameter_apply_status: str = Field(..., alias='ParameterApplyStatus')


class SubnetAvailabilityZone(BaseModel):
    name: str = Field(..., alias='Name')


class Subnet(BaseModel):
    subnet_identifier: str = Field(..., alias='SubnetIdentifier')
    subnet_availability_zone: SubnetAvailabilityZone = Field(
        ..., alias='SubnetAvailabilityZone'
    )
    subnet_outpost: Dict[str, Any] = Field(..., alias='SubnetOutpost')
    subnet_status: str = Field(..., alias='SubnetStatus')


class DbSubnetGroup(BaseModel):
    db_subnet_group_name: str = Field(..., alias='DBSubnetGroupName')
    db_subnet_group_description: str = Field(..., alias='DBSubnetGroupDescription')
    vpc_id: str = Field(..., alias='VpcId')
    subnet_group_status: str = Field(..., alias='SubnetGroupStatus')
    subnets: List[Subnet] = Field(..., alias='Subnets')


class OptionGroupMembership(BaseModel):
    option_group_name: str = Field(..., alias='OptionGroupName')
    status: str = Field(..., alias='Status')


class CertificateDetails(BaseModel):
    ca_identifier: str = Field(..., alias='CAIdentifier')
    valid_till: str = Field(..., alias='ValidTill')


class DbInstance(BaseModel):
    db_instance_identifier: str = Field(..., alias='DBInstanceIdentifier')
    db_instance_class: str = Field(..., alias='DBInstanceClass')
    engine: str = Field(..., alias='Engine')
    db_instance_status: str = Field(..., alias='DBInstanceStatus')
    master_username: str = Field(..., alias='MasterUsername')
    endpoint: Endpoint = Field(..., alias='Endpoint')
    allocated_storage: int = Field(..., alias='AllocatedStorage')
    instance_create_time: str = Field(..., alias='InstanceCreateTime')
    preferred_backup_window: str = Field(..., alias='PreferredBackupWindow')
    backup_retention_period: int = Field(..., alias='BackupRetentionPeriod')
    db_security_groups: List = Field(..., alias='DBSecurityGroups')
    vpc_security_groups: List[VpcSecurityGroup] = Field(..., alias='VpcSecurityGroups')
    db_parameter_groups: List[DbParameterGroup] = Field(..., alias='DBParameterGroups')
    availability_zone: str = Field(..., alias='AvailabilityZone')
    db_subnet_group: DbSubnetGroup = Field(..., alias='DBSubnetGroup')
    preferred_maintenance_window: str = Field(..., alias='PreferredMaintenanceWindow')
    pending_modified_values: Dict[str, Any] = Field(..., alias='PendingModifiedValues')
    latest_restorable_time: str = Field(..., alias='LatestRestorableTime')
    multi_az: bool = Field(..., alias='MultiAZ')
    engine_version: str = Field(..., alias='EngineVersion')
    auto_minor_version_upgrade: bool = Field(..., alias='AutoMinorVersionUpgrade')
    read_replica_db_instance_identifiers: List = Field(
        ..., alias='ReadReplicaDBInstanceIdentifiers'
    )
    license_model: str = Field(..., alias='LicenseModel')
    option_group_memberships: List[OptionGroupMembership] = Field(
        ..., alias='OptionGroupMemberships'
    )
    publicly_accessible: bool = Field(..., alias='PubliclyAccessible')
    storage_type: str = Field(..., alias='StorageType')
    db_instance_port: int = Field(..., alias='DbInstancePort')
    storage_encrypted: bool = Field(..., alias='StorageEncrypted')
    kms_key_id: str = Field(..., alias='KmsKeyId')
    dbi_resource_id: str = Field(..., alias='DbiResourceId')
    ca_certificate_identifier: str = Field(..., alias='CACertificateIdentifier')
    domain_memberships: List = Field(..., alias='DomainMemberships')
    copy_tags_to_snapshot: bool = Field(..., alias='CopyTagsToSnapshot')
    monitoring_interval: int = Field(..., alias='MonitoringInterval')
    enhanced_monitoring_resource_arn: str = Field(
        ..., alias='EnhancedMonitoringResourceArn'
    )
    monitoring_role_arn: str = Field(..., alias='MonitoringRoleArn')
    db_instance_arn: str = Field(..., alias='DBInstanceArn')
    iam_database_authentication_enabled: bool = Field(
        ..., alias='IAMDatabaseAuthenticationEnabled'
    )
    performance_insights_enabled: bool = Field(..., alias='PerformanceInsightsEnabled')
    deletion_protection: bool = Field(..., alias='DeletionProtection')
    associated_roles: List = Field(..., alias='AssociatedRoles')
    max_allocated_storage: int = Field(..., alias='MaxAllocatedStorage')
    tag_list: List = Field(..., alias='TagList')
    customer_owned_ip_enabled: bool = Field(..., alias='CustomerOwnedIpEnabled')
    activity_stream_status: str = Field(..., alias='ActivityStreamStatus')
    backup_target: str = Field(..., alias='BackupTarget')
    network_type: str = Field(..., alias='NetworkType')
    storage_throughput: int = Field(..., alias='StorageThroughput')
    certificate_details: CertificateDetails = Field(..., alias='CertificateDetails')
    dedicated_log_volume: bool = Field(..., alias='DedicatedLogVolume')
    is_storage_config_upgrade_available: bool = Field(
        ..., alias='IsStorageConfigUpgradeAvailable'
    )
    engine_lifecycle_support: str = Field(..., alias='EngineLifecycleSupport')


class HttpHeaders(BaseModel):
    x_amzn_requestid: str = Field(..., alias='x-amzn-requestid')
    strict_transport_security: str = Field(..., alias='strict-transport-security')
    content_type: str = Field(..., alias='content-type')
    content_length: str = Field(..., alias='content-length')
    date: str


class ResponseMetadata(BaseModel):
    request_id: str = Field(..., alias='RequestId')
    http_status_code: int = Field(..., alias='HTTPStatusCode')
    http_headers: HttpHeaders = Field(..., alias='HTTPHeaders')
    retry_attempts: int = Field(..., alias='RetryAttempts')


class DBInstanceList(BaseModel):
    db_instances: Optional[List[DbInstance]] = Field(None, alias='DBInstances')
    response_metadata: Optional[ResponseMetadata] = Field(
        None, alias='ResponseMetadata'
    )
