from flask import Flask, request, jsonify  # added to top of file
from flask_cors import CORS  # added to top of file
from flask import _app_ctx_stack
import sqlite3

# execucao das queries do banco de dados
def exec_qry(qry):
    conn = get_db()
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(qry)
    rows = cur.fetchall()
    return rows

# retorno do JSON das transacoes realizadas
def prepare_json_trans(rows):
    trans = []
    try:
        for i in rows:
            trn = {}
            trn["rateId"] = i["rateId"]
            trn["customerId"] = i["customerId"]
            trn["transactionId"] = i["transactionId"]
            trn["parcelas"] = i["parcelas"]
            trn["valorTomado"] = i["valorTomado"]
            trn["disponivel"] = i["disponivel"]
            trn["venc1p"] = i["venc1p"]
            trn
            trans.append(trn)
    except Exception:
        trans = []
    return trans

# retorno do JSON das taxas oferecidas
def prepare_json_rates(rows):
    rates = []
    try:
        for i in rows:
            rate = {}
            rate["bankId"] = i["bankId"]
            rate["bankName"] = i["bankName"]
            rate["bankRate"] = i["bankRate"]
            rates.append(rate)
    except Exception:
        rates = []
    return rates

# retorno do JSON das opcoes de onboarding
def prepare_json_onb(rows):
    onbs = []
    try:
        for i in rows:
            onb = {}
            onb["onboardingId"] = i["onboardingId"]
            onb["onboardingName"] = i["onboardingName"]
            onbs.append(onb)
    except Exception:
        onbs = []
    return onbs

# retorno do JSON das agro insights (dump original da BTG)
def prepare_json(rows):
    agros = []
    try:
        for i in rows:
            agro = {}
            agro["customerId"] = i["customerId"]
            agro["contractId"] = i["contractId"]
            agro["organizationId"] = i["organizationId"]
            agro["organizationName"] = i["organizationName"]
            agro["contractNumber"] = i["contractNumber"]
            agro["productName"] = i["productName"]
            agro["contractAmount"] = i["contractAmount"]
            agro["fd_productType"] = i["fd_productType"]
            agro["fc_productType"] = i["fc_productType"]
            agro["warrantyType"] = i["warrantyType"]
            agro["warrantySubType"] = i["warrantySubType"]
            agro["warrantyAmount"] = i["warrantyAmount"]
            agro["brandName"] = i["warrantyAmount"]
            agro["totalNumberOfInstalments"] = i["totalNumberOfInstalments"]
            agro["fp_paidInstalments"] = i["fp_paidInstalments"]
            agro["fsi_paidInstalments"] = i["fsi_paidInstalments"]
            agro["contractOutstandingBalance"] = i["contractOutstandingBalance"]
            agro["anomId"] = i["anomId"]
            agros.append(agro)
    except Exception:
        agros = []
    return agros


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
DATABASE = "./database.db"

# conexao com o banco de dados
def get_db():
    top = _app_ctx_stack.top
    if not hasattr(top, 'sqlite_db'):
        top.sqlite_db = sqlite3.connect(DATABASE)
    return top.sqlite_db

# fechamento da conexao com o banco de dados
@app.teardown_appcontext
def close_connection(exception):
    top = _app_ctx_stack.top
    if hasattr(top, 'sqlite_db'):
        top.sqlite_db.close()

# GET das agro insights (dump original da BTG)
def get_insights():
    qry = "SELECT * FROM agro_insights"
    rows = exec_qry(qry)
    return prepare_json(rows)

@app.route('/api/insights', methods=['GET'])
def api_get_insights():
    return jsonify(get_insights())

# GET das opcoes de onboarding
def get_onboarding():
    qry = "SELECT * FROM agro_onboarding"
    rows = exec_qry(qry)
    return prepare_json_onb(rows)

@app.route('/api/onboarding', methods=['GET'])
def api_get_onboarding():
    return jsonify(get_onboarding())


# GET das taxas oferecidas
def get_bank_rates():
    qry = "SELECT * FROM agro_bank_rates"
    rows = exec_qry(qry)
    return prepare_json_rates(rows)

@app.route('/api/rates', methods=['GET'])
def api_get_bank_rates():
    return jsonify(get_bank_rates())

# GET das transacoes realizadas
def get_transactions():
    qry = "SELECT * FROM agro_transaction"
    rows = exec_qry(qry)
    return prepare_json_trans(rows)

@app.route('/api/transaction', methods=['GET'])
def api_get_transactions():
    return jsonify(get_transactions())

# GET de uma agro insight específica
def get_insight_by_id(customer_id):
    qry = 'SELECT * FROM agro_insights WHERE customerId = {}'.format(
        customer_id)
    rows = exec_qry(qry)
    return prepare_json(rows)

@app.route('/api/insight/<customer_id>', methods=['GET'])
def api_get_insight(customer_id):
    return jsonify(get_insight_by_id(customer_id))
if __name__ == "__main__":
    app.run()
