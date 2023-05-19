// Modal Filtro Fecha
let modal = document.getElementById('myModalExcel');

let html;

html = `
<form method="get" action="/pago/reporte_excel_pago/" class="form-validate">
<div class="modal-dialog modal-dialog-scrollable modal-lg">
    <div class="modal-content">
        <div class="modal-header">
            <h4 class="modal-title text-break">
                <i class="fas fa-search"></i>
                Excel Detalles
            </h4>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
            </button>
        </div>
        <div class="modal-body">
            <div class="row">
                <div class="col-lg-4">
                    <div class="form-group">
                        <label>Ingrese Mes *</label>
                        <select class="form-control" name="cbo-mes" id="cbo-mes" required>
                            <option value="" selected>-------</option>
                            <option value="ENERO">ENERO</option>
                            <option value="FEBRERO">FEBRERO</option>
                            <option value="MARZO">MARZO</option>
                            <option value="ABRIL">ABRIL</option>
                            <option value="MAYO">MAYO</option>
                            <option value="JUNIO">JUNIO</option>
                            <option value="JULIO">JULIO</option>
                            <option value="AGOSTO">AGOSTO</option>
                            <option value="SEPTIEMBRE">SEPTIEMBRE</option>
                            <option value="OCTUBRE">OCTUBRE</option>
                            <option value="NOVIEMBRE">NOVIEMBRE</option>
                            <option value="DICIEMBRE">DICIEMBRE</option>
                        </select>
                    </div>
                </div>
                <div class="col-lg-4">
                    <div class="form-group">
                        <label>Ingrese Año *</label>
                        <input type="number" class="form-control" name="txt-year" id="txt-year" min=2020 max=2050 required>
                    </div>
                </div>
                <div class="col-lg-4">
                    <div class="form-group">
                        <label>Ingrese Estado *</label>
                        <select class="form-control" name="cbo-estado" id="cbo-estado" required>
                            <option value="" selected>-------</option>
                            <option value="DEBE">DEBE</option>
                            <option value="PAGADA">PAGADA</option>
                            <option value="ANULADA">ANULADA</option>
                        </select>
                    </div>
                </div>
                <div class="col-lg-4">
                    <div class="form-group">
                        <label>Pago Contador</label>
                        <input type="number" class="form-control" name="txt-contador" id="txt-contador" min=0 value=0>
                    </div>
                </div>
                <div class="col-lg-4">
                    <div class="form-group">
                        <label>Pago Ahorro VPS</label>
                        <input type="number" class="form-control" name="txt-ahorro-vps" id="txt-ahorro-vps" min=0 value=0>
                    </div>
                </div>
                <div class="col-lg-4">
                    <div class="form-group">
                        <label>Sueldo Roraima</label>
                        <input type="number" class="form-control" name="txt-sueldo-roraima" id="txt-sueldo-roraima" min=0 value=0>
                    </div>
                </div>
            </div>
        </div>
        <div class="card-footer">
            <div class="d-flex justify-content-end">
                <button class="btn bg-gradient-secondary mr-2" data-dismiss="modal">
                    <i class="fas fa-times"></i> Cancelar
                </button>
                <button type="reset" class="btn bg-gradient-danger mr-2">
                    <i class="fas fa-sync-alt"></i> Limpiar
                </button>
                <button type="submit" class="btn bg-gradient-success">
                    <i class="fas fa-file-excel"></i>
                    Procesar
                </button>
            </div>
        </div>
    </div>
    <!-- /.modal-content -->
</div>
</form>
`;

modal.innerHTML = html;

