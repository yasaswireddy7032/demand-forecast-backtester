import json,numpy as np
from sklearn.linear_model import Ridge
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

def series(n=240,seed=7):
    rng=np.random.default_rng(seed);t=np.arange(n)
    return 50+.08*t+9*np.sin(2*np.pi*t/7)+rng.normal(0,2,n)

def feature(history):
    h=np.asarray(history)
    if len(h)<14:raise ValueError('At least 14 historical observations required')
    t=len(h)
    return [h[-1],h[-7],h[-14],h[-7:].mean(),np.sin(2*np.pi*t/7),np.cos(2*np.pi*t/7),t]

def backtest(values,start=100):
    y=np.asarray(values,dtype=float)
    if not np.isfinite(y).all() or start<30 or start>=len(y):raise ValueError('Invalid series or split')
    rows=[]
    for cutoff in range(start,len(y)):
        x=[feature(y[:i]) for i in range(14,cutoff)]
        model=make_pipeline(StandardScaler(),Ridge(alpha=1))
        model.fit(x,y[14:cutoff])
        prediction=float(model.predict([feature(y[:cutoff])])[0])
        rows.append(dict(cutoff=cutoff,actual=float(y[cutoff]),prediction=prediction,baseline=float(y[cutoff-7])))
    mae=float(np.mean([abs(r['actual']-r['prediction']) for r in rows]))
    baseline=float(np.mean([abs(r['actual']-r['baseline']) for r in rows]))
    return {'folds':len(rows),'model_mae':mae,'seasonal_naive_mae':baseline,'relative_mae_improvement':1-mae/baseline if baseline else None,'last_predictions':rows[-5:]}
if __name__=='__main__':print(json.dumps(backtest(series()),indent=2))
