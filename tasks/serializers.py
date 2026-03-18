from rest_framework import serializers
from .models import Task
from datetime import date

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'

    # ✅ Existing validation (unchanged)
    def validate_due_date(self, value):
        if value < date.today():
            raise serializers.ValidationError("Due date cannot be in the past")
        return value

    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Title cannot be empty")
        return value

    # ✅ NEW: Control update behavior
    def update(self, instance, validated_data):
        request = self.context.get('request')

        # 🔴 If no request (safety check)
        if not request:
            return super().update(instance, validated_data)

        user = request.user

        # ✅ Assigned user → ONLY update status
        if user == instance.assigned_to:
            return super().update(instance, {
                'status': validated_data.get('status', instance.status)
            })

        # ✅ Creator → can update everything
        if user == instance.created_by:
            return super().update(instance, validated_data)

        # ❌ Others → not allowed
        raise serializers.ValidationError("You are not allowed to update this task")