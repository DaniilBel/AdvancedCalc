import json
from flask import Response, request

from controller import bp
from model.calc_history import History
from repository.history_repository import HistoryRepository


repository = HistoryRepository()


@bp.route("/feedback", methods=['POST'])
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

    feedback = repository.add_history(entity)
    if feedback is None:
        msg = json.dumps({"message": "не удалось добавить данные"}, ensure_ascii=False)
        return Response(msg, status=400, mimetype='application/json')
    msg = json.dumps({"message": "строка вычислений успешно добавлена"}, ensure_ascii=False)
    return Response(msg, status=201, mimetype='application/json')

# other methods
