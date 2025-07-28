from django.shortcuts import render, get_object_or_404, redirect


def statutes(request):
    return render(request, 'youth_org/statutes.html')

def sovereign_youth(request):
    return render(request, 'youth_org/sovereign_youth.html')

def programm(request):
    return render(request, 'youth_org/programm.html')
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils import timezone
from .models import ForumMessage, YouthOrganization, YouthMember
from .forms import YouthOrganizationForm, YouthMemberForm

def home(request):
    return render(request, 'home.html')

def organization_list(request):
    organizations = YouthOrganization.objects.filter(is_active=True).order_by('name')
    return render(request, 'youth_org/organization_list.html', {'organizations': organizations})

def organization_detail(request, pk):
    organization = get_object_or_404(YouthOrganization, pk=pk)
    return render(request, 'youth_org/organization_detail.html', {'organization': organization})

@login_required
def organization_create(request):
    if not request.user.is_staff:
        return redirect('home')  # Or some other page
    if request.method == 'POST':
        form = YouthOrganizationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Organization created successfully!')
            return redirect('organization_list')
    else:
        form = YouthOrganizationForm()
    return render(request, 'youth_org/organization_form.html', {'form': form})

@login_required
def organization_update(request, pk):
    if not request.user.is_staff:
        return redirect('home')
    organization = get_object_or_404(YouthOrganization, pk=pk)
    if request.method == 'POST':
        form = YouthOrganizationForm(request.POST, instance=organization)
        if form.is_valid():
            form.save()
            messages.success(request, 'Organization updated successfully!')
            return redirect('organization_detail', pk=organization.pk)
    else:
        form = YouthOrganizationForm(instance=organization)
    return render(request, 'youth_org/organization_form.html', {'form': form})

class YouthMemberCreateView(LoginRequiredMixin, CreateView):
    model = YouthMember
    form_class = YouthMemberForm
    template_name = 'youth_org/member_form.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Successfully joined the youth organization!')
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('youth-organization-detail', kwargs={'pk': self.object.organization.pk})

class YouthMemberUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = YouthMember
    form_class = YouthMemberForm
    template_name = 'youth_org/member_form.html'
    
    def test_func(self):
        member = self.get_object()
        return self.request.user == member.user or self.request.user.is_staff
    
    def form_valid(self, form):
        messages.success(self.request, 'Profile updated successfully!')
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('youth-organization-detail', kwargs={'pk': self.object.organization.pk})

@login_required
def youth_dashboard(request):
    try:
        member = request.user.youth_profile
        organization = member.organization
        context = {
            'member': member,
            'organization': organization,
            'upcoming_events': [],  # You can add events functionality later
        }
        return render(request, 'youth_org/dashboard.html', context)
    except YouthMember.DoesNotExist:
        organizations = YouthOrganization.objects.filter(is_active=True)
        return render(request, 'youth_org/join_organization.html', {'organizations': organizations})

@login_required(login_url='/login/')
def member(request):
    channel = request.GET.get('channel', 'general')
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            ForumMessage.objects.create(
                author=request.user,
                channel=channel,
                content=content,
                timestamp=timezone.now()
            )
            return redirect(f'/member/?channel={channel}')
    messages = ForumMessage.objects.filter(channel=channel).order_by('timestamp')
    channels = [
        ('general', 'Allgemein'),
        ('projects', 'Projekte'),
        ('offtopic', 'Off-Topic'),
    ]
    return render(request, 'member.html', {
        'messages': messages,
        'channels': channels,
        'current_channel': channel,
    })
