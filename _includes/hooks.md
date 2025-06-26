<p id="hooks"><b>Open Hooks</b></p>
{: .text-delta }

{% for item in site.pages %}
{% if item.hooks %}
<p>
<a href="{{ site.url }}/{{ item.url }}">{{ item.title }}</a>
</p>
{: .text-delta }
{% for hook in item.hooks %}
> {{ hook }}
{: .fs-4 }
{% endfor %}
{% endif %}
{% endfor %}

<p id="market"><b>Market Research</b></p>
{: .text-delta }

<div style="height:45vh; width:110%;">
  <iframe
    src="https://docs.google.com/spreadsheets/d/e/2PACX-1vT6OmJ2_LeAkUhedPWZPdrCLIMhZjNa2TbFYBToFOmTALiP2_NupZ4ZCnaHuEx04sjq4yL6g_zAMkxy/pubhtml?gid=35129677&single=true&widget=false&headers=false&chrome=false"
    style="border:none; width:90%; height:100%;"
    allowfullscreen
  ></iframe>
</div>