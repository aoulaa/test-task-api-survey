from rest_framework import serializers

from .models import Survey, Question, Choice, Answer


class CurrentUserDefault(object):
    def set_context(self, serializer_field):
        self.user_id = serializer_field.context['request'].user.id

    def __call__(self):
        return self.user_id


class AnswerSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField(default=CurrentUserDefault())
    survey = serializers.SlugRelatedField(queryset=Survey.objects.all(), slug_field='id')
    question = serializers.SlugRelatedField(queryset=Question.objects.all(), slug_field='id')
    choice = serializers.SlugRelatedField(queryset=Choice.objects.all(), slug_field='id', allow_null=True)
    choice_text = serializers.CharField(max_length=200, allow_null=True, required=False)

    class Meta:
        model = Answer
        fields = [
            'id',
            'user_id',
            'survey',
            'question',
            'choice',
            'choice_text',
        ]

    def create(self, validated_data):
        return Answer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

    def validate(self, attrs):
        question_type = Question.objects.get(id=attrs['question'].id).question_type
        try:
            if question_type == "one" or question_type == "text":
                obj = Answer.objects.get(question=attrs['question'].id, survey=attrs['survey'],
                                         user_id=attrs['user_id'])
            elif question_type == "multiple":
                obj = Answer.objects.get(question=attrs['question'].id, survey=attrs['survey'],
                                         user_id=attrs['user_id'],
                                         choice=attrs['choice'])
        except Answer.DoesNotExist:
            return attrs
        else:
            raise serializers.ValidationError('?????? ??????????????')


class ChoiceSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    question = serializers.SlugRelatedField(queryset=Question.objects.all(), slug_field='id')
    choice_text = serializers.CharField(max_length=200)

    def validate(self, attrs):
        try:
            obj = Choice.objects.get(question=attrs['question'].id, choice_text=attrs['choice_text'])
        except Choice.DoesNotExist:
            return attrs
        else:
            raise serializers.ValidationError('?????????? ?????? ????????????????????')

    class Meta:
        model = Choice
        fields = [
            'id'
            'question',
            'choice_text',
        ]

    def create(self, validated_data):
        return Choice.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class QuestionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    survey = serializers.SlugRelatedField(queryset=Survey.objects.all(), slug_field='id')
    question_text = serializers.CharField(max_length=200)
    question_type = serializers.CharField(max_length=200)
    choices = ChoiceSerializer(many=True, read_only=True)

    def validate(self, attrs):
        question_type = attrs['question_type']
        if question_type == 'one' or question_type == 'multiple' or question_type == 'text':
            return attrs
        raise serializers.ValidationError('?????? ?????????????? ?????????? ???????? ???????????? ????????, ?????????????????? ?????? ??????????????????')

    class Meta:
        model = Question
        fields = [
            'id'
            'survey',
            'question_text',
            'question_type',
            'choices',
        ]

    def create(self, validated_data):
        return Question.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class SurveySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=200)
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()
    description = serializers.CharField(max_length=200)
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Survey
        fields = [
            'name',
            'start_date',
            'start_date',
            'end_date',
            'description',
            'questions',
            'id',

        ]

    def create(self, validated_data):
        return Survey.objects.create(**validated_data)

    def update(self, instance, validated_data):
        if 'start_date' in validated_data:
            raise serializers.ValidationError({'start_date': '???? ???? ???????????? ???????????????? ?????? ????????.'})
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
