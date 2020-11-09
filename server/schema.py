import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from .models import Schedule as ScheduleModel


class Schedule(SQLAlchemyObjectType):
    class Meta:
        model = ScheduleModel
        interfaces = (relay.Node,)


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_schedules = SQLAlchemyConnectionField(Schedule.connection)


schema = graphene.Schema(query=Query)
