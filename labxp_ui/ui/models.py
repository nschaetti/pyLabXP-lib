from django.db import models


# Basic log class
class LabLogger(models.Model):
    """
    Basic log class
    """

    # Fields
    lab = models.TextField()
    exp = models.TextField()
    instance = models.BigIntegerField()
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Saving date")

    # Abstract
    class Meta:
        abstract = True
    # end Meta

# end LabLogger


class LabLoggerVariableValue(models.Model):
    # Fields
    name = models.CharField(max_length=100)
    int_value = models.TextField(null=True)
    float_value = models.FloatField(null=True)
    text_value = models.TextField(null=True)
    bool_value = models.BooleanField(default=False)

    # Abstract
    class Meta:
        abstract = True
    # end Meta

# end LabLoggerVariableValue


class LabLoggerGlobalValue(LabLoggerVariableValue):
    # Fields
    globals = models.ForeignKey('LabLoggerGlobals')

    # Specify the collection
    class Meta:
        db_table = "global_values"
    # end Meta

# end LabLoggerGlobalValue


# Log values of globals variables
class LabLoggerGlobals(LabLogger):
    """
    Log values of global variables
    """

    # Fields
    count = models.IntegerField()

    # Specify the collection
    class Meta:
        db_table = "globals"
    # end Meta

# end LabLoggerGlobals


class LabLoggerLocalValue(LabLoggerVariableValue):
    # Fields
    vars = models.ForeignKey('LabLoggerLocals')

    # Specify the collection
    class Meta:
        db_table = "local_values"
    # end Meta
# end LabLoggerLocalValue


# Log values of local variables
class LabLoggerLocals(LabLogger):
    """
    Log values of local variables
    """

    # Fields
    count = models.IntegerField()

    # Specify the collection
    class Meta:
        db_table = "vars"
    # end Meta

# end LabloggerLocals


# Log param values
class LabLoggerParam(LabLogger):
    """
    Log parameter values
    """

    # Fields
    param = models.TextField()
    value = models.FloatField()

    # Specify the collection
    class Meta:
        db_table = "param"
    # end Meta

# end LabLoggerParam


class LabLoggerParamValue(LabLoggerVariableValue):
    # Fields
    result = models.ForeignKey('LabLoggerResult')

    # Specify the collection
    class Meta:
        db_table = "param_values"
    # end Meta
# end LabLoggerParamValue


# Log results
class LabLoggerResult(LabLogger):
    """
    Log results
    """

    # Fields
    result = models.TextField()
    value = models.FloatField()

    # Specify the collection
    class Meta:
        db_table = "result"
    # end Meta

# end LagLoggerResult


class LabLoggerTracebackValue(LabLoggerVariableValue):
    # Fields
    traceback = models.ForeignKey('LabLoggerTraceback')

    # Specify the collection
    class Meta:
        db_table = "traceback_values"
    # end Meta
# end LabLoggerTracebackValue


# Log traceback
class LabLoggerTraceback(LabLogger):
    """
    Log tracebacks
    """

    # Fields
    exec_info = models.TextField()

    # Specify the collection
    class Meta:
        db_table = "traceback"
    # end Meta

# end LabLoggerTraceback
