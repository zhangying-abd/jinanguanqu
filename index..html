<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>济南南部灌区节水灌溉与用水调度系统</title>
  <script src="https://cdn.jsdelivr.net/npm/echarts@5.5.1/dist/echarts.min.js"></script>

  <style>
    :root {
      --primary: #1677ff;
      --primary-dark: #0958d9;
      --bg: #f4f7fb;
      --card: #ffffff;
      --text: #1f2937;
      --sub-text: #64748b;
      --border: #e5e7eb;
      --green: #16a34a;
      --orange: #f59e0b;
      --red: #dc2626;
      --blue-bg: #eaf3ff;
    }

    * {
      box-sizing: border-box;
    }

    body {
      margin: 0;
      color: var(--text);
      background: var(--bg);
      font-family: "Microsoft YaHei", "PingFang SC", Arial, sans-serif;
      font-size: 14px;
    }

    button,
    input,
    select,
    textarea {
      font-family: inherit;
    }

    button {
      cursor: pointer;
    }

    .app {
      min-height: 100vh;
      display: flex;
    }

    .sidebar {
      position: fixed;
      z-index: 10;
      width: 240px;
      height: 100vh;
      padding: 20px 14px;
      color: #dbeafe;
      background: linear-gradient(180deg, #0f2747, #123866);
    }

    .brand {
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 0 10px 24px;
      color: white;
      font-weight: bold;
      font-size: 17px;
      line-height: 1.35;
    }

    .brand-icon {
      display: flex;
      width: 38px;
      height: 38px;
      align-items: center;
      justify-content: center;
      border-radius: 10px;
      color: #0f2747;
      background: #8bd3ff;
      font-size: 22px;
    }

    .nav-title {
      padding: 14px 10px 8px;
      color: #93b4d8;
      font-size: 12px;
    }

    .nav-item {
      display: flex;
      align-items: center;
      gap: 12px;
      margin: 4px 0;
      padding: 12px 14px;
      border-radius: 8px;
      color: #c7dcf5;
      transition: 0.2s;
    }

    .nav-item:hover,
    .nav-item.active {
      color: white;
      background: rgba(255, 255, 255, 0.14);
    }

    .nav-icon {
      width: 22px;
      text-align: center;
      font-size: 17px;
    }

    .sidebar-bottom {
      position: absolute;
      right: 16px;
      bottom: 22px;
      left: 16px;
      padding: 12px;
      border: 1px solid rgba(255,255,255,0.16);
      border-radius: 8px;
      color: #b9d4ef;
      background: rgba(255,255,255,0.06);
      font-size: 12px;
      line-height: 1.8;
    }

    .main {
      width: calc(100% - 240px);
      margin-left: 240px;
    }

    .topbar {
      display: flex;
      height: 68px;
      align-items: center;
      justify-content: space-between;
      padding: 0 28px;
      border-bottom: 1px solid var(--border);
      background: white;
    }

    .topbar-title {
      font-size: 20px;
      font-weight: bold;
    }

    .topbar-right {
      display: flex;
      align-items: center;
      gap: 20px;
      color: var(--sub-text);
    }

    .user {
      display: flex;
      align-items: center;
      gap: 8px;
      color: var(--text);
    }

    .avatar {
      display: flex;
      width: 32px;
      height: 32px;
      align-items: center;
      justify-content: center;
      border-radius: 50%;
      color: white;
      background: var(--primary);
      font-weight: bold;
    }

    .content {
      padding: 24px 28px 40px;
    }

    .page-title {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 20px;
    }

    .page-title h1 {
      margin: 0;
      font-size: 22px;
    }

    .page-title p {
      margin: 7px 0 0;
      color: var(--sub-text);
      font-size: 13px;
    }

    .page {
      display: none;
    }

    .page.active {
      display: block;
    }

    .card {
      padding: 18px;
      border: 1px solid var(--border);
      border-radius: 10px;
      background: var(--card);
      box-shadow: 0 3px 12px rgba(15, 39, 71, 0.04);
    }

    .card-title {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 15px;
      font-size: 16px;
      font-weight: bold;
    }

    .card-title small {
      color: var(--sub-text);
      font-size: 12px;
      font-weight: normal;
    }

    .metric-grid {
      display: grid;
      grid-template-columns: repeat(6, 1fr);
      gap: 14px;
      margin-bottom: 18px;
    }

    .metric-card {
      position: relative;
      overflow: hidden;
      padding: 17px;
      border: 1px solid var(--border);
      border-radius: 10px;
      background: white;
    }

    .metric-card::after {
      position: absolute;
      right: -15px;
      bottom: -22px;
      width: 75px;
      height: 75px;
      border-radius: 50%;
      background: var(--blue-bg);
      content: "";
    }

    .metric-label {
      color: var(--sub-text);
      font-size: 13px;
    }

    .metric-value {
      margin: 9px 0 4px;
      color: #142b4a;
      font-size: 25px;
      font-weight: bold;
    }

    .metric-unit {
      margin-left: 4px;
      color: var(--sub-text);
      font-size: 12px;
      font-weight: normal;
    }

    .metric-desc {
      color: var(--green);
      font-size: 12px;
    }

    .dashboard-grid {
      display: grid;
      grid-template-columns: 1.35fr 1fr;
      gap: 18px;
      margin-bottom: 18px;
    }

    .dashboard-grid.bottom {
      grid-template-columns: 1fr 1fr 0.95fr;
    }

    .chart {
      width: 100%;
      height: 300px;
    }

    .chart.small {
      height: 265px;
    }

    .filter-bar {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 10px;
      margin-bottom: 18px;
      padding: 15px;
      border: 1px solid var(--border);
      border-radius: 10px;
      background: white;
    }

    .filter-label {
      color: var(--sub-text);
      font-size: 13px;
    }

    input,
    select,
    textarea {
      min-height: 36px;
      padding: 7px 10px;
      border: 1px solid #d5dbe5;
      border-radius: 6px;
      outline: none;
      color: var(--text);
      background: white;
    }

    input:focus,
    select:focus,
    textarea:focus {
      border-color: var(--primary);
      box-shadow: 0 0 0 2px rgba(22, 119, 255, 0.12);
    }

    textarea {
      width: 100%;
      resize: vertical;
    }

    .btn {
      min-height: 36px;
      padding: 7px 14px;
      border: 1px solid #d5dbe5;
      border-radius: 6px;
      color: #334155;
      background: white;
    }

    .btn:hover {
      border-color: var(--primary);
      color: var(--primary);
    }

    .btn-primary {
      border-color: var(--primary);
      color: white;
      background: var(--primary);
    }

    .btn-primary:hover {
      color: white;
      background: var(--primary-dark);
    }

    .btn-danger {
      border-color: #fecaca;
      color: var(--red);
      background: #fff5f5;
    }

    .btn-success {
      border-color: #bbf7d0;
      color: var(--green);
      background: #f0fdf4;
    }

    .btn-warning {
      border-color: #fde68a;
      color: #b45309;
      background: #fffbeb;
    }

    table {
      width: 100%;
      border-collapse: collapse;
    }

    th,
    td {
      padding: 12px 10px;
      border-bottom: 1px solid #edf0f4;
      text-align: left;
      white-space: nowrap;
    }

    th {
      color: #526174;
      background: #f8fafc;
      font-size: 13px;
      font-weight: bold;
    }

    td {
      color: #334155;
      font-size: 13px;
    }

    tbody tr:hover {
      background: #f8fbff;
    }

    .table-wrap {
      overflow-x: auto;
    }

    .tag {
      display: inline-block;
      padding: 4px 9px;
      border-radius: 12px;
      font-size: 12px;
    }

    .tag-green {
      color: #15803d;
      background: #dcfce7;
    }

    .tag-orange {
      color: #b45309;
      background: #fef3c7;
    }

    .tag-red {
      color: #b91c1c;
      background: #fee2e2;
    }

    .tag-blue {
      color: #1d4ed8;
      background: #dbeafe;
    }

    .tag-gray {
      color: #475569;
      background: #e2e8f0;
    }

    .progress {
      width: 120px;
      height: 7px;
      overflow: hidden;
      border-radius: 10px;
      background: #e5e7eb;
    }

    .progress-bar {
      height: 100%;
      border-radius: 10px;
      background: var(--primary);
    }

    .map-box {
      position: relative;
      height: 300px;
      overflow: hidden;
      border-radius: 8px;
      background:
        linear-gradient(135deg, rgba(207, 239, 255, 0.8), rgba(241, 250, 255, 0.9)),
        repeating-linear-gradient(30deg, transparent 0, transparent 28px, rgba(85, 160, 190, 0.08) 29px);
    }

    .map-title {
      position: absolute;
      top: 12px;
      left: 14px;
      z-index: 2;
      padding: 7px 10px;
      border-radius: 5px;
      color: #17466d;
      background: rgba(255,255,255,0.8);
      font-weight: bold;
    }

    .river {
      position: absolute;
      top: -30px;
      left: 45%;
      width: 34px;
      height: 390px;
      border-radius: 50%;
      background: #70c4e8;
      transform: rotate(26deg);
      opacity: 0.78;
    }

    .area {
      position: absolute;
      display: flex;
      align-items: center;
      justify-content: center;
      border: 2px solid rgba(29, 78, 121, 0.42);
      border-radius: 48%;
      color: #1e4e76;
      background: rgba(129, 197, 112, 0.55);
      font-size: 12px;
      font-weight: bold;
    }

    .area.east {
      top: 46px;
      right: 35px;
      width: 145px;
      height: 92px;
    }

    .area.west {
      top: 60px;
      left: 32px;
      width: 145px;
      height: 90px;
      background: rgba(250, 204, 88, 0.56);
    }

    .area.south {
      right: 58px;
      bottom: 25px;
      width: 160px;
      height: 88px;
      background: rgba(244, 127, 82, 0.52);
    }

    .area.north {
      bottom: 30px;
      left: 36px;
      width: 145px;
      height: 88px;
      background: rgba(119, 190, 222, 0.48);
    }

    .monitor-point {
      position: absolute;
      z-index: 3;
      display: flex;
      width: 22px;
      height: 22px;
      align-items: center;
      justify-content: center;
      border: 3px solid white;
      border-radius: 50%;
      color: white;
      background: var(--green);
      box-shadow: 0 1px 5px rgba(0,0,0,0.3);
      cursor: pointer;
      font-size: 10px;
      font-weight: bold;
    }

    .point-1 { top: 78px; right: 102px; }
    .point-2 { top: 92px; left: 88px; background: var(--orange); }
    .point-3 { right: 132px; bottom: 57px; background: var(--red); }
    .point-4 { bottom: 60px; left: 93px; background: var(--green); }

    .map-legend {
      position: absolute;
      right: 12px;
      bottom: 10px;
      z-index: 4;
      padding: 7px 10px;
      border-radius: 6px;
      background: rgba(255,255,255,0.88);
      color: #526174;
      font-size: 11px;
      line-height: 1.8;
    }

    .legend-dot {
      display: inline-block;
      width: 8px;
      height: 8px;
      margin-right: 4px;
      border-radius: 50%;
    }

    .alert-list {
      display: flex;
      flex-direction: column;
      gap: 10px;
    }

    .alert-item {
      display: flex;
      gap: 10px;
      padding: 11px;
      border-radius: 7px;
      background: #f8fafc;
    }

    .alert-icon {
      font-size: 20px;
    }

    .alert-content {
      flex: 1;
    }

    .alert-title {
      margin-bottom: 4px;
      color: #334155;
      font-weight: bold;
    }

    .alert-desc {
      color: var(--sub-text);
      font-size: 12px;
      line-height: 1.6;
    }

    .two-column {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 18px;
    }

    .dispatch-list {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 14px;
    }

    .task-card {
      padding: 16px;
      border: 1px solid var(--border);
      border-radius: 9px;
      background: white;
    }

    .task-head {
      display: flex;
      justify-content: space-between;
      gap: 10px;
      margin-bottom: 12px;
    }

    .task-title {
      color: #1e3a5f;
      font-weight: bold;
    }

    .task-info {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
      margin-bottom: 13px;
      color: var(--sub-text);
      font-size: 12px;
    }

    .task-info strong {
      display: block;
      margin-top: 3px;
      color: #334155;
      font-size: 13px;
    }

    .task-actions {
      display: flex;
      gap: 8px;
      margin-top: 13px;
    }

    .timeline {
      position: relative;
      margin: 5px 0;
      padding-left: 24px;
    }

    .timeline::before {
      position: absolute;
      top: 5px;
      bottom: 5px;
      left: 7px;
      width: 2px;
      background: #dbeafe;
      content: "";
    }

    .timeline-item {
      position: relative;
      margin-bottom: 18px;
    }

    .timeline-item::before {
      position: absolute;
      top: 3px;
      left: -21px;
      width: 10px;
      height: 10px;
      border: 3px solid white;
      border-radius: 50%;
      background: var(--primary);
      box-shadow: 0 0 0 1px #93c5fd;
      content: "";
    }

    .timeline-time {
      color: var(--primary);
      font-size: 12px;
      font-weight: bold;
    }

    .timeline-text {
      margin-top: 3px;
      color: #475569;
      font-size: 13px;
    }

    .modal-mask {
      position: fixed;
      z-index: 100;
      top: 0;
      right: 0;
      bottom: 0;
      left: 0;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 20px;
      background: rgba(15, 23, 42, 0.45);
    }

    .modal-mask.show {
      display: flex;
    }

    .modal {
      width: min(560px, 100%);
      max-height: 90vh;
      overflow-y: auto;
      border-radius: 10px;
      background: white;
      box-shadow: 0 20px 60px rgba(0,0,0,0.22);
    }

    .modal-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 18px 20px;
      border-bottom: 1px solid var(--border);
    }

    .modal-header h3 {
      margin: 0;
      font-size: 17px;
    }

    .close {
      border: 0;
      color: #64748b;
      background: transparent;
      font-size: 22px;
    }

    .modal-body {
      padding: 20px;
    }

    .form-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 14px;
    }

    .form-item {
      display: flex;
      flex-direction: column;
      gap: 6px;
    }

    .form-item.full {
      grid-column: 1 / -1;
    }

    .form-item label {
      color: #475569;
      font-size: 13px;
    }

    .modal-footer {
      display: flex;
      justify-content: flex-end;
      gap: 10px;
      padding: 14px 20px;
      border-top: 1px solid var(--border);
    }

    .toast {
      position: fixed;
      z-index: 200;
      top: 82px;
      right: 24px;
      display: none;
      min-width: 240px;
      padding: 13px 17px;
      border: 1px solid #bfdbfe;
      border-radius: 7px;
      color: #1e40af;
      background: #eff6ff;
      box-shadow: 0 8px 25px rgba(0,0,0,0.1);
    }

    .toast.show {
      display: block;
    }

    .empty {
      padding: 30px;
      color: var(--sub-text);
      text-align: center;
    }

    @media (max-width: 1200px) {
      .metric-grid {
        grid-template-columns: repeat(3, 1fr);
      }

      .dashboard-grid,
      .dashboard-grid.bottom,
      .two-column {
        grid-template-columns: 1fr;
      }
    }

    @media (max-width: 820px) {
      .sidebar {
        position: relative;
        width: 70px;
        padding: 14px 8px;
      }

      .main {
        width: calc(100% - 70px);
        margin-left: 70px;
      }

      .brand {
        justify-content: center;
        padding: 0 0 22px;
      }

      .brand-text,
      .nav-title,
      .nav-item span:not(.nav-icon),
      .sidebar-bottom {
        display: none;
      }

      .nav-item {
        justify-content: center;
        padding: 12px 5px;
      }

      .topbar {
        padding: 0 15px;
      }

      .topbar-title {
        font-size: 16px;
      }

      .content {
        padding: 16px;
      }

      .metric-grid {
        grid-template-columns: repeat(2, 1fr);
      }

      .dispatch-list,
      .form-grid {
        grid-template-columns: 1fr;
      }

      .form-item.full {
        grid-column: auto;
      }
    }
  </style>
</head>

<body>
<div class="app">
  <aside class="sidebar">
    <div class="brand">
      <div class="brand-icon">💧</div>
      <div class="brand-text">灌区智慧调度<br>原型系统</div>
    </div>

    <div class="nav-title">业务管理</div>

    <div class="nav-item active" data-page="dashboard">
      <span class="nav-icon">▦</span>
      <span>综合驾驶舱</span>
    </div>

    <div class="nav-item" data-page="demand">
      <span class="nav-icon">◒</span>
      <span>需水预测</span>
    </div>

    <div class="nav-item" data-page="moisture">
      <span class="nav-icon">♧</span>
      <span>土壤墒情</span>
    </div>

    <div class="nav-item" data-page="plans">
      <span class="nav-icon">☷</span>
      <span>配水计划</span>
    </div>

    <div class="nav-item" data-page="dispatch">
      <span class="nav-icon">⇄</span>
      <span>调度执行</span>
    </div>

    <div class="nav-item" data-page="statistics">
      <span class="nav-icon">▥</span>
      <span>统计分析</span>
    </div>

    <div class="sidebar-bottom">
      数据更新时间：2026-09-20 09:50<br>
      系统状态：<span style="color:#86efac">运行正常</span><br>
      数据来源：示例模拟数据
    </div>
  </aside>

  <main class="main">
    <header class="topbar">
      <div class="topbar-title">济南市南部某灌区节水灌溉与用水调度系统</div>
      <div class="topbar-right">
        <span id="currentTime"></span>
        <span>消息提醒：<b style="color:#dc2626">3</b></span>
        <div class="user">
          <div class="avatar">管</div>
          <span>灌区管理员</span>
        </div>
      </div>
    </header>

    <section class="content">

      <!-- 综合驾驶舱 -->
      <div id="page-dashboard" class="page active">
        <div class="page-title">
          <div>
            <h1>综合驾驶舱</h1>
            <p>查看灌区整体用水、墒情、配水计划和调度执行情况</p>
          </div>
          <button class="btn btn-primary" onclick="showToast('数据已刷新')">↻ 刷新数据</button>
        </div>

        <div class="metric-grid">
          <div class="metric-card">
            <div class="metric-label">今日灌溉面积</div>
            <div class="metric-value">12,680<span class="metric-unit">亩</span></div>
            <div class="metric-desc">较昨日增长 4.6%</div>
          </div>

          <div class="metric-card">
            <div class="metric-label">今日实际用水量</div>
            <div class="metric-value">86.4<span class="metric-unit">万m³</span></div>
            <div class="metric-desc">低于计划 6.1%</div>
          </div>

          <div class="metric-card">
            <div class="metric-label">计划用水量</div>
            <div class="metric-value">92.0<span class="metric-unit">万m³</span></div>
            <div class="metric-desc">今日计划 18 项</div>
          </div>

          <div class="metric-card">
            <div class="metric-label">综合节水率</div>
            <div class="metric-value">8.7<span class="metric-unit">%</span></div>
            <div class="metric-desc">较上周提升 1.3%</div>
          </div>

          <div class="metric-card">
            <div class="metric-label">当前执行任务</div>
            <div class="metric-value">8<span class="metric-unit">项</span></div>
            <div class="metric-desc">完成率 76.4%</div>
          </div>

          <div class="metric-card">
            <div class="metric-label">异常预警</div>
            <div class="metric-value" style="color:#dc2626">3<span class="metric-unit">条</span></div>
            <div class="metric-desc" style="color:#dc2626">需及时处理</div>
          </div>
        </div>

        <div class="dashboard-grid">
          <div class="card">
            <div class="card-title">
              灌区墒情与监测点
              <small>点击监测点查看详情</small>
            </div>

            <div class="map-box">
              <div class="map-title">济南南部某灌区示意图</div>
              <div class="river"></div>
              <div class="area east">东灌区</div>
              <div class="area west">西灌区</div>
              <div class="area south">南灌区</div>
              <div class="area north">北灌区</div>

              <div class="monitor-point point-1" onclick="showMoistureDetail('东区-03')">3</div>
              <div class="monitor-point point-2" onclick="showMoistureDetail('西区-02')">2</div>
              <div class="monitor-point point-3" onclick="showMoistureDetail('南区-01')">1</div>
              <div class="monitor-point point-4" onclick="showMoistureDetail('北区-04')">4</div>

              <div class="map-legend">
                <span class="legend-dot" style="background:#16a34a"></span>适宜
                <span class="legend-dot" style="background:#f59e0b"></span>偏低
                <span class="legend-dot" style="background:#dc2626"></span>干旱
              </div>
            </div>
          </div>

          <div class="card">
            <div class="card-title">
              未来7日需水预测
              <small>单位：万m³</small>
            </div>
            <div id="dashboardDemandChart" class="chart"></div>
          </div>
        </div>

        <div class="dashboard-grid bottom">
          <div class="card">
            <div class="card-title">
              各灌区用水对比
              <small>计划 / 实际</small>
            </div>
            <div id="areaWaterChart" class="chart small"></div>
          </div>

          <div class="card">
            <div class="card-title">
              配水计划执行率
              <small>按灌区统计</small>
            </div>
            <div id="planProgressChart" class="chart small"></div>
          </div>

          <div class="card">
            <div class="card-title">重点预警</div>
            <div class="alert-list">
              <div class="alert-item">
                <div class="alert-icon">⚠️</div>
                <div class="alert-content">
                  <div class="alert-title">南灌区土壤墒情偏低</div>
                  <div class="alert-desc">南区-01当前含水率39%，建议24小时内安排灌溉。</div>
                </div>
              </div>

              <div class="alert-item">
                <div class="alert-icon">⚠️</div>
                <div class="alert-content">
                  <div class="alert-title">东干渠实际流量偏低</div>
                  <div class="alert-desc">当前流量较计划值低12%，请检查闸门状态。</div>
                </div>
              </div>

              <div class="alert-item">
                <div class="alert-icon">ℹ️</div>
                <div class="alert-content">
                  <div class="alert-title">北灌区计划即将开始</div>
                  <div class="alert-desc">北灌区灌溉任务将于10:30开始，请提前检查设备。</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- 需水预测 -->
      <div id="page-demand" class="page">
        <div class="page-title">
          <div>
            <h1>需水预测</h1>
            <p>综合历史用水、墒情和作物种植情况，辅助制定灌溉计划</p>
          </div>
        </div>

        <div class="filter-bar">
          <span class="filter-label">灌区：</span>
          <select id="demandArea">
            <option value="全部灌区">全部灌区</option>
            <option value="东灌区">东灌区</option>
            <option value="西灌区">西灌区</option>
            <option value="南灌区">南灌区</option>
            <option value="北灌区">北灌区</option>
          </select>

          <span class="filter-label">预测周期：</span>
          <select id="demandDays">
            <option value="7">未来7天</option>
            <option value="3">未来3天</option>
          </select>

          <button class="btn btn-primary" onclick="renderDemandPage()">查询</button>
          <button class="btn" onclick="resetDemandFilter()">重置</button>
        </div>

        <div class="two-column">
          <div class="card">
            <div class="card-title">需水量预测趋势 <small>预测值与建议供水量</small></div>
            <div id="demandTrendChart" class="chart"></div>
          </div>

          <div class="card">
            <div class="card-title">作物需水结构 <small>按种植作物统计</small></div>
            <div id="cropDemandChart" class="chart"></div>
          </div>
        </div>

        <div class="card" style="margin-top:18px">
          <div class="card-title">
            需水预测明细
            <small>建议优先保障墒情较低区域</small>
          </div>
          <div class="table-wrap">
            <table>
              <thead>
              <tr>
                <th>日期</th>
                <th>灌区</th>
                <th>主要作物</th>
                <th>预测需水量</th>
                <th>建议供水量</th>
                <th>墒情</th>
                <th>优先级</th>
                <th>操作</th>
              </tr>
              </thead>
              <tbody id="demandTableBody"></tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- 土壤墒情 -->
      <div id="page-moisture" class="page">
        <div class="page-title">
          <div>
            <h1>土壤墒情监测</h1>
            <p>监测各灌区土壤含水率，辅助判断灌溉时机和灌溉优先级</p>
          </div>
        </div>

        <div class="filter-bar">
          <span class="filter-label">灌区：</span>
          <select id="moistureArea">
            <option value="全部灌区">全部灌区</option>
            <option value="东灌区">东灌区</option>
            <option value="西灌区">西灌区</option>
            <option value="南灌区">南灌区</option>
            <option value="北灌区">北灌区</option>
          </select>

          <span class="filter-label">墒情等级：</span>
          <select id="moistureLevel">
            <option value="全部">全部</option>
            <option value="适宜">适宜</option>
            <option value="偏低">偏低</option>
            <option value="干旱">干旱</option>
          </select>

          <button class="btn btn-primary" onclick="renderMoisturePage()">查询</button>
          <button class="btn" onclick="resetMoistureFilter()">重置</button>
        </div>

        <div class="two-column">
          <div class="card">
            <div class="card-title">土壤含水率分布 <small>单位：%</small></div>
            <div id="moistureChart" class="chart"></div>
          </div>

          <div class="card">
            <div class="card-title">近7日墒情变化 <small>监测点：南区-01</small></div>
            <div id="moistureTrendChart" class="chart"></div>
          </div>
        </div>

        <div class="card" style="margin-top:18px">
          <div class="card-title">
            墒情监测点明细
            <small>点击“查看”查看监测点历史数据</small>
          </div>
          <div class="table-wrap">
            <table>
              <thead>
              <tr>
                <th>监测点</th>
                <th>所属灌区</th>
                <th>主要作物</th>
                <th>土壤含水率</th>
                <th>墒情等级</th>
                <th>温度</th>
                <th>采集时间</th>
                <th>建议</th>
                <th>操作</th>
              </tr>
              </thead>
              <tbody id="moistureTableBody"></tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- 配水计划 -->
      <div id="page-plans" class="page">
        <div class="page-title">
          <div>
            <h1>配水计划</h1>
            <p>根据需水预测和墒情情况制定、审核灌区配水计划</p>
          </div>
          <button class="btn btn-primary" onclick="openPlanModal()">＋ 新建配水计划</button>
        </div>

        <div class="filter-bar">
          <span class="filter-label">灌区：</span>
          <select id="planArea">
            <option value="全部灌区">全部灌区</option>
            <option value="东灌区">东灌区</option>
            <option value="西灌区">西灌区</option>
            <option value="南灌区">南灌区</option>
            <option value="北灌区">北灌区</option>
          </select>

          <span class="filter-label">状态：</span>
          <select id="planStatus">
            <option value="全部">全部</option>
            <option value="待审核">待审核</option>
            <option value="已审核">已审核</option>
            <option value="执行中">执行中</option>
            <option value="已完成">已完成</option>
          </select>

          <button class="btn btn-primary" onclick="renderPlanTable()">查询</button>
          <button class="btn" onclick="resetPlanFilter()">重置</button>
        </div>

        <div class="card">
          <div class="card-title">
            配水计划列表
            <small>计划水量单位：万m³</small>
          </div>
          <div class="table-wrap">
            <table>
              <thead>
              <tr>
                <th>计划编号</th>
                <th>灌区</th>
                <th>计划日期</th>
                <th>供水来源</th>
                <th>计划水量</th>
                <th>灌溉面积</th>
                <th>优先级</th>
                <th>状态</th>
                <th>操作</th>
              </tr>
              </thead>
              <tbody id="planTableBody"></tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- 调度执行 -->
      <div id="page-dispatch" class="page">
        <div class="page-title">
          <div>
            <h1>调度执行</h1>
            <p>查看灌溉任务执行进度、泵站闸门状态和异常信息</p>
          </div>
          <button class="btn btn-primary" onclick="showToast('调度数据已刷新')">↻ 刷新任务</button>
        </div>

        <div class="metric-grid" style="grid-template-columns:repeat(4,1fr)">
          <div class="metric-card">
            <div class="metric-label">今日调度任务</div>
            <div class="metric-value">18<span class="metric-unit">项</span></div>
            <div class="metric-desc">已完成 10 项</div>
          </div>
          <div class="metric-card">
            <div class="metric-label">执行中任务</div>
            <div class="metric-value" style="color:#1677ff">8<span class="metric-unit">项</span></div>
            <div class="metric-desc">当前运行正常</div>
          </div>
          <div class="metric-card">
            <div class="metric-label">计划完成率</div>
            <div class="metric-value">76.4<span class="metric-unit">%</span></div>
            <div class="metric-desc">较昨日提高 5.2%</div>
          </div>
          <div class="metric-card">
            <div class="metric-label">异常任务</div>
            <div class="metric-value" style="color:#dc2626">2<span class="metric-unit">项</span></div>
            <div class="metric-desc" style="color:#dc2626">需要人工处理</div>
          </div>
        </div>

        <div class="dispatch-list" id="dispatchList"></div>

        <div class="card" style="margin-top:18px">
          <div class="card-title">今日调度时间轴 <small>东灌区调度任务 TS20260920008</small></div>
          <div class="timeline">
            <div class="timeline-item">
              <div class="timeline-time">06:30</div>
              <div class="timeline-text">泵站启动，供水系统进入运行状态</div>
            </div>
            <div class="timeline-item">
              <div class="timeline-time">07:00</div>
              <div class="timeline-text">1号闸门开启，东干渠开始预供水</div>
            </div>
            <div class="timeline-item">
              <div class="timeline-time">08:00</div>
              <div class="timeline-text">东灌区水稻灌溉正式开始</div>
            </div>
            <div class="timeline-item">
              <div class="timeline-time">10:20</div>
              <div class="timeline-text" style="color:#dc2626">实际流量低于计划值12%，系统发出预警</div>
            </div>
          </div>
        </div>
      </div>

      <!-- 统计分析 -->
      <div id="page-statistics" class="page">
        <div class="page-title">
          <div>
            <h1>统计分析</h1>
            <p>分析灌区供水完成率、节水率、亩均用水量和渠道输水损失</p>
          </div>
          <button class="btn btn-primary" onclick="exportCSV()">导出统计数据</button>
        </div>

        <div class="metric-grid" style="grid-template-columns:repeat(4,1fr)">
          <div class="metric-card">
            <div class="metric-label">本月累计供水量</div>
            <div class="metric-value">2,438<span class="metric-unit">万m³</span></div>
            <div class="metric-desc">同比下降 7.4%</div>
          </div>
          <div class="metric-card">
            <div class="metric-label">本月综合节水率</div>
            <div class="metric-value">9.2<span class="metric-unit">%</span></div>
            <div class="metric-desc">达到目标值</div>
          </div>
          <div class="metric-card">
            <div class="metric-label">平均亩均用水</div>
            <div class="metric-value">192<span class="metric-unit">m³/亩</span></div>
            <div class="metric-desc">较去年下降 13m³</div>
          </div>
          <div class="metric-card">
            <div class="metric-label">渠道输水损失率</div>
            <div class="metric-value">7.8<span class="metric-unit">%</span></div>
            <div class="metric-desc">低于控制目标</div>
          </div>
        </div>

        <div class="two-column">
          <div class="card">
            <div class="card-title">各灌区节水率</div>
            <div id="savingChart" class="chart"></div>
          </div>

          <div class="card">
            <div class="card-title">月度用水趋势</div>
            <div id="monthlyWaterChart" class="chart"></div>
          </div>
        </div>

        <div class="card" style="margin-top:18px">
          <div class="card-title">灌区综合指标排名</div>
          <div class="table-wrap">
            <table>
              <thead>
              <tr>
                <th>排名</th>
                <th>灌区</th>
                <th>灌溉面积</th>
                <th>计划用水量</th>
                <th>实际用水量</th>
                <th>节水率</th>
                <th>供水完成率</th>
                <th>综合评价</th>
              </tr>
              </thead>
              <tbody>
              <tr>
                <td>1</td>
                <td>北灌区</td>
                <td>3,100亩</td>
                <td>21.2万m³</td>
                <td>18.7万m³</td>
                <td><span class="tag tag-green">11.8%</span></td>
                <td>98.2%</td>
                <td><span class="tag tag-green">优秀</span></td>
              </tr>
              <tr>
                <td>2</td>
                <td>西灌区</td>
                <td>2,850亩</td>
                <td>19.8万m³</td>
                <td>18.4万m³</td>
                <td><span class="tag tag-green">7.1%</span></td>
                <td>95.4%</td>
                <td><span class="tag tag-blue">良好</span></td>
              </tr>
              <tr>
                <td>3</td>
                <td>东灌区</td>
                <td>3,620亩</td>
                <td>28.6万m³</td>
                <td>26.8万m³</td>
                <td><span class="tag tag-green">6.3%</span></td>
                <td>93.7%</td>
                <td><span class="tag tag-blue">良好</span></td>
              </tr>
              <tr>
                <td>4</td>
                <td>南灌区</td>
                <td>3,110亩</td>
                <td>30.4万m³</td>
                <td>29.5万m³</td>
                <td><span class="tag tag-orange">3.0%</span></td>
                <td>89.4%</td>
                <td><span class="tag tag-orange">需关注</span></td>
              </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

    </section>
  </main>
</div>

<!-- 通用弹窗 -->
<div id="modalMask" class="modal-mask" onclick="closeModalByMask(event)">
  <div class="modal">
    <div class="modal-header">
      <h3 id="modalTitle">详情</h3>
      <button class="close" onclick="closeModal()">×</button>
    </div>
    <div id="modalBody" class="modal-body"></div>
    <div id="modalFooter" class="modal-footer"></div>
  </div>
</div>

<div id="toast" class="toast"></div>

<script>
  // -----------------------------
  // 示例数据：济南市南部某灌区
  // -----------------------------
  const moistureData = [
    {
      id: "东区-03",
      area: "东灌区",
      crop: "水稻",
      moisture: 48,
      level: "偏低",
      temperature: 24.6,
      time: "2026-09-20 09:42",
      suggestion: "48小时内安排灌溉"
    },
    {
      id: "西区-02",
      area: "西灌区",
      crop: "玉米",
      moisture: 72,
      level: "适宜",
      temperature: 23.8,
      time: "2026-09-20 09:40",
      suggestion: "当前无需灌溉"
    },
    {
      id: "南区-01",
      area: "南灌区",
      crop: "小麦",
      moisture: 39,
      level: "干旱",
      temperature: 25.3,
      time: "2026-09-20 09:46",
      suggestion: "24小时内优先灌溉"
    },
    {
      id: "北区-04",
      area: "北灌区",
      crop: "蔬菜",
      moisture: 81,
      level: "适宜",
      temperature: 22.9,
      time: "2026-09-20 09:38",
      suggestion: "当前无需灌溉"
    }
  ];

  const demandData = [
    ["2026-09-21", "东灌区", "水稻", 30.2, 28.5, "48%", "高"],
    ["2026-09-21", "西灌区", "玉米", 18.6, 17.8, "72%", "中"],
    ["2026-09-21", "南灌区", "小麦", 35.4, 33.8, "39%", "高"],
    ["2026-09-21", "北灌区", "蔬菜", 12.8, 12.0, "81%", "低"],
    ["2026-09-22", "东灌区", "水稻", 31.6, 29.4, "48%", "高"],
    ["2026-09-22", "西灌区", "玉米", 17.9, 17.0, "72%", "中"],
    ["2026-09-22", "南灌区", "小麦", 36.2, 34.8, "39%", "高"],
    ["2026-09-22", "北灌区", "蔬菜", 12.5, 11.8, "81%", "低"]
  ];

  let plans = [
    {
      id: "PD20260920001",
      area: "东灌区",
      date: "2026-09-20",
      source: "卧虎山水库",
      water: 28.6,
      land: 3620,
      priority: "高",
      status: "执行中"
    },
    {
      id: "PD20260920002",
      area: "西灌区",
      date: "2026-09-20",
      source: "东风渠",
      water: 19.8,
      land: 2850,
      priority: "中",
      status: "已审核"
    },
    {
      id: "PD20260920003",
      area: "南灌区",
      date: "2026-09-20",
      source: "玉符河泵站",
      water: 30.4,
      land: 3110,
      priority: "高",
      status: "待审核"
    },
    {
      id: "PD20260919004",
      area: "北灌区",
      date: "2026-09-19",
      source: "北部干渠",
      water: 21.2,
      land: 3100,
      priority: "低",
      status: "已完成"
    }
  ];

  let dispatchTasks = [
    {
      id: "TS20260920008",
      title: "东灌区水稻灌溉",
      area: "东灌区",
      time: "08:00—12:00",
      planned: 12.5,
      actual: 10.8,
      progress: 86,
      status: "执行中"
    },
    {
      id: "TS20260920009",
      title: "西灌区玉米补水",
      area: "西灌区",
      time: "09:00—11:30",
      planned: 8.6,
      actual: 8.2,
      progress: 92,
      status: "执行中"
    },
    {
      id: "TS20260920010",
      title: "南灌区优先灌溉",
      area: "南灌区",
      time: "10:30—15:00",
      planned: 15.4,
      actual: 0,
      progress: 0,
      status: "待执行"
    },
    {
      id: "TS20260920011",
      title: "北灌区蔬菜灌溉",
      area: "北灌区",
      time: "06:30—09:30",
      planned: 9.6,
      actual: 9.4,
      progress: 100,
      status: "已完成"
    }
  ];

  let charts = {};

  // -----------------------------
  // 基础工具
  // -----------------------------
  function showToast(message) {
    const toast = document.getElementById("toast");
    toast.textContent = message;
    toast.classList.add("show");
    setTimeout(() => toast.classList.remove("show"), 2200);
  }

  function updateTime() {
    const now = new Date();
    const text = now.toLocaleString("zh-CN", {
      year: "numeric",
      month: "2-digit",
      day: "2-digit",
      hour: "2-digit",
      minute: "2-digit",
      second: "2-digit",
      hour12: false
    });
    document.getElementById("currentTime").textContent = text;
  }

  setInterval(updateTime, 1000);
  updateTime();

  function openModal(title, body, footer = "") {
    document.getElementById("modalTitle").textContent = title;
    document.getElementById("modalBody").innerHTML = body;
    document.getElementById("modalFooter").innerHTML = footer;
    document.getElementById("modalMask").classList.add("show");
  }

  function closeModal() {
    document.getElementById("modalMask").classList.remove("show");
  }

  function closeModalByMask(event) {
    if (event.target.id === "modalMask") {
      closeModal();
    }
  }

  function statusTag(status) {
    const map = {
      "适宜": "tag-green",
      "已完成": "tag-green",
      "正常": "tag-green",
      "偏低": "tag-orange",
      "待审核": "tag-orange",
      "待执行": "tag-gray",
      "执行中": "tag-blue",
      "已审核": "tag-blue",
      "干旱": "tag-red",
      "异常": "tag-red",
      "高": "tag-red",
      "中": "tag-orange",
      "低": "tag-green"
    };

    return `<span class="tag ${map[status] || "tag-gray"}">${status}</span>`;
  }

  // -----------------------------
  // 页面导航
  // -----------------------------
  document.querySelectorAll(".nav-item").forEach(item => {
    item.addEventListener("click", () => {
      const page = item.dataset.page;

      document.querySelectorAll(".nav-item").forEach(nav => {
        nav.classList.remove("active");
      });

      document.querySelectorAll(".page").forEach(content => {
        content.classList.remove("active");
      });

      item.classList.add("active");
      document.getElementById("page-" + page).classList.add("active");

      if (page === "dashboard") {
        renderDashboardCharts();
      }

      if (page === "demand") {
        renderDemandPage();
      }

      if (page === "moisture") {
        renderMoisturePage();
      }

      if (page === "plans") {
        renderPlanTable();
      }

      if (page === "dispatch") {
        renderDispatch();
      }

      if (page === "statistics") {
        renderStatistics();
      }
    });
  });

  // -----------------------------
  // 图表工具
  // -----------------------------
  function initChart(id, option) {
    const element = document.getElementById(id);
    if (!element) return;

    if (charts[id]) {
      charts[id].dispose();
    }

    charts[id] = echarts.init(element);
    charts[id].setOption(option);
    window.addEventListener("resize", () => charts[id] && charts[id].resize());
  }

  function renderDashboardCharts() {
    initChart("dashboardDemandChart", {
      tooltip: { trigger: "axis" },
      legend: { data: ["预测需水量", "建议供水量"] },
      grid: { left: 45, right: 20, top: 45, bottom: 30 },
      xAxis: {
        type: "category",
        data: ["9/20", "9/21", "9/22", "9/23", "9/24", "9/25", "9/26"]
      },
      yAxis: { type: "value", name: "万m³" },
      series: [
        {
          name: "预测需水量",
          type: "line",
          smooth: true,
          data: [86, 97, 98, 92, 89, 84, 81],
          itemStyle: { color: "#1677ff" },
          areaStyle: { color: "rgba(22,119,255,.12)" }
        },
        {
          name: "建议供水量",
          type: "line",
          smooth: true,
          data: [82, 91, 93, 88, 84, 80, 76],
          itemStyle: { color: "#16a34a" }
        }
      ]
    });

    initChart("areaWaterChart", {
      tooltip: { trigger: "axis" },
      legend: { data: ["计划用水", "实际用水"] },
      grid: { left: 40, right: 15, top: 45, bottom: 30 },
      xAxis: {
        type: "category",
        data: ["东灌区", "西灌区", "南灌区", "北灌区"]
      },
      yAxis: { type: "value", name: "万m³" },
      series: [
        {
          name: "计划用水",
          type: "bar",
          data: [28.6, 19.8, 30.4, 21.2],
          itemStyle: { color: "#91caff" }
        },
        {
          name: "实际用水",
          type: "bar",
          data: [26.8, 18.4, 29.5, 18.7],
          itemStyle: { color: "#1677ff" }
        }
      ]
    });

    initChart("planProgressChart", {
      tooltip: { trigger: "item" },
      series: [
        {
          type: "pie",
          radius: ["48%", "72%"],
          label: { formatter: "{b}\n{d}%" },
          data: [
            { name: "已完成", value: 10, itemStyle: { color: "#16a34a" } },
            { name: "执行中", value: 6, itemStyle: { color: "#1677ff" } },
            { name: "待执行", value: 2, itemStyle: { color: "#f59e0b" } }
          ]
        }
      ]
    });
  }

  function renderDemandPage() {
    const area = document.getElementById("demandArea").value;
    const days = Number(document.getElementById("demandDays").value);

    let rows = demandData.slice(0, days * 4);

    if (area !== "全部灌区") {
      rows = rows.filter(item => item[1] === area);
    }

    const dates = days === 3
      ? ["9/21", "9/22", "9/23"]
      : ["9/21", "9/22", "9/23", "9/24", "9/25", "9/26", "9/27"];

    const demandBase = area === "南灌区"
      ? [35.4, 36.2, 34.8, 32.5, 31.6, 30.8, 30.2]
      : area === "东灌区"
        ? [30.2, 31.6, 29.8, 28.9, 28.2, 27.4, 26.8]
        : [97, 98, 92, 89, 84, 81, 79];

    initChart("demandTrendChart", {
      tooltip: { trigger: "axis" },
      legend: { data: ["预测需水量", "建议供水量"] },
      grid: { left: 50, right: 20, top: 45, bottom: 30 },
      xAxis: { type: "category", data: dates },
      yAxis: { type: "value", name: "万m³" },
      series: [
        {
          name: "预测需水量",
          type: "line",
          smooth: true,
          data: demandBase.slice(0, dates.length),
          itemStyle: { color: "#1677ff" }
        },
        {
          name: "建议供水量",
          type: "line",
          smooth: true,
          data: demandBase.slice(0, dates.length).map(v => +(v * 0.94).toFixed(1)),
          itemStyle: { color: "#16a34a" }
        }
      ]
    });

    initChart("cropDemandChart", {
      tooltip: { trigger: "item" },
      legend: { bottom: 0 },
      series: [
        {
          type: "pie",
          radius: "65%",
          data: [
            { value: 42, name: "水稻", itemStyle: { color: "#1677ff" } },
            { value: 26, name: "小麦", itemStyle: { color: "#f59e0b" } },
            { value: 20, name: "玉米", itemStyle: { color: "#16a34a" } },
            { value: 12, name: "蔬菜", itemStyle: { color: "#8b5cf6" } }
          ]
        }
      ]
    });

    const tbody = document.getElementById("demandTableBody");

    if (rows.length === 0) {
      tbody.innerHTML = `<tr><td colspan="8"><div class="empty">暂无符合条件的数据</div></td></tr>`;
      return;
    }

    tbody.innerHTML = rows.map((item, index) => `
      <tr>
        <td>${item[0]}</td>
        <td>${item[1]}</td>
        <td>${item[2]}</td>
        <td>${item[3]}万m³</td>
        <td>${item[4]}万m³</td>
        <td>${item[5]}</td>
        <td>${statusTag(item[6])}</td>
        <td>
          <button class="btn" onclick="showDemandDetail(${index})">查看</button>
        </td>
      </tr>
    `).join("");
  }

  function showDemandDetail(index) {
    const item = demandData[index] || demandData[0];

    openModal(
      "需水预测详情",
      `
      <div class="form-grid">
        <div class="form-item">
          <label>预测日期</label>
          <div>${item[0]}</div>
        </div>
        <div class="form-item">
          <label>所属灌区</label>
          <div>${item[1]}</div>
        </div>
        <div class="form-item">
          <label>主要作物</label>
          <div>${item[2]}</div>
        </div>
        <div class="form-item">
          <label>当前墒情</label>
          <div>${item[5]}</div>
        </div>
        <div class="form-item">
          <label>预测需水量</label>
          <div style="color:#1677ff;font-size:20px;font-weight:bold">${item[3]}万m³</div>
        </div>
        <div class="form-item">
          <label>建议供水量</label>
          <div style="color:#16a34a;font-size:20px;font-weight:bold">${item[4]}万m³</div>
        </div>
      </div>
      `,
      `<button class="btn btn-primary" onclick="closeModal()">关闭</button>`
    );
  }

  function resetDemandFilter() {
    document.getElementById("demandArea").value = "全部灌区";
    document.getElementById("demandDays").value = "7";
    renderDemandPage();
  }

  function renderMoisturePage() {
    const area = document.getElementById("moistureArea").value;
    const level = document.getElementById("moistureLevel").value;

    let rows = moistureData.filter(item => {
      const areaMatch = area === "全部灌区" || item.area === area;
      const levelMatch = level === "全部" || item.level === level;
      return areaMatch && levelMatch;
    });

    initChart("moistureChart", {
      tooltip: {
        trigger: "axis",
        formatter: params => {
          const p = params[0];
          return `${p.name}<br>土壤含水率：${p.value}%`;
        }
      },
      grid: { left: 45, right: 20, top: 30, bottom: 35 },
      xAxis: {
        type: "category",
        data: rows.map(item => item.id)
      },
      yAxis: {
        type: "value",
        min: 0,
        max: 100,
        name: "%"
      },
      series: [
        {
          type: "bar",
          barWidth: 32,
          data: rows.map(item => ({
            value: item.moisture,
            itemStyle: {
              color: item.level === "干旱"
                ? "#dc2626"
                : item.level === "偏低"
                  ? "#f59e0b"
                  : "#16a34a"
            }
          }))
        }
      ]
    });

    initChart("moistureTrendChart", {
      tooltip: { trigger: "axis" },
      grid: { left: 45, right: 20, top: 30, bottom: 30 },
      xAxis: {
        type: "category",
        data: ["9/14", "9/15", "9/16", "9/17", "9/18", "9/19", "9/20"]
      },
      yAxis: { type: "value", min: 20, max: 90, name: "%" },
      series: [
        {
          type: "line",
          smooth: true,
          data: [51, 49, 47, 45, 43, 41, 39],
          itemStyle: { color: "#dc2626" },
          areaStyle: { color: "rgba(220,38,38,.12)" }
        }
      ]
    });

    const tbody = document.getElementById("moistureTableBody");

    if (rows.length === 0) {
      tbody.innerHTML = `<tr><td colspan="9"><div class="empty">暂无符合条件的数据</div></td></tr>`;
      return;
    }

    tbody.innerHTML = rows.map(item => `
      <tr>
        <td>${item.id}</td>
        <td>${item.area}</td>
        <td>${item.crop}</td>
        <td><b style="color:${item.level === "干旱" ? "#dc2626" : item.level === "偏低" ? "#f59e0b" : "#16a34a"}">${item.moisture}%</b></td>
        <td>${statusTag(item.level)}</td>
        <td>${item.temperature}℃</td>
        <td>${item.time}</td>
        <td>${item.suggestion}</td>
        <td>
          <button class="btn" onclick="showMoistureDetail('${item.id}')">查看</button>
        </td>
      </tr>
    `).join("");
  }

  function showMoistureDetail(id) {
    const item = moistureData.find(item => item.id === id) || moistureData[0];

    openModal(
      "土壤墒情监测点详情",
      `
      <div class="form-grid">
        <div class="form-item">
          <label>监测点</label>
          <div>${item.id}</div>
        </div>
        <div class="form-item">
          <label>所属灌区</label>
          <div>${item.area}</div>
        </div>
        <div class="form-item">
          <label>主要作物</label>
          <div>${item.crop}</div>
        </div>
        <div class="form-item">
          <label>墒情等级</label>
          <div>${statusTag(item.level)}</div>
        </div>
        <div class="form-item">
          <label>当前含水率</label>
          <div style="font-size:23px;font-weight:bold;color:${item.level === "干旱" ? "#dc2626" : "#1677ff"}">${item.moisture}%</div>
        </div>
        <div class="form-item">
          <label>土壤温度</label>
          <div>${item.temperature}℃</div>
        </div>
        <div class="form-item full">
          <label>灌溉建议</label>
          <div style="padding:12px;border-radius:6px;background:#f8fafc">${item.suggestion}</div>
        </div>
        <div class="form-item full">
          <label>近7日变化</label>
          <div style="height:100px;background:linear-gradient(180deg,#eff6ff,#fff);padding:15px;border-radius:6px;color:#64748b">
            当前监测点近7日含水率呈${item.level === "干旱" || item.level === "偏低" ? "下降" : "稳定"}趋势，系统建议结合天气和作物生育期制定灌溉计划。
          </div>
        </div>
      </div>
      `,
      `<button class="btn btn-primary" onclick="closeModal()">关闭</button>`
    );
  }

  function resetMoistureFilter() {
    document.getElementById("moistureArea").value = "全部灌区";
    document.getElementById("moistureLevel").value = "全部";
    renderMoisturePage();
  }

  // -----------------------------
  // 配水计划
  // -----------------------------
  function renderPlanTable() {
    const area = document.getElementById("planArea").value;
    const status = document.getElementById("planStatus").value;

    const rows = plans.filter(item => {
      const areaMatch = area === "全部灌区" || item.area === area;
      const statusMatch = status === "全部" || item.status === status;
      return areaMatch && statusMatch;
    });

    const tbody = document.getElementById("planTableBody");

    if (rows.length === 0) {
      tbody.innerHTML = `<tr><td colspan="9"><div class="empty">暂无符合条件的数据</div></td></tr>`;
      return;
    }

    tbody.innerHTML = rows.map(item => `
      <tr>
        <td>${item.id}</td>
        <td>${item.area}</td>
        <td>${item.date}</td>
        <td>${item.source}</td>
        <td>${item.water}</td>
        <td>${item.land.toLocaleString()}亩</td>
        <td>${statusTag(item.priority)}</td>
        <td>${statusTag(item.status)}</td>
        <td>
          <button class="btn" onclick="showPlanDetail('${item.id}')">详情</button>
          ${item.status === "待审核" ? `<button class="btn btn-success" onclick="approvePlan('${item.id}')">审核</button>` : ""}
        </td>
      </tr>
    `).join("");
  }

  function openPlanModal() {
    openModal(
      "新建配水计划",
      `
      <div class="form-grid">
        <div class="form-item">
          <label>所属灌区</label>
          <select id="newPlanArea">
            <option>东灌区</option>
            <option>西灌区</option>
            <option>南灌区</option>
            <option>北灌区</option>
          </select>
        </div>

        <div class="form-item">
          <label>计划日期</label>
          <input id="newPlanDate" type="date" value="2026-09-20">
        </div>

        <div class="form-item">
          <label>供水来源</label>
          <select id="newPlanSource">
            <option>卧虎山水库</option>
            <option>东风渠</option>
            <option>玉符河泵站</option>
            <option>北部干渠</option>
          </select>
        </div>

        <div class="form-item">
          <label>计划水量（万m³）</label>
          <input id="newPlanWater" type="number" value="20" min="0">
        </div>

        <div class="form-item">
          <label>灌溉面积（亩）</label>
          <input id="newPlanLand" type="number" value="2500" min="0">
        </div>

        <div class="form-item">
          <label>优先级</label>
          <select id="newPlanPriority">
            <option>高</option>
            <option selected>中</option>
            <option>低</option>
          </select>
        </div>

        <div class="form-item full">
          <label>计划说明</label>
          <textarea id="newPlanRemark" rows="3" placeholder="例如：重点保障南灌区小麦苗期用水"></textarea>
        </div>
      </div>
      `,
      `
      <button class="btn" onclick="closeModal()">取消</button>
      <button class="btn btn-primary" onclick="submitPlan()">提交计划</button>
      `
    );
  }

  function submitPlan() {
    const area = document.getElementById("newPlanArea").value;
    const date = document.getElementById("newPlanDate").value;
    const source = document.getElementById("newPlanSource").value;
    const water = Number(document.getElementById("newPlanWater").value);
    const land = Number(document.getElementById("newPlanLand").value);
    const priority = document.getElementById("newPlanPriority").value;

    if (!date || !water || !land) {
      showToast("请完整填写计划日期、水量和灌溉面积");
      return;
    }

    const id = "PD" + date.replaceAll("-", "") + String(plans.length + 1).padStart(3, "0");

    plans.unshift({
      id,
      area,
      date,
      source,
      water,
      land,
      priority,
      status: "待审核"
    });

    closeModal();
    renderPlanTable();
    showToast("配水计划已提交，等待审核");
  }

  function showPlanDetail(id) {
    const item = plans.find(item => item.id === id);

    openModal(
      "配水计划详情",
      `
      <div class="form-grid">
        <div class="form-item">
          <label>计划编号</label>
          <div>${item.id}</div>
        </div>
        <div class="form-item">
          <label>计划状态</label>
          <div>${statusTag(item.status)}</div>
        </div>
        <div class="form-item">
          <label>所属灌区</label>
          <div>${item.area}</div>
        </div>
        <div class="form-item">
          <label>计划日期</label>
          <div>${item.date}</div>
        </div>
        <div class="form-item">
          <label>供水来源</label>
          <div>${item.source}</div>
        </div>
        <div class="form-item">
          <label>优先级</label>
          <div>${statusTag(item.priority)}</div>
        </div>
        <div class="form-item">
          <label>计划水量</label>
          <div style="font-size:20px;color:#1677ff;font-weight:bold">${item.water}万m³</div>
        </div>
        <div class="form-item">
          <label>灌溉面积</label>
          <div style="font-size:20px;color:#16a34a;font-weight:bold">${item.land.toLocaleString()}亩</div>
        </div>
      </div>
      `,
      `<button class="btn btn-primary" onclick="closeModal()">关闭</button>`
    );
  }

  function approvePlan(id) {
    const item = plans.find(item => item.id === id);
    if (item) {
      item.status = "已审核";
      renderPlanTable();
      showToast("配水计划已审核通过");
    }
  }

  function resetPlanFilter() {
    document.getElementById("planArea").value = "全部灌区";
    document.getElementById("planStatus").value = "全部";
    renderPlanTable();
  }

  // -----------------------------
  // 调度执行
  // -----------------------------
  function renderDispatch() {
    const container = document.getElementById("dispatchList");

    container.innerHTML = dispatchTasks.map(task => {
      const statusClass = task.status === "异常"
        ? "tag-red"
        : task.status === "执行中"
          ? "tag-blue"
          : task.status === "已完成"
            ? "tag-green"
            : "tag-gray";

      return `
        <div class="task-card">
          <div class="task-head">
            <div>
              <div class="task-title">${task.title}</div>
              <div style="margin-top:5px;color:#94a3b8;font-size:12px">${task.id}</div>
            </div>
            <span class="tag ${statusClass}">${task.status}</span>
          </div>

          <div class="task-info">
            <div>所属灌区<strong>${task.area}</strong></div>
            <div>执行时间<strong>${task.time}</strong></div>
            <div>计划水量<strong>${task.planned}万m³</strong></div>
            <div>实际水量<strong>${task.actual}万m³</strong></div>
          </div>

          <div style="display:flex;align-items:center;gap:10px">
            <div class="progress" style="flex:1">
              <div class="progress-bar" style="width:${task.progress}%;background:${task.status === "异常" ? "#dc2626" : "#1677ff"}"></div>
            </div>
            <b>${task.progress}%</b>
          </div>

          <div class="task-actions">
            <button class="btn" onclick="showTaskDetail('${task.id}')">查看详情</button>
            ${
              task.status === "待执行"
                ? `<button class="btn btn-primary" onclick="startTask('${task.id}')">开始执行</button>`
                : ""
            }
            ${
              task.status === "执行中"
                ? `<button class="btn btn-success" onclick="finishTask('${task.id}')">完成任务</button>`
                : ""
            }
            ${
              task.status !== "已完成"
                ? `<button class="btn btn-warning" onclick="reportException('${task.id}')">异常上报</button>`
                : ""
            }
          </div>
        </div>
      `;
    }).join("");
  }

  function showTaskDetail(id) {
    const task = dispatchTasks.find(item => item.id === id);

    openModal(
      "调度任务详情",
      `
      <div class="form-grid">
        <div class="form-item">
          <label>任务编号</label>
          <div>${task.id}</div>
        </div>
        <div class="form-item">
          <label>任务状态</label>
          <div>${statusTag(task.status)}</div>
        </div>
        <div class="form-item">
          <label>任务名称</label>
          <div>${task.title}</div>
        </div>
        <div class="form-item">
          <label>所属灌区</label>
          <div>${task.area}</div>
        </div>
        <div class="form-item">
          <label>计划水量</label>
          <div>${task.planned}万m³</div>
        </div>
        <div class="form-item">
          <label>实际水量</label>
          <div>${task.actual}万m³</div>
        </div>
        <div class="form-item full">
          <label>当前执行进度</label>
          <div class="progress" style="width:100%;height:12px">
            <div class="progress-bar" style="width:${task.progress}%"></div>
          </div>
          <div style="margin-top:7px">${task.progress}%</div>
        </div>
      </div>
      `,
      `<button class="btn btn-primary" onclick="closeModal()">关闭</button>`
    );
  }

  function startTask(id) {
    const task = dispatchTasks.find(item => item.id === id);
    if (task) {
      task.status = "执行中";
      task.progress = 5;
      task.actual = 0.6;
      renderDispatch();
      showToast("调度任务已开始执行");
    }
  }

  function finishTask(id) {
    const task = dispatchTasks.find(item => item.id === id);
    if (task) {
      task.status = "已完成";
      task.progress = 100;
      task.actual = task.planned;
      renderDispatch();
      showToast("调度任务已完成");
    }
  }

  function reportException(id) {
    const task = dispatchTasks.find(item => item.id === id);
    if (!task) return;

    openModal(
      "调度异常上报",
      `
      <div class="form-grid">
        <div class="form-item full">
          <label>任务名称</label>
          <div>${task.title}</div>
        </div>
        <div class="form-item">
          <label>异常类型</label>
          <select id="exceptionType">
            <option>实际流量低于计划</option>
            <option>闸门设备异常</option>
            <option>泵站运行异常</option>
            <option>现场道路或渠道堵塞</option>
          </select>
        </div>
        <div class="form-item">
          <label>责任人</label>
          <input id="exceptionPerson" value="东区管理站">
        </div>
        <div class="form-item full">
          <label>异常描述</label>
          <textarea id="exceptionDesc" rows="4">当前实际流量低于计划值，请安排人员检查渠道和闸门状态。</textarea>
        </div>
      </div>
      `,
      `
      <button class="btn" onclick="closeModal()">取消</button>
      <button class="btn btn-danger" onclick="submitException('${id}')">提交异常</button>
      `
    );
  }

  function submitException(id) {
    const task = dispatchTasks.find(item => item.id === id);

    if (task) {
      task.status = "异常";
      closeModal();
      renderDispatch();
      showToast("异常信息已上报");
    }
  }

  // -----------------------------
  // 统计分析
  // -----------------------------
  function renderStatistics() {
    initChart("savingChart", {
      tooltip: { trigger: "axis" },
      grid: { left: 45, right: 20, top: 30, bottom: 35 },
      xAxis: {
        type: "category",
        data: ["东灌区", "西灌区", "南灌区", "北灌区"]
      },
      yAxis: { type: "value", name: "%", max: 15 },
      series: [
        {
          type: "bar",
          barWidth: 36,
          data: [
            { value: 6.3, itemStyle: { color: "#1677ff" } },
            { value: 7.1, itemStyle: { color: "#1677ff" } },
            { value: 3.0, itemStyle: { color: "#f59e0b" } },
            { value: 11.8, itemStyle: { color: "#16a34a" } }
          ]
        }
      ]
    });

    initChart("monthlyWaterChart", {
      tooltip: { trigger: "axis" },
      grid: { left: 45, right: 20, top: 30, bottom: 35 },
      xAxis: {
        type: "category",
        data: ["4月", "5月", "6月", "7月", "8月", "9月"]
      },
      yAxis: { type: "value", name: "万m³" },
      series: [
        {
          type: "line",
          smooth: true,
          data: [1680, 1840, 2130, 2680, 2520, 2438],
          itemStyle: { color: "#1677ff" },
          areaStyle: { color: "rgba(22,119,255,.12)" }
        }
      ]
    });
  }

  function exportCSV() {
    const rows = [
      ["灌区", "计划用水量(万m³)", "实际用水量(万m³)", "节水率", "供水完成率"],
      ["东灌区", "28.6", "26.8", "6.3%", "93.7%"],
      ["西灌区", "19.8", "18.4", "7.1%", "95.4%"],
      ["南灌区", "30.4", "29.5", "3.0%", "89.4%"],
      ["北灌区", "21.2", "18.7", "11.8%", "98.2%"]
    ];

    const csv = rows.map(row => row.join(",")).join("\n");
    const blob = new Blob(["\ufeff" + csv], { type: "text/csv;charset=utf-8;" });
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");

    link.href = url;
    link.download = "济南南部灌区统计分析.csv";
    link.click();

    URL.revokeObjectURL(url);
    showToast("统计数据已导出");
  }

  // -----------------------------
  // 初始化
  // -----------------------------
  renderDashboardCharts();
  renderDemandPage();
  renderMoisturePage();
  renderPlanTable();
  renderDispatch();
  renderStatistics();
</script>
</body>
</html>
