from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class Endpoint(BaseModel):
    address: str = Field(alias='Address')
    port: int = Field(alias='Port')
    hosted_zone_id: str = Field(alias='HostedZoneId')


class VpcSecurityGroup(BaseModel):
    vpc_security_group_id: str = Field(alias='VpcSecurityGroupId')
    status: str = Field(alias='Status')


class DbParameterGroup(BaseModel):
    db_parameter_group_name: str = Field(alias='DBParameterGroupName')
    parameter_apply_status: str = Field(alias='ParameterApplyStatus')


class SubnetAvailabilityZone(BaseModel):
    name: str = Field(alias='Name')


class Subnet(BaseModel):
    subnet_identifier: str = Field(alias='SubnetIdentifier')
    subnet_availability_zone: SubnetAvailabilityZone = Field(
        alias='SubnetAvailabilityZone'
    )
    subnet_outpost: Dict[str, Any] = Field(alias='SubnetOutpost')
    subnet_status: str = Field(alias='SubnetStatus')


class DbSubnetGroup(BaseModel):
    db_subnet_group_name: str = Field(alias='DBSubnetGroupName')
    db_subnet_group_description: str = Field(alias='DBSubnetGroupDescription')
    vpc_id: str = Field(alias='VpcId')
    subnet_group_status: str = Field(alias='SubnetGroupStatus')
    subnets: List[Subnet] = Field(alias='Subnets')


class OptionGroupMembership(BaseModel):
    option_group_name: str = Field(alias='OptionGroupName')
    status: str = Field(alias='Status')


class CertificateDetails(BaseModel):
    ca_identifier: str = Field(alias='CAIdentifier')
    valid_till: datetime = Field(alias='ValidTill')


class DbInstance(BaseModel):
    db_instance_identifier: Optional[str] = Field(None, alias='DBInstanceIdentifier')
    db_instance_class: Optional[str] = Field(None, alias='DBInstanceClass')
    engine: Optional[str] = Field(None, alias='Engine')
    db_instance_status: Optional[str] = Field(None, alias='DBInstanceStatus')
    master_username: Optional[str] = Field(None, alias='MasterUsername')
    endpoint: Optional[Endpoint] = Field(None, alias='Endpoint')
    allocated_storage: Optional[int] = Field(None, alias='AllocatedStorage')
    instance_create_time: Optional[datetime] = Field(None, alias='InstanceCreateTime')
    preferred_backup_window: Optional[str] = Field(None, alias='PreferredBackupWindow')
    backup_retention_period: Optional[int] = Field(None, alias='BackupRetentionPeriod')
    db_security_groups: Optional[List] = Field(None, alias='DBSecurityGroups')
    vpc_security_groups: Optional[List[VpcSecurityGroup]] = Field(None, alias='VpcSecurityGroups')
    db_parameter_groups: Optional[List[DbParameterGroup]] = Field(None, alias='DBParameterGroups')
    availability_zone: Optional[str] = Field(None, alias='AvailabilityZone')
    db_subnet_group: Optional[DbSubnetGroup] = Field(None, alias='DBSubnetGroup')
    preferred_maintenance_window: Optional[str] = Field(None, alias='PreferredMaintenanceWindow')
    pending_modified_values: Optional[Dict[str, Any]] = Field(None, alias='PendingModifiedValues')
    latest_restorable_time: Optional[datetime] = Field(None, alias='LatestRestorableTime')
    multi_az: Optional[bool] = Field(None, alias='MultiAZ')
    engine_version: Optional[str] = Field(None, alias='EngineVersion')
    auto_minor_version_upgrade: Optional[bool] = Field(None, alias='AutoMinorVersionUpgrade')
    read_replica_db_instance_identifiers: Optional[List] = Field(None, alias='ReadReplicaDBInstanceIdentifiers')
    license_model: Optional[str] = Field(None, alias='LicenseModel')
    option_group_memberships: Optional[List[OptionGroupMembership]] = Field(None, alias='OptionGroupMemberships')
    publicly_accessible: Optional[bool] = Field(None, alias='PubliclyAccessible')
    storage_type: Optional[str] = Field(None, alias='StorageType')
    db_instance_port: Optional[int] = Field(None, alias='DbInstancePort')
    storage_encrypted: Optional[bool] = Field(None, alias='StorageEncrypted')
    kms_key_id: Optional[str] = Field(None, alias='KmsKeyId')
    dbi_resource_id: Optional[str] = Field(None, alias='DbiResourceId')
    ca_certificate_identifier: Optional[str] = Field(None, alias='CACertificateIdentifier')
    domain_memberships: Optional[List] = Field(None, alias='DomainMemberships')
    copy_tags_to_snapshot: Optional[bool] = Field(None, alias='CopyTagsToSnapshot')
    monitoring_interval: Optional[int] = Field(None, alias='MonitoringInterval')
    enhanced_monitoring_resource_arn: Optional[str] = Field(None, alias='EnhancedMonitoringResourceArn')
    monitoring_role_arn: Optional[str] = Field(None, alias='MonitoringRoleArn')
    db_instance_arn: Optional[str] = Field(None, alias='DBInstanceArn')
    iam_database_authentication_enabled: Optional[bool] = Field(None, alias='IAMDatabaseAuthenticationEnabled')
    performance_insights_enabled: Optional[bool] = Field(None, alias='PerformanceInsightsEnabled')
    deletion_protection: Optional[bool] = Field(None, alias='DeletionProtection')
    associated_roles: Optional[List] = Field(None, alias='AssociatedRoles')
    max_allocated_storage: Optional[int] = Field(None, alias='MaxAllocatedStorage')
    tag_list: Optional[List] = Field(None, alias='TagList')
    customer_owned_ip_enabled: Optional[bool] = Field(None, alias='CustomerOwnedIpEnabled')
    activity_stream_status: Optional[str] = Field(None, alias='ActivityStreamStatus')
    backup_target: Optional[str] = Field(None, alias='BackupTarget')
    network_type: Optional[str] = Field(None, alias='NetworkType')
    storage_throughput: Optional[int] = Field(None, alias='StorageThroughput')
    certificate_details: Optional[CertificateDetails] = Field(None, alias='CertificateDetails')
    dedicated_log_volume: Optional[bool] = Field(None, alias='DedicatedLogVolume')
    is_storage_config_upgrade_available: Optional[bool] = Field(None, alias='IsStorageConfigUpgradeAvailable')
    engine_lifecycle_support: Optional[str] = Field(None, alias='EngineLifecycleSupport')


# class DbInstance(BaseModel):
#     db_instance_identifier: str = Field(alias='DBInstanceIdentifier')
#     db_instance_class: str = Field(alias='DBInstanceClass')
#     engine: str = Field(alias='Engine')
#     db_instance_status: str = Field(alias='DBInstanceStatus')
#     master_username: str = Field(alias='MasterUsername')
#     endpoint: Endpoint = Field(alias='Endpoint')
#     allocated_storage: int = Field(alias='AllocatedStorage')
#     instance_create_time: datetime = Field(alias='InstanceCreateTime')
#     preferred_backup_window: str = Field(alias='PreferredBackupWindow')
#     backup_retention_period: int = Field(alias='BackupRetentionPeriod')
#     db_security_groups: List = Field(alias='DBSecurityGroups')
#     vpc_security_groups: List[VpcSecurityGroup] = Field(alias='VpcSecurityGroups')
#     db_parameter_groups: List[DbParameterGroup] = Field(alias='DBParameterGroups')
#     availability_zone: str = Field(alias='AvailabilityZone')
#     db_subnet_group: DbSubnetGroup = Field(alias='DBSubnetGroup')
#     preferred_maintenance_window: str = Field(alias='PreferredMaintenanceWindow')
#     pending_modified_values: Dict[str, Any] = Field(alias='PendingModifiedValues')
#     latest_restorable_time: datetime = Field(alias='LatestRestorableTime')
#     multi_az: bool = Field(alias='MultiAZ')
#     engine_version: str = Field(alias='EngineVersion')
#     auto_minor_version_upgrade: bool = Field(alias='AutoMinorVersionUpgrade')
#     read_replica_db_instance_identifiers: List = Field(
#         alias='ReadReplicaDBInstanceIdentifiers'
#     )
#     license_model: str = Field(alias='LicenseModel')
#     option_group_memberships: List[OptionGroupMembership] = Field(
#         alias='OptionGroupMemberships'
#     )
#     publicly_accessible: bool = Field(alias='PubliclyAccessible')
#     storage_type: str = Field(alias='StorageType')
#     db_instance_port: int = Field(alias='DbInstancePort')
#     storage_encrypted: bool = Field(alias='StorageEncrypted')
#     kms_key_id: str = Field(alias='KmsKeyId')
#     dbi_resource_id: str = Field(alias='DbiResourceId')
#     ca_certificate_identifier: str = Field(alias='CACertificateIdentifier')
#     domain_memberships: List = Field(alias='DomainMemberships')
#     copy_tags_to_snapshot: bool = Field(alias='CopyTagsToSnapshot')
#     monitoring_interval: int = Field(alias='MonitoringInterval')
#     enhanced_monitoring_resource_arn: Optional[str] = Field(default=None,
#                                                             alias='EnhancedMonitoringResourceArn'
#                                                             )
#     monitoring_role_arn: Optional[str] = Field(alias='MonitoringRoleArn', default=None)
#     db_instance_arn: str = Field(alias='DBInstanceArn')
#     iam_database_authentication_enabled: bool = Field(
#         alias='IAMDatabaseAuthenticationEnabled'
#     )
#     performance_insights_enabled: bool = Field(alias='PerformanceInsightsEnabled')
#     deletion_protection: bool = Field(alias='DeletionProtection')
#     associated_roles: List = Field(alias='AssociatedRoles')
#     max_allocated_storage: Optional[int] = Field(alias='MaxAllocatedStorage', default=None)
#     tag_list: List = Field(alias='TagList')
#     customer_owned_ip_enabled: bool = Field(alias='CustomerOwnedIpEnabled')
#     activity_stream_status: str = Field(alias='ActivityStreamStatus')
#     backup_target: str = Field(alias='BackupTarget')
#     network_type: str = Field(alias='NetworkType')
#     storage_throughput: int = Field(alias='StorageThroughput')
#     certificate_details: CertificateDetails = Field(alias='CertificateDetails')
#     dedicated_log_volume: bool = Field(alias='DedicatedLogVolume')
#     is_storage_config_upgrade_available: bool = Field(
#         alias='IsStorageConfigUpgradeAvailable'
#     )
#     engine_lifecycle_support: str = Field(alias='EngineLifecycleSupport')


class HttpHeaders(BaseModel):
    x_amzn_requestid: str = Field(alias='x-amzn-requestid')
    strict_transport_security: str = Field(alias='strict-transport-security')
    content_type: str = Field(alias='content-type')
    content_length: str = Field(alias='content-length')
    date: str


class ResponseMetadata(BaseModel):
    request_id: str = Field(alias='RequestId')
    http_status_code: int = Field(alias='HTTPStatusCode')
    http_headers: HttpHeaders = Field(alias='HTTPHeaders')
    retry_attempts: int = Field(alias='RetryAttempts')


class DBInstanceList(BaseModel):
    db_instances: Optional[List[DbInstance]] = Field(None, alias='DBInstances')
    response_metadata: Optional[ResponseMetadata] = Field(
        None, alias='ResponseMetadata'
    )
