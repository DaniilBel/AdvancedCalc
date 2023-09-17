import json
import datetime
from flask import Response, request

from controller import bp
from database.model.calc_history import History
from database.repository.history_repository import HistoryRepository


repository = HistoryRepository()


@bp.route("/history", methods=['POST'])
def add_feedback() -> Response:
    content = request.get_json()
    line = content.get("line", None)
    answer = content.get("answer", None)

    if line is None or type(line) is not str:
        msg = json.dumps({"message": "line должен быть числовой строкой"}, ensure_ascii=False)
        return Response(msg, status=422, mimetype='application/json')
    if answer is None or type(answer) is not int:
        msg = json.dumps({"message": "answer должен быть числом"}, ensure_ascii=False)
        return Response(msg, status=422, mimetype='application/json')
    
    entity = History()
    entity.line = line
    entity.answer = answer
    entity.date = datetime.datetime.now()

    feedback = repository.add_history(entity)
    if feedback is None:
        msg = json.dumps({"message": "не удалось добавить данные"}, ensure_ascii=False)
        return Response(msg, status=400, mimetype='application/json')
    msg = json.dumps({"message": "строка вычислений успешно добавлена"}, ensure_ascii=False)
    return Response(msg, status=201, mimetype='application/json')


@bp.route("/history/delete", methods=['DELETE'])
def delete_history() -> Response:
    tag = repository.clear_history()
    if tag is None:
        msg = json.dumps({"message": "данные отсутствует"}, ensure_ascii=False)
        return Response(msg, status=422, mimetype='application/json')
    msg = json.dumps({"message": "история вычислений успешно удалена"}, ensure_ascii=False)
    return Response(msg, status=202, mimetype='application/json')


@bp.route("/history/<line>", methods=['GET'])
def get_one_answer(line: str) -> Response:
    tag = repository.get_answer(line)
    if tag is None:
        msg = json.dumps({"message": "строка с данными вычислениями отсутсвует"}, ensure_ascii=False)
        return Response(msg, status=422, mimetype='application/json')
    json_list = json.dumps(tag, default=lambda x: x.__dict__, ensure_ascii=False)
    return Response(json_list, status=200, mimetype='application/json')


@bp.route("/history", methods=['GET'])
def get_history() -> Response:
    tags = repository.get_history()
    if tags is None:
        msg = json.dumps({"message": "невозможно получить список вычислений"}, ensure_ascii=False)
        return Response(msg, status=400, mimetype='application/json')
    json_list = json.dumps(tags, default=lambda x: x.__dict__, ensure_ascii=False)
    return Response(json_list, status=200, mimetype='application/json')

